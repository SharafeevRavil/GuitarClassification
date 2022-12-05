import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from datetime import datetime
from Ui.ui_GuitarCog import Ui_MainWindow
from Register import Register
from Login import Login
from Profile import Profile
import settings
import keyring
import Requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.username = ''

        self.check_authorized()

        self.setWindowTitle("GuitarCog")
        
        self.ui.action_register.triggered.connect(self.open_register)
        self.ui.action_login.triggered.connect(self.open_login)
        self.ui.action_logout.triggered.connect(self.logout)
        self.ui.action_open_profile.triggered.connect(self.open_profile)

        self.profile = Profile()
        self.ui.stackedWidget.addWidget(self.profile)

    def check_authorized(self):
        isAuthed = False
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if datetime.strptime(keyring.get_password('GuitarCog', 'expiration'), '%Y-%m-%dT%H:%M:%SZ') <= datetime.utcnow():
                Requests.refresh_token()
            response = Requests.get(settings.api_path + settings.checkauth_path, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})            

            if response.status_code == 200:
                isAuthed = True
                response_json = response.json()
                self.username = response_json['username']

        if not isAuthed:
            self.username = ''            

        self.ui.action_login.setVisible(not isAuthed)
        self.ui.action_register.setVisible(not isAuthed)
        
        self.ui.action_open_profile.setVisible(isAuthed)
        self.ui.action_logout.setVisible(isAuthed)
        self.ui.action_view_global.setVisible(isAuthed)
        self.ui.action_view_owned.setVisible(isAuthed)

        if self.username == '':
            self.ui.label_welcome.setText('Welcome!')
        else:
            self.ui.label_welcome.setText(f'Welcome, {self.username}!')

    def open_register(self):
        dlg = Register()
        if dlg.exec():
            self.check_authorized()

    def open_login(self):
        dlg = Login()
        if dlg.exec():
            self.check_authorized()

    def logout(self):
        keyring.delete_password('GuitarCog', 'token')
        keyring.delete_password('GuitarCog', 'refreshToken')
        keyring.delete_password('GuitarCog', 'expiration')
        self.check_authorized()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)

    def open_profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.profile)
        self.profile.load_profile()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())