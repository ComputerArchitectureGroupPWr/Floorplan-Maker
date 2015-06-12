# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Fri Apr 12 17:07:46 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(221, 329)
        AboutDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Logo = QtGui.QLabel(AboutDialog)
        self.Logo.setGeometry(QtCore.QRect(60, 50, 101, 141))
        self.Logo.setText(_fromUtf8(""))
        self.Logo.setPixmap(QtGui.QPixmap(_fromUtf8("/usr/local/include/.icons/FloorplanMaker/logo.png")))
        self.Logo.setObjectName(_fromUtf8("Logo"))
        self.titleLabel = QtGui.QLabel(AboutDialog)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 221, 51))
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.infoLabel = QtGui.QLabel(AboutDialog)
        self.infoLabel.setGeometry(QtCore.QRect(0, 190, 221, 91))
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.closeButton = QtGui.QPushButton(AboutDialog)
        self.closeButton.setGeometry(QtCore.QRect(70, 290, 95, 31))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.titleLabel.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#ff0000;\">FloorplanMaker</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.infoLabel.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p align=\"center\">Version: 1.01</p><p align=\"center\">Build: 002</p><p align=\"center\"><span style=\" font-weight:600;\">Project Heat Toolset member</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("AboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

class AboutDlg(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

