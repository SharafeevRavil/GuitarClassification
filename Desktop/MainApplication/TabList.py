from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog, QListWidgetItem
from PySide6.QtGui import QPixmap, QImage
from Ui.ui_TabList import Ui_TabList
from TabListItem import TabListItem
import Requests
import settings

class TabList(QtWidgets.QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.ui = Ui_TabList()
        self.ui.setupUi(self)

        self.ui.button_next_page.clicked.connect(self.next_page)
        self.ui.button_previous_page.clicked.connect(self.prev_page)

    def load_test_tabs(self):
        # Add to list a new item (item is simply an entry in your list)
        for i in range(10):
            item = QListWidgetItem(self.ui.list)
            self.ui.list.addItem(item)

            # Instanciate a custom widget 
            row = TabListItem('alena shvets - dve devochki', 'ravil', 100)
            item.setSizeHint(row.minimumSizeHint())

            # Associate the custom widget to the list entry
            self.ui.list.setItemWidget(item, row)

    def load_global(self, page = 1):
        self.source_type = 'global'
        self.load({'Page': page, 'PageSize': 2})        

    def load_user(self, user_id, page = 1):
        self.source_type = 'user'
        self.user_id = user_id
        self.load({'UserIds': [user_id], 'Page': page, 'PageSize': 2})

    def load(self, params):
        self.ui.list.clear()
        response = Requests.get(settings.api_path + settings.tab_path, params=params)
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

    def next_page(self):
        match self.source_type:
            case 'global':
                self.load_global(self.page + 1)
            case 'user':
                self.load_user(self.user_id, self.page + 1)

    def prev_page(self):
        match self.source_type:
            case 'global':
                self.load_global(self.page - 1)
            case 'user':
                self.load_user(self.user_id, self.page - 1)