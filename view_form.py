#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide import QtGui, QtCore
import controller
from nuevoProducto import Ui_nuevoProducto

class Form (QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_nuevoProducto()
        self.ui.setupUi(self)
        self.ui.Btn_add.clicked.connect(self.add_valores)
        self.ui.Btn_cancel.clicked.connect(self.reject)
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
        print self.valores[0]
#        print valores[1]
#        print valores[2]
#        print valores[3]
#        print valores[4]
#        print valores[5]
#        self.reject()
        return self.valores

