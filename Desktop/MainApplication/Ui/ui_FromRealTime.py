# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FromRealTime.ui'
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

class Ui_FromRealTime(object):
    def setupUi(self, FromRealTime):
        if not FromRealTime.objectName():
            FromRealTime.setObjectName(u"FromRealTime")
        FromRealTime.resize(638, 498)
        self.gridLayout = QGridLayout(FromRealTime)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_play = QPushButton(FromRealTime)
        self.button_play.setObjectName(u"button_play")

        self.gridLayout.addWidget(self.button_play, 1, 0, 1, 1)

        self.button_return = QPushButton(FromRealTime)
        self.button_return.setObjectName(u"button_return")

        self.gridLayout.addWidget(self.button_return, 2, 3, 1, 1)

        self.button_stop = QPushButton(FromRealTime)
        self.button_stop.setObjectName(u"button_stop")

        self.gridLayout.addWidget(self.button_stop, 1, 1, 1, 1)

        self.webEngineView = QWebEngineView(FromRealTime)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 4)

        self.button_submit = QPushButton(FromRealTime)
        self.button_submit.setObjectName(u"button_submit")

        self.gridLayout.addWidget(self.button_submit, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 2)


        self.retranslateUi(FromRealTime)

        QMetaObject.connectSlotsByName(FromRealTime)
    # setupUi

    def retranslateUi(self, FromRealTime):
        FromRealTime.setWindowTitle(QCoreApplication.translate("FromRealTime", u"Form", None))
        self.button_play.setText(QCoreApplication.translate("FromRealTime", u"Play", None))
        self.button_return.setText(QCoreApplication.translate("FromRealTime", u"Return", None))
        self.button_stop.setText(QCoreApplication.translate("FromRealTime", u"Stop", None))
        self.button_submit.setText(QCoreApplication.translate("FromRealTime", u"Submit", None))
    # retranslateUi

