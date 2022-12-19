# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserListItem.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_UserListItem(object):
    def setupUi(self, UserListItem):
        if not UserListItem.objectName():
            UserListItem.setObjectName(u"UserListItem")
        UserListItem.resize(468, 114)
        self.gridLayout = QGridLayout(UserListItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(UserListItem)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_open = QPushButton(self.frame)
        self.button_open.setObjectName(u"button_open")

        self.gridLayout_2.addWidget(self.button_open, 2, 2, 1, 1)

        self.username = QLabel(self.frame)
        self.username.setObjectName(u"username")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.username.setFont(font)

        self.gridLayout_2.addWidget(self.username, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.email = QLabel(self.frame)
        self.email.setObjectName(u"email")

        self.gridLayout_2.addWidget(self.email, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(UserListItem)

        QMetaObject.connectSlotsByName(UserListItem)
    # setupUi

    def retranslateUi(self, UserListItem):
        UserListItem.setWindowTitle(QCoreApplication.translate("UserListItem", u"Form", None))
        self.button_open.setText(QCoreApplication.translate("UserListItem", u"Open", None))
        self.username.setText(QCoreApplication.translate("UserListItem", u"TextLabel", None))
        self.email.setText(QCoreApplication.translate("UserListItem", u"TextLabel", None))
    # retranslateUi

