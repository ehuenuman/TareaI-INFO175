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
            self.ui.Btn_cancel.clicked.connect(self.cancel)
        else:
            self.edit = Ui_nuevoProducto()
            self.edit.setupUi(self)
            self.edit.Btn_add.clicked.connect(self.edit_valores)
            self.edit.Btn_cancel.clicked.connect(self.cancel)

    def cancel(self):
        self.reject()

    def add_valores(self):
        cod = (self.ui.codigo.text())
        nom = (self.ui.nombre.text())
        des = (self.ui.descripcion.text())
        col = (self.ui.color.text())
        pre = (self.ui.precio.text())
        mar = (self.ui.marca.text())

        ingreso_valido = self.validar(nom, des, col, pre, mar)

        if ingreso_valido is True:
            valores = [cod, nom, des, col, pre, mar]

            marcas = controller.obtener_marcas()

            if valores[5] in marcas:
                valores[5] = marcas.index(valores[5]) + 1
            else:
                valores[5] = len(marcas) + 1
                id_marca = len(marcas) + 1
                controller.ingresar_marca(id_marca, valores[5])

            controller.ingresar_producto(valores)
            self.reject()
        else:
            self.mensajeError(ingreso_valido)

    def llenarFormEditar(self, datos):
        self.edit.codigo.setText(datos[0])
        self.edit.nombre.setText(datos[1])
        self.edit.descripcion.setText(datos[2])
        self.edit.color.setText(datos[3])
        self.edit.precio.setText(str(datos[4]))
        self.edit.marca.setText(datos[5])

    def edit_valores(self):
            cod = (self.edit.codigo.text())
            nom = (self.edit.nombre.text())
            des = (self.edit.descripcion.text())
            col = (self.edit.color.text())
            pre = (self.edit.precio.text())
            mar = (self.edit.marca.text())

            ingreso_valido = self.validar(nom, des, col, pre, mar)

            if ingreso_valido is True:
                valores = [cod, nom, des, col, pre, mar]

                marcas = controller.obtener_marcas()

                if valores[5] in marcas:
                    valores[5] = marcas.index(valores[5]) + 1
                else:
                    valores[5] = len(marcas) + 1
                    id_marca = len(marcas) + 1
                    controller.ingresar_marca(id_marca, valores[5])

                controller.update(self.codi, valores)
                self.reject()
            else:
                self.mensajeError(ingreso_valido)

    def validar(self, nom, des, col, pre, mar):
        valido = nom.replace(" ", "").isalnum()
        valido2 = des.replace(" ", "").isalnum()
        valido3 = col.replace(" ", "").isalpha()
        valido4 = pre.replace(" ", "").isdigit()
        valido5 = mar.replace(" ", "").isalnum()

        if valido4 is False:
            mensaje = u"Precio no valido.\nCorrija e intente nuevamente."
            return mensaje
        else:
            if valido3 is False:
                mensaje = u"Color no valido.\nCorrija e intente nuevamente."
                return mensaje
            else:
                if valido is False or valido2 is False or valido5 is False:
                    mensaje = u"""Algunos campos fueron ingresados
                              incorrectamente.\nCorrija e intente nuevamente."""
                    return mensaje
                else:
                    return True

    def mensajeError(self, mensaje):
        correctoQMessageBox = QtGui.QMessageBox()
        correctoQMessageBox.setWindowTitle("ERROR!")
        correctoQMessageBox.setText(mensaje)
        correctoQMessageBox.exec_()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main_window = Form()
    main_window.show()
    sys.exit(app.exec_())