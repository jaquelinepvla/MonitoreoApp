import email
from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import InputRequired, Email, Length, equal_to

class registro_val(FlaskForm):
    nombre = StringField('Nombre', validators= [InputRequired(), Length(min=6, max=50)])
    email = EmailField('Correo electrónico', validators=[InputRequired(), Email(), Length(min=10, max=50)])
    usuario = StringField('Usuario', validators=[InputRequired(), Length(min=6, max=20)])
    contrasena = PasswordField('Contraseña', validators =[InputRequired(), Length(min=5, max=20)])
    enviar = SubmitField('Registrarse')

class acceso_val(FlaskForm):
    usuario = StringField('Usuario')
    contrasena = PasswordField('Contraseña')
    acceder = SubmitField('Acceder')

class contrasena_val(FlaskForm):
    email = EmailField('Correo electrónico', validators=[InputRequired(), Email(), Length(min=10, max=50)])
    contrasena = PasswordField('Nueva contraseña', validators=[InputRequired(), Length(min=5, max=20)])
    confirmacion = PasswordField('Confirmar contraseña')
    restablecer = SubmitField('Restablecer')

class email_val(FlaskForm):
    email = EmailField('Correo electrónico', validators=[InputRequired(), Email(), Length(min=10, max=50)])
    enviar = SubmitField('Enviar')

        