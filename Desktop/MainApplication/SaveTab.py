from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, QIODevice, QFile
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWebEngineCore import QWebEngineSettings
from Ui.ui_SaveTab import Ui_SaveTab
import GPCreator
import Requests
import settings
import os
import sys
import magic
import FileHelper as fh

class SaveTab(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_SaveTab()
        self.ui.setupUi(self)

        self.ui.button_save_file.clicked.connect(self.save_file)
        self.ui.button_upload.clicked.connect(self.upload)
        self.ui.button_return.clicked.connect(self.return_button)
        self.ui.button_upload.setDisabled(True)
        self.ui.field_tab_name.textChanged.connect(self.disable_upload)

    def generate(self, filename, isAuthed):
        self.ui.button_save_file.setDisabled(False)
        self.ui.button_upload.setDisabled(True)
        self.ui.field_tab_name.setDisabled(not isAuthed)

        GPCreator.create(filename)
        url = QUrl.fromLocalFile(fh.getPathInRoot('.\\tab.html'))
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.ui.webEngineView.load(url)

    def save_file(self):
        tab_file = QFile(settings.tab_file)
        if tab_file.open(QIODevice.ReadOnly):
            QFileDialog.saveFileContent(tab_file.readAll(), 'tabs.gp5')
            tab_file.close()

    def upload(self):
        content_type = magic.Magic(mime=True).from_file(fh.getPathInRoot(settings.tab_file))

        data = {'Name': self.ui.field_tab_name.text()}

        files = {'File': (self.ui.field_tab_name.text() + '.gp5', open(fh.getPathInRoot(settings.tab_file), 'rb'), content_type)}

        response = Requests.post(settings.api_path + settings.tab_path, files=files, data=data, needAuth=True)
        if response.status_code == 200:
            pass
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])

    def disable_upload(self):
        if len(self.ui.field_tab_name.text()) > 0:
            self.ui.button_upload.setDisabled(False)
        else:
            self.ui.button_upload.setDisabled(True)

    def clear(self):
        self.ui.field_tab_name.setText('')
        self.ui.label_error.setText('')

    def return_button(self):
        self.main_window.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)