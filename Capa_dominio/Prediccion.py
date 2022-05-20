from datetime import date, timedelta
import datetime
from pprint import pprint
from time import time
from webbrowser import get
from Conexion import conectar;
from datetime import datetime

def prediccion_temp():
    con = conectar()
    cursor = con.cursor() 
    di="Select temperatura from parametros order by id asc limit 1;"
    df="Select temperatura from parametros order by id desc limit 1;"
    ti="Select hora from parametros order by id asc limit 1;"
    tf="Select hora from parametros order by id desc limit 1;"
    oi="Select oxigeno from parametros order by id asc limit 1;"
    of="Select oxigeno from parametros order by id desc limit 1;"
    cursor.execute(di)
    cdi=cursor.fetchone()
    cursor.execute(df)
    cdf=cursor.fetchone()
    cursor.execute(ti)
    cti=cursor.fetchone()
    cursor.execute(tf)
    ctf=cursor.fetchone()
    cursor.execute(oi)
    coi=cursor.fetchone()
    cursor.execute(of)
    cof=cursor.fetchone()
   
    con.commit()
    cursor.close()
    con.close()
   
    tiempoi = cti[0].strftime('%H:%M:%S')
    tsi = get_hra(tiempoi)
    tiempof = ctf[0].strftime('%H:%M:%S')
    tsf = get_hra(tiempof)
    
    pt=extrapolacion(tsi, tsf, cdi, cdf)
    po=extrapolacion(tsi, tsf, coi, cof)

    str_hp=get_string_hra(tsf+(5/60))
    
    almacear_prediccion(pt, po, str_hp, date.today())

def extrapolacion(xi, xf, yi, yf):
    di=float(yi[0])
    df=float(yf[0])
    print(yi, yf, di, df, xi, xf)
    xp= xf+5
    dx=xp-xi
    p=((df-di)/(xf-xi))*dx + di
    print(p)
    return format(p, '2.1f')

def get_hra(t):
    h, m, s = t.split(':')
    print()
    return int(h) + int(m)/60 + (int(s)/3600)

def get_string_hra(t):
    segundos=t*3600
    horas= segundos//3600
    sobrante1=segundos % 3600
    minutos= sobrante1//60
    sobrante2=sobrante1 % 60
    str='%s::%s::%s'  % (int(horas),int(minutos),int(sobrante2))
    hora = datetime.strptime(str, '%H::%M::%S').time()
    return hora
 

def almacear_prediccion(pt,po,h,f):
    con = conectar()
    cursor = con.cursor() 
    #Crear y ejecutar consulta
    consulta = "INSERT INTO prediccion(oxigeno, temperatura, fecha, hora) VALUES('{0}', '{1}', '{2}', '{3}')".format(po, pt, f, h) 
    cursor.execute(consulta)
    #Hacer cambios en la base de datos
    con.commit()
    #Cerrar cursor y conexión
    cursor.close()
    con.close()

def actualizacion_prediccion():
    con = conectar()
    cursor = con.cursor() 
    consulta = "SELECT * from prediccion order by id desc limit 10;"
    cursor.execute(consulta)
    registro=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return registro
