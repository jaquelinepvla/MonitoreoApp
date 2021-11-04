import json
from urllib import request
from Conexion import conectar
#cargar json
url = 'https://my.api.mockaroo.com/parametros.json?key=52609c40'
f = request.urlopen(url)
c = f.read()
#desempaquetar json
js = json.loads(c.decode('utf-8'))
oxigeno = js['oxigeno']
temperatura = js['temperatura']
fecha = js['fecha']
hora = js['hora']

def almacenamiento():  
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
    consulta = "SELECT * from parametros order by id desc limit 3;"
    cursor.execute(consulta)
    registro=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    print (registro)
    return registro
    


   
    