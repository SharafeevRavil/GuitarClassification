from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_FromFile import Ui_FromFile
from ChangePassword import ChangePassword
import os

class FromFile(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_FromFile()
        self.ui.setupUi(self)

        self.ui.button_select.clicked.connect(self.select_file)
        #self.ui.button_generate.clicked.connect(self.generate) is in MainWindow.py
        self.ui.button_return.clicked.connect(self.return_button)

    def select_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Audio files (*.mp3 *.wav)")
        self.filename = fname[0]
        self.ui.audio_name.setText(os.path.basename(self.filename))
        self.ui.button_generate.setEnabled(True)

    def clear(self):
        self.ui.audio_name.setText('')
        self.ui.button_select.setEnabled(True)
        self.ui.button_generate.setEnabled(False)

    def return_button(self):
        self.main_window.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)
        