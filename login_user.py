# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_user.ui'
#
# Created: Wed Jun  4 23:23:16 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LoginUser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login User")
        Dialog.resize(320, 240)
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
        self.loginButton = QtGui.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(70, 150, 95, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.cancelarButton = QtGui.QPushButton(Dialog)
        self.cancelarButton.setGeometry(QtCore.QRect(180, 150, 95, 31))
        self.cancelarButton.setObjectName("cancelarButton")
        self.nuevaCuentaButton = QtGui.QPushButton(Dialog)
        self.nuevaCuentaButton.setEnabled(True)
        self.nuevaCuentaButton.setGeometry(QtCore.QRect(90, 190, 151, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.nuevaCuentaButton.setFont(font)
        self.nuevaCuentaButton.setObjectName("nuevaCuentaButton")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancelarButton, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def closeDialog(self, Dialog):
        Dialog.close()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Confirmación de Identidad", None, QtGui.QApplication.UnicodeUTF8))
        self.usuarioLabel.setText(QtGui.QApplication.translate("Dialog", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.passLabel.setText(QtGui.QApplication.translate("Dialog", "Contraseña:", None, QtGui.QApplication.UnicodeUTF8))
        self.instLabel.setText(QtGui.QApplication.translate("Dialog", "Ingrese sus datos para verificar el ingreso. ", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setText(QtGui.QApplication.translate("Dialog", "&Login", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelarButton.setText(QtGui.QApplication.translate("Dialog", "&Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevaCuentaButton.setText(QtGui.QApplication.translate("Dialog", "Crear &Nueva Cuenta", None, QtGui.QApplication.UnicodeUTF8))

