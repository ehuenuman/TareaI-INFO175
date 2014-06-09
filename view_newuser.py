#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui
from new_user import Ui_NewUser
import controller_user


class FormNewUser (QtGui.QDialog):
    def __init__(self, parent=None):
        """Constructor del nuevo usuario"""
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_NewUser()
        self.ui.setupUi(self)
        #Señales
        self.ui.crearButton.clicked.connect(self.checkDatos)

    def checkDatos(self):
        """Funcion que crea el nuevo usuario"""
        nombre = self.ui.nombreLineEdit.text()
        usuario = self.ui.usuarioLineEdit.text()
        password = self.ui.passLineEdit.text()
        mensaje = controller_user.nuevosDatos(nombre, usuario, password)
        if mensaje is "Correcto":
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("Usuario Creado!")
            correctoQMessageBox.setText(u"""Nuevo usuario creado exitosamente.
                                        \nAhora ya se puede loguear.""")
            correctoQMessageBox.exec_()

            self.ui.closeDialog(self)

        else:
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("ERROR!")
            correctoQMessageBox.setText(mensaje)
            correctoQMessageBox.exec_()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = FormNewUser()
    main_window.show()
    sys.exit(app.exec_())