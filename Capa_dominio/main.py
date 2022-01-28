
from flask import Flask, request, render_template
from flask import redirect, url_for
from Prediccion import actualizacion_prediccion
from Prediccion import prediccion_temp
from Usuarios import Usuario
from Notificacion import detectar_condicion, consulta_email
from Monitoreo import actualizacion, almacenamiento
from Validaciones import acceso_val, registro_val
from flask_socketio import SocketIO
from flask_mail import Mail, Message
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USERNAME']='monitoreoapp.service@gmail.com'
app.config['MAIL_PASSWORD']='udkqdqvpwtxnvdcz'
app.config['MAIL_DEFAULT_SENDER']= 'monitoreoapp.service@gmail.com'
app.config['MAIL_USE_TLS']=True

mail= Mail(app)

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
			msg.html =(f'<b>Se han detectado valores fuera de rango</b><br><br>{r}<br><b> <br>Consulta más información </b><A HREF="http://192.168.1.16:8000">aquí. </A>')
			conn.send(msg) 

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
	
@app.route("/", methods=['POST', 'GET'])
def acceder():
	
	form = acceso_val()

	if request.method == 'POST': 
		usuario = form.usuario.data
		contrasena = form.contrasena.data
		u = Usuario('', '', usuario, contrasena)
		acceso = u.acceso()
		if acceso == True:
			return redirect(url_for('monitoreo'))
		else: print('Acceso incorrecto')
	
	return render_template('index.html', form=form)

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro_val()
	if request.method == 'POST':
		nombre = form.nombre.data
		email = form.email.data.lower()
		usuario = form.usuario.data.lower()
		contrasena = form.contrasena.data
		
		u = Usuario(nombre, email, usuario, contrasena)
		registro = u.registro()
		
		if registro == True:
			return redirect(url_for('acceder'))
		else:
			print ('El nombre de usuario o el email ya se han registrado')
			return render_template('Registro.html', form=form)
	
	return render_template('Registro.html', form=form)

#variable registro


@app.route('/Monitoreo/',  methods=['POST', 'GET'])
def monitoreo():
	registro = actualizacion()
	return render_template('Monitoreo.html', registro=registro)

@app.route('/datos/', methods=['POST', 'GET'])
def graficar():
	registro = actualizacion()
	o =[]
	t = []
	h = []
	f=[]
	#datos = actualizacion()
	
	for dato in registro:
		o.append(dato[1])
		t.append(dato[2])
		h.append(dato[4].strftime('%H:%M:%S'))
		f.append(dato[3].strftime('%d/%m/%Y'))	
	data = {
	"oxigeno": o,
	"temperatura": t,
	"hora": h,
	"fecha": f
    }
	#prediccion_temp()
	return data

@app.route('/Prediccion/',  methods=['POST', 'GET'])
def predecir():
	return render_template('Prediccion.html')

@app.route('/predecir/', methods=['POST', 'GET'])
def graficar_prediccion():
	registro = actualizacion_prediccion()
	o =[]
	t = []
	h = []
	f=[]
	#datos = actualizacion()
	
	for dato in registro:
		o.append(dato[1])
		t.append(dato[2])
		h.append(dato[4].strftime('%H:%M:%S'))
		f.append(dato[3].strftime('%d/%m/%Y'))	
	data = {
	"oxigeno": o,
	"temperatura": t,
	"hora": h,
	"fecha": f
    }
	#prediccion_temp()
	return data
	
if __name__ == "__main__":
	#debug=True para no tener que estar reiniciando el servidor cada que se actualice algo
	 socketio.run(app, host="192.168.1.16", port=8000, debug=True)
    #app.run(debug=True)

