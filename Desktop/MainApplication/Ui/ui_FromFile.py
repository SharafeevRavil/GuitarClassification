# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FromFile.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_FromFile(object):
    def setupUi(self, FromFile):
        if not FromFile.objectName():
            FromFile.setObjectName(u"FromFile")
        FromFile.resize(667, 517)
        self.gridLayout = QGridLayout(FromFile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_select = QPushButton(FromFile)
        self.button_select.setObjectName(u"button_select")

        self.gridLayout.addWidget(self.button_select, 1, 0, 1, 1)

        self.button_generate = QPushButton(FromFile)
        self.button_generate.setObjectName(u"button_generate")
        self.button_generate.setEnabled(False)
        self.button_generate.setAutoDefault(False)
        self.button_generate.setFlat(False)

        self.gridLayout.addWidget(self.button_generate, 3, 0, 1, 1)

        self.webEngineView_tabs = QWebEngineView(FromFile)
        self.webEngineView_tabs.setObjectName(u"webEngineView_tabs")
        self.webEngineView_tabs.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView_tabs, 0, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.audio_name = QLabel(FromFile)
        self.audio_name.setObjectName(u"audio_name")

        self.gridLayout.addWidget(self.audio_name, 1, 1, 1, 1)


        self.retranslateUi(FromFile)

        self.button_generate.setDefault(False)


        QMetaObject.connectSlotsByName(FromFile)
    # setupUi

    def retranslateUi(self, FromFile):
        FromFile.setWindowTitle(QCoreApplication.translate("FromFile", u"Form", None))
        self.button_select.setText(QCoreApplication.translate("FromFile", u"Select audio file", None))
        self.button_generate.setText(QCoreApplication.translate("FromFile", u"Generate tabs", None))
        self.audio_name.setText("")
    # retranslateUi

