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
from ui_cReports import Ui_cReports
# create the dialog for zoom to point


class cReportsDialog(QtGui.QDialog, Ui_cReports):
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.ui = Ui_cReports()
		self.ui.setupUi(self)

	def setTextBrowser(self, output):
		self.ui.txtBrowser.append(output)

	def setDocumentBrowser(self, output):
		self.ui.txtBrowser.setDocument(output)

	def clearTextBrowser(self):
		self.ui.txtBrowser.clear()
