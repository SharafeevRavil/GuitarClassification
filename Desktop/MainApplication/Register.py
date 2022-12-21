import sys
import Requests
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_Register import Ui_Register
import settings
import json
import keyring

class Register(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Register()
        self.ui.setupUi(self)

        self.setWindowTitle("Register")

        self.ui.register_cancel_button.clicked.connect(self.cancel)
        self.ui.register_button.clicked.connect(self.register)

    def cancel(self):
        self.close()

    def register(self):
        url = settings.api_path + settings.signup_path
        data = {
            'email': self.ui.email_field.text(),
            'username': self.ui.login_field.text(),
            'password': self.ui.passworld_field.text()
        }

        response = Requests.post(url, json=data)
        response_json = response.json()
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
            self.accept()
        elif 'application/json' in response.headers.get('content-type'):
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.error_label.setText(response_json['message'])