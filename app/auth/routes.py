import logging

from flask import (render_template, redirect, url_for, request, current_app)
from flask_login import login_required, logout_user, current_user
from werkzeug.urls import url_parse

from app import login_manager
from app.common.mail import send_email
from . import auth_bp
from .forms import SignupForm
from app.models import User



logger = logging.getLogger(__name__)


# #* CREATE USER -------------------------------------------------------------
# @auth_bp.route("/signup/", methods=["GET", "POST"])
# def signup_superadmin():
#     #! Validar existencia de usuario admin para bloquear acceso a ruta
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('auth.pos'))
    
#     # Creamos el objeto form
#     form = SignupForm()
    
#     error = None
    
#     # Validmos los campos del formulario
#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
#         user_name = form.user_name.data
#         password = form.password.data
        
#         # Comprobamos que no existe ese usuario
#         user = User.get_by_user_name(user_name)
#         if user is not None:
#             error = f'El nombre {user_name} ya está siendo utilizado por otro usuario'
        
#         else:
            
#             # Creamos el usuario super-admin y lo guardamos
#             user = User(name=name, email=email, user_name=user_name)
#             user.set_password(password)
#             user.set_admin(True)
#             user.set_superadmin(True)
#             user.save()
            
#             # Enviamos un email de bienvenida
#             send_email(subject='POS-Admin creado con éxito',
#                        sender=current_app.config['DONT_REPLY_FROM_EMAIL'],
#                        recipients=[email, ],
#                        text_body=f'Hola {name}, has creado correctamente el perfil administrador.',
#                        html_body=f'<p>Hola <strong>{name}</strong>, has creado correctamente el perfil administrador</p>')

#             # Dejamos al usuario logueado
#             login_user(user, remember=True)
            
#             # Comprobamos si recibimos el parámetro 'next', cuando el usuario ha intentado acceder a una página protegida pero no estaba autenticado
#             next_page = request.args.get('next', None)
#             if not next_page or url_parse(next_page).netloc != '':
#                 next_page = url_for('auth.show_pos')
                
#             return redirect(next_page)
        
#     return render_template("auth/signup_admin_form.html", form=form, error=error)


#* LOGOUT -------------------------------------------------------------------------
@auth_bp.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('public.login'))


#* SHOW POS -----------------------------------------------------------------------
@auth_bp.route("/pos")
@login_required
def show_pos():
#     logger.info('Mostrando el POS')
    # page = int(request.args.get('page', 1))
    # per_page = current_app.config['ITEMS_PER_PAGE']
    # post_pagination = Post.all_paginated(page, per_page)
    
    return render_template("auth/pos.html")



# def pos():

#     sql = "SELECT code, type, name, info, stock, cost, price, img FROM pos.products;"
#     cursor.execute(sql)
#     products = cursor.fetchall()

#     conn.commit()

#     return render_template('pos/pos.html', products=products)



# @public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
# def show_post(slug):
    
#     logger.info('Mostrando un post')
#     logger.debug(f'Slug: {slug}')
#     post = Post.get_by_slug(slug)
    
#     if not post:
#         logger.info(f'El post {slug} no existe')
#         abort(404)
        
#     form = CommentForm()
    
#     if current_user.is_authenticated and form.validate_on_submit():
#         content = form.content.data
#         comment = Comment(content=content,
#                           user_id=current_user.id,
#                           user_name=current_user.name,
#                           post_id=post.id)
#         comment.save()
        
#         return redirect(url_for('public.show_post', slug=post.title_slug))
    
#     return render_template("public/post_view.html", post=post, form=form)




#* LOAD USER ------------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))