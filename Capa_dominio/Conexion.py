import psycopg2
def conectar():
    #Realizar conexión a la base de datos
	try: 
		conn = psycopg2.connect(
			host = "localhost",
			database = "Sistema_monitoreo",
			port= "5432",
			user="postgres",
			password= "12345"
			)
		return conn
	except:
		print("Falló la conexión, vuelva a intentarlo más tarde")

       
       