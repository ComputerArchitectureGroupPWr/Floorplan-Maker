# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgFPGAdescrition.ui'
#
# Created: Sun Oct 28 22:26:24 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_progresbarFPGA(object):
    def setupUi(self, progresbarFPGA):
        progresbarFPGA.setObjectName(_fromUtf8("progresbarFPGA"))
        progresbarFPGA.resize(400, 102)
        self.progressBar = QtGui.QProgressBar(progresbarFPGA)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(progresbarFPGA)
        self.label.setGeometry(QtCore.QRect(80, 10, 241, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.Ok = QtGui.QDialogButtonBox(progresbarFPGA)
        self.Ok.setGeometry(QtCore.QRect(295, 70, 91, 27))
        self.Ok.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.Ok.setObjectName(_fromUtf8("Ok"))
        self.Cancel = QtGui.QDialogButtonBox(progresbarFPGA)
        self.Cancel.setGeometry(QtCore.QRect(195, 70, 91, 27))
        self.Cancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel)
        self.Cancel.setObjectName(_fromUtf8("Cancel"))

        self.retranslateUi(progresbarFPGA)
        QtCore.QObject.connect(self.Ok, QtCore.SIGNAL(_fromUtf8("accepted()")), progresbarFPGA.accept)
        QtCore.QObject.connect(self.Cancel, QtCore.SIGNAL(_fromUtf8("rejected()")), progresbarFPGA.accept)
        QtCore.QMetaObject.connectSlotsByName(progresbarFPGA)

    def retranslateUi(self, progresbarFPGA):
        progresbarFPGA.setWindowTitle(QtGui.QApplication.translate("progresbarFPGA", "Wczytywanie opisu FPGA", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("progresbarFPGA", "Wczytywanie opisu FPGA z pliku xdl", None, QtGui.QApplication.UnicodeUTF8))

