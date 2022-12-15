import sys
import Requests
from PySide6.QtWidgets import (
    QDialog, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from Ui.ui_Settings import Ui_Settings

class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")

        self.ui.button_cancel.clicked.connect(self.cancel)
        self.ui.button_ok.clicked.connect(self.ok)
        self.ui.button_apply.clicked.connect(self.apply)

    def cancel(self):
        self.close()

    def ok(self):
        self.apply()
        self.accept()

    def apply(self):
        pass