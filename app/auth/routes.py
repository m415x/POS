import logging

from flask import (render_template, redirect, url_for, request, current_app, jsonify)
from flask_login import login_required, logout_user, current_user
from werkzeug.urls import url_parse

from app import login_manager
from app.common.mail import send_email
from . import auth_bp
from .forms import ItemForm
from app.models import Users
from .models import Items



logger = logging.getLogger(__name__)


#* SHOW POS -----------------------------------------------------------------------
@auth_bp.route("/pos")
@login_required
def show_pos():
    items = Items.get_all()
    # jitems = jsonify(Item.get_all())
    # print(jitems.serialize())
    
    return render_template("auth/pos.html", items=items)


#* SHOW INVENTORY -----------------------------------------------------------------
@auth_bp.route("/inventory")
@login_required
def show_inventory():
    items = Items.get_all()
    # jitems = jsonify(Item.get_all())
    # print(jitems.serialize())
    
    return render_template("auth/inventory.html", items=items)


#* ADD ITEM -----------------------------------------------------------------
@auth_bp.route("/inventory/add-item/", methods=['GET', 'POST'])
@login_required
def add_item():
    form = ItemForm()
    
    if form.validate_on_submit():
        name = form.name.data
        content = form.content.data
        file = form.post_image.data
        image_name = None
        
        # Comprueba si la petición contiene la parte del fichero
        if file:
            image_name = secure_filename(file.filename)
            images_dir = current_app.config['POSTS_IMAGES_DIR']
            os.makedirs(images_dir, exist_ok=True)
            file_path = os.path.join(images_dir, image_name)
            file.save(file_path)
                
        post = Post(user_id=current_user.id, name=name, content=content)
        post.image_name = image_name
        post.save()
        logger.info(f'Guardando nuevo post {name}')
        
        return redirect(url_for('admin.list_posts'))
    
    return render_template("admin/post_form.html", form=form)

#* LOAD USER ------------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return Users.get_by_id(int(user_id))


#* LOGOUT -------------------------------------------------------------------------
@auth_bp.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('public.login'))


#* CREATE USER --------------------------------------------------------------------
# !COPIAR SUPERADMIN Y MODIFICAR PARAMETROS DE USUARIO