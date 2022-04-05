
from Conexion import conectar
''' def ordenar(datos):
    d_f = sorted(datos, key="F")
    d_h = sorted(d_f, key="H")
    return d_h'''


def almacenamiento(datos):  
    data=datos
    temperatura = data["T"]
    oxigeno = data["O"]
    tiempo = data["F"]  + ' ' + data["H"]
    #fecha = data["F"]
    #hora = data["H"].replace('.','').replace(' ','')
    print(oxigeno, temperatura, tiempo)
    
    #Iniciar conexión con la base de datos
    con = conectar()
    cursor = con.cursor() 
    #Crear y ejecutar consulta
    consulta = "INSERT INTO parametros(oxigeno, temperatura, tiempo) VALUES('{0}', '{1}', '{2}', '{3}')".format(oxigeno, temperatura, tiempo) 
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

   
    