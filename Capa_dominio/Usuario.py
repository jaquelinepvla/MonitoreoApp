from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms import validators
from wtforms.validators import InputRequired, DataRequired, Email, Length, EqualTo
import email_validator


class registro(FlaskForm):
    nombre = StringField('Nombre', validators= [InputRequired('Favor de insertar su nombre completo'), Length(min=5, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email('Favor de incertar un correo valido'), Length(min=5, max=20)])
    usuario = StringField('Nombre de usuario', validators=[InputRequired('Favor de insertar un nombre de usuario valido'), Length(min=5, max=20)])
    contrasena = PasswordField('Contraseña', validators =[InputRequired(), Length(min=8, max=20)])
    enviar = SubmitField('Registrarse')


class acceso(FlaskForm):
    usuario = StringField('Nombre de usuario', validators=[InputRequired('Favor de insertar un nombre de usuario valido'), Length(min=5, max=20)])
    contrasena = PasswordField('contraseña', validators =[InputRequired(), Length(min=8, max=20)])
    #recordarme= BooleanField('Recordarme')
    enviar = SubmitField('Acceder')
        
        
