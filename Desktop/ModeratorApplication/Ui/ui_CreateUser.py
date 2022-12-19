# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUser.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        if not CreateUser.objectName():
            CreateUser.setObjectName(u"CreateUser")
        CreateUser.resize(400, 301)
        self.gridLayout = QGridLayout(CreateUser)
        self.gridLayout.setObjectName(u"gridLayout")
        self.email_label = QLabel(CreateUser)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)

        self.groupBox = QGroupBox(CreateUser)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.cancel_button = QPushButton(self.groupBox)
        self.cancel_button.setObjectName(u"cancel_button")

        self.gridLayout_2.addWidget(self.cancel_button, 2, 1, 1, 1)

        self.create_button = QPushButton(self.groupBox)
        self.create_button.setObjectName(u"create_button")

        self.gridLayout_2.addWidget(self.create_button, 2, 0, 1, 1)

        self.error_label = QLabel(self.groupBox)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(True)
        self.error_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.error_label, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 2)

        self.email_field = QLineEdit(CreateUser)
        self.email_field.setObjectName(u"email_field")

        self.gridLayout.addWidget(self.email_field, 2, 1, 1, 1)

        self.login_field = QLineEdit(CreateUser)
        self.login_field.setObjectName(u"login_field")

        self.gridLayout.addWidget(self.login_field, 3, 1, 1, 1)

        self.passworld_field = QLineEdit(CreateUser)
        self.passworld_field.setObjectName(u"passworld_field")
        self.passworld_field.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passworld_field, 6, 1, 1, 1)

        self.password_label = QLabel(CreateUser)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 6, 0, 1, 1)

        self.login_label = QLabel(CreateUser)
        self.login_label.setObjectName(u"login_label")

        self.gridLayout.addWidget(self.login_label, 3, 0, 1, 1)


        self.retranslateUi(CreateUser)

        QMetaObject.connectSlotsByName(CreateUser)
    # setupUi

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(QCoreApplication.translate("CreateUser", u"Dialog", None))
        self.email_label.setText(QCoreApplication.translate("CreateUser", u"Email:", None))
        self.groupBox.setTitle("")
        self.cancel_button.setText(QCoreApplication.translate("CreateUser", u"Cancel", None))
        self.create_button.setText(QCoreApplication.translate("CreateUser", u"Create", None))
        self.error_label.setText("")
        self.password_label.setText(QCoreApplication.translate("CreateUser", u"Password:", None))
        self.login_label.setText(QCoreApplication.translate("CreateUser", u"Login:", None))
    # retranslateUi

