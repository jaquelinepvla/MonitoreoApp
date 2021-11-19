from Conexion import conectar
from Monitoreo import actualizacion
def consulta_email():  
    #Iniciar conexión con la base de datos
    con = conectar()
    cursor = con.cursor() 
    #Crear y ejecutar consulta
    consulta = "SELECT email from usuarios"
    cursor.execute(consulta)
    filas = cursor.fetchall()
    print(filas)
    #Hacer cambios en la base de datos
    con.commit()
    #Cerrar cursor y conexión
    cursor.close()
    con.close()
    return consulta

def detectar_condicion(datos):
    resultado=[]
    d=datos
    oxigeno = d["oxigeno"]
    temperatura = d['temperatura']
    fecha = d["fecha"]
    hora = d["hora"]

    if oxigeno<3 or oxigeno>8:
        print(f"Se han detectado valores fuera de rango. Oxigeno: {oxigeno, fecha, hora} ")
        resultado.append(f"Se han detectado valores fuera de rango. Oxigeno: {oxigeno, fecha, hora} ")
    else:
        print("El oxigeno se encuentra en condiciones normales")
    if  temperatura<29 or temperatura>32:
        print(f"Se han detectado valores fuera de rango. Temperatura: {temperatura, fecha, hora} ") 
        resultado.append(f"Se han detectado valores fuera de rango. Temperatura: {temperatura, fecha, hora} ")
    else:
        print("La temperatura se encuentra en condiciones normales")
    return resultado
