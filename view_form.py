#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
import controller
from nuevoProducto import Ui_nuevoProducto


class Form (QtGui.QDialog):
    def __init__(self, code=None, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.codi = code
        if (self.codi is None):
            self.ui = Ui_nuevoProducto()
            self.ui.setupUi(self)
            self.ui.Btn_add.clicked.connect(self.add_valores)
            self.ui.Btn_cancel.clicked.connect(self.add)
        else:
            self.edit = Ui_nuevoProducto()
            self.edit.setupUi(self)
            self.edit.Btn_add.clicked.connect(self.edit_valores)
            self.edit.Btn_cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.reject()

    def add_valores(self):
        self.cod = (self.ui.codigo.text())
        self.nom = (self.ui.nombre.text())
        self.des = (self.ui.descripcion.text())
        self.col = (self.ui.color.text())
        self.pre = (self.ui.precio.text())
        self.mar = (self.ui.marca.text())

        valido = self.nom.isalpha()
        valido2 = self.des.isalpha()
        valido3 = self.col.isalpha()
        valido4 = self.pre.isdigit()
        valido5 = self.mar.isalpha()
        if(valido is False or valido2 is False or valido3 is False or valido4 is False or valido5 is False):
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("ERROR!")
            correctoQMessageBox.setText(u"""Campo ingresado incorrectamente.
                                        \nIntente nuevamente!""")
            correctoQMessageBox.exec_()
        else:
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
            self.cod = (self.edit.codigo.text())
            self.nom = (self.edit.nombre.text())
            self.des = (self.edit.descripcion.text())
            self.col = (self.edit.color.text())
            self.pre = (self.edit.precio.text())
            self.mar = (self.edit.marca.text())

            valido = self.nom.isalpha()
            valido2 = self.des.isalpha()
            valido3 = self.col.isalpha()
            valido4 = self.pre.isdigit()
            valido5 = self.mar.isalpha()
            if(valido is False or valido2 is False or valido3 is False or valido4 is False or valido5 is False):
                correctoQMessageBox = QtGui.QMessageBox()
                correctoQMessageBox.setWindowTitle("ERROR!")
                correctoQMessageBox.setText(u"""Campo ingresado incorrectamente.
                                            \nIntente nuevamente!""")
                correctoQMessageBox.exec_()
            else:
                self.valores = [self.cod, self.nom, self.des, self.col, self.pre, self.mar]

                marcas = controller.obtener_marcas()
                temp_marcas = [row["nombre"] for row in marcas]

                if self.valores[5] in temp_marcas:
                    self.valores[5] = temp_marcas.index(self.valores[5]) + 1
                else:
                    self.valores[5] = len(marcas) + 1
                    id_marca = len(marcas) + 1
                    controller.ingresar_marca(id_marca, self.valores[5])

                controller.update(self.codi,self.valores)

                self.reject()