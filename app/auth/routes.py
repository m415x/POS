import logging
import os

from flask import (render_template, redirect, url_for, request, current_app, abort, jsonify)
from flask_login import (login_required, logout_user, current_user)
from werkzeug.utils import secure_filename
from datetime import datetime

from app import login_manager
from app.common.mail import send_email
from . import auth_bp
# from .forms import ItemForm
from app.models import Users
from .models import Items, Categories



logger = logging.getLogger(__name__)


#* SHOW POS -----------------------------------------------------------------------
@auth_bp.route("/pos/")
@login_required
def show_pos():
    items = Items.get_all()
    
    # Serializamos los items y los convertimos a json
    json_items = [ item.json() for item in Items.get_all() ]
    
    # Almacenamos los items en el objeto items
    json_items = {'items': json_items }
    
    return render_template("auth/pos.html", json_items=json_items, items=items)


#* SHOW INVENTORY -----------------------------------------------------------------
@auth_bp.route("/inventory/")
@login_required
def show_inventory():
    
    # Guardamos los datos de la petición en una variable
    items = Items.get_all()
    
    # Leemos argumentos de la petición
    field = request.args.get('field')
    order = request.args.get('order')
    if field != None and order != None:
        items = Items.get_order_by(field, order)
        
    # Guardamos los datos de la petición en una variable
    categories = Categories.get_all()
    
    return render_template("auth/inventory.html", items=items, categories=categories)


#* ADD ITEM -----------------------------------------------------------------------
@auth_bp.route("/inventory/add/", methods=['POST'])
@login_required
def add_item():
    
    # Leemos los campos del formulario
    category = request.form['addCategory']
    name = request.form['addName']
    info = request.form['addInfo']
    stock = request.form['addStock']
    cost = request.form['addCost']
    price = request.form['addPrice']
    file = request.files['addFile']
    image_name = None
    
    # Comprueba si la petición contiene la parte del fichero
    if file:
        image_name = secure_filename(file.filename)
        images_dir = current_app.config['ITEMS_IMAGES_DIR']
        os.makedirs(images_dir, exist_ok=True)
        now = datetime.now().strftime('%Y%m%d%H%M%S%f')
        image_name = f"{now}.jpg"
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
    else:
        image_name = 'no_image.jpg'
    
    # Si algun campo está vacío, no se crea
    if name == '' or info == '' or stock == '' or cost == '' or price == '':
        return redirect(url_for('auth.show_inventory'))
    
    # Guardamos los datos de la petición en una variable
    item = Items(user_id=current_user.id, category_id=category, name=name, info=info, stock=stock, cost=cost, price=price, img_name=image_name)
    item.save()
    logger.info(f'Guardando nuevo item {name}')
    
    return redirect(url_for('auth.show_inventory'))


#* EDIT ITEM ----------------------------------------------------------------------
@auth_bp.route("/inventory/edit/", methods=['GET', 'POST'])
@login_required
def edit_item():
    
    # Leemos los campos del formulario
    item_id = request.form['editCode']
    category = request.form['editCategory']
    name = request.form['editName']
    info = request.form['editInfo']
    stock = request.form['editStock']
    cost = request.form['editCost']
    price = request.form['editPrice']
    file = request.files['editFile']
    
    # Guardamos los datos de la petición en una variable
    logger.info(f'Se va a editar el item {item_id}')
    item = Items.get_by_id(item_id)
    
    # Comprobamos que el id pertenece a un item existente
    if item is None:
        logger.info(f'El item {item_id} no existe')
        abort(404)
    
    # Asignamos el nuevo valor a cada campo
    item.user_id=current_user.id
    item.category_id=category
    item.name=name
    item.info=info
    item.stock=stock
    item.cost=cost
    item.price=price
    
    # Comprueba si la petición contiene la parte del fichero
    if file:
        image_name = secure_filename(file.filename)
        images_dir = current_app.config['ITEMS_IMAGES_DIR']
        os.makedirs(images_dir, exist_ok=True)
        now = datetime.now().strftime('%Y%m%d%H%M%S%f')
        image_name = f"{now}.jpg"
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
        
        # Evitamos eliminar el archivo 'no_image.jpg'
        if image_name != 'no_image.jpg': #! Borra la imagen igualmente
            try:
                os.remove(os.path.join(images_dir, item.img_name))
            except:
                pass
        item.img_name = image_name
    
    # Si algun campo está vacío, no se actualiza
    if name == '' or info == '' or stock == '' or cost == '' or price == '':
        return redirect(url_for('auth.show_inventory'))

    item.save()
    logger.info(f'Actualizado el item {name}')

    return redirect(url_for('auth.show_inventory'))


#* DELETE ITEM --------------------------------------------------------------------
@auth_bp.route("/inventory/delete/<int:item_id>/", methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    
    # Guardamos los datos de la petición en una variable
    logger.info(f'Se va a eliminar el item {item_id}')
    item = Items.get_by_id(item_id)
    
    # Comprobamos que el id pertenece a un item existente
    if item is None:
        logger.info(f'El item {item_id} no existe')
        abort(404)
    
    image_name = item.img_name
    images_dir = current_app.config['ITEMS_IMAGES_DIR']
    if image_name != 'no_image.jpg':
        try:
            os.remove(os.path.join(images_dir, image_name))
        except:
            pass
        
    # Eliminamos el registro
    item.delete()
    logger.info(f'El item {item_id} ha sido eliminado')
    
    return redirect(url_for('auth.show_inventory'))


#* LOAD USER ----------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return Users.get_by_id(int(user_id))


#* LOGOUT -------------------------------------------------------------------------
@auth_bp.route('/logout/')
def logout():
    logout_user()
    
    return redirect(url_for('public.login'))


#* CREATE USER --------------------------------------------------------------------
# !COPIAR SUPERADMIN Y MODIFICAR PARAMETROS DE USUARIO