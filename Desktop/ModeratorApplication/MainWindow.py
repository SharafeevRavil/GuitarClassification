import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_GuitarCog_Moderator import Ui_GuitarCogModerator
from Profile import Profile
from List import List
from Login import Login
from UserProfile import UserProfile
from ViewTab import ViewTab
from CreateUser import CreateUser
import keyring
import Requests
from dateutil import parser
import jwt
import settings
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_GuitarCogModerator()
        self.ui.setupUi(self)

        self.setWindowTitle("GuitarCog Moderator")

        self.ui.action_users_all.triggered.connect(self.open_users_all)
        self.ui.action_users_banned.triggered.connect(self.open_users_banned)
        self.ui.action_reports_all.triggered.connect(self.open_reports_all)
        self.ui.action_reports_new.triggered.connect(self.open_reports_new)
        self.ui.action_view_all.triggered.connect(self.open_tabs_all)
        self.ui.actionLogin.triggered.connect(self.open_login)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.actionOpen.triggered.connect(self.open_profile)
        self.ui.actionCreate.triggered.connect(self.create_user)

        self.check_authorized()

        self.profile = Profile()
        self.ui.stackedWidget.addWidget(self.profile)
        self.list = List(self)
        self.ui.stackedWidget.addWidget(self.list)
        self.user_profile = UserProfile(self)
        self.ui.stackedWidget.addWidget(self.user_profile)
        self.view_tab = ViewTab()
        self.ui.stackedWidget.addWidget(self.view_tab)

    def check_authorized(self):
        self.isAuthed = False
        if keyring.get_password('GuitarCogModerator', 'token') != None and keyring.get_password('GuitarCogModerator', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCogModerator', 'expiration'), ignoretz=True) <= datetime.utcnow():
                Requests.refresh_token()
            response = Requests.get(settings.api_path + settings.checkauth_path, needAuth=True)            

            if response.status_code == 200:
                response_json = response.json()
                self.username = response_json['username']
                decoded = jwt.decode(keyring.get_password('GuitarCogModerator', 'token'), options={"verify_signature": False})
                self.user_id = decoded['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier']
                if 'http://schemas.microsoft.com/ws/2008/06/identity/claims/role' in decoded:
                    self.isAuthed = True
                    if not isinstance(decoded['http://schemas.microsoft.com/ws/2008/06/identity/claims/role'], list):
                        decoded['http://schemas.microsoft.com/ws/2008/06/identity/claims/role'] = [decoded['http://schemas.microsoft.com/ws/2008/06/identity/claims/role']]
                    if 'SuperAdmin' in decoded['http://schemas.microsoft.com/ws/2008/06/identity/claims/role']:
                        self.ui.action_users_all.setVisible(True)
                        self.ui.action_users_banned.setVisible(True)
                        self.ui.action_view_all.setVisible(True)
                        self.ui.action_view_reported.setVisible(True)
                        self.ui.actionCreate.setVisible(True)
                    elif 'Moderator' in decoded['http://schemas.microsoft.com/ws/2008/06/identity/claims/role']:
                        self.ui.action_users_all.setVisible(True)
                        self.ui.action_users_banned.setVisible(True)
                        self.ui.action_view_all.setVisible(True)
                        self.ui.action_view_reported.setVisible(True)
                        self.ui.actionCreate.setVisible(False)
                else:
                    self.ui.action_users_all.setVisible(False)
                    self.ui.action_users_banned.setVisible(False)
                    self.ui.action_view_all.setVisible(False)
                    self.ui.action_view_reported.setVisible(False)
                    self.ui.actionCreate.setVisible(False)
                    self.logout()

        if not self.isAuthed:
            self.username = ''
            self.user_id = ''           

        self.ui.actionLogin.setVisible(not self.isAuthed)
        
        self.ui.actionLogout.setVisible(self.isAuthed)
        self.ui.actionOpen.setVisible(self.isAuthed)

    def open_users_all(self):
        self.list.load_users_all()
        self.ui.stackedWidget.setCurrentWidget(self.list)

    def open_users_banned(self):
        self.list.load_users_banned()
        self.ui.stackedWidget.setCurrentWidget(self.list)

    def open_tabs_all(self):
        self.list.load_tabs_all()
        self.ui.stackedWidget.setCurrentWidget(self.list)

    def open_reports_all(self):
        self.list.load_reports_all()
        self.ui.stackedWidget.setCurrentWidget(self.list)

    def open_reports_new(self):
        self.list.load_reports_new()
        self.ui.stackedWidget.setCurrentWidget(self.list)

    def open_login(self):
        dlg = Login()
        if dlg.exec():
            self.check_authorized()

    def logout(self):
        keyring.delete_password('GuitarCogModerator', 'token')
        keyring.delete_password('GuitarCogModerator', 'refreshToken')
        keyring.delete_password('GuitarCogModerator', 'expiration')
        self.check_authorized()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_welcome)

    def open_profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.profile)
        self.profile.load_profile()

    def create_user(self):
        dlg = CreateUser()
        dlg.exec()
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())