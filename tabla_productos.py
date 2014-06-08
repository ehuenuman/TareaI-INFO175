#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
import sys
import controller
import view_form


class TablaProductos(QtGui.QWidget):
    def __init__(self):
        super(TablaProductos, self).__init__()

        self.tipoModel = None
        self.setWindowTitle("Productos Distribuidor")
        self.resize(900, 500)
        self.center()
        self.mainLayout = QtGui.QVBoxLayout()
        #Dibujar Interfaz
        self.renderToolBox()
        self.renderSearchToolBox()
        self.renderProxyTable()
        self.setSignals()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
        for i in range(len(marcas)):
            self.filtroBusquedaMarcaComboBox.insertItem(index, marcas[i])
            index = index + 1

        #Añadimos los Label, ComboBox y LineEdit al layout
        self.tb2_layout.addWidget(self.filtroBusquedaProductoLabel)
        self.tb2_layout.addWidget(self.filtroBusquedaProductoLineEdit)
        self.tb2_layout.addWidget(self.filtroBusquedaMarcaLabel)
        self.tb2_layout.addWidget(self.filtroBusquedaMarcaComboBox)

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

        self.proxyView.setColumnWidth(0, 80)
        self.proxyView.setColumnWidth(1, 160)
        self.proxyView.setColumnWidth(2, 270)
        self.proxyView.setColumnWidth(3, 100)
        self.proxyView.setColumnWidth(4, 120)
        self.proxyView.setColumnWidth(5, 90)

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
            self.model.setData(index, marcas[row['fk_id_marca'] - 1])
            r = r + 1

        return self.model

    def setSignals(self):
        self.btn_add.clicked.connect(self.add)
        self.btn_edit.clicked.connect(self.edit)
        self.btn_delete.clicked.connect(self.delete)
        self.filtroBusquedaProductoLineEdit.textChanged.connect(
            self.filtrarProductos
            )
        self.filtroBusquedaMarcaComboBox.currentIndexChanged.connect(
            self.filtrarMarca
            )

    def add(self):
        form = view_form.Form(self.code())
        form.exec_()
        self.setSourceModel(self.loadData(self.tipoModel))

    def edit(self):
        index = self.proxyView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR!")
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
        else:
            datos_producto = controller.obtener_datosProducto(self.code())
            form = view_form.Form(self.code())
            form.llenarFormEditar(datos_producto)
            form.exec_()
            self.setSourceModel(self.loadData(self.tipoModel))

    def code(self):
        model = self.proxyView.model()
        index = self.proxyView.currentIndex()
        self.codi = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        return self.codi

    def delete(self):
        index = self.proxyView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR!")
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
        else:
            #caracteristicas ventana mensaje
            self.msg = QtGui.QWidget()
            self.msg.resize(260, 100)
            self.msg.setMinimumSize(260, 100)
            self.msg.setMaximumSize(260, 100)
            self.msg.setWindowTitle('Mensaje')
            screen = QtGui.QDesktopWidget().screenGeometry()
            size = self.msg.geometry()
            self.msg.move(
                (screen.width() - size.width()) / 2,
                (screen.height() - size.height()) / 2
                )

            self.ms_layout = QtGui.QVBoxLayout()
            self.men_label = QtGui.QLabel()
            self.men_label.setText(u"¿Desea borrar de la base de datos?")
            self.msg.setLayout(self.ms_layout)
            self.btn_ok = QtGui.QPushButton(u"&Confirmar")
            #Agregamos los botones  y label al layout
            self.ms_layout.addWidget(self.men_label)
            self.ms_layout.addWidget(self.btn_ok)

            self.msg.show()

            self.btn_ok.clicked.connect(self.borrar)

    def borrar(self):
        model = self.proxyView.model()
        index = self.proxyView.currentIndex()
        codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        self.msg.close()
        if (controller.delete(codigo)):
            self.setSourceModel(self.loadData(self.tipoModel))
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Felicitaciones!")
            msgBox.setText("EL registro fue eliminado.")
            msgBox.exec_()

        else:
            self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
            self.ui.errorMessageDialog.showMessage("""Error al eliminar el
                                                    registro""")

    def filtrarProductos(self):
        self.proxyModel.setFilterKeyColumn(1)

        productoAFiltrar = QtCore.QRegExp(
            self.filtroBusquedaProductoLineEdit.text(),
            QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)

        self.proxyModel.setFilterRegExp(productoAFiltrar)

    def filtrarMarca(self):
        self.proxyModel.setFilterKeyColumn(5)

        index = self.filtroBusquedaMarcaComboBox.currentIndex()
        if (index != 0):
            marcaFiltro = self.filtroBusquedaMarcaComboBox.itemText(index)

        else:
            marcaFiltro = u"|"

        marcaAFiltrar = QtCore.QRegExp(
            marcaFiltro, QtCore.Qt.CaseInsensitive, QtCore.QRegExp.RegExp)
        self.proxyModel.setFilterRegExp(marcaAFiltrar)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TablaProductos()
    window.setSourceModel(window.loadData(window))
    sys.exit(app.exec_())