import sys
import os
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QUrl, QFile
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings  
from datetime import datetime
from Ui.ui_GuitarCog import Ui_MainWindow
from Register import Register
from Login import Login
from Profile import Profile
from FromFile import FromFile
from SaveTab import SaveTab
from TabList import TabList
from ViewTab import ViewTab
from SettingsDialog import SettingsDialog
from FromRealTime import FromRealTime
import settings
import keyring
import Requests
from dateutil import parser
import jwt
import GPCreator
from PySide6.QtCore import Qt, QUrl, QRunnable, Slot, QThreadPool, QTimer, QObject, Signal

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
        self.ui.action_new_from_file.triggered.connect(self.open_from_file)
        self.ui.action_view_global.triggered.connect(self.view_global)
        self.ui.action_view_owned.triggered.connect(self.view_owned)
        self.ui.action_settings.triggered.connect(self.open_settings)
        self.ui.action_new_from_realtime.triggered.connect(self.open_from_real_time)

        self.profile = Profile()
        self.ui.stackedWidget.addWidget(self.profile)
        self.from_file = FromFile(self)
        self.ui.stackedWidget.addWidget(self.from_file)
        self.save_tab = SaveTab(self)
        self.ui.stackedWidget.addWidget(self.save_tab)
        self.tab_list = TabList(self)
        self.ui.stackedWidget.addWidget(self.tab_list)
        self.view_tab = ViewTab()
        self.ui.stackedWidget.addWidget(self.view_tab)
        self.from_real_time = FromRealTime(self)
        self.ui.stackedWidget.addWidget(self.from_real_time)

        self.from_file.ui.button_generate.clicked.connect(lambda: self.generate_gp(self.from_file.filename))
        self.from_real_time.ui.button_submit.clicked.connect(self.generate_gp)
        self.view_tab.ui.button_return.clicked.connect(self.return_to_list)

        GPCreator.create(settings.preload_file)

    def check_authorized(self):
        self.isAuthed = False
        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            if parser.parse(keyring.get_password('GuitarCog', 'expiration'), ignoretz=True) <= datetime.utcnow():
                Requests.refresh_token()
            response = Requests.get(settings.api_path + settings.checkauth_path, needAuth=True)            

            if response.status_code == 200:
                self.isAuthed = True
                response_json = response.json()
                self.username = response_json['username']
                decoded = jwt.decode(keyring.get_password('GuitarCog', 'token'), options={"verify_signature": False})
                self.user_id = decoded['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier']


        if not self.isAuthed:
            self.username = ''
            self.user_id = ''           

        self.ui.action_login.setVisible(not self.isAuthed)
        self.ui.action_register.setVisible(not self.isAuthed)
        
        self.ui.action_open_profile.setVisible(self.isAuthed)
        self.ui.action_logout.setVisible(self.isAuthed)
        self.ui.action_view_owned.setVisible(self.isAuthed)

        if self.username == '':
            self.ui.label_welcome.setText('Welcome!')
        else:
            self.ui.label_welcome.setText(f'Welcome, {self.username}!')
        
        self.load_ads()
        self.adTimer = QTimer()
        self.adTimer.setInterval(60 * 1000)
        self.adTimer.timeout.connect(self.load_ads)
        self.adTimer.start()
  
    def generate_gp(self, filename = None):
        self.check_authorized()
        self.save_tab.clear()
        self.save_tab.generate(filename, self.isAuthed)
        self.ui.stackedWidget.setCurrentWidget(self.save_tab)

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

    def open_settings(self):
        dlg = SettingsDialog()
        dlg.exec()

    def open_profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.profile)
        self.profile.load_profile()

    def open_from_file(self):
        self.from_file.clear()
        self.ui.stackedWidget.setCurrentWidget(self.from_file)

    def open_from_real_time(self):
        self.from_real_time.clear()
        self.ui.stackedWidget.setCurrentWidget(self.from_real_time)

    def view_global(self):
        self.tab_list.load_global()
        self.ui.stackedWidget.setCurrentWidget(self.tab_list)

    def view_owned(self):
        self.check_authorized()
        if self.isAuthed:
            self.tab_list.load_user(self.user_id)
            self.ui.stackedWidget.setCurrentWidget(self.tab_list)

    def return_to_list(self):
        self.ui.stackedWidget.setCurrentWidget(self.tab_list)

    def load_ads(self):
        response = Requests.get(settings.api_path + settings.ads_path, params={'count': 3}, needAuth=self.isAuthed)
        if response.status_code == 200:
            response_json = response.json()
            if response_json['needToShowAds']:
                self.ui.ad1.setVisible(True)
                self.ui.ad1.setFixedHeight(response_json['ads'][0]['height'])
                self.ui.ad1.setFixedWidth(response_json['ads'][0]['width'])
                self.ui.ad1.setUrl(response_json['ads'][0]['url'])
                self.ui.ad2.setVisible(True)
                self.ui.ad2.setFixedHeight(response_json['ads'][1]['height'])
                self.ui.ad2.setFixedWidth(response_json['ads'][1]['width'])
                self.ui.ad2.setUrl(response_json['ads'][1]['url'])
                self.ui.ad3.setVisible(True)
                self.ui.ad3.setFixedHeight(response_json['ads'][2]['height'])
                self.ui.ad3.setFixedWidth(response_json['ads'][2]['width'])
                self.ui.ad3.setUrl(response_json['ads'][2]['url'])
            else:
                self.ui.ad1.setVisible(False)
                self.ui.ad2.setVisible(False)
                self.ui.ad3.setVisible(False)

        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())