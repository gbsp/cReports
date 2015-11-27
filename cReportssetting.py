# -*- coding: utf-8 -*-
"""
/***************************************************************************
		Name                 : cReports
		Description          : Customised cReports
        copyright            : (C) 2015 by Geobaza (radzio)
        email                : qgis@geobaza.com.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_setting import Ui_setting

class cReportsSetting(QtGui.QDialog, Ui_setting):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_setting()
		self.ui.setupUi(self)
		
	def setSetting(self, name, layer, encoding):
		self.ui.nameTxt.setText(name)
		self.ui.layerTxt.setText(layer)
		self.ui.encodingTxt.setText(encoding)
	
	def getName(self):
		return self.ui.nameTxt.text()

	def getLayer(self):
		return self.ui.layerTxt.text()

	def getEncoding(self):
		return self.ui.encodingTxt.text()
		