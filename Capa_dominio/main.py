from flask import Flask, request, render_template
import psycopg2
from Usuario import registro 


app = Flask(__name__)
app.config['SECRET_KEY'] = '\xa6\x8b\xafF\xee\x81\xaa\x0e\xb8/\xd4H\xdb\xff\x9b\x19g+sM\x8dQ\xda\x05'
@app.route("/", methods=['POST', 'GET'])
def inicio():
	return render_template('index.html')

@app.route('/Registro', methods = ['POST', 'GET'])
def registrar():
	form = registro()
	if request.method == 'POST':
		Nombre = form.nombre.data
		Email = form.email.data
		Usuario = form.usuario.data
		Contraseña = form.contraseña.data
	
		print(Nombre, Email, Usuario, Contraseña)
		
		#Enviar información a la base de datos sin el contexto de la app
		conn = psycopg2.connect(
			host = "localhost",
			database = "Sistema_monitoreo",
			port= "5432",
			user="postgres",
			password= "12345"
		)
		cursor = conn.cursor()
		cursor.execute("INSERT INTO usuarios (email, nombre, usuario, contrasena) VALUES('{0}', '{1}', '{2}', '{3}')".format(Email, Nombre, Usuario, Contraseña))
		conn.commit()
		cursor.close()
		conn.close()
	
		return render_template('Index.html', form=form)
	return render_template('Registro.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)