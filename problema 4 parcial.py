import random
import psycopg2

connection =  psycopg2.connect(
    host="localhost",
    user="postgres",
    password="contraseña",
    database="postgres",
    port="5432"
)

while True:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("Dado1: ",dado1)
    print("Dado2: ", dado2)

    try:
        if dado1 + dado2 == 8 : 
            print("\n ¡GANASTE!")
            connection.autocommit = True
            def insertardatos(dados,resultado):
                cursor = connection.cursor()
                query = f""" INSERT INTO problema4p1(dados,resultado) values('{dados}','{resultado}')"""
                cursor.execute(query)
                cursor.close()
            insertardatos(dado1+dado2,"ganó")
            break
        elif dado1 + dado2 == 7:
            print("\n Ouhhh... perdiste")
            connection.autocommit = True
            def insertardatos(dados,resultado):
                cursor = connection.cursor()
                query = f""" INSERT INTO problema4p1(dados,resultado) values('{dados}','{resultado}')"""
                cursor.execute(query)
                cursor.close()
            insertardatos(dado1+dado2,"perdió")
            break
        else:
            print("Intentalo de nuevo")
    except:
        break