# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
from PyQt4.QtCore import QString, Qt
from PyQt4.QtGui import QColor

__author__ = 'pawel'
from Parameters import Param


class Floorplan:

    colors = {QString("niebieski"):Qt.blue, QString("ciemny niebieski"): Qt.darkBlue,
              QString("czerwony"):Qt.red, QString("ciemny czerwony"): Qt.darkRed,
              QString("zielony"):Qt.green, QString("ciemny zielony"): Qt.darkGreen,
              QString("cyjan"): Qt.cyan, QString("ciemny cyjan"): Qt.darkCyan,
              QString("magenta"): Qt.magenta, QString("ciemna magenta"): Qt.darkMagenta,
              QString("szary"): Qt.gray, QString("ciemny szary"): Qt.darkGray,
              QtGui.QApplication.translate("newHeaterDialog", "żółty", None, QtGui.QApplication.UnicodeUTF8): Qt.yellow,
              QtGui.QApplication.translate("newHeaterDialog", "ciemny żółty", None,
                                           QtGui.QApplication.UnicodeUTF8): Qt.darkYellow}

    def __init__(self, cols, rows):
        #Zdefiniowanie pustego floorplanu i wyczysczenie listy zawartości
        self.floorplan = []
        self.cols = cols
        self.rows = rows

        for i in range(rows):
            for j in range(cols):
                self.floorplan.append(0)

        #Lista przechowująca inofrmacje o nazwie i identyfikatorze grzałki
        self.heaters = []
        self.therms = {}
        self.term_index = 30

    def addNewHeater(self, params):
        color = params["color"]

        if self.heaters:
            self.heaters.append([params["name"], self.heaters[-1][1]+1, color, params["type"]])
        else:
            self.heaters.append([params["name"], 1, color, params["type"]])

    def addNewTerm(self, params):
        attributes = {'index': self.term_index, 'type': params['type'], 'placed': False}
        self.therms[params['name']] = attributes
        self.term_index += 1

    def modifyHeater(self, params,index):
        item = QtGui.QTableWidgetItem("")
        item.setBackgroundColor(QColor(params["color"]))
        color = item.backgroundColor().name()

        self.heaters[index][0] = params["name"]
        self.heaters[index][2] = color
        self.heaters[index][3] = params["type"]

    def modifyThermometer(self,name,new_name):
        self.therms[new_name] = self.therms[name]
        del self.therms[name]

    def removeHeater(self, params):
        index = self.indexOfHeater(params["name"])

        item = QtGui.QTableWidgetItem("")
        item.setBackgroundColor(QColor(params["color"]))
        color = item.backgroundColor().name()

        self.heaters.remove([params["name"], index, color, params["type"]])
        for i in range(self.cols*self.rows):
            if self.floorplan[i] == index:
                self.floorplan[i]=0

        for i in range(self.cols*self.rows):
            if index < self.floorplan[i] < 30:
                self.floorplan[i]-=1

        for i in range(len(self.heaters)):
            if index < self.heaters[i][1] < 30:
                self.heaters[i][1]-= 1

    def removeThermometer(self, params):
        index = self.therms[params['name']]['index']

        self.removeTermUnit(params['name'],params['pos_x'],params['pos_y'])

        self.therms.pop(params['name'])
        self.term_index-=1

        for key,value in self.therms.items():
            if value['index']>index:
                self.reIndexTermUnit(value['index'])
                value['index']-=1

    def heatersNumber(self):
        return self.heaters[-1][1]

    def indexOfHeater(self,name):
        for h in self.heaters:
            if h[0] == name:
                return h[1]

    def addHeaterUnit(self,name,x,y):
        self.floorplan[y*self.cols+x] = self.indexOfHeater(name)

    def removeHeaterUnit(self,name,x,y):
        if self.floorplan[y*self.cols+x] == self.indexOfHeater(name):
            self.floorplan[y*self.cols+x] = 0

    def addTermUnit(self, name, x, y, openProject = False):
        self.floorplan[y*self.cols+x] = self.therms[name]['index']
        self.therms[name]['placed'] = True
        if openProject:
            self.therms[name]['x_pos'] = x
            self.therms[name]['y_pos'] = y

    def replaceTermUnit(self,name,x,y,x_new,y_new):
        if self.floorplan[y*self.cols+x] == self.therms[str(name)]['index']:
            self.floorplan[y*self.cols+x] = 0
        self.floorplan[y_new*self.cols+x_new] = self.therms[str(name)]['index']

    def removeTermUnit(self,name,x,y):
        if self.floorplan[y*self.cols+x] == self.therms[name]['index']:
            self.floorplan[y*self.cols+x] = 0

    def reIndexTermUnit(self,index):
        for i in range(self.cols*self.rows):
            if self.floorplan[i] == index:
                self.floorplan[i]-=1

    def addObstacle(self,x,y):
        self.floorplan[y*self.cols+x] = Param.obstacle

    def addUnit(self,x,y):
        self.floorplan[y*self.cols+x] = Param.unit

    def getElementIndex(self,x,y):
        return self.floorplan[y*self.cols+x]

    def getTermPosition(self,name):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.getElementIndex(i,j) == self.therms[name]['index']:
                    return j,i

    def emptyElement(self,x,y):
        if self.floorplan[y*self.cols+x]:
            return False
        else:
            return True

    def getColorByIndex(self, index):
        return self.heaters[int(index)-1][2]

    def sortTherms(self):
        for therm in sorted(self.therms.items()):
            print therm


    '''Metoda wypisująca tekstowo wyglad płytki'''
    def printTextFloorplan(self):
        k = 0
        for i in range(self.rows):
            if i!=0:
                sys.stdout.write(str(i) + "\t")
            for j in range(self.cols):
                if i==0:
                    sys.stdout.write("\t" + str(j+1))
                else:
                    sys.stdout.write(str(self.floorplan[self.cols*(i-1) + j]) + " ")
                    k += 1
            sys.stdout.write("\n")
        print "Razem bloków funkcyjnych: " + str(k)
