import sys
import Requests
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_Login import Ui_LogIn
import settings
import json
import keyring

class Login(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_LogIn()
        self.ui.setupUi(self)

        self.setWindowTitle("Login")

        self.ui.login_cancel_button.clicked.connect(self.cancel)
        self.ui.login_button.clicked.connect(self.login)

    def cancel(self):
        self.close()

    def login(self):
        url = settings.api_path + settings.signin_path
        data = {
            'username': self.ui.login_field.text(),
            'password': self.ui.passworld_field.text()
        }

        response = Requests.post(url, json=data)
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCogModerator', 'token', response_json['token'])
            keyring.set_password('GuitarCogModerator', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCogModerator', 'expiration', response_json['expiration'])
            self.accept()
        elif response.status_code == 401:
            self.ui.error_label.setText('Wrong username of password')
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.error_label.setText(response_json['message'])