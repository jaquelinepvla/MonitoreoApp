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
    oxigeno = d["O"]
    temperatura = d["T"]
    tiempo = d["F"]  + ' ' + d["H"]
    #fecha = d["F"]
    #hora = d["H"]
    if oxigeno<3 or oxigeno>8:
        resultado.append({'Oxígeno': oxigeno, 'Fecha': tiempo} )
    else:
        print("El oxigeno se encuentra en condiciones normales")
    if  temperatura<29 or temperatura>32:
        
<<<<<<< HEAD
        resultado.append({'Temperatura': temperatura, 'Fecha': tiempo})
=======
        resultado.append({'Temperatura': temperatura, 'Fecha': fecha, 'Hora':hora})
>>>>>>> 891d60ac1912d1a49be323c36494c48e192f6302
    else:
        print("La temperatura se encuentra en condiciones normales")


    return resultado

