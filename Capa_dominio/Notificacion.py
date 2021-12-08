from Conexion import conectar

def consulta_email(): 
    con = conectar()
    cursor = con.cursor() 
    consulta = "SELECT email from usuarios"
    cursor.execute(consulta)
    filas = cursor.fetchall()
    print(filas)
    con.commit()
    cursor.close()
    con.close()
    usuarios=[]
    for fila in filas:
        usuarios.append(fila[0])
    print(usuarios) 
    return usuarios

def detectar_condicion(datos):
    resultado=[]
    d=datos
    oxigeno = d["oxigeno"]
    temperatura = d['temperatura']
    fecha = d["fecha"]
    hora = d["hora"]
    if oxigeno<3 or oxigeno>8:
        resultado.append({'Oxígeno': oxigeno, 'Fecha': fecha, 'Hora':hora} )
    else:
        print("El oxigeno se encuentra en condiciones normales")
    if  temperatura<29 or temperatura>32:
        
        resultado.append({'Temperatura': temperatura, 'Fecha': fecha, 'Hora':hora})
    else:
        print("La temperatura se encuentra en condiciones normales")

    return resultado

