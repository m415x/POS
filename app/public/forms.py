from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length



class LoginForm(FlaskForm):
    '''
    Campos formulario: Ingreso de usuarios
    '''
    user_name = StringField('usuario', validators=[DataRequired(), Length(max=12)])
    password = PasswordField('contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Entrar')