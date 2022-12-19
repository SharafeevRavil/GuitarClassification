from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QListWidgetItem
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_List import Ui_List
from TabListItem import TabListItem
from UserListItem import UserListItem
from ReportListItem import ReportListItem
import Requests
import settings

class List(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_List()
        self.ui.setupUi(self)

        self.ui.button_next_page.clicked.connect(self.next_page)
        self.ui.button_previous_page.clicked.connect(self.prev_page)

    def load_tabs(self, params):
        self.ui.list.clear()
        response = Requests.get(settings.api_path + settings.tab_path, params=params, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            self.page = response_json['page']
            self.page_count = response_json['pageCount']
            data = response_json['data']

            self.ui.button_previous_page.setVisible(self.page > 1)
            self.ui.button_next_page.setVisible(self.page < self.page_count)

            for tab in data:
                item = QListWidgetItem(self.ui.list)
                self.ui.list.addItem(item)
                row = TabListItem(tab['name'], tab['authorName'], tab['id'], tab['fileUrl'], self.main_window)
                item.setSizeHint(row.minimumSizeHint())
                self.ui.list.setItemWidget(item, row)

    def load_tabs_all(self, page = 1):
        self.source_type = 'tabs_all'
        params = {'Page': page, 'PageSize': 2}
        self.load_tabs(params)        

    def load_users(self, params):
        self.ui.list.clear()
        response = Requests.get(settings.api_path + settings.moder_user_path, params=params, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            self.page = response_json['page']
            self.page_count = response_json['pageCount']
            data = response_json['data']

            self.ui.button_previous_page.setVisible(self.page > 1)
            self.ui.button_next_page.setVisible(self.page < self.page_count)

            for user in data:
                item = QListWidgetItem(self.ui.list)
                self.ui.list.addItem(item)
                row = UserListItem(user['username'], user['email'], user['id'], self.main_window)
                item.setSizeHint(row.minimumSizeHint())
                self.ui.list.setItemWidget(item, row)

    def load_users_all(self, page = 1):
        self.source_type = 'users_all'
        params = {'Page': page, 'PageSize': 2, 'HideBannedUsers': True, 'HideUnbannedUsers': False}
        self.load_users(params)

    def load_users_banned(self, page = 1):
        self.source_type = 'users_banned'
        params = {'Page': page, 'PageSize': 2, 'HideBannedUsers': False, 'HideUnbannedUsers': True}
        self.load_users(params)
    
    def load_reports_all(self, page = 1):
        self.source_type = 'reports_all'
        params = {'Page': page, 'PageSize': 2, 'ShowViewedReports': True}
        self.load_reports(params)

    def load_reports_new(self, page = 1):
        self.source_type = 'reports_new'
        params = {'Page': page, 'PageSize': 2, 'ShowViewedReports': False}
        self.load_reports(params)

    def load_reports(self, params):
        self.ui.list.clear()
        response = Requests.get(settings.api_path + settings.moder_report_path, params=params, needAuth=True)
        if response.status_code == 200:
            response_json = response.json()
            self.page = response_json['page']
            self.page_count = response_json['pageCount']
            data = response_json['data']

            self.ui.button_previous_page.setVisible(self.page > 1)
            self.ui.button_next_page.setVisible(self.page < self.page_count)

            for report in data:
                item = QListWidgetItem(self.ui.list)
                self.ui.list.addItem(item)
                row = ReportListItem(report['id'], report['fromUserId'], report['fromUserName'],
                 report['tabId'], report['tabName'], report['tabUrl'], report['reportedUserId'],
                 report['reportedUserName'], report['isReportMarkedAsViewed'], self.main_window)
                item.setSizeHint(row.minimumSizeHint())
                self.ui.list.setItemWidget(item, row)

    def next_page(self):
        match self.source_type:
            case 'tabs_all':
                self.load_tabs_all(self.page + 1)
            case 'reports_new':
                self.load_reports_new(self.page + 1)
            case 'reports_all':
                self.load_reports_all(self.page + 1)
            case 'users_all':
                self.load_users_all(self.page + 1)
            case 'users_banned':
                self.load_users_banned(self.page + 1)

    def prev_page(self):
        match self.source_type:
            case 'tabs_all':
                self.load_tabs_all(self.page - 1)
            case 'reports_new':
                self.load_reports_new(self.page - 1)
            case 'reports_all':
                self.load_reports_all(self.page - 1)
            case 'users_all':
                self.load_users_all(self.page - 1)
            case 'users_banned':
                self.load_users_banned(self.page - 1)

    def reload(self):
        match self.source_type:
            case 'tabs_all':
                self.load_tabs_all(self.page)
            case 'reports_new':
                self.load_reports_new(self.page)
            case 'reports_all':
                self.load_reports_all(self.page)
            case 'users_all':
                self.load_users_all(self.page)
            case 'users_banned':
                self.load_users_banned(self.page)