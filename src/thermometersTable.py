# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString, Qt
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidget, QTableWidgetItem, QFont

__author__ = 'pawel'

class ThermometersTable(QTableWidget):

    columns_names = ["Name","Pos. x","Pos. y","Type"]
    columns_keys = {"name" : 0, "pos_x" : 1, "pos_y" : 2, "type" : 3}
    elements = 0

    def __init__(self, *args):
        QTableWidget.__init__(self, *args)
        self.setGeometry(QtCore.QRect(15, 400, 391, 301))
        self.setMaximumSize(QtCore.QSize(400, 16777215))
        self.setObjectName("Thermometers Table")
        self.setColumnCount(4)
        self.setRowCount(0)
        for i in range(4):
            item = QtGui.QTableWidgetItem()
            self.setHorizontalHeaderItem(i, item)
            self.horizontalHeaderItem(i).setText(QtGui.QApplication.translate("FloorplanMaker", self.columns_names[i], None, QtGui.QApplication.UnicodeUTF8))
            self.setColumnWidth(i,90)
        self.setColumnWidth(0,120)

    def initData(self, data):
        n = 0
        for item in data:
            for val in item:
                new_item = QtGui.QTableWidgetItem(str(item[val]))
                new_item.setTextAlignment(4)
                flags = new_item.flags()
                flags.__ixor__(Qt.ItemIsEditable)
                new_item.setFlags(flags)
                self.setItem(n, self.columns_keys[val], new_item)
            n += 1

    def refresh(self, data):
        self.list_graph = data
        self.setRowCount(len(data))
        self.initData(data)

    def selectIndex(self):
        return self.currentRow()
