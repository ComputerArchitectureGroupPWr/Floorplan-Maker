# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString, Qt, QObject, pyqtSignal
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QTableWidget, QTableWidgetItem, QFont, QColor

__author__ = 'pawel'

class HeatersTable(QTableWidget):

    colors = {QString("niebieski"):Qt.blue, QString("ciemny niebieski"): Qt.darkBlue,
              QString("czerwony"):Qt.red, QString("ciemny czerwony"): Qt.darkRed,
              QString("zielony"):Qt.green, QString("ciemny zielony"): Qt.darkGreen,
              QString("cyjan"): Qt.cyan, QString("ciemny cyjan"): Qt.darkCyan,
              QString("magenta"): Qt.magenta, QString("ciemna magenta"): Qt.darkMagenta,
              QString("szary"): Qt.gray, QString("ciemny szary"): Qt.darkGray,
              QtGui.QApplication.translate("newHeaterDialog", "żółty", None, QtGui.QApplication.UnicodeUTF8): Qt.yellow,
              QtGui.QApplication.translate("newHeaterDialog", "ciemny żółty", None,
                                           QtGui.QApplication.UnicodeUTF8): Qt.darkYellow}

    columns_names = ["Color","Name","Type"]
    columns_keys = {"name" : 1, "type" : 2, "color" : 0}
    elements = 0

    tableClicked = pyqtSignal()

    def __init__(self, *args):
        QTableWidget.__init__(self, *args)
        self.setMaximumSize(QtCore.QSize(400, 16777215))
        self.setGeometry(QtCore.QRect(15, 400, 391, 301))
        self.setColumnCount(3)
        self.setRowCount(0)
        for i in range(3):
            item = QtGui.QTableWidgetItem()
            self.setHorizontalHeaderItem(i, item)
            self.horizontalHeaderItem(i).setText(QtGui.QApplication.translate("FloorplanMaker", self.columns_names[i], None, QtGui.QApplication.UnicodeUTF8))

        self.setColumnWidth(0,145)

    def initData(self,data):
        n=0
        for item in data:
            for val in item:
                if val == "color":
                    new_item = QtGui.QTableWidgetItem("")
                    new_item.setBackgroundColor(QColor(item[val]))
                    self.setItem(n,self.columns_keys[val],new_item)
                else:
                    new_item = QtGui.QTableWidgetItem(str(item[val]))
                    new_item.setTextAlignment(4)
                    flags = new_item.flags()
                    flags.__ixor__(Qt.ItemIsEditable)
                    new_item.setFlags(flags)
                    self.setItem(n,self.columns_keys[val],new_item)
            n+=1

    def refresh(self,data):
        self.list_graph = data
        self.setRowCount(len(data))
        self.initData(data)

    def selectIndex(self):
        return self.currentRow()
