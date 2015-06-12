# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString
from Parameters import Param
from floorplan import Floorplan
__author__ = 'pawel'

from PyQt4 import QtCore, QtGui
from xmldoc.XMLReader import XMLreader

class FloorplanFrame(QtGui.QFrame):

    def __init__(self, parent, main):
        super(FloorplanFrame, self).__init__(parent)
        self.loaded_file = False
        self.added_heater = False
        self.added_term = False
        self.mouseSelection = False
        self.mouseDoubleClick = False
        self.initUI()
        self.heaters = []
        self.main = main
        self.oldmovex = 0
        self.moveX = 0
        self.block_size = 8
        self.block_shift = 10
        self.zoom = 0

    def initUI(self):
        self.show()

    #Metoda zdarzenia załadowania nowego pliku z opisem układu wczytuje zdany układ i odwzorowywuje go.
    def fileLoadedEvent(self, fpgaDescription, device):
        self.loaded_file = True
        self.xml = XMLreader(fpgaDescription)
        self.xml.parseFile()
        #Wczytanie do obiektu klasy FloorPlan informacji o Unitach i Obstaclach
        self.floorplan = Floorplan(self.xml.cols, self.xml.rows)
        for y in range(self.xml.rows):
            for x in range(self.xml.cols):
                if self.xml.floorplan[y*self.xml.cols + x] == 1:
                    self.floorplan.addObstacle(x,y)
                elif self.xml.floorplan[y*self.xml.cols + x] == 2:
                    self.floorplan.addUnit(x,y)
        print device
        if device == "s3e500":
            self.resizeFloorplan(460, 585)
        elif device == "Atlys":
            self.resizeFloorplan(940, 1450)
        elif device == "Virtex5":
            self.resizeFloorplan()

    def resizeFloorplan(self, x=1690, y=1830, device='Virtex5'):
        self.main.FrameFloorplan.setMinimumSize(x, y)
        self.main.FrameFloorplan.resize(x, y)
        self.setMinimumSize(x, y)
        self.resize(x, y)
        self.main.floorplanScrollArea.resize(x + 35, y + 35)
        self.x = x
        self.y = y
        self.repaint()

    #Metoda zdarzenia załadowania odczytywanego pliku floorplanu
    def fileFloorplanLoadedEvent(self, floorplanFile):
        print "Floorplan " + floorplanFile
        self.loaded_file = True
        self.xmlFl = XMLreader(floorplanFile)
        print self.floorplan.cols
        self.xmlFl.parseFile(file="floor",floorplan=self.floorplan)
        self.repaint()

    '''METODY OBSŁUGI ZDARZEŃ NA GRZAŁKACH'''
    def heaterLoadEvent(self, params):
        self.added_heater = True
        self.floorplan.addNewHeater(params)
        self.repaint()

    def heaterModifyEvent(self, params, index):
        self.floorplan.modifyHeater(params, index)
        self.repaint()

    def removeHeater(self,params):
        self.floorplan.removeHeater(params)
        self.repaint()

    '''METODY OBSŁUGI ZDARZEŃ NA TERMOMETRACH'''
    def thermLoadEvent(self, params):
        self.added_term = True
        self.floorplan.addNewTerm(params)
        self.repaint()

    def removeThermometer(self,params):
        self.floorplan.removeThermometer(params)
        self.repaint()

    def thermModifyEvent(self, name, new_name):
        self.floorplan.modifyThermometer(name, new_name)
        self.repaint()

    '''METODY OBSŁUGI SYGNAŁÓW MYSZY'''

    '''Metoda pojedynczego kliknięcia myszy.
        * Pobranie współrzędnych
        * Sprawdzenie ruchu na potrzeby zaznaczenia '''
    def mousePressEvent(self,event):
        self.oldmovex = self.moveX
        self.mouseSelection = True
        self.pressX = event.x()
        self.pressY = event.y()
        self.moveX = event.x()
        self.moveY = event.y()

    '''Metoda podwójnego kliknięcia myszy.
        *Pobranie współrzędnych kliknięcia
        *Zaznaczenie lub usunięcie pojedynczej grzałki '''
    def mouseDoubleClickEvent(self, QMouseEvent):
        self.mouseSelection = False
        self.pressX = QMouseEvent.x()
        self.pressY = QMouseEvent.y()

        if self.main.heaterTable.selectedItems():
            #dane grzałek
            tabHeater = self.main.heaterTable
            indexes = tabHeater.selectedItems()
            nameHeater = str(tabHeater.itemFromIndex(tabHeater.indexFromItem(indexes[1])).text())
            xy = self.getXY()
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                if self.floorplan.emptyElement(xy[0],xy[1]):
                    self.floorplan.addHeaterUnit(nameHeater,xy[0],xy[1])
                    self.repaint()
            elif QMouseEvent.button() == QtCore.Qt.RightButton:
                self.floorplan.removeHeaterUnit(nameHeater,xy[0],xy[1])
                self.repaint()
        elif self.main.tableThermometers.selectedItems():
            #dane termometrów
            tabTerm = self.main.tableThermometers
            indexes = tabTerm.selectedItems()
            nameTerm = str(QtCore.QString(tabTerm.itemFromIndex(tabTerm.indexFromItem(indexes[0])).text()))

            therm = self.floorplan.therms[nameTerm]

            xy = self.getXY()
            if QMouseEvent.button() == QtCore.Qt.LeftButton:
                if self.floorplan.emptyElement(xy[0],xy[1]) and therm['placed']:
                    self.floorplan.replaceTermUnit(nameTerm,therm['x_pos'],therm['y_pos'],xy[0],xy[1])
                    self.floorplan.therms[nameTerm]['x_pos'] = self.main.thermometers_list[therm['index']-30]['pos_x'] = xy[0]
                    self.floorplan.therms[nameTerm]['y_pos'] = self.main.thermometers_list[therm['index']-30]['pos_y'] = xy[1]
                    self.repaint()
                if self.floorplan.emptyElement(xy[0],xy[1]) and not(self.floorplan.therms[nameTerm]['placed']):
                    self.floorplan.addTermUnit(nameTerm,xy[0],xy[1])
                    self.floorplan.therms[nameTerm]['x_pos'] = self.main.thermometers_list[therm['index']-30]['pos_x'] = xy[0]
                    self.floorplan.therms[nameTerm]['y_pos'] = self.main.thermometers_list[therm['index']-30]['pos_y'] = xy[1]
                    self.repaint()
                self.main.tableThermometers.refresh(self.main.thermometers_list)
            elif QMouseEvent.button() == QtCore.Qt.RightButton:
                pass
                self.repaint()

    '''Metoda obsługi ruchu myszy
        * Pobieranie współrzędnych
        * Wyzwalanie rysowania okienka zaznaczenia '''
    def mouseMoveEvent(self, event):
        self.moveX = event.x()
        self.moveY = event.y()

        self.repaint()

    #Metoda podaje XY grzałki zaznaczonej na floorplanie
    def getXY(self):
        x = (self.pressX-20)/self.block_shift
        y = (self.pressY-20)/self.block_shift
        return [x,y]

    def roundXY(self, number):
        number /= self.block_shift
        number *= self.block_shift

        return number

    def getXYHeatersNumber(self):
        x = (abs(self.pressX-self.moveX))/self.block_shift
        y = (abs(self.pressY-self.moveY))/self.block_shift
        return [x,y]

    def mouseReleaseEvent(self, event):
        if self.mouseSelection:
            try:
                if self.main.heaterTable.selectedItems():
                    if self.oldmovex!=self.moveX:
                        tab = self.main.heaterTable
                        indexes = tab.selectedItems()
                        name = str(tab.itemFromIndex(tab.indexFromItem(indexes[1])).text())
                        if self.moveX < self.pressX:
                            self.moveX = self.roundXY(self.moveX)
                            self.pressX = self.roundXY(self.pressX+self.block_shift)
                        else:
                            self.pressX = self.roundXY(self.pressX)
                            self.moveX = self.roundXY(self.moveX+self.block_shift)
                        if self.moveY < self.pressY:
                            self.pressY = self.roundXY(self.pressY+self.block_shift)
                            self.moveY = self.roundXY(self.moveY)
                        else:
                            self.pressY = self.roundXY(self.pressY)
                            self.moveY = self.roundXY(self.moveY+self.block_shift)
                        xy = self.getXY()
                        mxy = self.getXYHeatersNumber()
                        if self.moveX < self.pressX:
                            xy[0] -= (mxy[0])
                        if self.moveY < self.pressY:
                            xy[1] -= (mxy[1])

                        if event.button() == QtCore.Qt.LeftButton:
                            for i in range(mxy[0]):
                                for j in range(mxy[1]):
                                    if self.floorplan.emptyElement(i+xy[0],j+xy[1]):
                                        self.floorplan.addHeaterUnit(name,i+xy[0],j+xy[1])
                        elif event.button()==QtCore.Qt.RightButton:
                            for i in range(mxy[0]):
                                for j in range(mxy[1]):
                                    self.floorplan.removeHeaterUnit(name,i+xy[0],j+xy[1])
            except IndexError:
                pass
        self.mouseSelection = False
        self.repaint()

    ''' METODY RYSOWANIA '''

    def paintEvent(self, QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.loaded_file:
            self.drawFpga(qp)
        if self.added_heater:
            self.drawHeaters(qp)
        if self.mouseSelection:
            self.drawMouseSelection(qp)
        qp.end()

    def drawHeaters(self, qp):
        for heater in self.heaters:
            x_pos = int(heater["x"])
            y_pos = int(heater["y"])
            w = heater["width"]
            h = heater["height"]
            color = heater["color"]
            kolor = QtGui.QColor(color)
            for x in range(w):
                for y in range(h):
                    qp.fillRect(QtCore.QRect(20+(x+x_pos)*self.block_shift, 20+(y+y_pos)*self.block_shift, self.block_size, self.block_size), kolor)

    def drawMouseSelection(self, qp):
        try:
            qp.setPen(QtCore.Qt.black)
            qp.drawRect(self.pressX, self.pressY, self.moveX-self.pressX,
                self.moveY-self.pressY)
            qp.fillRect(QtCore.QRect(self.pressX, self.pressY, self.moveX-self.pressX,
                self.moveY-self.pressY), QtCore.Qt.Dense5Pattern)
        except: pass

    def zoomIn(self):
        if self.zoom == 2:
            self.block_size = 6
            self.block_shift = 7
            self.resizeFloorplan(self.x*(7./5),self.y*(7./5))
            self.zoom = 1
        elif self.zoom == 1:
            self.block_size = 8
            self.block_shift = 10
            self.resizeFloorplan(self.x*(10./7),self.y*(10./7))
            self.zoom = 0
        self.repaint()
        #self.generateTexFile()

    def zoomOut(self):
        if self.zoom == 0:
            self.block_size = 6
            self.block_shift = 7
            self.resizeFloorplan(self.x*0.7, self.y*0.7)
            self.zoom = 1
        elif self.zoom == 1:
            self.block_size = 4
            self.block_shift = 5
            self.resizeFloorplan(self.x*(5./7), self.y*(5./7))
            self.zoom = 2
        self.repaint()

    def drawFpga(self, qp):
        qp.setPen(QtCore.Qt.black)
        qp.setFont(QtGui.QFont('Decorative', 5))

        #Rysowanie czystego układu FPGA
        for x in range(self.xml.cols):
            for y in range(self.xml.rows):
                if self.floorplan.getElementIndex(x, y) == Param.obstacle:
                    qp.fillRect(QtCore.QRect(20+x*self.block_shift, 20+y*self.block_shift, self.block_size, self.block_size), QtCore.Qt.black)
                elif self.floorplan.getElementIndex(x, y) == Param.unit:
                    qp.fillRect(QtCore.QRect(20+x*self.block_shift, 20+y*self.block_shift, self.block_size, self.block_size), QtCore.Qt.darkGray)
                elif self.floorplan.getElementIndex(x, y) == Param.free:
                    qp.fillRect(QtCore.QRect(20+x*self.block_shift, 20+y*self.block_shift, self.block_size, self.block_size),QtCore.Qt.white)
                elif 1 <= self.floorplan.getElementIndex(x, y) <= Param.heater_top:
                    qp.fillRect(QtCore.QRect(20+x*self.block_shift ,20+y*self.block_shift, self.block_size, self.block_size),
                        QtGui.QColor(self.floorplan.getColorByIndex(self.floorplan.getElementIndex(x, y))))
                #Rysowanie termometrów
                elif self.floorplan.getElementIndex(x,y)>=30:
                    if self.main.tableThermometers.selectedItems():
                        tabTerm = self.main.tableThermometers
                        indexes = tabTerm.selectedItems()
                        nameTerm = str(QtCore.QString(tabTerm.itemFromIndex(tabTerm.indexFromItem(indexes[0])).text()))
                        try:
                            if self.floorplan.getElementIndex(x,y) == self.floorplan.therms[nameTerm]['index']:
                                qp.setBrush(QtCore.Qt.green)
                        except:
                            qp.setBrush(QtCore.Qt.red)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(QtCore.QRect(20+x*self.block_shift, 20+y*self.block_shift, self.block_size, self.block_size))
                    qp.setBrush(QtCore.Qt.transparent)

                #Rysowanie opisu osi
                if y==0:
                    qp.drawText(QtCore.QPointF(20+x*self.block_shift,15),str(x))
                    #qp.drawText(QtCore.QPointF(20+x*10,575),str(x))
                if x==0:
                    qp.drawText(QtCore.QPointF(6,26+y*self.block_shift),str(y))
                    #qp.drawText(QtCore.QPointF(430,26+y*10),str(y))

    def generateTexFile(self):
        doc = u"""
                \\documentclass{article}
                \\usepackage{tikz}

                \\begin{document}
               """

        for x in range(self.xml.cols):
            for y in range(self.xml.rows):
                if self.floorplan.getElementIndex(x, y) == Param.obstacle:
                    doc += "\\tikz \\fill [{color}] ({col},{row}) rectangle ({col2},{row2});\n".format(color="black",
                                col=0.01+0.01*x, col2=0.02+0.01*x, row=0.01+0.01*y, row2=0.02+0.01*y)
                elif self.floorplan.getElementIndex(x, y) == Param.unit:
                    doc += "\\tikz \\fill [{color}] ({col},{row}) rectangle ({col2},{row2});\n".format(color="gray",
                                col=0.01+0.01*x, col2=0.02+0.01*x, row=0.01+0.01*y, row2=0.02+0.01*y)
                elif self.floorplan.getElementIndex(x, y) == Param.free:
                    doc += "\\tikz \\fill [{color}] ({col},{row}) rectangle ({col2},{row2});\n".format(color="white",
                                col=0.01+0.01*x, col2=0.02+0.01*x, row=0.01+0.01*y, row2=0.02+0.01*y)
                elif 1 <= self.floorplan.getElementIndex(x, y) <= Param.heater_top:
                    doc += "\\tikz \\fill [{color}] ({col},{row}) rectangle ({col2},{row2});\n".format(color="orange",
                                col=0.01+0.01*x, col2=0.02+0.01*x, row=0.01+0.01*y, row2=0.02+0.01*y)
                #Rysowanie termometrów
                '''
                elif self.floorplan.getElementIndex(x,y)>=30:
                    if self.main.tableThermometers.selectedItems():
                        tabTerm = self.main.tableThermometers
                        indexes = tabTerm.selectedItems()
                        nameTerm = QtCore.QString(tabTerm.itemFromIndex(tabTerm.indexFromItem(indexes[0])).text())
                        try:
                            if self.floorplan.getElementIndex(x,y) == self.floorplan.therms[nameTerm]['index']:
                                qp.setBrush(QtCore.Qt.green)
                        except:
                            qp.setBrush(QtCore.Qt.red)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(QtCore.QRect(20+x*self.block_shift, 20+y*self.block_shift, self.block_size, self.block_size))
                    qp.setBrush(QtCore.Qt.transparent)

                #Rysowanie opisu osi
                if y==0:
                    qp.drawText(QtCore.QPointF(20+x*self.block_shift,15),str(x))
                    #qp.drawText(QtCore.QPointF(20+x*10,575),str(x))
                if x==0:
                    qp.drawText(QtCore.QPointF(6,26+y*self.block_shift),str(y))
                    #qp.drawText(QtCore.QPointF(430,26+y*10),str(y))
                '''
        doc += "\end{document}"

        f = open("lol.tex","w+")
        f.write(doc)
        f.close()
