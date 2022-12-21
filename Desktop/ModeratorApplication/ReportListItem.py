from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_ReportListItem import Ui_ReportListItem
import Requests
import settings

class ReportListItem(QtWidgets.QWidget):

    def __init__(self, report_id, from_user_id, from_user_name, tab_id, tab_name, tab_url, reported_user_id, reported_user_name, isViewed, main_window):
        super().__init__()
        self.tab_id = tab_id
        self.user_id = reported_user_id
        self.tab_name = tab_name
        self.tab_url = tab_url
        self.id = report_id
        self.main_window = main_window

        self.ui = Ui_ReportListItem()
        self.ui.setupUi(self)

        self.ui.label_from.setText(from_user_name)
        self.ui.label_reported.setText(reported_user_name)
        self.ui.button_profile.clicked.connect(self.open_profile)
        self.ui.button_tab.clicked.connect(self.open_tab)
        self.ui.button_viewed.clicked.connect(self.mark_viewed)
        if isViewed:
            self.ui.button_viewed.setEnabled(False)
            self.ui.button_viewed.setText('Viewed')
        else:
            self.ui.button_viewed.setEnabled(True)
            self.ui.button_viewed.setText('Mark as Viewed')


    def open_profile(self):
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.user_profile)
        self.main_window.user_profile.load_profile(self.user_id)

    def open_tab(self):
        self.main_window.view_tab.open(self.tab_url, self.tab_name, self.ui.label_reported.text(), self.tab_id, self.main_window)
        self.main_window.ui.stackedWidget.setCurrentWidget(self.main_window.view_tab)

    def mark_viewed(self):
        response = Requests.post(settings.api_path + settings.mark_report_as_viewed_path, params={'reportId': self.id}, needAuth=True)
        if response.status_code == 200:
            self.main_window.list.load_reports(self.main_window.list.page)
