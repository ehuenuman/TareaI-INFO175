#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui
import shutil
import os
import controller
from nuevoProducto import Ui_nuevoProducto


class Form (QtGui.QDialog):
    def __init__(self, code=None, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.codi = code
        self.direccion_imagen = None
        if (self.codi is None):
            self.ui = Ui_nuevoProducto()
            self.ui.setupUi(self)
            self.ui.Btn_add.clicked.connect(self.add_valores)
            self.ui.Btn_cancel.clicked.connect(self.cancel)
            self.ui.imagenButton.clicked.connect(self.examinarImagen)
        else:
            self.edit = Ui_nuevoProducto()
            self.edit.setupUi(self)
            self.edit.setEdit(self)
            self.edit.Btn_add.clicked.connect(self.edit_valores)
            self.edit.Btn_cancel.clicked.connect(self.cancel)
            self.edit.imagenButton.clicked.connect(self.examinarImagen)

    def cancel(self):
        self.reject()

    def add_valores(self):
        cod = (self.ui.codigo.text())
        nom = (self.ui.nombre.text())
        des = (self.ui.descripcion.toPlainText())
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

            exito = controller.ingresar_producto(valores)
            if exito is False:
                mensaje = u"Código ya existe.\nIntente con otro."
                self.mensajeError(mensaje)
            else:
                if self.direccion_imagen is not None:
                    self.almacenarImagen(self.direccion_imagen, cod)
                self.reject()
        else:
            self.mensajeError(ingreso_valido)

    def llenarFormEditar(self, datos):
        self.edit.codigo.setText(datos[0])
        self.edit.nombre.setText(datos[1])
        self.edit.descripcion.setPlainText(datos[2])
        self.edit.color.setText(datos[3])
        self.edit.precio.setText(str(datos[4]))
        self.edit.marca.setText(datos[5])
        ficheros = os.listdir('ImgProductos/')
        fichero = datos[0] + ".jpg" in ficheros
        if fichero is True:
            direccion = 'ImgProductos/{0}'.format(datos[0] + ".jpg")
            self.edit.setImageLabel(direccion)
        else:
            fichero = datos[0] + ".png" in ficheros
            if fichero is True:
                direccion = 'ImgProductos/{0}'.format(datos[0] + ".png")
                self.edit.setImageLabel(direccion)
            else:
                self.edit.limpiarLabel()

    def edit_valores(self):
            cod = (self.edit.codigo.text())
            nom = (self.edit.nombre.text())
            des = (self.edit.descripcion.toPlainText())
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
                if self.direccion_imagen is not None:
                    self.almacenarImagen(self.direccion_imagen, cod)
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
                    mensaje = u"Algunos campos fueron ingresados"
                    mensaje = mensaje + " incorrectamente.\n"
                    mensaje = mensaje + "Recuerde que no se permiten simbolos."
                    mensaje = mensaje + "\nCorrija e intente nuevamente."
                    return mensaje
                else:
                    return True

    def mensajeError(self, mensaje):
        correctoQMessageBox = QtGui.QMessageBox()
        correctoQMessageBox.setWindowTitle("ERROR!")
        correctoQMessageBox.setText(mensaje)
        correctoQMessageBox.exec_()

    def examinarImagen(self):
        nueva_imagen = QtGui.QFileDialog.getOpenFileNames(self,
            "Abrir Imagenes", '', "Imagenes (*.png *.xpm *.jpg)")
            #";;All Files (*)")

        try:
            self.direccion_imagen = nueva_imagen[0][0]
        except:
            self.direccion_imagen = None
        try:
            self.ui.setImageLabel(self.direccion_imagen)
        except:
            pass
        try:
            self.edit.setImageLabel(self.direccion_imagen)
        except:
            pass

    def almacenarImagen(self, origen_imagen, nuevo_nombre):
        info = os.path.splitext(origen_imagen)
        extencion = info[1]
        destino_imagen = "ImgProductos/{0}{1}".format(nuevo_nombre, extencion)
        shutil.copy(origen_imagen, destino_imagen)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main_window = Form()
    main_window.show()
    sys.exit(app.exec_())