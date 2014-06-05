# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProducto.ui'
#
# Created: Sat May 31 16:32:12 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_nuevoProducto(object):
    def setupUi(self, nuevoProducto):
        nuevoProducto.setObjectName("nuevoProducto")
        nuevoProducto.resize(400, 300)
        self.Btn_add = QtGui.QPushButton(nuevoProducto)
        self.Btn_add.setGeometry(QtCore.QRect(80, 230, 95, 31))
        self.Btn_add.setObjectName("Btn_add")
        self.Btn_cancel = QtGui.QPushButton(nuevoProducto)
        self.Btn_cancel.setGeometry(QtCore.QRect(220, 230, 95, 31))
        self.Btn_cancel.setObjectName("Btn_cancel")
        self.label = QtGui.QLabel(nuevoProducto)
        self.label.setGeometry(QtCore.QRect(40, 40, 67, 21))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(nuevoProducto)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(nuevoProducto)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(nuevoProducto)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 67, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(nuevoProducto)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 67, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(nuevoProducto)
        self.label_6.setGeometry(QtCore.QRect(40, 190, 67, 21))
        self.label_6.setObjectName("label_6")
        self.codigo = QtGui.QLineEdit(nuevoProducto)
        self.codigo.setGeometry(QtCore.QRect(100, 40, 91, 21))
        self.codigo.setObjectName("codigo")
        self.nombre = QtGui.QLineEdit(nuevoProducto)
        self.nombre.setGeometry(QtCore.QRect(100, 70, 91, 21))
        self.nombre.setObjectName("nombre")
        self.descripcion = QtGui.QLineEdit(nuevoProducto)
        self.descripcion.setGeometry(QtCore.QRect(120, 100, 101, 21))
        self.descripcion.setObjectName("descripcion")
        self.color = QtGui.QLineEdit(nuevoProducto)
        self.color.setGeometry(QtCore.QRect(90, 130, 101, 21))
        self.color.setObjectName("color")
        self.precio = QtGui.QLineEdit(nuevoProducto)
        self.precio.setGeometry(QtCore.QRect(90, 160, 101, 21))
        self.precio.setObjectName("precio")
        self.marca = QtGui.QLineEdit(nuevoProducto)
        self.marca.setGeometry(QtCore.QRect(90, 190, 101, 21))
        self.marca.setObjectName("marca")

        self.retranslateUi(nuevoProducto)
        QtCore.QMetaObject.connectSlotsByName(nuevoProducto)

    def retranslateUi(self, nuevoProducto):
        nuevoProducto.setWindowTitle(QtGui.QApplication.translate("nuevoProducto", "Producto Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_add.setText(QtGui.QApplication.translate("nuevoProducto", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_cancel.setText(QtGui.QApplication.translate("nuevoProducto", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("nuevoProducto", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("nuevoProducto", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("nuevoProducto", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("nuevoProducto", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("nuevoProducto", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("nuevoProducto", "Marca", None, QtGui.QApplication.UnicodeUTF8))

