from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWebEngineCore import QWebEngineSettings
from Ui.ui_ViewTab import Ui_ViewTab

class ViewTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_ViewTab()
        self.ui.setupUi(self)

        self.ui.button_save_file.clicked.connect(self.save_file)
        self.ui.button_upload.clicked.connect(self.upload)

    def save_file(self):
        pass

    def upload(self):
        pass