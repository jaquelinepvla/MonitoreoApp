
from Conexion import conectar

def almacenamiento(datos):  
    data=datos
    oxigeno = data["O"]
    temperatura = data["T"]
    fecha = data["F"]
    hora = data["H"]
    print(oxigeno, temperatura, fecha, hora)
    
    #Iniciar conexión con la base de datos
    con = conectar()
    cursor = con.cursor() 
    #Crear y ejecutar consulta
    consulta = "INSERT INTO parametros(oxigeno, temperatura, fecha, hora) VALUES('{0}', '{1}', '{2}', '{3}')".format(oxigeno, temperatura, fecha, hora) 
    cursor.execute(consulta)
    #Hacer cambios en la base de datos
    con.commit()
    #Cerrar cursor y conexión
    cursor.close()
    con.close()

def actualizacion():
    
    con = conectar()
    cursor = con.cursor() 
    consulta = "SELECT * from parametros order by id desc limit 10;"
    cursor.execute(consulta)
    registro=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return registro

   
    