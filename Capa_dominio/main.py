from flask import Flask, request, render_template
from flask.globals import session
import psycopg2
from Usuario import registro, acceso
from Conexion import conectar
from Monitoreo import actualizacion
from Notificacion import email_alert

#from Monitoreo import actualizacion

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'

@app.route("/", methods=['POST', 'GET'])
def inicio():
	return render_template('index.html')

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro()
	if request.method == 'POST':
		nombre = form.nombre.data
		email = form.email.data
		usuario = form.usuario.data
		contrasena = form.contrasena.data
		print(nombre, email, usuario, contrasena)
		
		conn = conectar()
		cursor= conn.cursor()
		cursor.execute("INSERT INTO usuarios (email, nombre, usuario, contrasena) VALUES('{0}', '{1}', '{2}', '{3}')".format(email, nombre, usuario, contrasena))
		conn.commit()
		cursor.close()
		conn.close()
	
		return render_template('Index.html', form=form)
	return render_template('Registro.html', form=form)

@app.route('/Acceso', methods = ['POST', 'GET'])
def acceder():

	conn=conectar()
	cursor = conn.cursor()
	form = acceso()

	if request.method == 'POST': 
		usuario = form.usuario.data
		contrasena = form.contrasena.data
		consulta = "SELECT*from usuarios where usuario='{0}' and contrasena= '{1}' ".format(usuario, contrasena)
		cursor.execute(consulta)
		filas = cursor.fetchone()
		print(usuario, contrasena)

		if filas is not None:
			return render_template('Monitoreo.html', form=form)
		print("Acceso incorrecto")

		conn.commit()
		cursor.close()
		conn.close()
		
	return render_template('Acceso.html', form=form)

@app.route('/Monitoreo/')
def Monitoreo():
	registro = actualizacion()
	return render_template('Monitoreo.html', registro=registro)


email_alert("Hey", "Hello world", "jaquelinepvla@gmail.com")		
	
if __name__ == "__main__":
	#debug=True para no tener que estar reiniciando el servidor cada que se actualice algo
    app.run(debug=True)


