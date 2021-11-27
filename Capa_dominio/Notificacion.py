from Conexion import conectar

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
    resultado=['¡Se han detectado valores fuera de rango!'] 
    d=datos
    oxigeno = d["oxigeno"]
    temperatura = d['temperatura']
    fecha = d["fecha"]
    hora = d["hora"]
    if oxigeno<3 or oxigeno>8:
        
        resultado.append(f"Oxigeno: {oxigeno}, 'Fecha:' {fecha}, 'Hora:'{hora} ")
    else:
        print("El oxigeno se encuentra en condiciones normales")
    if  temperatura<29 or temperatura>32:
        
        resultado.append(f" Temperatura: {temperatura}, 'Fecha:' {fecha}, 'Hora:' {hora} ")
    else:
        print("La temperatura se encuentra en condiciones normales")
    return resultado
