#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    con = sqlite3.connect('DatosUsuario.db')
    con.row_factory = sqlite3.Row
    return con


def confirmarDatos(user, password):
    con = conectar()
    c = con.cursor()
    query = ("SELECT * FROM Usuarios WHERE Usuario = ? AND Pass = ?")
    resultado = c.execute(query, [user, password])
    usuario = resultado.fetchall()
    con.close()
    if len(usuario) == 1:
        correcto = True

    else:
        correcto = False

    return correcto