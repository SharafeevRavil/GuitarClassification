# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserProfile.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_UserProfile(object):
    def setupUi(self, UserProfile):
        if not UserProfile.objectName():
            UserProfile.setObjectName(u"UserProfile")
        UserProfile.resize(924, 563)
        self.gridLayout = QGridLayout(UserProfile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_error = QLabel(UserProfile)
        self.label_error.setObjectName(u"label_error")

        self.gridLayout.addWidget(self.label_error, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 219, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.email_value = QLabel(UserProfile)
        self.email_value.setObjectName(u"email_value")

        self.gridLayout.addWidget(self.email_value, 1, 2, 1, 1)

        self.login_value = QLabel(UserProfile)
        self.login_value.setObjectName(u"login_value")

        self.gridLayout.addWidget(self.login_value, 0, 2, 1, 1)

        self.button_ban = QPushButton(UserProfile)
        self.button_ban.setObjectName(u"button_ban")

        self.gridLayout.addWidget(self.button_ban, 4, 1, 1, 1)

        self.label_image = QLabel(UserProfile)
        self.label_image.setObjectName(u"label_image")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setPixmap(QPixmap(u"C:/Users/dimao/MainApplication/Ui/no-image-icon.png"))

        self.gridLayout.addWidget(self.label_image, 0, 0, 4, 1)

        self.verticalSpacer = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.label_email = QLabel(UserProfile)
        self.label_email.setObjectName(u"label_email")

        self.gridLayout.addWidget(self.label_email, 1, 1, 1, 1)

        self.container_subscription = QGroupBox(UserProfile)
        self.container_subscription.setObjectName(u"container_subscription")
        self.gridLayout_6 = QGridLayout(self.container_subscription)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_subscribed_until = QLabel(self.container_subscription)
        self.label_subscribed_until.setObjectName(u"label_subscribed_until")
        self.label_subscribed_until.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_subscribed_until, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.label_subscription = QLabel(self.container_subscription)
        self.label_subscription.setObjectName(u"label_subscription")
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_subscription.setFont(font)
        self.label_subscription.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_6.addWidget(self.label_subscription, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.container_subscription, 0, 4, 4, 1)

        self.label_login = QLabel(UserProfile)
        self.label_login.setObjectName(u"label_login")

        self.gridLayout.addWidget(self.label_login, 0, 1, 1, 1)

        self.button_return = QPushButton(UserProfile)
        self.button_return.setObjectName(u"button_return")

        self.gridLayout.addWidget(self.button_return, 6, 4, 1, 1)


        self.retranslateUi(UserProfile)

        QMetaObject.connectSlotsByName(UserProfile)
    # setupUi

    def retranslateUi(self, UserProfile):
        UserProfile.setWindowTitle(QCoreApplication.translate("UserProfile", u"Form", None))
        self.label_error.setText("")
        self.email_value.setText(QCoreApplication.translate("UserProfile", u"TextLabel", None))
        self.login_value.setText(QCoreApplication.translate("UserProfile", u"TextLabel", None))
        self.button_ban.setText(QCoreApplication.translate("UserProfile", u"Ban", None))
        self.label_image.setText("")
        self.label_email.setText(QCoreApplication.translate("UserProfile", u"Email:", None))
        self.container_subscription.setTitle(QCoreApplication.translate("UserProfile", u"Subscription", None))
        self.label_subscribed_until.setText("")
        self.label_subscription.setText(QCoreApplication.translate("UserProfile", u"No subscription", None))
        self.label_login.setText(QCoreApplication.translate("UserProfile", u"Login:", None))
        self.button_return.setText(QCoreApplication.translate("UserProfile", u"Return", None))
    # retranslateUi

