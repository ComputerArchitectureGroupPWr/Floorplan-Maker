# -*- coding: utf-8 -*-
import glob
import os
import signal

from PyQt4.QtCore import QString

from pgFPGAdescriptionBeh import PgFPGAdescriptionDlg


__author__ = 'pawel'
#test
from PyQt4 import QtCore, QtGui
from newProject import Ui_Dialog
from xmldoc.XMLReader import XMLreader
import subprocess as sub

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class StatusBarProcess(QtCore.QThread):
    procDone = QtCore.pyqtSignal(bool)
    partDone = QtCore.pyqtSignal(int)

    def run(self):
        while True:
            try:
                file = open("status.log","r")
                percent = int(file.readline())
                self.partDone.emit(percent)
                file.close()
                if percent == 100 or break_proces:
                    break
            except:
                pass

        self.procDone.emit(True)

class FileDesignProcess(QtCore.QThread):

    def __init__(self, fname, device):
        QtCore.QThread.__init__(self)
        self.fname = fname
        self.device = device

    def run(self):
        self.proc = sub.Popen(["generilo","-d",str(self.fname),self.device,'-o','floorplan.xml'], preexec_fn=os.setsid)

    def stop(self):
        os.killpg(self.proc.pid, signal.SIGTERM)

class NewProjectDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.projectNamelineEdit.setEnabled(False)
        QtCore.QObject.connect(self.ui.DescribeLocationButton, QtCore.SIGNAL("clicked()"), self.showDialogDescribe)
        QtCore.QObject.connect(self.ui.projectLocationButton, QtCore.SIGNAL("clicked()"), self.showDialogLocation)
        QtCore.QObject.connect(self.ui.projectNamelineEdit, QtCore.SIGNAL("editingFinished()"), self.projectNameChanger)
        QtCore.QObject.connect(self.ui.deviceComboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.activateModeBox)

    #Otwarcie okienka po wybraniu opcji Nowy projekt w menu Plik
    def showNewProject(self, checked=None):
        if checked==None:
            return

        self.exec_()

    def getValues(self):
        return {'FPGA descriptor':self.fname_file,'project dir':self.dirName,'name':self.projectName,
                'device':self.device,'mode':self.ui.modeComboBox.currentText()}

    #Otwarcie MessageBox'a po wybraniu blednego formatu pliku lub zapisanie ścieżki
    def showDialogDescribe(self):

        device_dict = {
            "Spartan 3e1600": "s3e1600",
            "Spartan 3e500": "s3e500",
            "Spartan 6 (Atlys board)": "Atlys",
            "Virtex 5": "Virtex5"
        }

        #Wczytanie wskazanego przez użytkownika pliku
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', str(os.path.basename))
        self.fname_file = self.fname[str(self.fname).rfind('/')+1:]

        self.device = device_dict[str(self.ui.deviceComboBox.currentText())]

        self.projectName = ""
        # --DEBUGER LINES -- #
        #print self.fname
        #Sekcja sprawdzania poprawności wczytanego pliku
        try:
            try:
                describe_file = XMLreader(self.fname)
            except:
                pass

            if str(self.fname).find(".xdl")!=-1:
                self.thread = StatusBarProcess()
                self.thread2 = FileDesignProcess(self.fname, self.device)
                self.thread2.start()
                pbarwin = PgFPGAdescriptionDlg(self.thread)
                if pbarwin.exec_():
                    self.thread.terminate()
                    self.thread.wait()
                    self.thread2.stop()
                    self.thread2.terminate()
                    self.thread2.wait()
                    filelist = glob.glob("status.log")
                    for f in filelist:
                        os.remove(f)
                    if not(pbarwin.reject):
                        self.fname = "floorplan.xml"
                        text = QString(str(self.fname[:str(self.fname).rfind("/")])+self.fname)
                        print text
                        self.ui.DescribeLocationLineEdit.setText(text)
            elif describe_file.isDescriptionFile():
                text = QString(self.fname)
                self.ui.DescribeLocationLineEdit.setText(text)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setWindowTitle("Attention!")
                msgBox.setText(QtGui.QApplication.translate("NewProject", "Selected file is not FPGA description file!",
                    None, QtGui.QApplication.UnicodeUTF8))
                msgBox.setIcon(3)
                msgBox.exec_()
        except:
            msgBox = QtGui.QMessageBox();
            msgBox.setWindowTitle("Attention!")
            msgBox.setText(QtGui.QApplication.translate("NewProject", "Selected file is broken "
                "or is not xml file!", None, QtGui.QApplication.UnicodeUTF8))
            msgBox.setIcon(3)
            msgBox.exec_()


    def showDialogLocation(self):
        self.dirName = QtGui.QFileDialog.getExistingDirectory(self,'Project path', str(os.path.abspath))
        self.ui.projectLocationLineEdit.setText(self.dirName)
        self.ui.projectNamelineEdit.setEnabled(True)
        self.ui.deviceComboBox.setEnabled(True)
        self.ui.modeComboBox.setEnabled(True)

    def projectNameChanger(self):
        if not(self.projectName):
            self.projectName = self.ui.projectNamelineEdit.text()
            self.dirName = self.dirName + "/" + self.ui.projectNamelineEdit.text() + ".xml"
            self.ui.projectLocationLineEdit.setText(self.dirName)

    def activateModeBox(self):
        if self.ui.deviceComboBox.currentIndex() == 1:
            self.ui.modeComboBox.removeItem(1)
        elif self.ui.deviceComboBox.currentIndex() == 0:
            self.ui.modeComboBox.addItem(_fromUtf8("Microblaze measurement"))
