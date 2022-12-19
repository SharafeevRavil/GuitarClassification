from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_UserListItem import Ui_UserListItem
import Requests

class UserListItem(QtWidgets.QWidget):

    def __init__(self, username, email, user_id, main_window):
        super().__init__()
        self.id = user_id
        self.main_window = main_window

        self.ui = Ui_UserListItem()
        self.ui.setupUi(self)

        self.ui.username.setText(username)
        self.ui.email.setText(email)
        self.ui.button_open.clicked.connect(self.open)

    def open(self):
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.user_profile)
        self.main_window.user_profile.load_profile(self.id)