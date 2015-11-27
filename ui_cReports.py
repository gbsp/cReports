# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_cReports.ui'
#
# Created: Mon Feb 10 12:31:18 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os.path

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_cReports(object):
    def setupUi(self, cReports):
        cReports.setObjectName(_fromUtf8("cReports"))
        cReports.resize(800, 600)
        cReports.setModal(True)
        self.txtBrowser = QtGui.QTextBrowser(cReports)
        self.txtBrowser.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.txtBrowser.setAutoFillBackground(True)
        self.txtBrowser.setObjectName(_fromUtf8("txtBrowser"))
        self.printBtn = QtGui.QPushButton(cReports)
        self.printBtn.setGeometry(QtCore.QRect(600, 570, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printBtn.setIcon(icon)
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.closeBtn = QtGui.QPushButton(cReports)
        self.closeBtn.setGeometry(QtCore.QRect(700, 570, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.saveBtn = QtGui.QPushButton(cReports)
        self.saveBtn.setGeometry(QtCore.QRect(520, 570, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon2)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))

        self.retranslateUi(cReports)
        QtCore.QMetaObject.connectSlotsByName(cReports)

    def retranslateUi(self, cReports):
        cReports.setWindowTitle(QtGui.QApplication.translate("cReports", "cReports", None, QtGui.QApplication.UnicodeUTF8))
        self.printBtn.setText(QtGui.QApplication.translate("cReports", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.closeBtn.setText(QtGui.QApplication.translate("cReports", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("cReports", "Save", None, QtGui.QApplication.UnicodeUTF8))

