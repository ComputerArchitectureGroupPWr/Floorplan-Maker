from PyQt4 import QtGui
from newFloorplanDlg import Ui_newFloorplanFile

__author__ = 'pawel'

class FloorplanFileDlg(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_newFloorplanFile()
        self.ui.setupUi(self)

    def getValues(self):
        values = []
        values.append(self.ui.lineEditOldNcd.text())
        values.append(self.ui.lineEditNewNcd.text())
        return values