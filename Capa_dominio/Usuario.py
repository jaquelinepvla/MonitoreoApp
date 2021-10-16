from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, SubmitField, PasswordField
from wtforms import validators
from wtforms.validators import DataRequired, Email, Length, EqualTo
import email_validator

class registro(FlaskForm):
    nombre = StringField('Nombre', validators= [DataRequired('Favor de insertar su nombre completo'), Length(min=5, max=50)])
    email = StringField('Email', validators=[DataRequired('Favor de incertar un correo valido'), Email()])
    usuario = StringField('Nombre de usuario', validators=[DataRequired('Favor de insertar un nombre de usuario valido'), Length(min=5, max=20)])
    contraseña = PasswordField('contraseña', validators =[DataRequired()])
    confirmar = PasswordField('Confirmar contraseña: ', validators=[DataRequired(), EqualTo('contraseña', message='La contraseñas no coinciden')])
    enviar = SubmitField('Registrarse')