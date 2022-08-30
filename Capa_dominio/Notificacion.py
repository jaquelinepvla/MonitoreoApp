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
# Detecta si los datos se salen de los rangos establecidos para enviar las notificaciones 
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
        
        resultado.append({'Temperatura': temperatura, 'Fecha': tiempo})
    else:
        print("La temperatura se encuentra en condiciones normales")
    return resultado

