#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    """Funcion que conecta la base de datos
    y retorna el conector
    @return con"""
    con = sqlite3.connect('EmpresaDistribuidora.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_productos():
    """Funcion que retorna la informacion de la tabla productos
    @return productos"""
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM productos"
    resultado = c.execute(query)
    productos = resultado.fetchall()
    con.close()
    return productos


def obtener_marcas():
    """Funcion que retorna el nombre de la marca
    en la tabla marcas
    @return temp_marcas"""
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre FROM marcas"
    resultado = c.execute(query)
    marcas = resultado.fetchall()
    con.close()
    temp_marcas = [row["nombre"] for row in marcas]
    return temp_marcas


def obtener_datosProducto(index):
    """Funcion que retorna los datos de un producto
    segun su codigo
    @param index
    @return datos_productos"""
    con = conectar()
    c = con.cursor()
    query = """SELECT nombre, descripcion, color, precio, fk_id_marca
            FROM productos WHERE codigo = ?"""
    resultado = c.execute(query, [index])
    producto = resultado.fetchall()
    con.close()
    for row in producto:
        datos_producto = [index, row[0], row[1], row[2], row[3], row[4]]
    marcas = obtener_marcas()
    datos_producto[5] = marcas[datos_producto[5] - 1]

    return datos_producto


def ingresar_producto(valores):
    """Funcion que ingresa un producto en la
    base de datos y retorna falso en caso
    contrario
    @param valores
    @return False"""
    con = conectar()
    c = con.cursor()
    query = """INSERT INTO productos (
        codigo, nombre, descripcion,
        color, precio, fk_id_marca)
        VALUES (?,?,?,?,?,?)"""
    try:
        c.execute(query, valores)
        con.commit()
    except sqlite3.IntegrityError:
        return False


def ingresar_marca(id_marca, nueva_marca):
    """Funcion que ingresa una marca en
    la base de datos
    @param id_marca,nueva_marca"""
    con = conectar()
    c = con.cursor()

    val = [id_marca, nueva_marca, "No disponible", "No disponible"]
    query = """INSERT INTO marcas (
        id_marca, nombre, descripcion, pais)
        VALUES (?,?,?,?)"""

    c.execute(query, val)
    con.commit()


def update(codigo, valores):
    """Funcion que edita un valor en la
    base de datos y retorna una variable
    booleana
    @param codigo,valores
    @return exito"""
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


def delete(codigo):
    """Funcion que elimina un producto de la
    base de datos segun su codigo y retorna
    una variable booleana
    @param codigo
    @return exito"""
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


if __name__ == '__main__':
    obtener_datosProducto("1020B")
