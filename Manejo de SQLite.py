import sqlite3 as sql

#Crear base de datos

def crearDB(): 
    conn = sql.connect("pruebas.db") #se conecta con la base de datos
    conn.commit()
    conn.close

# Crear una tabla en la base de datos
 
def creartabla(): 
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE prueba (
            nombre text,
            seguidores integer,
            subscritos integer
        )"""
    )
    
    conn.commit()
    conn.close()

"""Insertar datos, se puede combinar con input al momento de llamar la funcion
para ingresar los datos desde la consola""" 

def insertar_datos(nombre, seguidores, subscritos): 
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"INSERT INTO prueba VALUES ('{nombre}', {seguidores}, {subscritos})" # Se realizan las operaciones en SQL 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

#Leer datos de la tabla e imprimirlos en listas

def leer_datos():
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM prueba"
    for datos in cursor.execute(instruccion):
        print(list(datos))
    conn.commit()
    conn.close()
      
def insertar_varios_datos(pruebalist):
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"INSERT INTO prueba VALUES (?, ?, ?)"
    cursor.executemany(instruccion, pruebalist)
    conn.commit()
    conn.close()    

def leerOrdenado(campo):
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM prueba ORDER BY {campo}"
    for datos in cursor.execute(instruccion):
        print(list(datos))
    conn.commit()
    conn.close()
    
def buscar():
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM prueba WHERE nombre like '{input('Cual es el nombre que busca: ')}%'"
    for datos in cursor.execute(instruccion):
        print(list(datos))
    conn.commit()
    conn.close()
    
def actualizar_datos():
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    nombre = input("Ingrese el nombre a actualizar: ")
        
    def opciones():
        while (True):
            opcion = int(input("seleccione 1 para actualizar seguidores o 2 para subscritores: "))
            if opcion == 1 or opcion == 2:
                if opcion == 1:
                    seguidores = input("Ingrese el numero de seguidores a actualizar: ")
                    instruccion = f"UPDATE prueba SET seguidores = {seguidores} WHERE nombre = '{nombre}'"
                    cursor.execute(instruccion)
                elif opcion == 2:
                    subscritos = input("Ingrese el numero de subscritos a actualizar: ")
                    instruccion = f"UPDATE prueba SET subscritos = {subscritos} WHERE nombre = '{nombre}'"
                    cursor.execute(instruccion)
                    
                conn.commit()
                conn.close()
            elif opcion != 1 or opcion != 2:
                print("Ingrese 1 o 2")
                opciones()
            
            def opcion_2():
                opcion2 = int(input("Desea actualizar otro dato: 1 para si, 2 para no: "))
                if opcion2 == 1:
                    actualizar_datos()
                elif opcion2 == 2:
                    pass
                elif opcion != 1 or opcion != 2:
                    print("Ingrese 1 o 2")
                    opcion_2()
            opcion_2()
                    
            break
    
    opciones()
    
def borrar():
    conn = sql.connect("pruebas.db") #Se conecta con la base de datos
    cursor = conn.cursor()
    instruccion = f"DELETE FROM prueba WHERE nombre = '{input('Cual nombre desea borrar: ')}'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()  
    
if __name__ == "__main__":
    #crearDB()
    #creartabla()
    #insertar_datos(input("Ingrese el nombre: "), input("Ingrese los seguidores: "), input("Ingrese los subscritos: "))
    leer_datos()
    pruebalista = [
        ("alberto", 50000, 10000),
        ("jose", 500000, 65000),
        ("karlos", 999999, 999999)
    ]    
    #insertar_varios_datos(pruebalista)
    #leerOrdenado("nombre")
    #buscar()
    #actualizar_datos()
    #borrar()