from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_TabListItem import Ui_TabListItem
import Requests

class TabListItem(QtWidgets.QWidget):

    def __init__(self, tab_name, author_name, tab_id, tab_url, main_window):
        super().__init__()
        self.id = tab_id
        self.url = tab_url
        self.main_window = main_window

        self.ui = Ui_TabListItem()
        self.ui.setupUi(self)

        self.ui.tab_name.setText(tab_name)
        self.ui.author_name.setText('by ' + author_name)
        self.ui.button_open.clicked.connect(self.open)
        self.ui.button_report.clicked.connect(self.report)

    def open(self):
        self.main_window.view_tab.open(self.url, self.ui.tab_name.text(), self.ui.author_name.text())
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.view_tab)

    def report(self):
        pass