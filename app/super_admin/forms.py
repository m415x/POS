from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, SubmitField, PasswordField)
from wtforms.validators import (DataRequired, Length, Email, Regexp)



class SignupSuperadminForm(FlaskForm):
    '''
    Campos formulario: Creacion/edición de superadmin
    '''
    name = StringField('nombre', validators=[DataRequired(), Length(max=64)])
    email = StringField('email', validators=[DataRequired(), Email()])
    user_name = StringField('nombre de usuario', validators=[DataRequired(), Length(min=5, max=12)])
    password = PasswordField('contraseña', validators=[DataRequired()])
    submit = SubmitField('Crear')


# class PostForm(FlaskForm):
    
#     title = StringField('Título', validators=[DataRequired(), Length(max=128)])
#     content = TextAreaField('Contenido')
#     post_image = FileField('Imagen de cabecera',
#                            validators=[FileAllowed(['jpg','png'],
#                                                    'Solo se permiten imágenes')]
#                  )
#     submit = SubmitField('Guardar')


# class UserAdminForm(FlaskForm):
    
#     is_admin = BooleanField('Administrador')
#     submit = SubmitField('Guardar')