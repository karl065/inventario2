from datetime import date
import sqlite3 as db


def creardb():
    nombredb = input("Ingrese el nombre de la base de datos nueva: ") + ".db"
    conectar = db.connect(nombredb)
    conectar.commit()
    cursor = conectar.cursor()
    
    cursor.execute(
        """CREATE TABLE inventario (
            item INTEGER,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant_entradas INTEGER,
            cant_salidas INTEGER,
            stock INTEGER
            )"""
    )
    cursor.execute(
        """CREATE TABLE entradas (
            item INTEGER,
            fecha TEXT,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant INTEGER
            )"""
    )
    cursor.execute(
        """CREATE TABLE salidas (
            item INTEGER,
            fecha TEXT,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant INTEGER
            )"""
    )
    conectar.commit()    
    
    conectar.close
    

creardb()

def abrirdb():
    
    dbabierta = input("Ingrese la base de datos que quiere abrir: ") + ".db"
    
    conectar = db.connect(dbabierta)
    cursor = conectar.cursor()
    
    tabla = input("Indique la tabla que quiere seleccionar: ")
    instruccion = f"SELECT * FROM {tabla}"
    for datos in cursor.execute(instruccion):
        print(list(datos))
    conectar.commit()
    conectar.close()
    
#abrirdb()

def tablainventario():
    conectar = db.connect("databaseisd.db")
    cursor = conectar.cursor()
    cursor.execute(
        """CREATE TABLE inventario (
            item INTEGER,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant_entradas INTEGER,
            cant_salidas INTEGER,
            stock INTEGER
            )"""
    )
    cursor.execute(
        """CREATE TABLE entradas (
            item INTEGER,
            fecha TEXT,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant INTEGER
            )"""
    )
    cursor.execute(
        """CREATE TABLE salidas (
            item INTEGER,
            fecha TEXT,
            numero_de_parte INTEGER,
            modelo TEXT,
            descripcion TEXT,
            cant INTEGER
            )"""
    )
    conectar.commit()
    conectar.close 

    