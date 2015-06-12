from PyQt4 import QtGui
from addNewHeaterBeh import NewHeaterDialog
from addNewHeater import Ui_newHeaterDialog

__author__ = 'pawel'

class ModifyHeaterDlg(NewHeaterDialog):

    def __init__(self,params):
        NewHeaterDialog.__init__(self)
        #Set current name
        self.ui.lineEditHeaterName.setText(params["name"])
        #Set current color
        self.ui.colorEdit.setColor(params['color'])
        #Set current type
        index = self.ui.comboBoxHeaterType.findText(params['type'])
        self.ui.comboBoxHeaterType.setCurrentIndex(index)