import sys
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_Subscribe import Ui_Subscribe
from datetime import datetime
import Requests
import settings

class Subscribe(QDialog):
    def __init__(self, username):
        super().__init__()

        self.ui = Ui_Subscribe()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.update_price()

        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_subsribe.clicked.connect(self.subscribe)
        self.ui.combo_currency.currentTextChanged.connect(self.update_price)
        self.ui.combo_period.currentTextChanged.connect(self.update_price)
        
        self.ui.input_username.setText(username)

    def cancel(self):
        self.close()

    def subscribe(self):
        json = {
            'currency': self.ui.combo_currency.currentText(),
            'period': self.ui.combo_period.currentText(),
            }
        response = Requests.post(settings.api_path + settings.subscribe_path, json=json, needAuth=True)
        if response.status_code == 200:
            self.accept()
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])

    def update_price(self):
        params = {
            'Currencies': [self.ui.combo_currency.currentText()],
            'Periods': [self.ui.combo_period.currentText()]
            }
        response = Requests.get(settings.api_path + settings.subscription_price_path, params=params)
        if response.status_code == 200:
            response_json = response.json()
            self.ui.label_price.setText(str(response_json[0]['money']['amount']))
        elif response.headers.get('content-type') == 'application/json':
            response_json = response.json()
            if 'status' in response_json and response_json['status'] == 'Error':
                self.ui.label_error.setText(response_json['message'])