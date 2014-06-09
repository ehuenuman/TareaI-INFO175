# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
#
# Created: Sat Jun  7 01:42:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_NewUser(object):
    def setupUi(self, Dialog):
        """Constructor del formulario nuevo usuario
        @param Dialog"""
        Dialog.setObjectName("NewUser")
        Dialog.resize(320, 195)
        self.usuarioLineEdit = QtGui.QLineEdit(Dialog)
        self.usuarioLineEdit.setGeometry(QtCore.QRect(140, 50, 113, 31))
        self.usuarioLineEdit.setObjectName("usuarioLineEdit")
        self.usuarioLabel = QtGui.QLabel(Dialog)
        self.usuarioLabel.setGeometry(QtCore.QRect(50, 50, 61, 31))
        self.usuarioLabel.setObjectName("usuarioLabel")
        self.passLabel = QtGui.QLabel(Dialog)
        self.passLabel.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.passLabel.setObjectName("passLabel")
        self.passLineEdit = QtGui.QLineEdit(Dialog)
        self.passLineEdit.setGeometry(QtCore.QRect(140, 100, 113, 31))
        self.passLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.passLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passLineEdit.setReadOnly(False)
        self.passLineEdit.setObjectName("passLineEdit")
        self.instLabel = QtGui.QLabel(Dialog)
        self.instLabel.setGeometry(QtCore.QRect(20, 0, 281, 51))
        self.instLabel.setObjectName("instLabel")
        self.crearButton = QtGui.QPushButton(Dialog)
        self.crearButton.setGeometry(QtCore.QRect(70, 150, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.crearButton.setFont(font)
        self.crearButton.setObjectName("loginButton")
        self.cancelarButton = QtGui.QPushButton(Dialog)
        self.cancelarButton.setGeometry(QtCore.QRect(180, 150, 95, 31))
        self.cancelarButton.setObjectName("cancelarButton")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancelarButton, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeDialog(self, Dialog):
        """Funcion que cierra el formulario nuevo usuario
        @param Dialog"""
        Dialog.close()

    def retranslateUi(self, Dialog):
        """Funcion que asigna los textos a los elementos del
        formulario nuevo usuario
        @param Dialog"""
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nuevo Usuario", None, QtGui.QApplication.UnicodeUTF8))
        self.usuarioLabel.setText(QtGui.QApplication.translate("Dialog", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.passLabel.setText(QtGui.QApplication.translate("Dialog", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))
        self.instLabel.setText(QtGui.QApplication.translate("Dialog", "Ingrese sus datos", None, QtGui.QApplication.UnicodeUTF8))
        self.crearButton.setText(QtGui.QApplication.translate("Dialog", "&Crear", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelarButton.setText(QtGui.QApplication.translate("Dialog", "C&ancelar", None, QtGui.QApplication.UnicodeUTF8))

