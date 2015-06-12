# -*- coding: utf-8 -*-
__author__ = 'pawel'

from PyQt4 import QtGui
from PyQt4.QtCore import Qt, QString
from addNewHeater import Ui_newHeaterDialog

class NewHeaterDialog(QtGui.QDialog):
    colors = {QString("niebieski"):Qt.blue, QString("ciemny niebieski"): Qt.darkBlue,
              QString("czerwony"):Qt.red, QString("ciemny czerwony"): Qt.darkRed,
              QString("zielony"):Qt.green, QString("ciemny zielony"): Qt.darkGreen,
              QString("cyjan"): Qt.cyan, QString("ciemny cyjan"): Qt.darkCyan,
              QString("magenta"): Qt.magenta, QString("ciemna magenta"): Qt.darkMagenta,
              QString("szary"): Qt.gray, QString("ciemny szary"): Qt.darkGray,
              QtGui.QApplication.translate("newHeaterDialog", "żółty", None, QtGui.QApplication.UnicodeUTF8): Qt.yellow,
              QtGui.QApplication.translate("newHeaterDialog", "ciemny żółty", None,
              QtGui.QApplication.UnicodeUTF8): Qt.darkYellow}

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_newHeaterDialog()
        self.ui.setupUi(self)

    #Otwarcie okienka po wcisnieciu przycisku nowa grzalka
    def showDialog(self, checked=None):
        if checked==None:
            return

        self.exec_()
        self.show()

    def getValues(self):
        values = {}
        values["name"] = self.ui.lineEditHeaterName.text()
        values["type"] = self.ui.comboBoxHeaterType.currentText()
        values["color"] = self.ui.colorEdit.currentColor()
        return values