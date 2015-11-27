# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_help.ui'
#
# Created: Fri Nov 27 11:29:02 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_help(object):
    def setupUi(self, help):
        help.setObjectName(_fromUtf8("help"))
        help.resize(800, 600)
        help.setModal(True)
        self.helpTxt = QtGui.QTextBrowser(help)
        self.helpTxt.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.helpTxt.setAutoFillBackground(True)
        self.helpTxt.setObjectName(_fromUtf8("helpTxt"))
        self.closeBtn = QtGui.QPushButton(help)
        self.closeBtn.setGeometry(QtCore.QRect(700, 570, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon)
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))

        self.retranslateUi(help)
        QtCore.QMetaObject.connectSlotsByName(help)

    def retranslateUi(self, help):
        help.setWindowTitle(QtGui.QApplication.translate("help", "cReports - help", None, QtGui.QApplication.UnicodeUTF8))
        self.closeBtn.setText(QtGui.QApplication.translate("help", "Close", None, QtGui.QApplication.UnicodeUTF8))

