# -*- coding: utf-8 -*-
__author__ = 'pawel'

# KSB: fix - genrilo.xml was placed in an incorrect place 
import os.path

from xml.dom.minidom import Document, parse

class XMLcreator:
    # Tworzy nowy document xml
    def __init__(self, fopen=None):
        if(fopen):
            self.doc = parse(str(fopen))
            self.proj_directory = os.path.dirname(os.path.realpath(str(fopen)))
        else:
            self.doc = Document()

    #Metoda sprawdzająca czy dany plik XML jest plikiem opisu projektu
    def isProjectFile(self):
        if self.doc.getElementsByTagName("FloorplanMaker"):
            return True
        else:
            return False

    def getDeviceDescriptor(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        des = project.getElementsByTagName("Description_file")[0]

        des_src = des.getAttribute("src")
        return '/'.join([self.proj_directory,des_src])

    def getDeviceVersion(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        device = project.getElementsByTagName("Properties")[0]

        return device.getAttribute("model")

    def getEmulationMode(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        device = project.getElementsByTagName("Properties")[0]

        return device.getAttribute("mode")

    def getDesignFile(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        fl = project.getElementsByTagName("Design_file")[0]

        fl_src = fl.getAttribute("src")
        return '/'.join([self.proj_directory,fl_src])

    def getProjectFile(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        fl = project.getElementsByTagName("Project_file")[0]

        fl_src = fl.getAttribute("scr")
        return fl_src

    def getProjectName(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]

        name = project.getAttribute("name")
        return name

    # Metoda tworząca pliku xml projektu
    def createNewProjectFile(self, project_name, project_file_dir, description_file_dir, device, mode):
        FloorplanMaker = self.doc.createElement("FloorplanMaker")
        FloorplanMaker.setAttribute("version","0.1")
        self.doc.appendChild(FloorplanMaker)

        # Tworzenie elementu project
        project = self.doc.createElement("Project")
        project.setAttribute("name", project_name)
        project.setAttribute("author", "Pawel")
        FloorplanMaker.appendChild(project)

        # Tworzenie elementu plik projektu
        fproject = self.doc.createElement("Project_file")
        fproject.setAttribute("src", project_name+'.xml')

        # Tworzenie elementu plik opisu płytki
        fdesign = self.doc.createElement("Description_file")
        fdesign.setAttribute("src", description_file_dir)

        # Tworzenie elementu device
        fproperties = self.doc.createElement("Properties")
        fproperties.setAttribute("model", device)
        fproperties.setAttribute("mode",mode)

        project.appendChild(fproject)
        project.appendChild(fdesign)
        project.appendChild(fproperties)

        # Zapisanie wygenerowanego opisu projektu do pliku
        # --DEBUGER_LINE--
        # print self.doc.toprettyxml(indent="  ")
        plik = open(project_file_dir, "w+")
        self.doc.writexml(plik, indent="\n", addindent="\t")
        plik.close()

    def createSimulationSystemDescription(self, floorplan, oldNcd, newNcd, dir, device, mode):
        board = self.doc.createElement("board")
        board.setAttribute("version","0.1")
        board.setAttribute("device",device)
        board.setAttribute("mode",mode)
        self.doc.appendChild(board)

        input = self.doc.createElement("input")
        input.setAttribute("name",str(oldNcd))
        board.appendChild(input)

        output = self.doc.createElement("output")
        output.setAttribute("name",str(newNcd))
        board.appendChild(output)

        #Heaters list creating
        for h in floorplan.heaters:
            heater = self.doc.createElement("heater")
            heater.setAttribute("name", h[0])
            heater.setAttribute("type", h[3])
            heater.setAttribute("FMColor", str(h[2]))
            board.appendChild(heater)
            unit = floorplan.floorplan

            clbs = 0
            for x in range(floorplan.cols):
                for y in range(floorplan.rows):
                    if unit[y*floorplan.cols+x] == floorplan.indexOfHeater(h[0]):
                        clb = self.doc.createElement("clb")
                        clb.setAttribute("col",str(x))
                        clb.setAttribute("row",str(y))
                        heater.appendChild(clb)
                        clbs = clbs + 1
            print "heater {} : {} CLBS".format(h[0], clbs)

        #Thermometer list creating
        for key,t in floorplan.therms.iteritems():
            thermometer = self.doc.createElement("thermometer")
            thermometer.setAttribute("name",key)
            thermometer.setAttribute("type",t["type"])
            thermometer.setAttribute("col", str(t["x_pos"]))
            thermometer.setAttribute("row", str(t["y_pos"]))
            board.appendChild(thermometer)

        #
        # KSB: fix - genrilo.xml was placed in an incorrect place 
        #      concatenating paths requires os.path.join to be portable
        #
        plik = open(os.path.join(dir,"generilo.xml"),"w+")
        self.doc.writexml(plik, indent="\n", addindent="\t")
        plik.close()

    def addFloorplanFile(self):
        fmaker = self.doc.getElementsByTagName("FloorplanMaker")[0]
        project = fmaker.getElementsByTagName("Project")[0]
        name = project.getAttribute("name")

        fproject = project.getElementsByTagName("Project_file")[0]
        project_dir = fproject.getAttribute("src")
        project_dir = project_dir[:len(project_dir)-(len(name)+4)]

        # Tworzenie elementu plik projektu
        if(not(project.getElementsByTagName("Design_file"))):
            flproject = self.doc.createElement("Design_file")
            flproject.setAttribute("src", "generilo.xml")
            project.appendChild(flproject)
            plik = open(fproject.getAttribute("src"),"w+")
            self.doc.writexml(plik, indent="\n", addindent="\t")
            plik.close()
