#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller


class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.resize(900, 500)
        self.setWindowTitle("Tabla Productos Distribuidor")
        #http://srinikom.github.io/pyside-docs/PySide/QtGui/QVBoxLayout.html
        self.main_layout = QtGui.QVBoxLayout(self)
        #Dibujar grilla
        self.render_toolbox()
        self.render_toolbox2()
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

    def render_toolbox2(self):

        self.toolbox2 = QtGui.QWidget(self)
        self.tb2_layout = QtGui.QHBoxLayout()
        self.tb2_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.toolbox2.setLayout(self.tb2_layout)

        self.label_producto = QtGui.QLabel(self)
        self.label_producto.setText(u"¿Qué producto está buscando?:")
        self.busqueda_rapida = QtGui.QLineEdit()

        self.label_marca = QtGui.QLabel(self)
        self.label_marca.setText(u"Seleccione Marca:")
        self.cb_marca = QtGui.QComboBox(self)
        self.cb_marca.insertItem(0, u"\t")

        marcas = controller.obtener_marcas()
        index = 1
        for row in marcas:
            self.cb_marca.insertItem(index, row["nombre"])
            index = index + 1

        self.tb2_layout.addWidget(self.label_producto)
        self.tb2_layout.addWidget(self.busqueda_rapida)
        self.tb2_layout.addWidget(self.label_marca)
        self.tb2_layout.addWidget(self.cb_marca)

        self.main_layout.addWidget(self.toolbox2)

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

        marcas = controller.obtener_marcas()
        temp_marcas = [row["nombre"] for row in marcas]

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
            self.model.setData(index, temp_marcas[row['fk_id_marca'] - 1])
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

    def delete(self):
        model = self.table.model()
        index = self.table.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(codigo)):
                self.load_data()
                msgBox = QtGui.QMessageBox()
                msgBox.setText("EL registro fue eliminado.")
                msgBox.exec_()
                return True
            else:
                self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                self.ui.errorMessageDialog.showMessage("""Error al eliminar el
                                                        registro""")
                return False


def run():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()



