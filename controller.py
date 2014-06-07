#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('EmpresaDistribuidora.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_productos():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM productos"
    resultado = c.execute(query)
    productos = resultado.fetchall()
    con.close()
    return productos


def obtener_marcas():
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre FROM marcas"
    resultado = c.execute(query)
    marcas = resultado.fetchall()
    con.close()
    return marcas


<<<<<<< HEAD
def obtener_datosProducto(index):
    con = conectar()
    c = con.cursor()
    query = """SELECT * FROM productos WHERE codigo = ?"""
    resultado = c.execute(query, [index])
    producto = resultado.fetchall()
    con.close()
    print producto


def ingresar_producto(valores):
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO productos (
        codigo, nombre, descripcion,
        color, precio, fk_id_marca)
        VALUES (?,?,?,?,?,?)"""
    c.execute(query, valores)
    con.commit()


def ingresar_marca(id_marca, nueva_marca):
    con = conectar()
    c = con.cursor()

    val = [id_marca, nueva_marca, "No disponible", "No disponible"]
    query = """INSERT INTO marcas (
        id_marca, nombre, descripcion, pais)
        VALUES (?,?,?,?)"""

    c.execute(query, val)
    con.commit()


def update(codigo, valores):
    exito = False
    con = conectar()
    c = con.cursor()
    cod = valores[0]
    nom = valores[1]
    des = valores[2]
    col = valores[3]
    pre = valores[4]
    fk = valores[5]
    total = (cod, nom, des, col, pre, fk, codigo)
    query = '''UPDATE productos
            SET codigo=?,nombre=?,descripcion=?,color=?, precio=?,fk_id_marca=?
            WHERE codigo=? '''
    try:
        c.execute(query, total)
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:",e.arg[0]
    con.close()
    return exito


=======
>>>>>>> master
def delete(codigo):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM productos WHERE codigo = ?"
    try:
        c.execute(query, [codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito


<<<<<<< HEAD
if __name__ == '__main__':
    obtener_datosProducto("1020B")
>>>>>>> master
