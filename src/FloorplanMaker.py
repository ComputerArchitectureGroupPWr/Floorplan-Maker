# -*- coding: utf-8 -*-
import sys, os
#
# KSB: fix - genrilo.xml was placed in an incorrect place 
#      if dir name and project name was the same
#
import os.path
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QShortcut
from addNewHeaterBeh import NewHeaterDialog
from FloorplanMakerUI import Ui_FloorplanMaker
from newFloorplanDlgBeh import FloorplanFileDlg
from newProjectBeh import NewProjectDialog
from modifyHeaterBeh import ModifyHeaterDlg
from newThermDlg import NewThermDlg, ModifyThermDlg
from about import AboutDlg
from xmldoc.XMLCreator import XMLcreator
from MyMessageBox import messageBox
from device import *
import xml.dom.minidom as dom
import PyQt4

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class FloorplanMakerWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_FloorplanMaker()
        self.ui.setupUi(self)
        self.newProjectDialog = NewProjectDialog()
        self.ui.actionOpenProject.triggered.connect(self.showDialogOpenProject)
        #Disable non fuctions
        self.ui.actionOpen_project.setEnabled(True)
        self.ui.actionSave_project.setEnabled(True)
        self.ui.actionNewProject.triggered.connect(self.showNewProject)
        self.ui.actionGeneriloFile.triggered.connect(self.showNewFloorplanFile)
        self.ui.actionSave.triggered.connect(self.showSaveFile)
        self.ui.actionAbout.triggered.connect(self.showAbout)

        #self.ui.pushButtonAddHeater.setEnabled(False)
        #self.ui.heaterTable = HeatersTable(self.ui.centralwidget)
        #self.ui.tableThermometers = ThermometersTable(self.ui.centralwidget)
        self.heaters_list = []
        self.project_properties = {}
        self.activeTab = 'heaters'

        #liczba elementów w tabeli grzałek
        self.elements = 0
        #obsługa zdarzenia kliknięcia przycisku dodania nowej grzałki
        QtCore.QObject.connect(self.ui.btnAddHeater, QtCore.SIGNAL("clicked()"), self.showDialogNewHeater)
        #obsługa zdarzenia usuwania grzałki
        QtCore.QObject.connect(self.ui.btnDeleteHeater, QtCore.SIGNAL("clicked()"), self.deleteHeater)
        #obsługa zdarzenia modyfikacji grzałki
        QtCore.QObject.connect(self.ui.btnModifyHeater, QtCore.SIGNAL("clicked()"), self.showDialogModifyHeater)
        #obsługa zdarzenia dodania termometru
        QtCore.QObject.connect(self.ui.btnAddTherm, QtCore.SIGNAL("clicked()"), self.showDialogNewTerm)
        #obsługa zmiany tabelki
        QtCore.QObject.connect(self.ui.heaterTable, QtCore.SIGNAL("itemSelectionChanged()"), self.heatersTableSelection)
        QtCore.QObject.connect(self.ui.tableThermometers, QtCore.SIGNAL("itemSelectionChanged()"), self.unselectHeater)
        #obsługa zdarzenia usunięcia termometru
        QtCore.QObject.connect(self.ui.btnDelete, QtCore.SIGNAL("clicked()"), self.deleteThermometer)
        #obsługa zdarzenia modyfikacji termometru
        QtCore.QObject.connect(self.ui.btnModifyTherm, QtCore.SIGNAL("clicked()"), self.showDialogModifyTherm)
        QtCore.QObject.connect(self.ui.generateButton, QtCore.SIGNAL("clicked()"), self.generateThermometers)

    def generateThermometers(self):
        floorplanFilename = str(self.project_properties['FPGA descriptor'])

        device = Device()
        inDoc = dom.parse(floorplanFilename)
        device.setFreeSpaceFromFile(inDoc)
        outDoc = dom.Document() 

        board = outDoc.createElement("board")
        outDoc.appendChild(board)


        thermsInRow = int(self.ui.thermsInRowEdit.text())
        thermsInColumn = int(self.ui.columnsInRowEdit.text()) #lol columns in row xD

        print("thermsInRow: {}".format(thermsInRow))
        print("thermsInColumn: {}".format(thermsInColumn))

        if(self.ui.generateActionCombo.currentIndex() == 0):
            pass           
        elif(self.ui.generateActionCombo.currentIndex() == 1):
            device.generateThermometersNet(outDoc,thermsInRow, thermsInColumn)

        therms = outDoc.getElementsByTagName("thermometer")

        for therm in therms:
            name = therm.getAttribute("name")
            tp = therm.getAttribute("type")
            col = therm.getAttribute("col")
            row = therm.getAttribute("row")

            tableRow = {}
            tableRow['name'] = str(name)
            tableRow['pos_x'] = int(col)
            tableRow['pos_y'] = int(row)
            tableRow['type'] = str(tp)

            self.ui.thermometers_list.append(tableRow)
            self.term_new = True
            self.ui.tableThermometers.refresh(self.ui.thermometers_list)
            #self.ui.FloorPlanFrame.thermLoadEvent(tableRow)
            index = len(self.ui.thermometers_list)
            self.ui.heaterTable.clearSelection()
            self.ui.tableThermometers.selectRow(index - 1)
            

    def heatersTableSelection(self):
        self.ui.tableThermometers.clearSelection()
        self.ui.FrameFloorplan.repaint()

        if self.ui.heaterTable.selectedIndexes():
            index = self.ui.heaterTable.selectIndex()
            self.ui.heaterTable.selectRow(index)
	
    def unselectHeater(self):
        self.ui.heaterTable.clearSelection()

        if self.term_new:
            self.term_new = False
        else:
            self.ui.FrameFloorplan.repaint()

        if self.ui.tableThermometers.selectedIndexes():
            index = self.ui.tableThermometers.selectIndex()
            self.ui.tableThermometers.selectRow(index)

    ##########################################################################
    #                       OPEN PROJECT METHODS                             #
    ##########################################################################

    def showDialogOpenProject(self):
        """
        Shows open project dialog and call functions loads the design to
        FloorplanMaker
        """
        self.loadProjectXML(QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                                                              os.getcwd()))

    def loadProjectXML(self, filename):
        """
        Loads the information about the project from indicated XML project
        file and proceed loading design information about heaters and
        thermometers

        :param filename: Name of xml file with project description
        """
        self.project_xml = XMLcreator(fopen=filename)

        if self.project_xml.isProjectFile():
            self.ui.FloorPlanFrame.fileLoadedEvent(
                self.project_xml.getDeviceDescriptor(),
                self.project_xml.getDeviceVersion()
            )
            self.ui.FloorPlanFrame.fileFloorplanLoadedEvent(self.project_xml.getDesignFile())
            self.project_properties['project dir'] = self.project_xml.getProjectFile()
            self.project_properties['name'] = self.project_xml.getProjectName()
            self.project_properties['device'] = self.project_xml.getDeviceVersion()
            self.project_properties['mode'] = self.project_xml.getEmulationMode()
            self.project_properties['FPGA descriptor'] = self.project_xml.getProjectFile() + '/' + \
                                                         self.project_xml.getDeviceDescriptor()

            self.loadHeatersToDesign()

            self.loadThermometersToDesign()
        else:
            messageBox("Error", "New project", "Selected file is not project file! "
                                              "Please try another.", 3)

    def loadHeatersToDesign(self):
        """
        Loads heaters stored in design description file into heaters' table and
        to floorplan frame for graphical representation
        """
        for i, heater in enumerate(self.ui.FloorPlanFrame.floorplan.heaters):
            values = {
                'name': heater[0],
                'type': heater[3],
                'color': heater[2]
            }
            self.heaters_list.append(values)
            self.ui.heaterTable.refresh(self.heaters_list)
            index = len(self.heaters_list)
            self.ui.tableThermometers.clearSelection()
            self.ui.heaterTable.selectRow(index - 1)
            self.ui.FloorPlanFrame.mouseSelection = False

    def loadThermometersToDesign(self):
        """
        Loads thermometers stored in design description file into thermometers'
        table and to floorplan frame for graphical representation.
        """
        for name, term in sorted(self.ui.FloorPlanFrame.floorplan.therms.items()):
            row, col = self.ui.FloorPlanFrame.floorplan.getTermPosition(name)
            values = {
                'name': name,
                'pos_x': col,
                'pos_y': row,
                'type': term['type']
            }

            self.ui.thermometers_list.append(values)
            self.ui.tableThermometers.refresh(self.ui.thermometers_list)

            index = len(self.ui.thermometers_list)
            self.term_new = True
            self.ui.heaterTable.clearSelection()
            self.ui.tableThermometers.selectRow(index - 1)


    ##########################################################################
    #                          NEW PROJECT METHODS                           #
    ##########################################################################


    # Jeżeli nowy projekt zaakceptowany ściągnij dane i utwórz pliki
    def showNewProject(self):
        try:
            del self.project_properties
        except:
            pass

        newProjectDlg = NewProjectDialog()
        try:
            if newProjectDlg.exec_():
                self.project_properties = newProjectDlg.getValues()
        except:
            #Informacja o błędzie przy tworzeniu projektu
            messageBox("Error", "New project", "New project has not been created", 3)

        self.project_xml = XMLcreator()
        self.project_xml.createNewProjectFile(
            self.project_properties['name'],
            self.project_properties['project dir'],
            self.project_properties['FPGA descriptor'],
            self.project_properties['device'],
            self.project_properties['mode']
        )
        self.ui.statusbar.showMessage(self.project_properties['project dir'])
        #Wczytanie pliku opisu fpga
        self.ui.FloorPlanFrame.fileLoadedEvent(self.project_properties['FPGA descriptor'],
                                               self.project_properties['device'])
        (x, y) = (self.ui.window.size().width(), self.ui.window.size().height())
        self.ui.window.resize(x + 1, y + 1)
        self.ui.floorplanScrollArea.resize(self.ui.floorplanScrollArea.size())

        #Informacja o poprawnym wczytaniu projektu
        self.ui.btnAddHeater.setEnabled(True)
        msg = "Project " + self.project_properties['name'] + " has been created successfully!"
        messageBox("Sukces", "New project", msg, 1)

    #Metoda obsługi dodawania nowych grzałek do floorplanu
    def showDialogNewHeater(self):
        #Utworzenie okienka dodawania grzałki
        newHeaterDlg = NewHeaterDialog()
        #Odpalenie okienka grzałki
        if newHeaterDlg.exec_():
            #Pobranie wartości z okienka dodowania grzałek
            values = newHeaterDlg.getValues()
            for heater in self.heaters_list:
                if heater['name'] == values['name']:
                    messageBox("Name already in use", "New heater", "Choosen name %s is already in use. "
                                                                    "Nothing change. Please choose another name." % (
                                                                    values['name']), 1)
                    return 0
            self.heaters_list.append(values)
            self.ui.heaterTable.refresh(self.heaters_list)

            index = len(self.heaters_list)
            self.ui.tableThermometers.clearSelection()
            self.ui.heaterTable.selectRow(index - 1)
            self.ui.FloorPlanFrame.heaterLoadEvent(values)
            self.ui.FloorPlanFrame.mouseSelection = False

    #Metoda obsługi dodawania nowych termometrów do floorplanu
    def showDialogNewTerm(self):
        #Utworzenie okienka dodawania termometru
        newTermDlg = NewThermDlg()
        #Odpalenie okienka dodania termometru
        if newTermDlg.exec_():
            #Pobranie wartości z okienka dodowania termometru
            values = newTermDlg.getValues()
            #Sprawdzenie dostępności nazwy
            for therm in self.ui.thermometers_list:
                if therm['name'] == values['name']:
                    messageBox("Name already in use", "New thermometer", "Choosen name %s is already in use. "
                                                                         "Please choose another" % (values['name']), 1)
                    return 0

            values["pos_x"] = ""
            values["pos_y"] = ""

            self.ui.thermometers_list.append(values)
            self.ui.tableThermometers.refresh(self.ui.thermometers_list)

            index = len(self.ui.thermometers_list)
            self.term_new = True
            self.ui.heaterTable.clearSelection()
            self.ui.tableThermometers.selectRow(index - 1)

            self.ui.FloorPlanFrame.thermLoadEvent(values)

            messageBox("Indicate thermometer position", "New thermometer", "Indicate the %s position. Please click "
                                                                           "on choosen block" % (values['name']), 1)
            self.ui.FloorPlanFrame.mouseSelection = False

    def deleteHeater(self):
        index = self.ui.heaterTable.selectIndex()
        params = self.heaters_list[index]
        self.heaters_list.remove(self.heaters_list[index])
        self.ui.heaterTable.refresh(self.heaters_list)
        self.ui.FloorPlanFrame.removeHeater(params)

    def deleteThermometer(self):
        index = self.ui.tableThermometers.selectIndex()
        params = self.ui.thermometers_list[index]
        self.ui.thermometers_list.remove(self.ui.thermometers_list[index])
        self.ui.tableThermometers.refresh(self.ui.thermometers_list)
        self.ui.FloorPlanFrame.removeThermometer(params)

    def showDialogModifyHeater(self):
        index = self.ui.heaterTable.selectIndex()
        modifyHeaterDlg = ModifyHeaterDlg(self.heaters_list[index])
        current_name = self.heaters_list[index]['name']

        if modifyHeaterDlg.exec_():
            values = modifyHeaterDlg.getValues()
            for heater in self.heaters_list:
                if heater['name'] == values['name'] and current_name != values['name']:
                    messageBox("Name already in use", "New heater", "Choosen name %s is already in use. "
                                                                    "Nothing change. Please choose another name." % (
                                                                    values['name']), 1)
                    return 0

            self.heaters_list[index]['name'] = values['name']
            self.heaters_list[index]['type'] = values['type']
            self.heaters_list[index]['color'] = values['color']
            self.ui.heaterTable.refresh(self.heaters_list)

            index = self.ui.heaterTable.selectIndex()

            self.ui.heaterTable.selectRow(index + 1)

            self.ui.FloorPlanFrame.heaterModifyEvent(values, index)

    def showDialogModifyTherm(self):
        index = self.ui.tableThermometers.selectIndex()
        modifyThermDlg = ModifyThermDlg(self.ui.thermometers_list[index])
        current_name = self.ui.thermometers_list[index]['name']

        if modifyThermDlg.exec_():
            #Pobranie wartości z okienka modyfikacji termometru
            values = modifyThermDlg.getValues()
            for therm in self.ui.thermometers_list:
                if therm['name'] == values['name'] and current_name != values['name']:
                    messageBox("Name already in use", "New thermometer", "Choosen name %s is already in use. "
                                                                         "Nothing change. Please choose another name." % (
                                                                         values['name']), 1)
                    return 0
            values["pos_x"] = ""
            values["pos_y"] = ""
            name = self.ui.thermometers_list[index]['name']
            self.ui.thermometers_list[index]['name'] = values['name']
            self.ui.thermometers_list[index]['type'] = values['type']

            self.ui.tableThermometers.refresh(self.ui.thermometers_list)

            self.ui.FloorPlanFrame.thermModifyEvent(name, values['name'])

    def showNewFloorplanFile(self):
        newFlDlgFile = FloorplanFileDlg()
        if newFlDlgFile.exec_():
            values = newFlDlgFile.getValues()
            xml = XMLcreator()
            #index = str(self.project_properties['project dir']).index(self.project_properties['name'])
            #dir = self.project_properties['project dir'][:index]
            #
            # KSB: fix - genrilo.xml was placed in an incorrect place 
            #      if dir name and project name was the same
            #      conversion to string is necessary for rfind feature not available in QString
            #
            dir = os.path.dirname(str(self.project_properties['project dir']))
            device = self.project_properties['device']
            mode = ''
            if self.project_properties['mode'] == QtCore.QString('emulation'):
                mode = 'emulation'
            elif self.project_properties['device'] == QtCore.QString('Microblaze measurement'):
                mode = 'uBlinux'

            xml.createSimulationSystemDescription(self.ui.FloorPlanFrame.floorplan, values[0], values[1], dir, device,
                                                  mode)
            self.project_xml.addFloorplanFile()

    def showSaveFile(self):
        self.showNewFloorplanFile()

    def showAbout(self):
        about = AboutDlg()
        if about.exec_():
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = FloorplanMakerWindow()
    myapp.show()
    sys.exit(app.exec_())
