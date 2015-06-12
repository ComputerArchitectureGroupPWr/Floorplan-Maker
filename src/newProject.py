# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project.ui'
#
# Created: Sat Mar  2 15:47:53 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(538, 284)
        self.DescribeLocationLabel = QtGui.QLabel(Dialog)
        self.DescribeLocationLabel.setGeometry(QtCore.QRect(10, 70, 371, 21))
        self.DescribeLocationLabel.setObjectName(_fromUtf8("DescribeLocationLabel"))
        self.projectLocationLabel = QtGui.QLabel(Dialog)
        self.projectLocationLabel.setGeometry(QtCore.QRect(10, 130, 231, 17))
        self.projectLocationLabel.setObjectName(_fromUtf8("projectLocationLabel"))
        self.projectNameLabel = QtGui.QLabel(Dialog)
        self.projectNameLabel.setGeometry(QtCore.QRect(10, 190, 171, 17))
        self.projectNameLabel.setObjectName(_fromUtf8("projectNameLabel"))
        self.DescribeLocationButton = QtGui.QPushButton(Dialog)
        self.DescribeLocationButton.setGeometry(QtCore.QRect(440, 90, 88, 27))
        self.DescribeLocationButton.setObjectName(_fromUtf8("DescribeLocationButton"))
        self.projectLocationButton = QtGui.QPushButton(Dialog)
        self.projectLocationButton.setGeometry(QtCore.QRect(400, 150, 131, 27))
        self.projectLocationButton.setObjectName(_fromUtf8("projectLocationButton"))
        self.DescribeLocationLineEdit = QtGui.QLineEdit(Dialog)
        self.DescribeLocationLineEdit.setGeometry(QtCore.QRect(10, 90, 401, 27))
        self.DescribeLocationLineEdit.setObjectName(_fromUtf8("DescribeLocationLineEdit"))
        self.projectLocationLineEdit = QtGui.QLineEdit(Dialog)
        self.projectLocationLineEdit.setGeometry(QtCore.QRect(10, 150, 361, 27))
        self.projectLocationLineEdit.setObjectName(_fromUtf8("projectLocationLineEdit"))
        self.projectNamelineEdit = QtGui.QLineEdit(Dialog)
        self.projectNamelineEdit.setGeometry(QtCore.QRect(10, 210, 211, 27))
        self.projectNamelineEdit.setObjectName(_fromUtf8("projectNamelineEdit"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(350, 250, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.modeLabel = QtGui.QLabel(Dialog)
        self.modeLabel.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.modeLabel.setObjectName(_fromUtf8("modeLabel"))
        self.deviceLabel = QtGui.QLabel(Dialog)
        self.deviceLabel.setGeometry(QtCore.QRect(250, 10, 91, 20))
        self.deviceLabel.setObjectName(_fromUtf8("deviceLabel"))
        self.modeComboBox = QtGui.QComboBox(Dialog)
        self.modeComboBox.setGeometry(QtCore.QRect(10, 30, 191, 31))
        self.modeComboBox.setObjectName(_fromUtf8("modeComboBox"))
        self.modeComboBox.addItem(_fromUtf8(""))
        self.modeComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox = QtGui.QComboBox(Dialog)
        self.deviceComboBox.setGeometry(QtCore.QRect(250, 30, 141, 31))
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        #Number of options
        [self.deviceComboBox.addItem(_fromUtf8("")) for x in range(4)]

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.DescribeLocationLabel.setText(QtGui.QApplication.translate("Dialog", "Localisation of FPGA describing file (xdl or xml)", None, QtGui.QApplication.UnicodeUTF8))
        self.projectLocationLabel.setText(QtGui.QApplication.translate("Dialog", "Project localisation:", None, QtGui.QApplication.UnicodeUTF8))
        self.projectNameLabel.setText(QtGui.QApplication.translate("Dialog", "Project name:", None, QtGui.QApplication.UnicodeUTF8))
        self.DescribeLocationButton.setText(QtGui.QApplication.translate("Dialog", "Select file", None, QtGui.QApplication.UnicodeUTF8))
        self.projectLocationButton.setText(QtGui.QApplication.translate("Dialog", "Select localisation", None, QtGui.QApplication.UnicodeUTF8))
        self.modeLabel.setText(QtGui.QApplication.translate("Dialog", "Select project mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("Dialog", "Select device:", None, QtGui.QApplication.UnicodeUTF8))
        self.modeComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "emulation", None, QtGui.QApplication.UnicodeUTF8))
        self.modeComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Microblaze mesurement", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Spartan 3e1600", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Spartan 3e500", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Spartan 6 (Atlys board)", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceComboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "Virtex 5", None,
                                                                        QtGui.QApplication.UnicodeUTF8))
