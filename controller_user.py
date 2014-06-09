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


def nuevosDatos(nombre, user, password):
    con = conectar()
    c = con.cursor()
    query = ("SELECT * FROM Usuarios WHERE Usuario = ?")
    resultado = c.execute(query, [user])
    usuario = resultado.fetchall()
    if len(usuario) == 1:
        mensaje = u"El usuario ya existe."
    else:
        if len(nombre.strip()) == 0:
            mensaje = u"Ingrese un nombre."
        else:
            if len(user.strip()) == 0:
                mensaje = u"Usuario invalido.\nIngrese caracteres."
            else:
                if len(password.strip()) == 0:
                    mensaje = u"Contraseña invalida.\nIngrese caracteres."
                else:
                    query = ("""INSERT INTO Usuarios (
                        Nombre, Usuario, Pass)
                        VALUES (?, ?, ?)""")
                    c.execute(query, [nombre, user, password])
                    con.commit()
                    mensaje = "Correcto"
    con.close()

    return mensaje