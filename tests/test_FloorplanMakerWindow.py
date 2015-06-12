from unittest import TestCase
from PyQt4 import QtGui
import sys
import unittest
from src.FloorplanMaker import FloorplanMakerWindow

__author__ = 'pawel'


class TestFloorplanMakerWindow(TestCase):
    @unittest.skip("Not used")
    def test_generateThermometers(self):
        pass

    @unittest.skip("Not used")
    def test_heatersTableSelection(self):
        pass

    @unittest.skip("Not used")
    def test_unselectHeater(self):
        pass

    @unittest.skip("Not used")
    def test_showDialogOpenProject(self):
        pass

    @unittest.skip("Not used")
    def test_showNewProject(self):
        pass

    @unittest.skip("Graphical function")
    def test_showDialogNewHeater(self):
        pass

    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.myapp = FloorplanMakerWindow()
        self.myapp.loadProjectXML('../test_data/proj.xml')

    def test_loadProjectXML(self):
        self.assertEqual(self.myapp.project_properties.get('project dir'), '')
        self.assertEqual(self.myapp.project_properties.get('name'), 'proj')
        self.assertEqual(self.myapp.project_properties.get('device'), 'Virtex5')
        self.assertEqual(self.myapp.project_xml.getDeviceDescriptor(),'/home/pawel/Development/FloorplanMaker/test_data/floorplan.xml')

    def test_loadHeatersToDesign(self):
        for index, heater in enumerate(self.myapp.heaters_list):
            self.assertEqual('heater{}'.format(index+1), heater['name'])

    def test_loadThermometersToDesign(self):
        for index, thermometer in enumerate(self.myapp.ui.thermometers_list):
            self.assertEqual(index+1, int(thermometer['name']))

    @unittest.skip("Not used")
    def test_showDialogNewTerm(self):
        pass

    @unittest.skip("Not used")
    def test_deleteHeater(self):
        pass

    @unittest.skip("Not used")
    def test_deleteThermometer(self):
        pass

    @unittest.skip("Not used")
    def test_showDialogModifyHeater(self):
        pass

    @unittest.skip("Not used")
    def test_showDialogModifyTherm(self):
        pass

    @unittest.skip("Not used")
    def test_showNewFloorplanFile(self):
        pass

    @unittest.skip("Not used")
    def test_showSaveFile(self):
        pass

    @unittest.skip("Not used")
    def test_showAbout(self):
        pass

    def tearDown(self):
        self.myapp.show()