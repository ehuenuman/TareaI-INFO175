#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui
import view_login


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main_window = view_login.FormLoginUser()
    main_window.show()
    sys.exit(app.exec_())
