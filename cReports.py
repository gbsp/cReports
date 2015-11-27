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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
import os.path
import datetime
import sip
import re
API_NAMES = ["QDate", "QDateTime", "QString", "QTextStream", "QTime", "QUrl", "QVariant"]
API_VERSION = 2
for name in API_NAMES:
	sip.setapi(name, API_VERSION)

# Import the code for the dialogs
from cReportsdialog import cReportsDialog
from cReportssetting import cReportsSetting
from cReportstemplate import cReportsTemplate
from cReportshelp import cReportsHelp

document = QTextDocument()
sLayer=""
selectAttr = []
sCoding=""
sName=""

class cReports:

	def __init__(self, iface):
		# Save reference to the QGIS interface
		self.iface = iface
		# initialize plugin directory
		self.plugin_dir = os.path.dirname(__file__)
		# initialize locale
		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'cReports_{}.qm'.format(locale))
		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)
			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)
		# refernce to map canvas
		self.canvas = self.iface.mapCanvas()
		# out click tool will emit a QgsPoint on every click
		self.clickTool = QgsMapToolEmitPoint(self.canvas)

	def initGui(self):
		self.readSetting()
		# Create action that will start plugin configuration
		self.action = QAction(
			QIcon(self.plugin_dir+"/icon.png"),sName, self.iface.mainWindow())
		self.actionSetting = QAction(
			QIcon(self.plugin_dir+"/setting.png"),"setting", self.iface.mainWindow())
		self.actionTemplate = QAction(
			QIcon(self.plugin_dir+"/template.png"),"template", self.iface.mainWindow())
		self.actionHelp = QAction(
			QIcon(self.plugin_dir+"/help.png"),"help", self.iface.mainWindow())
		# connect the action to the run method
		QObject.connect(self.action, SIGNAL("triggered()"), self.run)
		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(QCoreApplication.translate("cReports", "cReports"), self.action)
		self.iface.addPluginToMenu(QCoreApplication.translate("cReports", "cReports"), self.actionSetting)
		self.iface.addPluginToMenu(QCoreApplication.translate("cReports", "cReports"), self.actionTemplate)
		self.iface.addPluginToMenu(QCoreApplication.translate("cReports", "cReports"), self.actionHelp)
		self.actionSetting.triggered.connect(self.setting)
		self.actionTemplate.triggered.connect(self.template)
		self.actionHelp.triggered.connect(self.help)
		# connect our select function to the canvasClicked signal
		result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.selectFeature)

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu(u"&cReports", self.action)
		self.iface.removeToolBarIcon(self.action)

	def readSetting(self):
		file = open(self.plugin_dir+"/setting.ini", 'r')
		global sName
		sName=file.readline().strip()
		global sLayer
		sLayer=file.readline().strip()
		global sCoding
		sCoding=file.readline().strip()
		file.closed

	def readTemplate(self):
		file = open(self.plugin_dir+"/template.html", 'r')
		docTemp=""
		docTemp=file.read()
		file.closed
		return docTemp
	
	def readHelp(self):
		file = open(self.plugin_dir+"/help.html", 'r')
		docTemp=""
		docTemp=file.read()
		file.closed
		return docTemp

	def selectFeature(self, point, button):
		self.readSetting()
		# setup the provider select to filter results based on a rectangle
		pntGeom = QgsGeometry.fromPoint(point)  
		# get currentLayer and dataProvider
		cLayer = self.canvas.currentLayer()
		selectList = []
		global selectAttr
		del selectAttr[:]
		if cLayer:
			provider = cLayer.getFeatures()
			feat = QgsFeature()
			pntBuff = pntGeom.buffer( (self.canvas.mapUnitsPerPixel() * 2),0)
			rect = pntBuff.boundingBox()
			# create the select statement
			while provider.nextFeature(feat):
				# if the feat geom returned from the selection distance<1.5m our point then put it in a list
				if feat.geometry().intersects(rect):
					selectList.append(feat.id())
					for attr in feat.attributes():
						global selectAttr
						selectAttr.append(attr)
			#make the actual selection
			cLayer.setSelectedFeatures(selectList)
			if len(selectList)>0:
				if cLayer.name()==sLayer:
					self.createReport()
				else:
					QMessageBox.information( self.iface.mainWindow(),"Information", "The active layer is different than declared: "+sLayer )
			else:
				QMessageBox.information( self.iface.mainWindow(),"Information", "Nothing selected" )
		else:
			QMessageBox.information( self.iface.mainWindow(),"Information", "There is no active layer" )

	def createReport(self):
		file = open(self.plugin_dir+"/template.html", 'r')
		html=file.read()
		file.closed
		html=html.decode(sCoding)
		html=self.replaceVar(html)
		html=self.replaceAttr(html)
		html=self.replaceFile(html)
		html=self.replaceIf(html)
		# Create the dialog (after translation) and keep reference
		self.dlg = cReportsDialog()
		self.dlg.connect(self.dlg.ui.saveBtn, SIGNAL("clicked()"),self.pdf)
		self.dlg.connect(self.dlg.ui.printBtn, SIGNAL("clicked()"),self.printing)
		self.dlg.connect(self.dlg.ui.closeBtn, SIGNAL("clicked()"),self.close)
		self.dlg.show()
		self.updateTextBrowser(html)

	def replaceVar(self,html):
		for m in re.compile(ur'{!v:.*?!}',re.U).finditer(html):
			v=re.compile(m.group(0),re.U)
			w, ok=QInputDialog.getText(self.iface.mainWindow(), "Information",v.pattern[4:-2], QLineEdit.Normal)
			if(w):
				html=html.replace(v.pattern,w)
			else:
				html=html.replace(v.pattern,"")
		return html

	def replaceAttr(self,html):
		i=1
		for a in selectAttr:
			r="{!a:"+str(i)+"!}"
			if a and not isinstance(a,QPyNullVariant):
				if not isinstance(a, basestring):
					a=str(a)
				html=html.replace(r,a)
			else:
				html=html.replace(r,"")
			i+=1
		return html

	def replaceFile(self,html):
		for m in re.compile(ur'{!f:.*?!}',re.U).finditer(html):
			v=re.compile(m.group(0),re.U)
			file = open(self.plugin_dir+"/"+v.pattern[4:-2], 'r')
			r=file.read()
			file.closed
			r=r.decode(sCoding)
			html=html.replace(v.pattern,r)
		return html

	def replaceIf(self,html):
		f=0
		for m in re.compile(ur'{!\wf.*?!}',re.U|re.DOTALL).finditer(html):
			v=re.compile(m.group(0),re.U)
			vList=v.pattern.split('->')
			type=vList[0][2:4]
			if type=='if' or type=='ef':
				if ((not f and type=='ef') or (type=='if')):
					s=vList[0][3:-1].strip()
					sList=s.split('=')
					i=1
					for a in selectAttr:
						if(sList[0][4:].strip()==str(i)):
							af=sList[1].strip();
							if str(a)==af:
								html=html.replace(v.pattern,vList[1][:-2])
								f=1
							else:
								html=html.replace(v.pattern,"")
								f=0
						i+=1
				else:
					html=html.replace(v.pattern,"")
			else:
				if(not f):
					html=html.replace(v.pattern,vList[1][:-2])
				else:
					html=html.replace(v.pattern,"")
					f=0
		return html

	def updateTextBrowser(self,html):
		global document
		document.setHtml(html)
		self.dlg.setDocumentBrowser(document)

	def printing (self):
		printer=QPrinter()
		dialog = QPrintDialog(printer)
		dialog.setModal(True)
		dialog.setWindowTitle("Drukowanie")
		if dialog.exec_() == True:
			document.print_(printer)

	def pdf (self):
		fileName = QFileDialog.getSaveFileName(self.dlg, "Save file","report.pdf","(*.pdf)")
		printer=QPrinter()
		printer.setOutputFormat(QPrinter.PdfFormat)
		printer.setPageSize(QPrinter.A4)
		if fileName:
			printer.setOutputFileName(fileName)
			doc=document
			doc.print_(printer)
		
	def setting(self):
		self.dlg = cReportsSetting()
		self.dlg.connect(self.dlg.ui.saveBtn, SIGNAL("clicked()"),self.saveSetting)
		self.dlg.connect(self.dlg.ui.cancelBtn, SIGNAL("clicked()"),self.close)
		self.dlg.show()
		self.readSetting()
		self.dlg.setSetting(sName,sLayer,sCoding)
	
	def saveSetting(self):	
		file = open(self.plugin_dir+"/setting.ini", 'w')
		file.write(self.dlg.getName()+"\n")
		file.write(self.dlg.getLayer()+"\n")
		file.write(self.dlg.getEncoding())
		file.closed
		self.dlg.close()

	def template(self):
		self.dlg = cReportsTemplate()
		self.dlg.connect(self.dlg.ui.saveBtn, SIGNAL("clicked()"),self.saveTemplate)
		self.dlg.connect(self.dlg.ui.cancelBtn, SIGNAL("clicked()"),self.close)
		self.dlg.show()
		self.dlg.clearText()
		self.dlg.setText(self.readTemplate())

	def saveTemplate(self):	
		file = open(self.plugin_dir+"/template.html", 'w')
		file.write(self.dlg.getText())
		file.closed
		self.dlg.close()

	def help(self):
		self.dlg = cReportsHelp()
		self.dlg.connect(self.dlg.ui.closeBtn, SIGNAL("clicked()"),self.close)
		self.dlg.show()
		self.dlg.setTextBrowser(self.readHelp())

	def close (self):
		self.dlg.close()

	# run method that performs all the real work
	def run(self):
		# make our clickTool the tool that we'll use for now
		self.canvas.setMapTool(self.clickTool)


