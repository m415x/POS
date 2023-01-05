from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email, Length



class SignupForm(FlaskForm):
    '''
    Campos formulario: Creacion/edición de usuarios
    '''
    name = StringField('nombre', validators=[DataRequired(), Length(max=64)])
    email = StringField('email', validators=[DataRequired(), Email()])
    user_name = StringField('nombre de usuario', validators=[DataRequired(), Length(max=12)])
    password = PasswordField('contraseña', validators=[DataRequired()])
    submit = SubmitField('Crear Administrador')


class CategoryForm(FlaskForm):
    '''
    Campos formulario: Creacion/edición de categorías
    '''
    category = StringField('Categoría', validators=[DataRequired(), Length(max=25)])
    submit = SubmitField('Guardar')


class ProductForm(FlaskForm):
    '''
    Campos formulario: Creacion/edición de productos
    '''
    name = StringField('nombre', validators=[DataRequired(), Length(max=20)])
    info = StringField('Descripción', validators=[DataRequired(), Length(max=256)])
    stock = FloatField('Stock')
    cost = FloatField('Costo')
    price = FloatField('Precio')
    email = StringField('email', validators=[DataRequired(), Email()])
    img_name = FileField('Imagen',
                           validators=[FileAllowed(['jpg','png'],
                                                   'Solo se permiten imágenes')])
    submit = SubmitField('Guardar')