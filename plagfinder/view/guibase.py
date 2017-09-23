# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/guibase.ui'
#
# Created: Tue Oct  6 18:41:27 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.central_widget = QtGui.QWidget(MainWindow)
        self.central_widget.setObjectName(_fromUtf8("central_widget"))
        self._2 = QtGui.QVBoxLayout(self.central_widget)
        self._2.setObjectName(_fromUtf8("_2"))
        self.horizontal_layout_up = QtGui.QHBoxLayout()
        self.horizontal_layout_up.setObjectName(_fromUtf8("horizontal_layout_up"))
        self._2.addLayout(self.horizontal_layout_up)
        self.horizontal_layout_down = QtGui.QHBoxLayout()
        self.horizontal_layout_down.setObjectName(_fromUtf8("horizontal_layout_down"))
        self.start_button = QtGui.QPushButton(self.central_widget)
        self.start_button.setEnabled(False)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontal_layout_down.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.central_widget)
        self.stop_button.setEnabled(False)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontal_layout_down.addWidget(self.stop_button)
        self.progress_bar = QtGui.QProgressBar(self.central_widget)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.horizontal_layout_down.addWidget(self.progress_bar)
        self._2.addLayout(self.horizontal_layout_down)
        self.progress_bar_all = QtGui.QProgressBar(self.central_widget)
        self.progress_bar_all.setEnabled(False)
        self.progress_bar_all.setProperty("value", 0)
        self.progress_bar_all.setObjectName(_fromUtf8("progress_bar_all"))
        self._2.addWidget(self.progress_bar_all)
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtGui.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_help = QtGui.QMenu(self.menu_bar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtGui.QStatusBar(MainWindow)
        self.status_bar.setEnabled(True)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        MainWindow.setStatusBar(self.status_bar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "plagfinder", None))
        self.start_button.setText(_translate("MainWindow", "Start", None))
        self.stop_button.setText(_translate("MainWindow", "Stop", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.action_exit.setText(_translate("MainWindow", "Exit", None))
        self.action_open.setText(_translate("MainWindow", "Open", None))
        self.action_about.setText(_translate("MainWindow", "About", None))

