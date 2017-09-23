# -*- coding: utf-8 -*-

import sys
import os

import nltk
from PyQt4 import QtGui

import view.gui

def init():
    # Set the root path
    os.chdir(os.path.dirname(sys.argv[0]))

    # Set nltk path
    nltk.data.path.append(
        os.path.join(
            os.getcwd(),
            'res',
            'nltk_data'
        )
    )

def main():
    app = QtGui.QApplication(sys.argv)

    view.gui.Ui_MainWindow(app)

    sys.exit(app.exec_())

if __name__ == '__main__':
    init()
    main()
