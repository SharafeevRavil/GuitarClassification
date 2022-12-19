from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, QIODevice, QFile, QByteArray
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWebEngineCore import QWebEngineSettings
from Ui.ui_ViewTab import Ui_ViewTab
import Requests
import settings
import os
import sys

class ViewTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_ViewTab()
        self.ui.setupUi(self)

    def open(self, url, tab_name, author_name):
        self.ui.label_tab_name.setText(tab_name)
        self.ui.label_author_name.setText(author_name)

        file_responce = Requests.get(url)
        with open(settings.tab_file, 'w+b') as file:
            file.write(file_responce.content)

        url = QUrl.fromLocalFile(os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '.\\tab.html')))
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.ui.webEngineView.load(url)