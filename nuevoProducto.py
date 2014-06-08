# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProducto.ui'
#
# Created: Sun Jun  8 05:57:54 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_nuevoProducto(object):
    def setupUi(self, nuevoProducto):
        """Constructor principal del formulario nuevo producto
        @param nuevoProducto"""
        nuevoProducto.setObjectName("nuevoProducto")
        nuevoProducto.resize(458, 490)
        self.Btn_add = QtGui.QPushButton(nuevoProducto)
        self.Btn_add.setGeometry(QtCore.QRect(110, 450, 95, 31))
        self.Btn_add.setObjectName("Btn_add")
        self.Btn_cancel = QtGui.QPushButton(nuevoProducto)
        self.Btn_cancel.setGeometry(QtCore.QRect(250, 450, 95, 31))
        self.Btn_cancel.setObjectName("Btn_cancel")
        self.label = QtGui.QLabel(nuevoProducto)
        self.label.setGeometry(QtCore.QRect(40, 60, 67, 31))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(nuevoProducto)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 67, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(nuevoProducto)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(nuevoProducto)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 67, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(nuevoProducto)
        self.label_5.setGeometry(QtCore.QRect(40, 290, 67, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(nuevoProducto)
        self.label_6.setGeometry(QtCore.QRect(40, 330, 67, 31))
        self.label_6.setObjectName("label_6")
        self.codigo = QtGui.QLineEdit(nuevoProducto)
        self.codigo.setGeometry(QtCore.QRect(120, 60, 113, 31))
        self.codigo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.codigo.setObjectName("codigo")
        self.nombre = QtGui.QLineEdit(nuevoProducto)
        self.nombre.setGeometry(QtCore.QRect(120, 100, 113, 31))
        self.nombre.setInputMethodHints(QtCore.Qt.ImhNone)
        self.nombre.setObjectName("nombre")
        self.color = QtGui.QLineEdit(nuevoProducto)
        self.color.setGeometry(QtCore.QRect(120, 250, 113, 31))
        self.color.setObjectName("color")
        self.precio = QtGui.QLineEdit(nuevoProducto)
        self.precio.setGeometry(QtCore.QRect(120, 290, 113, 31))
        self.precio.setObjectName("precio")
        self.marca = QtGui.QLineEdit(nuevoProducto)
        self.marca.setGeometry(QtCore.QRect(120, 330, 113, 31))
        self.marca.setObjectName("marca")
        self.imagenButton = QtGui.QPushButton(nuevoProducto)
        self.imagenButton.setGeometry(QtCore.QRect(136, 370, 81, 61))
        self.imagenButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ImgProductos/buscarImagen1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imagenButton.setIcon(icon)
        self.imagenButton.setIconSize(QtCore.QSize(50, 50))
        self.imagenButton.setObjectName("imagenButton")
        self.imagenLabel = QtGui.QLabel(nuevoProducto)
        self.imagenLabel.setGeometry(QtCore.QRect(250, 280, 180, 150))
        self.imagenLabel.setText("")
        self.imagenLabel.setPixmap(QtGui.QPixmap("ImgProductos/No Imagen.png"))
        self.imagenLabel.setScaledContents(True)
        self.imagenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagenLabel.setWordWrap(False)
        self.imagenLabel.setOpenExternalLinks(False)
        self.imagenLabel.setObjectName("imagenLabel")
        self.descripcion = QtGui.QPlainTextEdit(nuevoProducto)
        self.descripcion.setGeometry(QtCore.QRect(120, 140, 200, 100))
        self.descripcion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.descripcion.setFrameShadow(QtGui.QFrame.Sunken)
        self.descripcion.setObjectName("descripcion")
        self.label_8 = QtGui.QLabel(nuevoProducto)
        self.label_8.setGeometry(QtCore.QRect(380, 260, 67, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line = QtGui.QFrame(nuevoProducto)
        self.line.setGeometry(QtCore.QRect(250, 270, 118, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.borrarImagenButton = QtGui.QPushButton(nuevoProducto)
        self.borrarImagenButton.setGeometry(QtCore.QRect(400, 390, 40, 40))
        self.borrarImagenButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ImgProductos/eliminarImagen1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.borrarImagenButton.setIcon(icon1)
        self.borrarImagenButton.setIconSize(QtCore.QSize(30, 30))
        self.borrarImagenButton.setObjectName("borrarImagenButton")
        self.label_7 = QtGui.QLabel(nuevoProducto)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Cantarell")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(nuevoProducto)
        QtCore.QObject.connect(self.Btn_cancel, QtCore.SIGNAL("clicked()"), nuevoProducto.close)
        QtCore.QObject.connect(self.borrarImagenButton, QtCore.SIGNAL("clicked()"), self.limpiarLabel)
        QtCore.QMetaObject.connectSlotsByName(nuevoProducto)

    def setImageLabel(self, direccion):
        """Funcion que asigna una imagen
        @param direccion"""
        self.imagenLabel.setPixmap(QtGui.QPixmap(direccion))

    def limpiarLabel(self):
        """Funcion que limpia el label de la imagen"""
        self.imagenLabel.setPixmap(QtGui.QPixmap("ImgProductos/No Imagen.png"))

    def setEdit(self, nuevoProducto):
        """Funcion que asigna un texto a la ventana principal
        y un texto al boton guardar en el formulario
        @param nuevoProducto"""
        nuevoProducto.setWindowTitle("Editar Producto")
        self.Btn_add.setText("&Guardar")

    def retranslateUi(self, nuevoProducto):
        """Funcion que asigna los textos a los elementos del formulario nuevo producto
        @param nuevoProducto"""
        nuevoProducto.setWindowTitle(QtGui.QApplication.translate("nuevoProducto", "Nuevo Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_add.setText(QtGui.QApplication.translate("nuevoProducto", "&Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.Btn_cancel.setText(QtGui.QApplication.translate("nuevoProducto", "&Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("nuevoProducto", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("nuevoProducto", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("nuevoProducto", "Descripcion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("nuevoProducto", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("nuevoProducto", "Precio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("nuevoProducto", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.imagenButton.setToolTip(QtGui.QApplication.translate("nuevoProducto", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Añada una imagen a su producto.</span></p><p align=\"center\"><span style=\" font-size:10pt;\">Tamaño recomendado 170px x 150px</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("nuevoProducto", "Preview:", None, QtGui.QApplication.UnicodeUTF8))
        self.borrarImagenButton.setToolTip(QtGui.QApplication.translate("nuevoProducto", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Eliminar imagen</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("nuevoProducto", "Complete el formulario y confirme para guardar los datos.", None, QtGui.QApplication.UnicodeUTF8))

