import psycopg2
def conectar():
    #Realizar conexión a la base de datos
	try: 
		conn = psycopg2.connect(
			host = "ec2-34-231-183-74.compute-1.amazonaws.com",
			database = "d3ujfsej46ci4f",
			port= "5432",
			user="htfobjplhphqsf",
			password= "671dbd9545c4439bd2f143d1ba32525ae8ccb455f436cddca04d19d0374cebc7"
			)
		return conn
	except:
		print("Falló la conexión, vuelva a intentarlo más tarde")

       
       