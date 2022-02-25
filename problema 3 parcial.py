import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="contraseña",
    database="postgres",
    port="5432"
)


print("10. Mostrar la unidad, la decena y centena. ")

while True:
    try:
        num = int(input("Ingrese un numero comprendido entre 1 y 999: "))
        print("Que opción desea realizar: ")
        op = str(input(""" Menú:
        1- Mostrar las centenas, decenas, unidades 
        2- Ver historial \n"""))
    except: 
        print ("ERROR")
        op = '?'

    if op == '1':
        cen = (num-(num%100))/100
        res = num%100
        dec = (res-(res%10))/10
        uni = res%10
        print("Centena: ",int(cen))
        print("Decena: ",int(dec))
        print("Unidad:",int(uni))
        connection.autocommit = True
        def insertardatos(centena,decena,unidad):
            cursor = connection.cursor()
            query = f""" INSERT INTO problema3p1 (centena,decena,unidad) values('{centena}','{decena}','{unidad}')"""
            cursor.execute(query)
            cursor.close()
        insertardatos(cen,dec,uni)
            
        break
    elif op == '2':
        
        cursor = connection.cursor()
        SQL = 'select * from problema3p1;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
        break
    else:
        print("""has ingresado una opción incorrecta""")




