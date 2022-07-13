from datetime import date, timedelta
import datetime
from itertools import count
from pprint import pprint
from time import time
from webbrowser import get
from Conexion import conectar;
from datetime import datetime
#import tensorflow as tf
#from tensorflow import keras
#from keras.models import load_model
#from sklearn.preprocessing import MinMaxScaler
#import pandas as pd

''' 
new_model =tf.keras.models.load_model('modelo_gru_1.h5')
new_model.summary()


# Ajustar el scaler usando los datos de entrada
temp_test = np.array(test_dataset['temperatura'])
oxg_test = np.array(test_dataset['oxigeno'])

# Aplicar el scaler a los datos
temperatura_test = temp_test.reshape(-1,1)
oxigeno_test = oxg_test.reshape(-1,1)

print(temp_test.shape)
print(temperatura_test.shape)

# Definir los rangos para cada variable 
scaler_t = MinMaxScaler(feature_range = (0,1))
scaler_o = MinMaxScaler(feature_range = (0,1))
# Ajustar el scaler usando los datos de entrenamiento
input_scaler_t = scaler_t.fit(temperatura_train)
input_scaler_o = scaler_o.fit(oxigeno_train)

# Aplicar el scaler a los datos de entrenamiento
train_norm_t = input_scaler_t.transform(temperatura_train)
train_norm_o = input_scaler_o.transform(oxigeno_train)



d_test={'oxigeno': test_norm_t.reshape(-1), 'temperatura': test_norm_o.reshape(-1)}

test_norm = pd.DataFrame(data=d_test)
def prediction(model):
    prediction = model.predict(data_test)
    temperatura_pred = prediction[:, 0].reshape(-1,1)
    oxigeno_pred = prediction[:, 1].reshape(-1,1)
    temp_pred_inverse = scaler_t.inverse_transform(temperatura_pred)
    oxg_pred_inverse = scaler_o.inverse_transform(oxigeno_pred)
    d= {'temperatura': temp_pred_inverse.reshape(-1), 'oxigeno': oxg_pred_inverse.reshape(-1)}
    df_pred = pd.DataFrame(data=d)
    return df_pred


prediction_gru = prediction(new_model)
'''



def prediccion_temp():

    con = conectar()
    cursor = con.cursor() 
    d="Select * from parametros order by id desc limit 11;"
    cursor.execute(d)
    datos=cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    pronostico_t=[]
    pronostico_o=[]
    d=datos[::-1]
    datos_f=d[10]
    tiempo_f=datos_f[5]
    oxig_f=datos_f[1]
    temp_f= datos_f[2]
    count=1
    incremento = timedelta(minutes=5)
    xf=tiempo_f
    tiempo=[]
    for dato in d:
        tiempo_i=dato[5]
        oxig_i=dato[1]
        temp_i=dato[2]
        p_temp=extrapolacion(tiempo_i, tiempo_f, temp_i, temp_f)   
        p_oxigeno=extrapolacion(tiempo_i, tiempo_f, oxig_i, oxig_f)
        pronostico_t.append(p_temp)  
        pronostico_o.append(p_oxigeno)
        xf+=incremento
        tiempo.append(xf)
        print(tiempo)
        #lmacenar_prediccion(p_oxigeno, p_temp, xf)
        count+=1
        if count>10:
            break

def extrapolacion(xi, xf, yi, yf):
    incremento = timedelta(minutes=5)
    di=float(yi)
    df=float(yf)
    print(yi, yf, di, df, xi, xf)
    xp= xf+incremento
    dx=resta_tiempo(xp, xi)
    dt=resta_tiempo(xf, xi)
    p=((df-di)/(dt))*dx + di
    print(p)
    return format(p, '2.1f')

def resta_tiempo(datef, datei):
 
    año=datef.year-datei.year
    mes=datef.month-datei.month
    dias=datef.day-datei.day
    minutos=datef.minute-datei.minute
    segundos=datef.second-datei.second

    hora1=datei.hour
    hora2=datef.hour
    if hora1==00:
        hora1=24
    if hora2==00:
        hora2=24
    horas = hora2-hora1
    a=año*31536000
    m=mes*2592000
    d=dias*86400
    h=horas*3600
    m=minutos*60
    
    total = a + m + d + h + m + segundos
    print('este es el total', total, a, m, d, h, m, segundos)
    return total

def almacenar_prediccion(o, temp, t):
    con = conectar()
    cursor = con.cursor() 
    #Crear y ejecutar consulta
    consulta = "INSERT INTO prediccion(oxigeno, temperatura, tiempo) VALUES('{0}', '{1}', '{2}')".format(o, temp, t) 
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



'''def get_hra(t):
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
 '''
