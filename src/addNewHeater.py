# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_heater.ui'
#
# Created: Wed Apr 17 09:37:08 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import fmWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_newHeaterDialog(object):
    def setupUi(self, newHeaterDialog):
        newHeaterDialog.setObjectName(_fromUtf8("newHeaterDialog"))
        newHeaterDialog.resize(391, 183)
        self.buttonBox = QtGui.QDialogButtonBox(newHeaterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 150, 371, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBoxHeaterType = QtGui.QComboBox(newHeaterDialog)
        self.comboBoxHeaterType.setGeometry(QtCore.QRect(50, 60, 131, 31))
        self.comboBoxHeaterType.setObjectName(_fromUtf8("comboBoxHeaterType"))
        self.comboBoxHeaterType.addItem(_fromUtf8(""))
        self.comboBoxHeaterType.addItem(_fromUtf8(""))
        self.lineEditHeaterName = QtGui.QLineEdit(newHeaterDialog)
        self.lineEditHeaterName.setGeometry(QtCore.QRect(110, 10, 271, 27))
        self.lineEditHeaterName.setObjectName(_fromUtf8("lineEditHeaterName"))
        self.labelHeaterName = QtGui.QLabel(newHeaterDialog)
        self.labelHeaterName.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.labelHeaterName.setObjectName(_fromUtf8("labelHeaterName"))
        self.labelHeaterType = QtGui.QLabel(newHeaterDialog)
        self.labelHeaterType.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.labelHeaterType.setObjectName(_fromUtf8("labelHeaterType"))
        self.line = QtGui.QFrame(newHeaterDialog)
        self.line.setGeometry(QtCore.QRect(0, 40, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(newHeaterDialog)
        self.line_2.setGeometry(QtCore.QRect(0, 90, 391, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.labelColor = QtGui.QLabel(newHeaterDialog)
        self.labelColor.setGeometry(QtCore.QRect(10, 120, 121, 17))
        self.labelColor.setObjectName(_fromUtf8("labelColor"))
        self.colorEdit = fmWidgets.FmColorEdit(newHeaterDialog)
        self.colorEdit.setEnabled(True)
        self.colorEdit.setGeometry(QtCore.QRect(130, 110, 51, 33))
        #self.colorEdit.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.colorEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.colorEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.colorEdit.setObjectName(_fromUtf8("colorEdit"))

        self.retranslateUi(newHeaterDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), newHeaterDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), newHeaterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newHeaterDialog)

    def retranslateUi(self, newHeaterDialog):
        newHeaterDialog.setWindowTitle(QtGui.QApplication.translate("newHeaterDialog", "New heater", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxHeaterType.setItemText(0, QtGui.QApplication.translate("newHeaterDialog", "RO1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxHeaterType.setItemText(1, QtGui.QApplication.translate("newHeaterDialog", "RO3", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHeaterName.setText(QtGui.QApplication.translate("newHeaterDialog", "Heater name:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelHeaterType.setText(QtGui.QApplication.translate("newHeaterDialog", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelColor.setText(QtGui.QApplication.translate("newHeaterDialog", "Color on schema:", None, QtGui.QApplication.UnicodeUTF8))

