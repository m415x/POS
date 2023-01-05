import logging

from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user
from werkzeug.urls import url_parse

from app.models import User
from . import public_bp
from .forms import LoginForm



logger = logging.getLogger(__name__)


#* LOGIN --------------------------------------------------------------------------
@public_bp.route('/', methods=['GET', 'POST'])
def login():
    # Comprobamos si el usuario está autenticado, si es así, lo redirigimos
    if current_user.is_authenticated:
        return redirect(url_for('auth.pos'))
    
    # Creamos el objeto form
    form = LoginForm()
    
    # Comprobamos si los datos enviados en el formulario son válidos
    if form.validate_on_submit():
        user = User.get_by_user_name(form.user_name.data)

        # Autenticamos (si existe dicho usuario y la contraseña coincide)
        if user is not None and user.check_password(form.password.data):
            
            # Dejamos al usuario logueado
            login_user(user, remember=form.remember_me.data)
            
            # Comprobamos si recibimos el parámetro 'next', cuando el usuario ha intentado acceder a una página protegida pero no estaba autenticado
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('auth.pos')
                
            return redirect(next_page)
        
    return render_template('public/login_user.html', form=form)
