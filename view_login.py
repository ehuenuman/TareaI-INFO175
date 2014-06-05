#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui
from login_user import Ui_LoginUser
import controller_user
import tabla_productos


class FormLoginUser (QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_LoginUser()
        self.ui.setupUi(self)
        #Señales
        self.ui.loginButton.clicked.connect(self.checkIngreso)
        self.ui.nuevaCuentaButton.clicked.connect(self.nuevaCuenta)

    def checkIngreso(self):
        usuario = self.ui.usuarioLineEdit.text()
        password = self.ui.passLineEdit.text()
        correcto = controller_user.confirmarDatos(usuario, password)
        if correcto:
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("LOGIN")
            correctoQMessageBox.setText(u"Identificación Correcta!")
            correctoQMessageBox.exec_()

            app = tabla_productos.TablaProductos()
            app.setSourceModel(app.loadData(app))
            self.ui.closeDialog(self)

        else:
            correctoQMessageBox = QtGui.QMessageBox()
            correctoQMessageBox.setWindowTitle("ERROR!")
            correctoQMessageBox.setText(u"""Usuario y/o contraseña incorrecta.
                                        \nIntente nuevamente!""")
            correctoQMessageBox.exec_()

    def nuevaCuenta(self):
        pass

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = FormLoginUser()
    main_window.show()
    sys.exit(app.exec_())