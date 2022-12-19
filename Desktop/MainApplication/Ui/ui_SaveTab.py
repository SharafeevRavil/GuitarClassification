# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SaveTab.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_SaveTab(object):
    def setupUi(self, SaveTab):
        if not SaveTab.objectName():
            SaveTab.setObjectName(u"SaveTab")
        SaveTab.resize(736, 565)
        self.gridLayout = QGridLayout(SaveTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_error = QLabel(SaveTab)
        self.label_error.setObjectName(u"label_error")

        self.gridLayout.addWidget(self.label_error, 3, 1, 1, 1)

        self.button_upload = QPushButton(SaveTab)
        self.button_upload.setObjectName(u"button_upload")

        self.gridLayout.addWidget(self.button_upload, 2, 0, 1, 1)

        self.webEngineView = QWebEngineView(SaveTab)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 5)

        self.button_save_file = QPushButton(SaveTab)
        self.button_save_file.setObjectName(u"button_save_file")

        self.gridLayout.addWidget(self.button_save_file, 3, 0, 1, 1)

        self.label = QLabel(SaveTab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.button_return = QPushButton(SaveTab)
        self.button_return.setObjectName(u"button_return")

        self.gridLayout.addWidget(self.button_return, 3, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.field_tab_name = QLineEdit(SaveTab)
        self.field_tab_name.setObjectName(u"field_tab_name")

        self.gridLayout.addWidget(self.field_tab_name, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 3, 1, 2)


        self.retranslateUi(SaveTab)

        QMetaObject.connectSlotsByName(SaveTab)
    # setupUi

    def retranslateUi(self, SaveTab):
        SaveTab.setWindowTitle(QCoreApplication.translate("SaveTab", u"Form", None))
        self.label_error.setText("")
        self.button_upload.setText(QCoreApplication.translate("SaveTab", u"Upload", None))
        self.button_save_file.setText(QCoreApplication.translate("SaveTab", u"Save as file...", None))
        self.label.setText(QCoreApplication.translate("SaveTab", u"Tab name:", None))
        self.button_return.setText(QCoreApplication.translate("SaveTab", u"Return", None))
    # retranslateUi

