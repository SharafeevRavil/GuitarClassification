from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from ui_Profile import Ui_Profile
from ChangePassword import ChangePassword
import settings
import requests
import keyring

class Profile(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Profile()
        self.ui.setupUi(self)

        self.ui.button_change_login.clicked.connect(self.change_nickname)
        self.ui.button_change_email.clicked.connect(self.change_email)
        self.ui.button_change_password.clicked.connect(self.change_password)

    def load_profile(self):
        pass

    def change_nickname(self):
        data = {'newUsername': self.ui.field_login.text()}
        response = requests.post(settings.api_path + settings.change_nickname_path, json=data, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
        self.load_profile()

    def change_email(self):
        data = {'newEmail': self.ui.field_email.text()}
        response = requests.post(settings.api_path + settings.change_email_path, json=data, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
        self.load_profile()

    def change_password(self):
        dlg = ChangePassword()
        if dlg.exec():
            self.load_profile()