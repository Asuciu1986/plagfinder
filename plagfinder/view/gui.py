# -*- coding: utf-8 -*-

import os

from PyQt4 import QtCore, QtGui

import model.file
import view.guibase
import core.router
import core.proc

class AboutWindow(QtGui.QWidget):
    def show_about(self):
        QtGui.QMainWindow.__init__(self)

        about_msg = "Plagiarism detection software."

        QtGui.QMessageBox.about(self, 'About', about_msg)

class FilesListWidget(QtGui.QListWidget):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)

        self.setAcceptDrops(True)

        # Enable multiple files selection
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))

            self.list_widget_updated_sign.emit(links)
        else:
            event.ignore()

class Ui_MainWindow(QtGui.QMainWindow, view.guibase.Ui_MainWindow):
    # Signals
    start_proc_sign = QtCore.pyqtSignal()
    end_proc_sign = QtCore.pyqtSignal()
    update_status_sign = QtCore.pyqtSignal(str)
    write_colored_sign = QtCore.pyqtSignal(str, str)
    update_progress_sign = QtCore.pyqtSignal(int)
    update_progress_all_sign = QtCore.pyqtSignal(int)
    file_choosen_sign = QtCore.pyqtSignal(list)
    update_files_list_sign = QtCore.pyqtSignal(list)
    list_widget_updated_sign = QtCore.pyqtSignal(list)

    def __init__(self, app):
        QtGui.QMainWindow.__init__(self)

        self.app = app

        self.setup_cust()

        self.listen()

        self.show()

    def setup_cust(self):
        # Load generated UI
        self.setupUi(self)

        # Create new text browser instance
        self.text_browser = QtGui.QTextBrowser(self.central_widget)
        self.text_browser.setEnabled(False) # Nothing to highlight
        self.text_browser.setObjectName("text_browser")

        # Create new files list widget
        self.list_widget = FilesListWidget()
        self.list_widget.setEnabled(True) # For drag and drops
        self.list_widget.setObjectName("list_widget")

        # Create new horizontal splitter
        self.splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)

        # Add text browser and files list widget to the splitter
        self.splitter.addWidget(self.text_browser)
        self.splitter.addWidget(self.list_widget)

        # Add the splitter to horizontal_layout_up
        self.horizontal_layout_up.addWidget(self.splitter)

    def listen(self):
        self.about_window = AboutWindow()

        self.loaded_files = model.file.LoadedFiles(self, self.app)

        self.process = core.proc.MainProcess(self, self.loaded_files)

        # Connect signals and slots
        self.action_exit.triggered.connect(exit)
        self.action_about.triggered.connect(self.about_window.show_about)
        self.action_open.triggered.connect(self.loaded_files.choose_file)
        self.start_button.clicked.connect(self.process.start)
        self.stop_button.clicked.connect(self.stop_proc)
        self.start_proc_sign.connect(self.start_proc)
        self.end_proc_sign.connect(self.end_proc)
        self.update_status_sign.connect(self.update_status)
        self.write_colored_sign.connect(self.write_colored)
        self.update_progress_sign.connect(self.update_progress)
        self.update_progress_all_sign.connect(self.update_all_progress)
        self.file_choosen_sign.connect(self.file_choosen)
        self.update_files_list_sign.connect(self.update_files_list)
        self.list_widget_updated_sign.connect(self.loaded_files.file_dropped)

    def stop_proc(self):
        # End main process
        self.process.terminate()

        # GUI changes
        self.end_proc()

    def start_proc(self):
        # Clear text browser for new output
        self.text_browser.clear()

        # Disable text_browser while process is running
        self.text_browser.setEnabled(False)

        # Disable start button while process is already running
        self.start_button.setEnabled(False)

        # Disable file menu open button while process is running
        self.action_open.setEnabled(False)

        # Enable stop button
        self.stop_button.setEnabled(True)

        # Disable drag and drop in files list widget
        self.list_widget.setEnabled(False)

    def end_proc(self):
        # Enable text browser for copy/paste
        self.text_browser.setEnabled(True)

        # Enable start button for starting a new process
        self.start_button.setEnabled(True)

        # Enable file menu open button for opening new files
        self.action_open.setEnabled(True)

        # Process is not running so disable stop_button
        self.stop_button.setEnabled(False)

        # Enable files list widget for drag and drops
        self.list_widget.setEnabled(True)

        # Reset progress bars to zero
        self.update_progress(0)
        self.update_all_progress(0)

    def write_colored(self, text, color):
        # Set text color
        self.text_browser.setTextColor(QtGui.QColor(color))

        # Append text
        self.text_browser.append(text)

    def update_status(self, text):
        self.status_bar.showMessage(text)

    def update_progress(self, done):
        self.progress_bar.setValue(done)

    def update_all_progress(self, done):
        self.progress_bar_all.setValue(done)

    def update_files_list(self, files_list):
        # Clear old files
        self.list_widget.clear()

        # Read files_list variable
        for file_name in files_list:
            self.list_widget.addItem(os.path.basename(file_name))

    def file_choosen(self, files_list):
        # Enable start button
        self.start_button.setEnabled(True)

        # Request updating files list widget
        self.update_files_list_sign.emit(files_list)
