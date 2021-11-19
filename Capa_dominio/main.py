from flask import Flask, request, render_template
from flask import redirect, url_for
from Notificacion import detectar_condicion
from Monitoreo import recibir_datos, actualizacion, almacenamiento
from Validaciones import acceso_val, registro_val
from Conexion import conectar
import json
	

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'



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
js=recibir_datos()
datos=json.loads(js)
print(type(datos))
almacenamiento(datos)
notificar=detectar_condicion(datos)

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro_val()
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
	
		return redirect(url_for('acceder'))
	return render_template('Registro.html', form=form)



@app.route('/Monitoreo/',  methods=['POST', 'GET'])
def monitoreo():
	registro = actualizacion()
	return render_template('Monitoreo.html', registro=registro)


@app.route('/Notificaciones/',  methods=['POST', 'GET'])
def notificar():
	alertas=notificar
	return render_template('Notificacion.html', notifcacion=alertas)

js=recibir_datos()
datos=json.loads(js)
print(type(datos))
almacenamiento(datos)
notificar=detectar_condicion(datos)


if __name__ == "__main__":
	#debug=True para no tener que estar reiniciando el servidor cada que se actualice algo
    app.run(debug=True)


