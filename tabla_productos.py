#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys
import controller


class TablaProductos(QtGui.QWidget):
    def __init__(self):
        super(TablaProductos, self).__init__()

        self.tipoModel = None
        self.setWindowTitle("Productos Distribuidor")
        self.resize(900, 500)
        self.mainLayout = QtGui.QVBoxLayout()
        #Dibujar Interfaz
        self.renderToolBox()
        self.renderSearchToolBox()
        self.renderProxyTable()
        self.setSignals()
        self.show()

    def renderToolBox(self):
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
        self.mainLayout.addWidget(self.toolbox)

    def renderSearchToolBox(self):
        self.toolbox2 = QtGui.QWidget(self)
        self.tb2_layout = QtGui.QHBoxLayout()
        self.tb2_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.toolbox2.setLayout(self.tb2_layout)

        #Busqueda rápida de produtos mediante ingreso del usuario
        self.filtroBusquedaProductoLineEdit = QtGui.QLineEdit()
        self.filtroBusquedaProductoLabel = QtGui.QLabel(
            u"¿Qué producto está buscando?"
            )

        #Busqueda a travez del ComboBox de marcas
        self.filtroBusquedaMarcaLabel = QtGui.QLabel(u"Seleccione marca:")
        self.filtroBusquedaMarcaComboBox = QtGui.QComboBox()

        marcas = controller.obtener_marcas()
        index = 1
        self.filtroBusquedaMarcaComboBox.insertItem(0, u"Todas")
        for row in marcas:
            self.filtroBusquedaMarcaComboBox.insertItem(index, row["nombre"])
            index = index + 1

        self.tb2_layout.addWidget(self.filtroBusquedaProductoLabel)
        self.tb2_layout.addWidget(self.filtroBusquedaProductoLineEdit)
        self.tb2_layout.addWidget(self.filtroBusquedaMarcaLabel)
        self.tb2_layout.addWidget(self.filtroBusquedaMarcaComboBox)

        #self.filtroBusquedaProductosLineEdit.setText("Polera")
        #self.filtroBusquedaMarcaComboBox.setCurrentIndex(0)
        self.mainLayout.addWidget(self.toolbox2)

    def renderProxyTable(self):
        producto = controller.obtener_productos()
        self.proxyModel = QtGui.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)

        self.proxyGroupBox = QtGui.QGroupBox(
            u"Total Productos: {0}".format(len(producto))
            )

        self.proxyView = QtGui.QTreeView()
        self.proxyView.setRootIsDecorated(False)
        self.proxyView.setAlternatingRowColors(True)
        self.proxyView.setModel(self.proxyModel)
        self.proxyView.setSortingEnabled(True)

        self.proxyView.sortByColumn(1, QtCore.Qt.AscendingOrder)

        proxyLayout = QtGui.QVBoxLayout()
        proxyLayout.addWidget(self.proxyView)
        self.proxyGroupBox.setLayout(proxyLayout)

        self.mainLayout.addWidget(self.proxyGroupBox)

        self.setLayout(self.mainLayout)

    def setSourceModel(self, model):
        self.proxyModel.setSourceModel(model)
        #self.proxyView.setModel(model)

    def loadData(self, parent):
        self.tipoModel = parent
        producto = controller.obtener_productos()

        self.model = QtGui.QStandardItemModel(len(producto), 6, parent)
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

        return self.model

    def setSignals(self):
        self.btn_delete.clicked.connect(self.delete)
        self.filtroBusquedaProductoLineEdit.textChanged.connect(
            self.filtrarProductos
            )
        self.filtroBusquedaMarcaComboBox.currentIndexChanged.connect(
            self.filtrarMarca
            )

    def delete(self):
        model = self.proxyView.model()
        index = self.proxyView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            if (controller.delete(codigo)):
                self.setSourceModel(self.loadData(self.tipoModel))
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
        print "Filtro Productos"
        self.proxyModel.setFilterKeyColumn(1)

        productoAFiltrar = QtCore.QRegExp(self.filtroBusquedaProductoLineEdit.text(),
                QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)

        self.proxyModel.setFilterRegExp(productoAFiltrar)

    def filtrarMarca(self):
        print "Filtro Marca"
        self.proxyModel.setFilterKeyColumn(5)

        index = self.filtroBusquedaMarcaComboBox.currentIndex()
        if (index != 0):
            print "Filtrados"
            marcaFiltro = self.filtroBusquedaMarcaComboBox.itemText(index)

        else:
            print "Lista Completa"
            marcaFiltro = u"|"

        marcaAFiltrar = QtCore.QRegExp(
            marcaFiltro, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(marcaAFiltrar)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TablaProductos()
    window.setSourceModel(window.loadData(window))
    sys.exit(app.exec_())