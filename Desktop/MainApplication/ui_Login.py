# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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

class Ui_LogIn(object):
    def setupUi(self, LogIn):
        if not LogIn.objectName():
            LogIn.setObjectName(u"LogIn")
        LogIn.resize(400, 300)
        self.gridLayout = QGridLayout(LogIn)
        self.gridLayout.setObjectName(u"gridLayout")
        self.login_label = QLabel(LogIn)
        self.login_label.setObjectName(u"login_label")

        self.gridLayout.addWidget(self.login_label, 1, 0, 1, 1)

        self.login_field = QLineEdit(LogIn)
        self.login_field.setObjectName(u"login_field")

        self.gridLayout.addWidget(self.login_field, 1, 3, 1, 1)

        self.passworld_field = QLineEdit(LogIn)
        self.passworld_field.setObjectName(u"passworld_field")

        self.gridLayout.addWidget(self.passworld_field, 2, 3, 1, 1)

        self.password_label = QLabel(LogIn)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 2, 0, 1, 1)

        self.groupBox = QGroupBox(LogIn)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.login_cancel_button = QPushButton(self.groupBox)
        self.login_cancel_button.setObjectName(u"login_cancel_button")

        self.gridLayout_3.addWidget(self.login_cancel_button, 3, 1, 1, 1)

        self.error_label = QLabel(self.groupBox)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(True)
        self.error_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.error_label, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.login_button = QPushButton(self.groupBox)
        self.login_button.setObjectName(u"login_button")

        self.gridLayout_3.addWidget(self.login_button, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 4)


        self.retranslateUi(LogIn)

        QMetaObject.connectSlotsByName(LogIn)
    # setupUi

    def retranslateUi(self, LogIn):
        LogIn.setWindowTitle(QCoreApplication.translate("LogIn", u"Dialog", None))
        self.login_label.setText(QCoreApplication.translate("LogIn", u"Login:", None))
        self.password_label.setText(QCoreApplication.translate("LogIn", u"Password:", None))
        self.groupBox.setTitle("")
        self.login_cancel_button.setText(QCoreApplication.translate("LogIn", u"Cancel", None))
        self.error_label.setText("")
        self.login_button.setText(QCoreApplication.translate("LogIn", u"Login", None))
    # retranslateUi

