#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller
import view_form



class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.resize(900, 500)
        self.setWindowTitle("Tabla Productos Distribuidor")
        #http://srinikom.github.io/pyside-docs/PySide/QtGui/QVBoxLayout.html
        self.main_layout = QtGui.QVBoxLayout(self)
        #Dibujar grilla
        self.render_toolbox()
        self.render_table()
        self.load_data()
        self.set_signals()
        self.show()

    def render_toolbox(self):
        self.toolbox = QtGui.QWidget(self)
        self.tb_layout = QtGui.QHBoxLayout()
        self.tb_layout.setAlignment(QtCore.Qt.AlignRight)
        self.toolbox.setLayout(self.tb_layout)

        self.btn_add = QtGui.QPushButton(u"&Nuevo Producto")
        self.btn_edit = QtGui.QPushButton(u"&Editar")
        self.btn_delete = QtGui.QPushButton(u"&Borrar")
        #Agregamos los botones al layout
        self.tb_layout.addWidget(self.btn_add)
        self.tb_layout.addWidget(self.btn_edit)
        self.tb_layout.addWidget(self.btn_delete)
        #Agregamos el widget toolbox a la pantalla principal
        self.main_layout.addWidget(self.toolbox)

    def render_table(self):
        self.table = QtGui.QTableView(self)
        self.table.setFixedWidth(890)
        self.table.setFixedHeight(450)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.setSortingEnabled(True)
        #Se incorpora la tabla al layout
        self.main_layout.addWidget(self.table)

    def load_data(self):
        producto = controller.obtener_productos()
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(producto), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Código"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripción"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Marca"))

        r = 0
        for row in producto:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['precio'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['fk_id_marca'])
            r = r + 1
        self.table.setModel(self.model)

        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(1, 210)
        self.table.setColumnWidth(2, 210)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 100)

    def set_signals(self):
        self.btn_delete.clicked.connect(self.delete)
        self.btn_add.clicked.connect(self.show_form)
        self.btn_edit.clicked.connect(self.edit)

    def show_form(self):
        form = view_form.Form(self.code())
        form.rejected.connect(self.load_data)
        form.exec_()

    def delete(self):
        def borrar():
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(codigo)):
                self.load_data()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                self.msg.close()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("""Error al eliminar el
                                                        registro""")
                return False

        model = self.table.model()
        index = self.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            #caracteristicas ventana mensaje
            self.msg = QtGui.QWidget()
            self.msg.resize(260,100)
            self.msg.setMinimumSize(260, 100)
            self.msg.setMaximumSize(260, 100)
            self.msg.setWindowTitle('Mensaje')
            screen = QtGui.QDesktopWidget().screenGeometry()
            size = self.msg.geometry()
            self.msg.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

            self.ms_layout = QtGui.QVBoxLayout()
            self.men_label = QtGui.QLabel()
            self.men_label.setText(u"¿Desea borrar de la base de datos?")
            self.msg.setLayout(self.ms_layout)
            self.btn_ok = QtGui.QPushButton(u"&Confirmar")
            #Agregamos los botones  y label al layout
            self.ms_layout.addWidget(self.men_label)
            self.ms_layout.addWidget(self.btn_ok)

            self.msg.show()

            self.btn_ok.clicked.connect(borrar)


    def edit(self):
        index = self.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:

            form = view_form.Form(self.code())
            form.rejected.connect(self.load_data)
            form.exec_()
        self.load_data()


    def code(self):
        model = self.table.model()
        index = self.table.currentIndex()
        self.codi = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        return self.codi

def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()



