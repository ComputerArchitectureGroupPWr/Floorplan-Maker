# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_floorplan.ui'
#
# Created: Mon May 14 12:39:25 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_newFloorplanFile(object):
    def setupUi(self, newFloorplanFile):
        newFloorplanFile.setObjectName(_fromUtf8("newFloorplanFile"))
        newFloorplanFile.resize(457, 138)
        self.buttonBox = QtGui.QDialogButtonBox(newFloorplanFile)
        self.buttonBox.setGeometry(QtCore.QRect(100, 100, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_one = QtGui.QLabel(newFloorplanFile)
        self.label_one.setGeometry(QtCore.QRect(10, 17, 201, 21))
        self.label_one.setObjectName(_fromUtf8("label_one"))
        self.lineEditOldNcd = QtGui.QLineEdit(newFloorplanFile)
        self.lineEditOldNcd.setGeometry(QtCore.QRect(220, 10, 231, 27))
        self.lineEditOldNcd.setObjectName(_fromUtf8("lineEditOldNcd"))
        self.lineEditOldNcd.setText(_fromUtf8("SimCore.ncd"))

        self.labe_two = QtGui.QLabel(newFloorplanFile)
        self.labe_two.setGeometry(QtCore.QRect(10, 60, 251, 17))
        self.labe_two.setObjectName(_fromUtf8("labe_two"))
        self.lineEditNewNcd = QtGui.QLineEdit(newFloorplanFile)
        self.lineEditNewNcd.setGeometry(QtCore.QRect(250, 50, 201, 27))
        self.lineEditNewNcd.setObjectName(_fromUtf8("lineEditNewNcd"))
        self.lineEditNewNcd.setText(_fromUtf8("SimCore_new.ncd"))

        self.retranslateUi(newFloorplanFile)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), newFloorplanFile.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), newFloorplanFile.reject)
        QtCore.QMetaObject.connectSlotsByName(newFloorplanFile)

    def retranslateUi(self, newFloorplanFile):
        newFloorplanFile.setWindowTitle(QtGui.QApplication.translate("newFloorplanFile", "Nowy plik floorplanu", None, QtGui.QApplication.UnicodeUTF8))
        self.label_one.setText(QtGui.QApplication.translate("newFloorplanFile",
            "Wskaż nazwę pliku ncd układu:", None, QtGui.QApplication.UnicodeUTF8))
        self.labe_two.setText(QtGui.QApplication.translate("newFloorplanFile", "Wskaż nazwę docelowego pliku .ncd:", None, QtGui.QApplication.UnicodeUTF8))

