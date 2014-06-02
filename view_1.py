#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
import controller


class TablaProductos(QtGui.QWidget):
    def __init__(self):
        super(TablaProductos, self).__init__()
        self.resize(900, 500)
        self.setWindowTitle("Productos Distribuidor")
        #http://srinikom.github.io/pyside-docs/PySide/QtGui/QVBoxLayout.html
        self.main_layout = QtGui.QVBoxLayout(self)
        #Dibujar grilla
        self.render_toolbox()
        self.render_toolbox2()
        self.render_proxyTable()
        self.load_data(TablaProductos)
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
        self.cb_marca.insertItem(0, u"Todas")

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

    def render_proxyTable(self):
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.proxyView = QtGui.QTreeView()
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.main_layout.addWidget(self.proxyView)

        self.proxyView.sortByColumn(1, QtCore.Qt.AscendingOrder)

    def setSourceModel(self, modelo):
        self.proxyModel.setSourceModel(modelo)

    def load_data(self, parent):
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

        self.proxyView.setModel(self.model)

        self.proxyView.setColumnWidth(0, 80)
        self.proxyView.setColumnWidth(1, 150)
        self.proxyView.setColumnWidth(2, 270)
        self.proxyView.setColumnWidth(3, 100)
        self.proxyView.setColumnWidth(4, 150)
        self.proxyView.setColumnWidth(5, 100)

    def set_signals(self):
        self.btn_delete.clicked.connect(self.delete)
        self.busqueda_rapida.textChanged.connect(self.filtrarProductos)

    def delete(self):
        model = self.proxyTable.model()
        index = self.proxyTable.currentIndex()
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

    def filtrarProductos(self):
        print "Filtrando"
        self.proxyModel.setFilterKeyColumn(1)
        regExp = QtCore.QRegExp(self.busqueda_rapida.text(),
                QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)

        self.proxyModel.setFilterRegExp(regExp)


def run():

    app = QtGui.QApplication(sys.argv)
    tabla = TablaProductos()
    #tabla.setSourceModel(load_data(tabla))
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()



