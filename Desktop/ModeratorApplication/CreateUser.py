import sys
import Requests
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_CreateUser import Ui_CreateUser
import settings
import json
import keyring

class CreateUser(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_CreateUser()
        self.ui.setupUi(self)

        self.setWindowTitle("Create User")

        self.ui.cancel_button.clicked.connect(self.cancel)
        self.ui.create_button.clicked.connect(self.create)

    def cancel(self):
        self.close()

    def create(self):
        url = settings.api_path + settings.moder_user_path
        data = {
            'email': self.ui.email_field.text(),
            'username': self.ui.login_field.text(),
            'password': self.ui.passworld_field.text()
        }

        response = Requests.post(url, json=data, needAuth=True)
        if response.status_code == 200:
            self.accept()
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.error_label.setText(response_json['message'])