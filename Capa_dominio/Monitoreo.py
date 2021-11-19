import json
from urllib import request
#from psycopg2 import connect
from Conexion import conectar
import socket
import time
import threading


def recibir_datos():
    PORT = 8085
    HOST ='127.0.0.1'
    #HOST = socket.gethostbyname(socket.gethostname())
    print(HOST)
    #AF_NET: para enviar información por la web  SOCK_STREM: TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ADDR = (HOST, PORT)
    FORMAT = 'utf-8'
    #SE ENVÍA UNA TUPLA CON EL HOST Y PORT PARA VINCULARSE
    server.bind((HOST, PORT)) 
    server.listen(5)
    #server es el socket para iniciar la comunicacion y commucation socket es el socket de comunicación
    #se espera por una conexión, cuando una conexion ocurre almacena el addres del servidor y luego 
    #almacena el objeto actual que nos permite enviar info de regreso a esa conexión   
    communication_socket, addres = server.accept()
    print(f"Conectado a {addres}")
    #server.bind((ADDR))
    #connected = True
    while True:
        #se reciben los datos, estableciendo el tamaño y el formato.
        data = communication_socket.recv(1024).decode(FORMAT)
        print(f"El mensaje del cliente es:  {data}")
        #se cierra la conexion 
        communication_socket.close()
        print(f"conexión con {addres} terminada")
        return data

    #js = json.loads(c.decode('utf-8'))
   

def almacenamiento(datos):  
    data=datos
    oxigeno = data["oxigeno"]
    temperatura = data["temperatura"]
    fecha = data["fecha"]
    hora = data["hora"]
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
    #time.sleep(300)
    return registro



   
    