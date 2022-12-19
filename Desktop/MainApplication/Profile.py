from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_Profile import Ui_Profile
from ChangePassword import ChangePassword
from Subscribe import Subscribe
from datetime import datetime
import settings
import Requests
import keyring
import magic
import os
import time
from dateutil import parser

class Profile(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.ui = Ui_Profile()
        self.ui.setupUi(self)
        self.main_window = main_window

        self.ui.button_change_login.clicked.connect(self.change_nickname)
        self.ui.button_change_email.clicked.connect(self.change_email)
        self.ui.button_change_password.clicked.connect(self.change_password)
        self.ui.button_change_avatar.clicked.connect(self.change_avatar)
        self.ui.button_subscribe.clicked.connect(self.open_subscribe)

    def load_profile(self):
        response = Requests.get(settings.api_path + settings.user_info_path, needAuth=True)            
        if response.status_code == 200:
            response_json = response.json()
            self.username = response_json['username']
            self.email = response_json['email']

            self.ui.field_login.setText(self.username)
            self.ui.field_email.setText(self.email)

            self.load_subscription_status()
            self.load_avatar(response_json['imageUrl'])

    def change_nickname(self):
        data = {'newUsername': self.ui.field_login.text()}
        response = Requests.post(settings.api_path + settings.change_nickname_path, json=data, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])
        self.load_profile()

    def change_email(self):
        data = {'newEmail': self.ui.field_email.text()}
        response = Requests.post(settings.api_path + settings.change_email_path, json=data, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            keyring.set_password('GuitarCog', 'token', response_json['token'])
            keyring.set_password('GuitarCog', 'refreshToken', response_json['refreshToken'])
            keyring.set_password('GuitarCog', 'expiration', response_json['expiration'])
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])
        self.load_profile()

    def change_password(self):
        dlg = ChangePassword()
        if dlg.exec():
            self.load_profile()

    def change_avatar(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.png)")
        imagepath = fname[0]
        pix = QPixmap(imagepath)
        content_type = magic.Magic(mime=True).from_file(imagepath)

        files = {'image': (os.path.basename(imagepath), open(imagepath, 'rb'), content_type)}

        if pix.width() >= pix.height() * 2:
            self.ui.label_error.setText('Image too wide')
        else:
            response = Requests.post(settings.api_path + settings.change_avatar_path, files=files, needAuth=True)
            if response.status_code == 200:
                response_json = response.json()
                self.load_avatar(response_json['avatarUrl'])
            elif response.headers.get('content-type') == 'application/json':
                response_json = response.json()
                if 'status' in response_json and response_json['status'] == 'Error':
                    self.ui.label_error.setText(response_json['message'])

    def load_avatar(self, url):
        self.image = QPixmap()
        if(url == None or url == ''):
            self.image.load('./Ui/no-image-icon.png')
        else:
            image_response = Requests.get(url)
            if image_response.status_code == 200:   
                self.image.loadFromData(image_response.content)
            else:
                self.image.load('./Ui/no-image-icon.png')
        image_width = self.ui.label_image.height() * self.image.width() / self.image.height()
        self.ui.label_image.setPixmap(self.image.scaled(image_width, self.ui.label_image.height(), aspectMode=Qt.KeepAspectRatio))
        self.ui.label_image.setFixedWidth(image_width)

    def open_subscribe(self):
        dlg = Subscribe(self.ui.field_login.text())
        if dlg.exec():
            self.load_subscription_status()
            self.main_window.load_ads()

    def load_subscription_status(self):
        response = Requests.get(settings.api_path + settings.subscription_status_path, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            if response_json['isSubscribed']:
                self.ui.label_subscription.setText('Subscribed')
                self.ui.label_subscribed_until.setText('until ' + parser.parse(response_json['end']).strftime("%m/%d/%Y, %H:%M:%S"))
                self.ui.button_subscribe.setVisible(False)
            else:
                self.ui.label_subscription.setText('No subscription')
                self.ui.label_subscribed_until.setText('')
                self.ui.button_subscribe.setVisible(True)
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])

