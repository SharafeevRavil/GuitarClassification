# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewTab.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_ViewTab(object):
    def setupUi(self, ViewTab):
        if not ViewTab.objectName():
            ViewTab.setObjectName(u"ViewTab")
        ViewTab.resize(736, 565)
        self.gridLayout = QGridLayout(ViewTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(298, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.webEngineView = QWebEngineView(ViewTab)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 2)

        self.button_upload = QPushButton(ViewTab)
        self.button_upload.setObjectName(u"button_upload")

        self.gridLayout.addWidget(self.button_upload, 2, 0, 1, 1)

        self.button_save_file = QPushButton(ViewTab)
        self.button_save_file.setObjectName(u"button_save_file")

        self.gridLayout.addWidget(self.button_save_file, 3, 0, 1, 1)


        self.retranslateUi(ViewTab)

        QMetaObject.connectSlotsByName(ViewTab)
    # setupUi

    def retranslateUi(self, ViewTab):
        ViewTab.setWindowTitle(QCoreApplication.translate("ViewTab", u"Form", None))
        self.button_upload.setText(QCoreApplication.translate("ViewTab", u"Upload", None))
        self.button_save_file.setText(QCoreApplication.translate("ViewTab", u"Save as file...", None))
    # retranslateUi

