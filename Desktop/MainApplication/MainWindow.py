import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from ui_GuitarCog import Ui_MainWindow
from Register import Register
from Login import Login
import settings
import keyring
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isAuthed = False

        if keyring.get_password('GuitarCog', 'token') != None and keyring.get_password('GuitarCog', 'refreshToken') != None:
            response = requests.post(settings.api_path + settings.checkauth_path, headers={'Authorization': 'Bearer ' + keyring.get_password('GuitarCog', 'token')})            
            response_json = response.json()

            if response.status_code == 200:
                self.isAuthed = True
                self.username = response_json['username']

        if self.isAuthed:
            self.ui.action_login.setVisible(False)
            self.ui.action_register.setVisible(False)
        else:
            self.ui.action_open_profile.setVisible(False)
            self.ui.action_logout.setVisible(False)
            self.ui.action_view_global.setVisible(False)
            self.ui.action_view_owned.setVisible(False)

        self.setWindowTitle("GuitarCog")
        
        self.ui.action_register.triggered.connect(self.open_register)
        self.ui.action_login.triggered.connect(self.open_login)


    def open_register(self):
        dlg = Register()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    def open_login(self):
        dlg = Login()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())