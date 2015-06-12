from PyQt4 import QtGui

__author__ = 'pawel'

def messageBox(title, parent_name, message, icon):
    msgBox = QtGui.QMessageBox()
    msgBox.setWindowTitle(QtGui.QApplication.translate(parent_name, title, None, QtGui.QApplication.UnicodeUTF8))
    msgBox.setText(QtGui.QApplication.translate(parent_name, message, None, QtGui.QApplication.UnicodeUTF8))
    msgBox.setIcon(icon)
    msgBox.exec_()