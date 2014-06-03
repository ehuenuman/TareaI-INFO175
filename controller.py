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

def obtener_marca():
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM marcas"
    resultado = c.execute(query)
    marca = resultado.fetchall()
    con.close()
    return marca


def ingresar_productos(valores):
    con = conectar()
    c = con.cursor()
    query = "INSERT INTO productos (codigo,nombre,descripcion,color,precio,fk_id_marca)VALUES (?,?,?,?,?,?)"
    c.execute(query, valores)
    con.commit()

def ingresar_marca(valores):
    con = conectar()
    c = con.cursor()
    t=0
    marcas = obtener_marca()
    for row in marcas:
        t = t+1
    cont = t+1
    print t
    val = [cont,valores[5],"No disponible","No disponible"]
    query = "INSERT INTO marcas (id_marca,nombre,descripcion,pais)VALUES (?,?,?,?)"
    c.execute(query, val)
    con.commit()

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

    marcas = obtener_marca()
    t=0
    for row in marcas:
        t = t+1
    print t
