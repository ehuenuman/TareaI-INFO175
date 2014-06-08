#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def conectar():
    """Funcion que conecta a la base
    de datos de los usuarios y retorna
    un conector
    @return con"""
    con = sqlite3.connect('DatosUsuario.db')
    con.row_factory = sqlite3.Row
    return con


def confirmarDatos(user, password):
    """Funcion que busca el usuario en
    la base de datos y retorna un booleano
    @param user,password
    @return correcto"""
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


def nuevosDatos(user, password):
    """Funcion que ingresa un nuevo usuario
    en la base de datos y retorna un mensaje
    @param user,password
    @return mensaje"""
    con = conectar()
    c = con.cursor()
    query = ("SELECT * FROM Usuarios WHERE Usuario = ?")
    resultado = c.execute(query, [user])
    usuario = resultado.fetchall()
    if len(usuario) == 1:
        mensaje = u"El usuario ya existe."
    else:
        if len(user.lstrip()) == 0:
            mensaje = u"Usuario invalido.\nIngrese caracteres."
        else:
            if len(password.lstrip()) == 0:
                mensaje = u"Contraseña invalida.\nIngrese caracteres."
            else:
                query = ("""INSERT INTO Usuarios (
                    Usuario, Pass)
                    VALUES (?, ?)""")
                c.execute(query, [user, password])
                con.commit()
                mensaje = "Correcto"
    con.close()

    return mensaje