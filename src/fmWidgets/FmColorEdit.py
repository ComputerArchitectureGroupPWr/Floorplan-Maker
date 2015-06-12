from PyQt4.QtGui import QPalette, QColor

__author__ = 'pawel'

from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class FmColorEdit(QtGui.QLineEdit):

    def __init__(self, parent):
        super(FmColorEdit, self).__init__(parent)
        self.setReadOnly(True)

    def mousePressEvent(self, event):
        self.color = QtGui.QColorDialog.getColor(Qt.blue)
        palette = self.palette()
        palette.setColor(QPalette.Base, self.color)
        self.setPalette(palette)

    def currentColor(self):
        return self.color.name()

    def setColor(self, color):
        self.color = color
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor(color))
        self.setPalette(palette)