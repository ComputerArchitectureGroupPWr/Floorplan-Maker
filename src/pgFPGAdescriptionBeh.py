from PyQt4 import QtGui
from PyQt4 import QtCore
from pgFPGAdescription import Ui_progresbarFPGA

__author__ = 'pawel'

class PgFPGAdescriptionDlg(QtGui.QDialog, QtCore.QThread):

    def __init__(self,thread):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_progresbarFPGA()
        self.ui.setupUi(self)
        self.reject = True
        self.ui.Ok.setDisabled(True)

        thread.partDone.connect(self.updatePBar)
        thread.procDone.connect(self.closeWindow)

        thread.start()

    def updatePBar(self, val):
        self.ui.progressBar.setValue(val)
        if val == 100:
            self.reject = False
            self.ui.Ok.setDisabled(False)

    def closeWindow(self):
        print "Close progrss bar window!"

    def rejectButton(self):
        self.reject = True
        self.ui.progressBar.accept()
