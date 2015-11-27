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
from ui_template import Ui_template_2
# create the dialog for zoom to point


class cReportsTemplate(QtGui.QDialog, Ui_template_2):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_template_2()
		self.ui.setupUi(self)

	def setText(self, output):
		self.ui.templateTxt.appendPlainText(output)
		
	def getText(self):
		return self.ui.templateTxt.toPlainText()

	def clearText(self):
		self.ui.templateTxt.clear()
