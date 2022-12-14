import sys
import Requests
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_Change_password import Ui_Change_password
import settings
import json
import keyring

class ChangePassword(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Change_password()
        self.ui.setupUi(self)

        self.setWindowTitle("Change password")

        self.ui.cancel_button.clicked.connect(self.cancel)
        self.ui.change_password_button.clicked.connect(self.change_password)

    def cancel(self):
        self.close()

    def change_password(self):
        url = settings.api_path + settings.change_password_path
        data = {
            'oldPassword': self.ui.field_old.text(),
            'newPassword': self.ui.field_new.text()
        }

        response = Requests.post(url, json=data, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
            self.accept()
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.error_label.setText(response_json['message'])