import email
import numpy as np
from flask import Flask, jsonify, request, render_template
from flask import redirect, url_for, flash
#from Usuarios import get_by_id
from Validaciones import contrasena_val, email_val
from Prediccion import actualizacion_prediccion
from Prediccion import prediccion_temp
from Usuarios import Usuario
from Notificacion import detectar_condicion, consulta_email
from Monitoreo import actualizacion, almacenamiento
from Validaciones import acceso_val, registro_val
from flask_socketio import SocketIO
from flask_mail import Mail, Message
import json
from flask_cors import CORS, cross_origin
#from flask_login import LoginManager, login_user, logout_user, login_required


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='monitoreoapp.service@gmail.com'
app.config['MAIL_PASSWORD']='udkqdqvpwtxnvdcz'
app.config['MAIL_DEFAULT_SENDER']= 'monitoreoapp.service@gmail.com'
app.config['MAIL_USE_TLS']=True
'''
mail= Mail(app)
#login_manager_app=LoginManager(app)
socketio = SocketIO(app)

@socketio.on('connect')
def connect():
	print('connected')

@socketio.on('my event')
def handle_json(js):
	print('received json: ', str(js))
	datos= json.loads(js)
	print(datos)
	almacenamiento(datos)
	resultado= detectar_condicion(datos)
	prediccion_temp()
	mensaje(resultado)

def mensaje(resultado):
	
	#print(len(resultado))
	if len(resultado) > 0: 
		r=str(resultado).replace('[','').replace(']','').replace('{','').replace('}','').replace("'",'')
		print(r)
		with mail.connect() as conn:
			subj = "Alerta"
			msg = Message(recipients=consulta_email(),  subject=subj)
			msg.html =(f'<b>Se han detectado valores fuera de rango</b><br><br>{r}<br><b> <br>Consulta más información </b><A HREF="https://iotacuicola.herokuapp.com/">aquí.</A>')
			conn.send(msg) 

def mensaje_contrasena(destinatario):

	with mail.connect() as conn:
		subj = "Restablecer contraseña"
		msg = Message(recipients=destinatario,  subject=subj)
		msg.html =('Has solicitado restablecer la contraseña de tu cuenta de MonitoreoApp. Ingresa <A HREF="https://iotacuicola.herokuapp.com//Restablecer_contrasena">aquí </A>para continuar.')
		conn.send(msg)

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')'''
''' 
@login_manager_app.user_loader
def load_user(id):
	return get_by_id(id)'''

'''
@app.route("/hola", methods=['POST', 'GET'])
def prueba():
	msg = request.get_json()
	print(msg)
	almacenamiento(msg)
	resultado= detectar_condicion(msg)
	prediccion_temp()
	mensaje(resultado)
	return "todo correcto"

@app.route("/", methods=['POST', 'GET'])
def acceder():
	
	form = acceso_val()

	if request.method == 'POST': 
		usuario = form.usuario.data
		contrasena = form.contrasena.data
		u = Usuario('','', '', usuario, contrasena)
		acceso = u.acceso()
		#user=u.get_id()
		#print (user)
		if  acceso == True:
			#login_user(u)
			return redirect(url_for('monitoreo'))
		else: print('Acceso incorrecto')
		flash('¡Acceso incorrecto! verifique que el usuario y la contraseña coincidan')
	
	return render_template('\index.html', form=form)

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro_val()
	if request.method == 'POST':
		nombre = form.nombre.data
		email = form.email.data.lower()
		usuario = form.usuario.data.lower()
		contrasena = form.contrasena.data
		
		u = Usuario('', nombre, email, usuario, contrasena)
		registro = u.registro()
		
		if registro == True:
			return redirect(url_for('acceder'))
		else:
			print ('El nombre de usuario o el email ya se han registrado')
			flash('El nombre de usuario o email ya han sido registrados')
			return render_template('Registro.html', form=form)
	
	return render_template('Registro.html', form=form)

@app.route('/Restablecer_contrasena', methods = ['POST', 'GET'])
def formulario_contrasena():
	form = contrasena_val()
	if request.method =='POST':
		email= form.email.data
		contrasena=form.contrasena.data
		nueva_contrasena = form.confirmacion.data
		if nueva_contrasena == contrasena:
			u=Usuario('', '', email, '', contrasena)
			u.actualizar_contrasena()
			flash('La contraseña fue restablecida')
			return redirect(url_for('acceder'))
		else: 
			flash('Las contraseñas no coinciden')
	return render_template('Restablecer_contrasena.html', form=form)

@app.route('/Cambio_de_contrasena', methods = ['POST', 'GET'])
def restablecer_contrasena():
	form = email_val()
	if request.method =='POST':
		destinatario=[]
		email= form.email.data
		u=Usuario('', '', email, '', '')
		destinatario.append(email)
		print(destinatario)
	
		if u.verificar_email():
			mensaje_contrasena(destinatario)
			flash('Se ha enviado un mensaje a tu correo electrónico con el link para restablecer la contraseña')
		else:
			flash('El correo proporcionado no se encuentra registrado en el sistema')
	return render_template('Cambio_de_contrasena.html', form=form)	


@app.route('/Monitoreo/',  methods=['POST', 'GET'])
def monitoreo():
	registro = actualizacion()
	return render_template('Monitoreo.html', registro=registro)'''

#================== Rutas Datos ==========================
@cross_origin
@app.route('/Prediccion/',  methods=['POST', 'GET'])
def predecir():
	registro = actualizacion_prediccion()
	js=[]
	for dato in registro:
		js.append({'O': dato[1], 'temp': dato[2], 'f':dato[4].strftime('%H:%M:%S'), 't':dato[3].strftime('%d/%m/%Y')})

	return jsonify(js)

@cross_origin
@app.route('/', methods=['POST', 'GET'])
def graficar():
	registro = actualizacion()
	js=[]
	for dato in registro:
		js.append({'O': dato[1], 'temp': dato[2], 'f':dato[4].strftime('%H:%M:%S'), 't':dato[3].strftime('%d/%m/%Y')})

	return jsonify(js)

cross_origin
@app.route('/Grafica/', methods=['POST', 'GET'])
def graficar_monitoreo():
	registro = actualizacion()
	o =[]
	t = []
	h = []
	f=[]
	for dato in registro:
		o.append(dato[1])
		t.append(dato[2])
		h.append(dato[4].strftime('%H:%M:%S'))
		f.append(dato[3].strftime('%d/%m/%Y'))
	o_reverse= o[::-1]
	t_reverse= t[::-1]
	h_reverse= h[::-1]	
	data = {
	"oxigeno": o_reverse,
	"temperatura": t_reverse,
	"hora": h_reverse,
	"fecha": f
    }
	return data

	
@cross_origin
@app.route('/Prediccion_grafica/', methods=['POST', 'GET'])
def graficar_prediccion():
	registro = actualizacion_prediccion()
	o =[]
	t = []
	h = []
	f=[]
	
	for dato in registro:
		o.append(dato[1])
		t.append(dato[2])
		h.append(dato[4].strftime('%H:%M:%S'))
		f.append(dato[3].strftime('%d/%m/%Y'))
	o_reverse= o[::-1]
	t_reverse= t[::-1]
	h_reverse= h[::-1]	
	data = {
	"oxigeno": o_reverse,
	"temperatura": t_reverse,
	"hora": h_reverse,
	"fecha": f
    }
	return data

if __name__ == "__main__":
	#debug=True para no tener que estar reiniciando el servidor cada que se actualice algo
	#socketio.run(app, host="https://iotacuicola.herokuapp.com", port=8000, debug=True)
    app.run(debug=True, port=8000)
