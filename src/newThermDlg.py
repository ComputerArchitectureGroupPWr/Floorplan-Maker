# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_term.ui'
#
# Created: Wed Feb 27 16:11:53 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddTermDialog(object):
    def setupUi(self, AddTermDialog):
        AddTermDialog.setObjectName(_fromUtf8("AddTermDialog"))
        AddTermDialog.setWindowModality(QtCore.Qt.NonModal)
        AddTermDialog.resize(350, 126)
        AddTermDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.atd = AddTermDialog
        self.buttonBox = QtGui.QDialogButtonBox(AddTermDialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.labelName = QtGui.QLabel(AddTermDialog)
        self.labelName.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.lineEditName = QtGui.QLineEdit(AddTermDialog)
        self.lineEditName.setGeometry(QtCore.QRect(150, 10, 191, 27))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.line = QtGui.QFrame(AddTermDialog)
        self.line.setGeometry(QtCore.QRect(0, 40, 391, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(AddTermDialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 59, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(AddTermDialog)
        self.comboBox.setGeometry(QtCore.QRect(50, 50, 82, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))

        self.retranslateUi(AddTermDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddTermDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddTermDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddTermDialog)

    def retranslateUi(self, AddTermDialog):
        AddTermDialog.setWindowTitle(QtGui.QApplication.translate("AddTermDialog", "Add thermometer", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("AddTermDialog", "Thermometer name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddTermDialog", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("AddTermDialog", "RO7", None, QtGui.QApplication.UnicodeUTF8))

class NewThermDlg(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_AddTermDialog()
        self.ui.setupUi(self)

    def getValues(self):
        values = {}
        values["name"] = self.ui.lineEditName.text()
        values["type"] = self.ui.comboBox.currentText()
        return values

class ModifyThermDlg(NewThermDlg):

    def __init__(self,params):
        NewThermDlg.__init__(self)
        self.ui.atd.setWindowTitle(QtGui.QApplication.translate("AddTermDialog", "Modify thermometer", None, QtGui.QApplication.UnicodeUTF8))
        self.ui.lineEditName.setText(params["name"])
        index = self.ui.comboBox.findText(params['type'])
        self.ui.comboBox.setCurrentIndex(index)