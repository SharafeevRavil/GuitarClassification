# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(400, 301)
        self.gridLayout = QGridLayout(Register)
        self.gridLayout.setObjectName(u"gridLayout")
        self.email_label = QLabel(Register)
        self.email_label.setObjectName(u"email_label")

        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 1)

        self.groupBox = QGroupBox(Register)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.register_cancel_button = QPushButton(self.groupBox)
        self.register_cancel_button.setObjectName(u"register_cancel_button")

        self.gridLayout_2.addWidget(self.register_cancel_button, 2, 1, 1, 1)

        self.register_button = QPushButton(self.groupBox)
        self.register_button.setObjectName(u"register_button")

        self.gridLayout_2.addWidget(self.register_button, 2, 0, 1, 1)

        self.error_label = QLabel(self.groupBox)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(True)
        self.error_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.error_label, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 2)

        self.email_field = QLineEdit(Register)
        self.email_field.setObjectName(u"email_field")

        self.gridLayout.addWidget(self.email_field, 2, 1, 1, 1)

        self.login_field = QLineEdit(Register)
        self.login_field.setObjectName(u"login_field")

        self.gridLayout.addWidget(self.login_field, 3, 1, 1, 1)

        self.passworld_field = QLineEdit(Register)
        self.passworld_field.setObjectName(u"passworld_field")
        self.passworld_field.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passworld_field, 6, 1, 1, 1)

        self.password_label = QLabel(Register)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 6, 0, 1, 1)

        self.login_label = QLabel(Register)
        self.login_label.setObjectName(u"login_label")

        self.gridLayout.addWidget(self.login_label, 3, 0, 1, 1)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Dialog", None))
        self.email_label.setText(QCoreApplication.translate("Register", u"Email:", None))
        self.groupBox.setTitle("")
        self.register_cancel_button.setText(QCoreApplication.translate("Register", u"Cancel", None))
        self.register_button.setText(QCoreApplication.translate("Register", u"Register", None))
        self.error_label.setText("")
        self.password_label.setText(QCoreApplication.translate("Register", u"Password:", None))
        self.login_label.setText(QCoreApplication.translate("Register", u"Login:", None))
    # retranslateUi

