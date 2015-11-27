# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_template.ui'
#
# Created: Fri Nov 27 10:50:07 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_template_2(object):
    def setupUi(self, template_2):
        template_2.setObjectName(_fromUtf8("template_2"))
        template_2.resize(800, 600)
        template_2.setModal(True)
        self.cancelBtn = QtGui.QPushButton(template_2)
        self.cancelBtn.setGeometry(QtCore.QRect(710, 560, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelBtn.setIcon(icon)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.saveBtn = QtGui.QPushButton(template_2)
        self.saveBtn.setGeometry(QtCore.QRect(630, 560, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon1)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.templateTxt = QtGui.QPlainTextEdit(template_2)
        self.templateTxt.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.templateTxt.setObjectName(_fromUtf8("templateTxt"))

        self.retranslateUi(template_2)
        QtCore.QMetaObject.connectSlotsByName(template_2)

    def retranslateUi(self, template_2):
        template_2.setWindowTitle(QtGui.QApplication.translate("template_2", "cReports - template", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("template_2", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("template_2", "Save", None, QtGui.QApplication.UnicodeUTF8))

