# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_setting.ui'
#
# Created: Fri Nov 27 09:26:16 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName(_fromUtf8("setting"))
        setting.resize(492, 166)
        setting.setModal(True)
        self.cancelBtn = QtGui.QPushButton(setting)
        self.cancelBtn.setGeometry(QtCore.QRect(370, 130, 75, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelBtn.setIcon(icon)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.saveBtn = QtGui.QPushButton(setting)
        self.saveBtn.setGeometry(QtCore.QRect(290, 130, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveBtn.setIcon(icon1)
        self.saveBtn.setObjectName(_fromUtf8("saveBtn"))
        self.nameTxt = QtGui.QLineEdit(setting)
        self.nameTxt.setGeometry(QtCore.QRect(220, 30, 221, 20))
        self.nameTxt.setObjectName(_fromUtf8("nameTxt"))
        self.layerTxt = QtGui.QLineEdit(setting)
        self.layerTxt.setGeometry(QtCore.QRect(220, 60, 221, 20))
        self.layerTxt.setObjectName(_fromUtf8("layerTxt"))
        self.encodingTxt = QtGui.QLineEdit(setting)
        self.encodingTxt.setGeometry(QtCore.QRect(220, 90, 221, 20))
        self.encodingTxt.setObjectName(_fromUtf8("encodingTxt"))
        self.label = QtGui.QLabel(setting)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(setting)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 181, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(setting)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(setting)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        setting.setWindowTitle(QtGui.QApplication.translate("setting", "cReports - setting", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("setting", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBtn.setText(QtGui.QApplication.translate("setting", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("setting", "plugin name displayed in QGIS:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("setting", "layer name on which the plugin runs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("setting", "character encoding:", None, QtGui.QApplication.UnicodeUTF8))

