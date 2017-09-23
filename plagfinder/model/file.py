# -*- coding: utf-8 -*-

import codecs

from PyQt4 import QtGui

import view.gui

class LoadedFiles():
    def __init__(self, window, app):
        self.window = window
        self.about_windowpp = app
        self.loaded_files_list = []

    def choose_file(self):
        for file_name in QtGui.QFileDialog().getOpenFileNames():
            if not file_name in self.loaded_files_list:
                self.loaded_files_list.append(file_name)

        # Update files list
        self.window.file_choosen_sign.emit(self.loaded_files_list)

    def file_dropped(self, files_list):
        for file_name in files_list:
            if not file_name in self.loaded_files_list:
                self.loaded_files_list.append(file_name)

        # Update files list
        self.window.file_choosen_sign.emit(self.loaded_files_list)

class File():
    def __init__(self, file_name):
        self.file_name = file_name

    def read_utf8_file(self):
        with codecs.open(self.file_name, "r", "utf-8") as current_file:
            return current_file.read()

    def write_utf8_file(self, data, f):
        with codecs.open(f, "a", "utf-8") as current_file:
            current_file.write(data)
