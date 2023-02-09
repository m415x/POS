import logging
import os

from flask import (render_template, redirect, url_for, request, current_app, abort)
from flask_login import (login_required, logout_user, current_user)
from werkzeug.utils import secure_filename
from datetime import datetime

from app import login_manager
from app.common.mail import send_email
from PIL import Image
from . import auth_bp
# from .forms import ItemForm
from app.models import Users
from .models import Items, Categories



logger = logging.getLogger(__name__)


#* SHOW POS -----------------------------------------------------------------------
@auth_bp.route("/pos/")
@login_required
def show_pos():
    
    # Se serializan los items y se convierten a json
    json_items = [ item.json() for item in Items.get_all() ]

    return render_template("auth/pos.html", json_items=json_items)


#* SHOW INVENTORY -----------------------------------------------------------------
@auth_bp.route("/inventory/")
@login_required
def show_inventory():
    
    # Se serializan los items y se convierten a json
    json_items = [ item.json() for item in Items.get_all() ]
    
    # Se serializan las categorías y se convierten a json
    json_categories = [ category.json() for category in Categories.get_all() ]
    
    return render_template("auth/inventory.html", json_items=json_items, json_categories=json_categories)

#!REVISAR TODO HACIA ABAJO, BORRA NO_IMG.PNG
#* ADD ITEM -----------------------------------------------------------------------
@auth_bp.route("/inventory/add/", methods=['POST'])
@login_required
def add_item():
    
    # Leer los campos del formulario
    category = request.form['addCategory']
    name = request.form['addName']
    info = request.form['addInfo']
    stock = request.form['addStock']
    unit = request.form['addUnit']
    cost = request.form['addCost']
    price = request.form['addPrice']
    file = request.files['addFile']
    image_name = None
    
    # Comprobar si la petición contiene la parte del fichero
    if file:
        image_name = secure_filename(file.filename)
        images_dir = current_app.config['ITEMS_IMAGES_DIR']
        os.makedirs(images_dir, exist_ok=True)
        now = datetime.now().strftime('%Y%m%d%H%M%S%f')
        
        # Convertir a JPG
        im = Image.open(image_name) #!Verificar funcionamiento
        if not im.mode == 'RGB':
            im = im.convert('RGB')
        image_name = im.save(f"{now}.jpg", quality=95)
        
        # Guardar fichero
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
    else:
        
        # Asignar no_image.png si no existe fichero
        image_name = 'no_image.png'
    
    # Si algun campo está vacío, no se crea #!No funciona validacion de campos
    if name == '' or info == '' or stock == '' or cost == '' or price == '':
        return redirect(url_for('auth.show_inventory'))
    
    # Guardar los datos de la petición en una variable
    item = Items(user_id=current_user.id, category_id=category, name=name, info=info, stock=stock, unit=unit, cost=cost, price=price, img_name=image_name)
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
        print('='*50)
        print(image_name)
        print('='*50)
        images_dir = current_app.config['ITEMS_IMAGES_DIR']
        os.makedirs(images_dir, exist_ok=True)
        now = datetime.now().strftime('%Y%m%d%H%M%S%f')
        image_name = f"{now}.jpg"
        file_path = os.path.join(images_dir, image_name)
        file.save(file_path)
        
        # Evitamos eliminar el archivo 'no_image.jpg'
        if item.img_name != 'no_image.png': #! Borra la imagen igualmente
            try:
                print('='*50)
                print('File DELETE')
                print('='*50)
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
@auth_bp.route("/delete/<int:item_id>/", methods=['GET', 'POST'])
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
    if image_name != 'no_image.png':
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