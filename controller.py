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


def delete(codigo):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM productos WHERE codigo = ?"
    try:
        resultado = c.execute(query, [codigo])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

if __name__ == "__main__":

    productos = obtener_productos()
    for producto in productos:
        print producto["nombre"]
