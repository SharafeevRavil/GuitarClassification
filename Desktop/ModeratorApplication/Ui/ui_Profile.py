# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Profile.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(929, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Profile.sizePolicy().hasHeightForWidth())
        Profile.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Profile)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_change_password = QPushButton(Profile)
        self.button_change_password.setObjectName(u"button_change_password")

        self.gridLayout.addWidget(self.button_change_password, 4, 1, 1, 1)

        self.field_login = QLineEdit(Profile)
        self.field_login.setObjectName(u"field_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.field_login.sizePolicy().hasHeightForWidth())
        self.field_login.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_login, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 230, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.label_email = QLabel(Profile)
        self.label_email.setObjectName(u"label_email")

        self.gridLayout.addWidget(self.label_email, 1, 1, 1, 1)

        self.label_login = QLabel(Profile)
        self.label_login.setObjectName(u"label_login")

        self.gridLayout.addWidget(self.label_login, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 230, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.button_change_avatar = QPushButton(Profile)
        self.button_change_avatar.setObjectName(u"button_change_avatar")

        self.gridLayout.addWidget(self.button_change_avatar, 4, 0, 1, 1)

        self.label_image = QLabel(Profile)
        self.label_image.setObjectName(u"label_image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy2)
        self.label_image.setPixmap(QPixmap(u"../../MainApplication/Ui/no-image-icon.png"))

        self.gridLayout.addWidget(self.label_image, 0, 0, 4, 1)

        self.button_change_login = QPushButton(Profile)
        self.button_change_login.setObjectName(u"button_change_login")

        self.gridLayout.addWidget(self.button_change_login, 0, 3, 1, 1)

        self.label_error = QLabel(Profile)
        self.label_error.setObjectName(u"label_error")

        self.gridLayout.addWidget(self.label_error, 2, 3, 1, 1)

        self.button_change_email = QPushButton(Profile)
        self.button_change_email.setObjectName(u"button_change_email")

        self.gridLayout.addWidget(self.button_change_email, 1, 3, 1, 1)

        self.field_email = QLineEdit(Profile)
        self.field_email.setObjectName(u"field_email")
        sizePolicy1.setHeightForWidth(self.field_email.sizePolicy().hasHeightForWidth())
        self.field_email.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.field_email, 1, 2, 1, 1)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Form", None))
        self.button_change_password.setText(QCoreApplication.translate("Profile", u"Change Password", None))
        self.label_email.setText(QCoreApplication.translate("Profile", u"Email:", None))
        self.label_login.setText(QCoreApplication.translate("Profile", u"Login:", None))
        self.button_change_avatar.setText(QCoreApplication.translate("Profile", u"Change Avatar", None))
        self.label_image.setText("")
        self.button_change_login.setText(QCoreApplication.translate("Profile", u"Change Login", None))
        self.label_error.setText("")
        self.button_change_email.setText(QCoreApplication.translate("Profile", u"Change Email", None))
    # retranslateUi

