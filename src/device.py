import xml.dom.minidom as dom
from math import *

class Element:
	x = 0
	y = 0

	def __eq__(self,other):
		if(isinstance(other,Element)):
			if( self.x == other.x and self.y == other.y):
				return True
			else:
				return False
		return NotImplemented

	def __ne__(self,other):
		if(isinstance(other,Element)):
			if(self.x != other.x or self.y != other.y):
				return True
			else:
				return False
		return NotImplemented

	def __init__(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
class Device:
	__columns = 0
	__rows = 0

	__occupiedSpace = list()
	__freeSpace = list()

        __firstUnit = 0

	def __init__(self):
		pass

	def getColumns(self):
		return self.__columns

	def getRows(self):
		return self.__rows

	def getOccupiedSpace(self):
		return self.__occupiedSpace

	def getFreeSpace(self):
		return self.__freeSpace

	def setFreeSpaceFromFile(self, xmlDocument):
		self.setOccupiedSpaceFromFile(xmlDocument)

		occ = self.getOccupiedSpace()

		oldY = occ[0].y

		freeList = list()

		for element in occ:

			diff = element.y - oldY

			if(diff > 1):
				for i in range(1,diff):
					newElement = Element(element.x, oldY + i)
					freeList.append(newElement)
			oldY = element.y

		sortedFreeList = sorted(freeList, key= lambda obj: (obj.x, obj.y))

		self.__freeSpace = sortedFreeList


	def setDeviceSizeFromFile(self,xmlDocument):
		size = xmlDocument.getElementsByTagName("size")
		size = size[0]

		self.__columns = size.getAttribute("cols")
		self.__rows = size.getAttribute("rows")

	def setOccupiedSpaceFromFile(self,xmlDocument):
		obstacles = xmlDocument.getElementsByTagName("obstacle")
		units = xmlDocument.getElementsByTagName("unit")
                self.getFirstUnitOccurence(units)
		occupied = obstacles + units

		occ = list()

		for element in occupied:
			x = element.getAttribute("x")
			y = element.getAttribute("y")

			newElement = Element(int(x),int(y))
			occ.append(newElement)

		sortedOccupied = sorted(occ, key= lambda obj: (obj.x, obj.y))

		self.__occupiedSpace = sortedOccupied


	def generateLinearThermometers(self,xmlOutputDocument, thermNumber):
		root = xmlOutputDocument.getElementsByTagName("board")
		root = root[0]
		oldY = 0

		thermID = 0

		occList = self.getOccupiedSpace()

		for occ in occList:

			col = occ.x
			row = occ.y

			diff = row - oldY
			

			if(diff > 1):
				for i in range(1,diff):
					newTherm = xmlOutputDocument.createElement("thermometer")
					newTherm.setAttribute("name", "t{}".format(thermID))
					newTherm.setAttribute("type", "RO7")
					newTherm.setAttribute("col", str(col)) 
					newTherm.setAttribute("row", str(oldY + i)) 
					root.appendChild(newTherm)

					thermID = thermID + 1

					if(thermID > int(thermNumber) - 1):
						return xmlOutputDocument

			oldY = row

		return xmlOutputDocument

	def getFreeRowLenList(self,freeList):
		rowsLen = list()

		freeList = self.getFreeSpace()
		
		oldRowLen = freeList[0].x

		#make a list of rows length
		for element in freeList:
			diff = element.x - oldRowLen

			if(diff < 0):
				rowsLen.append(int(oldRowLen + 1))
			elif(freeList[-1] is element):
				rowsLen.append(int(element.x + 1))

			oldRowLen = element.x

		return rowsLen

        def getFirstUnitOccurence(self,units):
                unitsList = list()


                for unit in units:
                    x = unit.getAttribute("x")
                    y = unit.getAttribute("y")
                    newElement = Element(int(x),int(y))
                    unitsList.append(newElement)


                firstElement = unitsList[1]

                self.__firstUnit = firstElement

                print("First Unit x: {} y: {}".format(firstElement.x,firstElement.y))


	def getFreeColumnLenList(self,freeList):
		colsLen = list()

		oldColLen = freeList[0].y

	
		for element in freeList:
			diff = element.y - oldColLen
			
			if(diff < 0):
				colsLen.append(int(oldColLen + 1))
			elif(freeList[-1] is element):
				colsLen.append(int(element.y + 1))

		return colsLen

	def getFreeRowLen(self,sortedFreeList):

		maximum = -1
                l = 0

		listLen = len(sortedFreeList)
		colLen = self.getFreeColLen(sortedFreeList)

		for i in range(0,listLen,colLen):
			if(sortedFreeList[i] > maximum):
				maximum = sortedFreeList[i].x
                                l = l + 1
			else:
				break
		return l

	def getFreeColLen(self,sortedFreeList):

		maximum = -1
                l = 0

		for i in sortedFreeList:
			if(i.y > maximum):
				maximum = i.y
                                l = l + 1
			else:
				break

		return l

        def getFreeSingleRow(self,freeList,index):

                singleColumnList = list()
                for item in freeList:
                    if(item.y == index):
                        singleColumnList.append(item.x)
                        
                return singleColumnList

        def getFreeSingleColumn(self, freeList, index):

                singleRowList = list()

                for item in freeList:
                    if(item.x == index):
                        singleRowList.append(item.y)
                    elif(item.x > index):
                        break

                return singleRowList

        def generateCoords(self, coordList, termNumber):
                coordLen = len(coordList)        
                posList = list()
                for i in range(1,coordLen):
                    termsLeft = termNumber
                    newList = list()
                    for item in range(0,coordLen,i):
                        newList.append(coordList[item])
                        termsLeft = termsLeft - 1

                        if(termsLeft < 0 or termsLeft == 0):
                            break

                    if(termsLeft == 0):
                        posList = newList

                return posList

	def generateThermometersNet(self, xmlOutDocument,thermsInRow, rowsNumber):

		xmlList = xmlOutDocument.getElementsByTagName("board")
		root = xmlList[0]
			
		freeList = self.getFreeSpace()
                row = self.getFreeSingleRow(freeList,6)
                column = self.getFreeSingleColumn(freeList,38)
                colsCoords = self.generateCoords(row,int(thermsInRow))
                rowsCoords = self.generateCoords(column, int(rowsNumber))

                thermID = 0

                for row in rowsCoords:
                    for col in colsCoords:
                        newElement = xmlOutDocument.createElement("thermometer")
                        newElement.setAttribute("type","RO7")
                        newElement.setAttribute("name","T{}".format(str(thermID)))
                        thermID = thermID + 1                       
                        newElement.setAttribute("col",str(col))
                        newElement.setAttribute("row",str(row))
                        root.appendChild(newElement)
		return xmlOutDocument

	def generateXmlHeader(self, xmlOutputDocument, ncdFile):
		root = xmlOutputDocument.createElement("board")
		root.setAttribute("device", "Virtex5")
		root.setAttribute("mode", "emulation")
		root.setAttribute("version", "0.1")
		xmlOutputDocument.appendChild(root)

		inputComponent = xmlOutputDocument.createElement("input")
		outputComponent = xmlOutputDocument.createElement("output")

		inputComponent.setAttribute("name", str(ncdFile))
		ncdName = str(ncdFile).rsplit(".")
		ncdName = ncdName[0]
		outputComponent.setAttribute("name", "{}_new.ncd".format(ncdName))

		root.appendChild(inputComponent)
		root.appendChild(outputComponent)

		return xmlOutputDocument


