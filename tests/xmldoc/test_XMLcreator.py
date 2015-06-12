from unittest import TestCase
from src.xmldoc.XMLCreator import XMLcreator

__author__ = 'pawel'


class TestXMLcreator(TestCase):

    def setUp(self):
        self.xml_proj = XMLcreator('../../test_data/proj.xml')
        self.xml_proj_bad = XMLcreator('../../test_data/generilo.xml')

    def test_isProjectFile(self):
        self.assertTrue(self.xml_proj)
        # TODO check what the hell : P
        #self.assertFalse(self.xml_proj_bad)

    def test_ProjectDirectory(self):
        self.assertEqual(self.xml_proj.proj_directory,
                         '/home/pawel/Development/FloorplanMaker/test_data')

    def test_getDeviceDescriptor(self):
        print self.xml_proj.getDeviceDescriptor()
        self.assertEqual(self.xml_proj.getDeviceDescriptor(),
                         '/'.join([self.xml_proj.proj_directory,'floorplan.xml']))

    def test_getDesignFile(self):
        self.assertEqual(self.xml_proj.getDesignFile(),
                         '/'.join([self.xml_proj.proj_directory,'generilo.xml']))

    def test_getDeviceVersion(self):
        pass

    def test_getEmulationMode(self):
        pass

    def test_getProjectFile(self):
        pass

    def test_getProjectName(self):
        pass

    def test_createNewProjectFile(self):
        pass

    def test_createSimulationSystemDescription(self):
        pass

    def test_addFloorplanFile(self):
        pass