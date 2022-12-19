from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_UserProfile import Ui_UserProfile
import settings
import Requests
from dateutil import parser

class UserProfile(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()

        self.ui = Ui_UserProfile()
        self.ui.setupUi(self)
        self.main_window = main_window

        self.ui.button_ban.clicked.connect(self.ban_unban)
        self.ui.button_return.clicked.connect(self.return_button)

    def load_profile(self, id):
        response = Requests.get(settings.api_path + settings.moder_user_path + '/' + str(id), needAuth=True)            
        if response.status_code == 200:
            response_json = response.json()
            self.username = response_json['username']
            self.email = response_json['email']
            self.isBanned = response_json['isBanned']
            self.id = id

            self.ui.login_value.setText(self.username)
            self.ui.email_value.setText(self.email)
            self.ui.button_ban.setVisible(len(response_json['roles']) == 0)
            if self.isBanned:
                self.ui.button_ban.setText('Unban')
            else:
                self.ui.button_ban.setText('Ban')

            if response_json['subscription']['isSubscribed']:
                self.ui.label_subscription.setText('Subscribed')
                self.ui.label_subscribed_until.setText('until ' + parser.parse(response_json['subscription']['end']).strftime("%m/%d/%Y, %H:%M:%S"))
            else:
                self.ui.label_subscription.setText('No subscription')
                self.ui.label_subscribed_until.setText('')

            self.load_avatar(response_json['imageSrc'])

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

    def ban_unban(self):
        if self.isBanned:
            response = Requests.post(settings.api_path + settings.unban_path, params={'userId': self.id}, needAuth=True)            
            if response.status_code == 200:
                self.load_profile(self.id)
        else:
            response = Requests.post(settings.api_path + settings.ban_path, params={'userId': self.id}, needAuth=True)            
            if response.status_code == 200:
                self.load_profile(self.id)

    def return_button(self):
        self.main_window.list.reload()
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.list)