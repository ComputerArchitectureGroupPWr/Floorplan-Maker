# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString, Qt

__author__ = 'pawel'

class Param:
    #Enumeracja nazw unitów:
    free = 0
    obstacle = -1
    unit = -2
    heater_top = 29
    thermometer_top = 158

    colors2 = ["niebieski","czerwony","zielony","cyjan","magenta","zolty","szary","ciemny niebieski",
               "ciemny czerwony","ciemny zielony","ciemny cyjan","ciemna magenta","ciemny zolty","ciemny szary"]

    colors_names = [QString("niebieski"),QString("czerwony"),QString("zielony"),QString("cyjan"),QString("magenta"),
                    QString("zolty"),QString("ciemny niebieski"),QString("ciemny czerwony"),QString("ciemny cyjan"),
                    QString("ciemna magenta"),QString("ciemny zielony"),QString("ciemny szary"),QString("ciemny zolty")]

    colors = {"niebieski": Qt.blue, "ciemny niebieski": Qt.darkBlue,
              "czerwony": Qt.red, "ciemny czerwony": Qt.darkRed,
              "zielony": Qt.green, "ciemny zielony": Qt.darkGreen,
              "cyjan": Qt.cyan, "ciemny cyjan": Qt.darkCyan,
              "magenta": Qt.magenta, "ciemna magenta": Qt.darkMagenta,
              "szary": Qt.gray, "ciemny szary": Qt.darkGray,
              "zolty": Qt.yellow, "ciemny zolty": Qt.darkYellow}

    colorsQt = {QString("niebieski"):Qt.blue, QString("ciemny niebieski"): Qt.darkBlue,
              QString("czerwony"):Qt.red, QString("ciemny czerwony"): Qt.darkRed,
              QString("zielony"):Qt.green, QString("ciemny zielony"): Qt.darkGreen,
              QString("cyjan"): Qt.cyan, QString("ciemny cyjan"): Qt.darkCyan,
              QString("magenta"): Qt.magenta, QString("ciemna magenta"): Qt.darkMagenta,
              QString("szary"): Qt.gray, QString("ciemny szary"): Qt.darkGray,
              QString("zolty"): Qt.yellow, QString("ciemny zolty"): Qt.darkYellow}