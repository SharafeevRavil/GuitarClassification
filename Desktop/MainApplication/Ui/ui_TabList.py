# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabList.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_TabList(object):
    def setupUi(self, TabList):
        if not TabList.objectName():
            TabList.setObjectName(u"TabList")
        TabList.resize(532, 300)
        self.gridLayout = QGridLayout(TabList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_next_page = QPushButton(TabList)
        self.button_next_page.setObjectName(u"button_next_page")

        self.gridLayout.addWidget(self.button_next_page, 1, 2, 1, 1)

        self.list = QListWidget(TabList)
        self.list.setObjectName(u"list")
        self.list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout.addWidget(self.list, 0, 0, 1, 3)

        self.button_previous_page = QPushButton(TabList)
        self.button_previous_page.setObjectName(u"button_previous_page")

        self.gridLayout.addWidget(self.button_previous_page, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.retranslateUi(TabList)

        QMetaObject.connectSlotsByName(TabList)
    # setupUi

    def retranslateUi(self, TabList):
        TabList.setWindowTitle(QCoreApplication.translate("TabList", u"Form", None))
        self.button_next_page.setText(QCoreApplication.translate("TabList", u">", None))
        self.button_previous_page.setText(QCoreApplication.translate("TabList", u"<", None))
    # retranslateUi

