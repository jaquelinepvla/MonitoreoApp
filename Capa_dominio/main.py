
from flask import Flask, request, render_template
from flask import redirect, url_for
from Notificacion import detectar_condicion
from Monitoreo import actualizacion, almacenamiento
from Validaciones import acceso_val, registro_val
from Conexion import conectar
from flask_socketio import SocketIO
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'
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
	print(detectar_condicion(datos))

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
	

@app.route("/", methods=['POST', 'GET'])
def acceder():
	form = acceso_val()

	if request.method == 'POST': 
		usuario = form.usuario.data
		contrasena = form.contrasena.data
		consulta = "SELECT*from usuarios where usuario='{0}' and contrasena= '{1}' ".format(usuario, contrasena)
		conn = conectar()
		cursor= conn.cursor()
		cursor.execute(consulta)
		filas = cursor.fetchone()
		print(usuario, contrasena)
		conn.commit()
		cursor.close()
		conn.close()
		if filas is not None:
			return redirect(url_for('monitoreo'))
		print("Acceso incorrecto")
	return render_template('index.html', form=form)

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro_val()
	if request.method == 'POST':
		nombre = form.nombre.data
		email = form.email.data.lower()
		usuario = form.usuario.data.lower()
		contrasena = form.contrasena.data
		print(nombre, email, usuario, contrasena)
		
		conn = conectar()
		cursor= conn.cursor()
		consulta1 = "INSERT INTO usuarios (email, nombre, usuario, contrasena) VALUES('{0}', '{1}', '{2}', '{3}')".format(email, nombre, usuario, contrasena)
		consulta2 = "SELECT * from usuarios where email='{0}'or usuario='{1}' ".format(email, usuario)
		cursor.execute(consulta2)
		filas = cursor.fetchone()
		print(filas)
		
		if filas is None:
			cursor.execute(consulta1)
			conn.commit()
			cursor.close()
			conn.close()
			
			return redirect(url_for('acceder'))
		else: 
			print ('El nombre de usuario o el email ya se han registrado')
			return render_template('Registro.html', form=form)
	
	return render_template('Registro.html', form=form)


@app.route('/Monitoreo/',  methods=['POST', 'GET'])
def monitoreo():
	registro = actualizacion()
	return render_template('Monitoreo.html', registro=registro)


@app.route('/Prediccion/',  methods=['POST', 'GET'])
def predecir():
	return render_template('Prediccion.html')


if __name__ == "__main__":
	#debug=True para no tener que estar reiniciando el servidor cada que se actualice algo
	 socketio.run(app, host="192.168.0.10", port=8000, debug=True)
    #app.run(debug=True)
