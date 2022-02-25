import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="contraseña",
    database="postgres",
    port="5432"
)

while True:
    try:
        a1 = int(input("Ingrese el valor del primer angulo: "))
        a2 = int(input("Ingrese el valor del segundo angulo "))
        print("Que opción desea realizar: ")
        op = str(input(""" Menú:
        1- Encontrar el tercer angulo
        2- Ver historial \n"""))
    except: 
        print ("ERROR")
        op = '?'

    if op == '1':
        a3= 180-a1-a2
        connection.autocommit = True
        def insertardatos(angulo1,angulo2,angulo3):
            cursor = connection.cursor()
            query = f""" INSERT INTO problema2p2 (angulo1,angulo2, angulo3) values('{angulo1}','{angulo2}','{angulo3}')"""
            cursor.execute(query)
            cursor.close()
        insertardatos(a1,a2,a3)
        print("El angulo 3 es: ",a3)
        break
    elif op == '2':
        
        cursor = connection.cursor()
        SQL = 'select * from problema2p2;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        break
    else:
        print("""has ingresado una opción incorrecta""")


