from datetime import date
import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="contraseña",
    database="postgres",
    port="5432"
)
nombre = str(input("Ingrese nombre de usuario: "))
def calcular_edad_años(fecha_nacimiento):
    fecha_actual = date.today()
    
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) <  (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

    
    

fecha_nacimiento_usuario = date(int(input("ingrese el año de nacimiento: ")),int(input("ingrese el mes: ")),int(input("ingrese el dia: ")))
edad = calcular_edad_años(fecha_nacimiento_usuario)
print(f'Esta persona cumplió {edad} años.')
connection.autocommit = True
def insertardatos(usuario,edad):
    cursor = connection.cursor()
    query = f""" INSERT INTO problema1p1 (usuario,edad) values('{usuario}','{edad}')"""
    cursor.execute(query)
    cursor.close()
insertardatos(nombre,edad)