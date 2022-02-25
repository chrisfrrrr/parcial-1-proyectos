from datetime import date
def calcular_edad_años(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day)< (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

fecha_nacimiento_usuario = date(int(input("ingrese el año de nacimiento: ")),int(input("ingrese el mes: ")),int(input("ingrese el dia: ")))
edad = calcular_edad_años(fecha_nacimiento_usuario)
print(f'su edad es {edad} años.')