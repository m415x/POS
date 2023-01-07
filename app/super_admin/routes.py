import logging
import os

from flask import render_template, redirect, url_for, abort, current_app, request
from flask_login import login_required, current_user, login_user
from werkzeug.utils import secure_filename
from werkzeug.urls import url_parse


# from app.auth.decorators import admin_required
from app.models import Users
from . import superadmin_bp
from .forms import SignupSuperadminForm
from app.common.mail import send_email



logger = logging.getLogger(__name__)


#* CREATE SUPER-ADMIN -------------------------------------------------------------
@superadmin_bp.route("/signup-superadmin/", methods=["GET", "POST"])
def signup_superadmin():
    # Validamos existencia de usuario super-admin para bloquear acceso a ruta
    super_admin = Users.get_by_super_admin()
    if super_admin:
        return redirect(url_for('auth.show_pos'))
        
    # Creamos el objeto form
    form = SignupSuperadminForm()
    
    error = None
    
    # Validmos los campos del formulario
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user_name = form.user_name.data
        password = form.password.data
        
        # Comprobamos que no existe ese usuario
        user = Users.get_by_user_name(user_name)
        if user is not None:
            error = f'El nombre {user_name} ya está siendo utilizado por otro usuario'
        
        else:
            
            # Creamos el usuario super-admin y lo guardamos
            user = Users(name=name, email=email, user_name=user_name)
            user.set_password(password)
            user.set_admin(True)
            user.set_superadmin(True)
            user.save()
            
            # Enviamos un email de bienvenida
            send_email(subject='POS-Superadmin creado con éxito',
                       sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
                       recipients=[email, ],
                       text_body=f'Hola {name}, has creado correctamente el perfil Superadmin',
                       html_body=f'<p>Hola <strong>{name}</strong>, has creado correctamente el perfil Superadmin</p>')

            # Dejamos al usuario logueado
            login_user(user, remember=True)
            
            # Comprobamos si recibimos el parámetro 'next', cuando el usuario ha intentado acceder a una página protegida pero no estaba autenticado
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('auth.show_pos')
                
            return redirect(next_page)
        
    return render_template("auth/signup_admin_form.html", form=form, error=error)








# @admin_bp.route("/admin/")
# @login_required
# @admin_required
# def index():

#     """Panel de administrador"""

#     return render_template("admin/index.html")


# @admin_bp.route("/admin/posts/")
# @login_required
# @admin_required
# def list_posts():
    
#     """Listar todos los Posts"""

#     posts = Post.get_all()

#     return render_template("admin/posts.html", posts=posts)


# @admin_bp.route("/admin/post/", methods=['GET', 'POST'])
# @login_required
# @admin_required
# def post_form():
    
#     """Crea un nuevo post"""
    
#     form = PostForm()
    
#     if form.validate_on_submit():
#         title = form.title.data
#         content = form.content.data
#         file = form.post_image.data
#         image_name = None
        
#         # Comprueba si la petición contiene la parte del fichero
#         if file:
#             image_name = secure_filename(file.filename)
#             images_dir = current_app.config['POSTS_IMAGES_DIR']
#             os.makedirs(images_dir, exist_ok=True)
#             file_path = os.path.join(images_dir, image_name)
#             file.save(file_path)
                
#         post = Post(user_id=current_user.id, title=title, content=content)
#         post.image_name = image_name
#         post.save()
#         logger.info(f'Guardando nuevo post {title}')
        
#         return redirect(url_for('admin.list_posts'))
    
#     return render_template("admin/post_form.html", form=form)


# @admin_bp.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
# @login_required
# @admin_required
# def update_post_form(post_id):
    
#     """Actualiza un post existente"""
    
#     post = Post.get_by_id(post_id)
    
#     if post is None:
#         logger.info(f'El post {post_id} no existe')
#         abort(404)
        
#     # Crea un formulario inicializando los campos con los valores del post.
#     form = PostForm(obj=post)
    
#     if form.validate_on_submit():
        
#         # Actualiza los campos del post existente
#         post.title = form.title.data
#         post.content = form.content.data
#         post.save()
#         logger.info(f'Guardando el post {post_id}')
        
#         return redirect(url_for('admin.list_posts'))
    
#     return render_template("admin/post_form.html", form=form, post=post)


# @admin_bp.route("/admin/post/delete/<int:post_id>/", methods=['POST', ])
# @login_required
# @admin_required
# def delete_post(post_id):
    
#     """Elimina un post existente"""
    
#     logger.info(f'Se va a eliminar el post {post_id}')
#     post = Post.get_by_id(post_id)
    
#     if post is None:
#         logger.info(f'El post {post_id} no existe')
#         abort(404)
        
#     post.delete()
#     logger.info(f'El post {post_id} ha sido eliminado')
    
#     return redirect(url_for('admin.list_posts'))


# @admin_bp.route("/admin/users/")
# @login_required
# @admin_required
# def list_users():
    
#     '''Listar usuarios registrados en el sistema'''
    
#     users = User.get_all()
    
#     return render_template("admin/users.html", users=users)


# @admin_bp.route("/admin/user/<int:user_id>/", methods=['GET', 'POST'])
# @login_required
# @admin_required
# def update_user_form(user_id):
    
#     '''Editar un usuario'''
    
#     # Aquí entra para actualizar un usuario existente
#     user = User.get_by_id(user_id)
    
#     if user is None:
#         logger.info(f'El usuario {user_id} no existe')
#         abort(404)
        
#     # Crea un formulario inicializando los campos con los valores del usuario.
#     form = UserAdminForm(obj=user)
    
#     if form.validate_on_submit():
        
#         # Actualiza los campos del usuario existente
#         user.is_admin = form.is_admin.data
#         user.save()
#         logger.info(f'Guardando el usuario {user_id}')
        
#         return redirect(url_for('admin.list_users'))
    
#     return render_template("admin/user_form.html", form=form, user=user)


# @admin_bp.route("/admin/user/delete/<int:user_id>/", methods=['POST', ])
# @login_required
# @admin_required
# def delete_user(user_id):
    
#     '''Eliminar un usuario'''
    
#     logger.info(f'Se va a eliminar al usuario {user_id}')
#     user = User.get_by_id(user_id)
    
#     if user is None:
#         logger.info(f'El usuario {user_id} no existe')
#         abort(404)
        
#     user.delete()
#     logger.info(f'El usuario {user_id} ha sido eliminado')
    
#     return redirect(url_for('admin.list_users'))