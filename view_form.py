#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import controller
from nuevoProducto import Ui_nuevoProducto
class Form (QtGui.QDialog):
    def __init__(self, code, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.codi = code
        self.ui = Ui_nuevoProducto()
        self.ui.setupUi(self)
        self.ui.Btn_add.clicked.connect(self.add_valores)
        self.ui.Btn_cancel.clicked.connect(self.add)
        self.edit = Ui_nuevoProducto()
        self.edit.setupUi(self)
        self.edit.Btn_add.clicked.connect(self.edit_valores)
        self.edit.Btn_cancel.clicked.connect(self.add)

    def add(self):
        self.reject()

    def add_valores(self):
        self.cod = str(self.ui.codigo.text())
        self.nom = str(self.ui.nombre.text())
        self.des = str(self.ui.descripcion.text())
        self.col = str(self.ui.color.text())
        self.pre = str(self.ui.precio.text())
        self.mar = str(self.ui.marca.text())
        self.valores = [self.cod, self.nom, self.des, self.col, self.pre, self.mar]

        marcas = controller.obtener_marcas()
        temp_marcas = [row["nombre"] for row in marcas]

        if self.valores[5] in temp_marcas:
            self.valores[5] = temp_marcas.index(self.valores[5]) + 1
        else:
            self.valores[5] = len(marcas) + 1
            id_marca = len(marcas) + 1
            controller.ingresar_marca(id_marca, self.valores[5])

        controller.ingresar_producto(self.valores)

        self.reject()

    def edit_valores(self):
            self.cod = str(self.edit.codigo.text())
            self.nom = str(self.edit.nombre.text())
            self.des = str(self.edit.descripcion.text())
            self.col = str(self.edit.color.text())
            self.pre = str(self.edit.precio.text())
            self.mar = str(self.edit.marca.text())
            self.valores = [self.cod, self.nom, self.des, self.col, self.pre, self.mar]

            marcas = controller.obtener_marcas()
            temp_marcas = [row["nombre"] for row in marcas]

            if self.valores[5] in temp_marcas:
                self.valores[5] = temp_marcas.index(self.valores[5]) + 1
            else:
                self.valores[5] = len(marcas) + 1
                id_marca = len(marcas) + 1
                controller.ingresar_marca(id_marca, self.valores[5])

            if(controller.update(self.codi,self.valores)):
                print "exito"

            self.reject()