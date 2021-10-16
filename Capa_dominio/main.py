from flask import Flask, request, render_template
from Usuario import registro 

app = Flask(__name__)
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
		return render_template('Registro.html', form=form)
	return render_template('Registro.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)