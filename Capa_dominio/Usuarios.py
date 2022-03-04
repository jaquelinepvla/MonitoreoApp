from Conexion import conectar
from flask_login import UserMixin
conn = conectar()
cursor= conn.cursor()

class Usuario(UserMixin):
    def __init__(self, id, nombre, email, usuario, contrasena):
        self.id=id
        self.nombre=nombre
        self.email=email
        self.usuario=usuario
        self.contrasena=contrasena

    def registro(self):

        #conn = conectar()
        #cursor= conn.cursor()
        
        consulta1 = "SELECT * from usuarios where email='{0}'or usuario='{1}' ".format(self.email, self.usuario)
        consulta2 = "INSERT INTO usuarios (email, nombre, usuario, contrasena) VALUES('{0}', '{1}', '{2}', '{3}')".format(self.email, self.nombre, self.usuario, self.contrasena)
        cursor.execute(consulta1)
        filas = cursor.fetchone()
        print(filas)
        
        if filas is None:
            cursor.execute(consulta2)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else: 
            print ('El nombre de usuario o el email ya se han registrado')
            return  False
       
    def acceso(self):

        consulta = "SELECT*from usuarios where usuario='{0}' and contrasena= '{1}' ".format(self.usuario, self.contrasena)
        conn = conectar()
        cursor= conn.cursor()
        cursor.execute(consulta)
        filas = cursor.fetchone()
        print(self.usuario, self.contrasena)
        conn.commit()
        cursor.close()
        conn.close()
        
        if filas is not None:
            return True
        else: 
            return False

    def actualizar_contrasena(self):
        
        consulta = "UPDATE usuarios SET contrasena='{1}' WHERE email='{0}'".format(self.email, self.contrasena)
        conn = conectar()
        cursor=conn.cursor()
        cursor.execute(consulta)
        conn.commit()
        cursor.close()
        conn.close()
        print('Se actualizo la contraseña con exito')
       
       
    def verificar_email(self):
        
        consulta = "SELECT * from usuarios where email='{0}'".format(self.email)
        conn = conectar()
        cursor=conn.cursor()
        cursor.execute(consulta)
        filas = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if filas is not None:
            return True
        else: 
            return False
'''            
def obtenerid(self):
        consulta = "SELECT id, nombre, usuario from usuarios where id='{0}'".format(self.id)
        conn = conectar()
        cursor=conn.cursor()
        cursor.execute(consulta)
        filas = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if filas is not None:
            logged_user= filas
            return logged_user
        else: 
            return None''' 
'''            
def get_id(self):

        consulta = "SELECT id from usuarios where usuario='{0}'".format(self.usuario)
        cursor=conn.cursor()
        cursor.execute(consulta)
        filas = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        if filas is not None:
            id = filas
            return id
        else: 
            return None''' 

