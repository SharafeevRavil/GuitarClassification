# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Change_password.ui'
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

class Ui_Change_password(object):
    def setupUi(self, Change_password):
        if not Change_password.objectName():
            Change_password.setObjectName(u"Change_password")
        Change_password.resize(400, 300)
        self.gridLayout = QGridLayout(Change_password)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_old = QLabel(Change_password)
        self.label_old.setObjectName(u"label_old")

        self.gridLayout.addWidget(self.label_old, 0, 0, 1, 1)

        self.label_new = QLabel(Change_password)
        self.label_new.setObjectName(u"label_new")

        self.gridLayout.addWidget(self.label_new, 2, 0, 1, 1)

        self.field_old = QLineEdit(Change_password)
        self.field_old.setObjectName(u"field_old")
        self.field_old.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.field_old, 0, 1, 1, 1)

        self.field_new = QLineEdit(Change_password)
        self.field_new.setObjectName(u"field_new")
        self.field_new.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.field_new, 2, 1, 1, 1)

        self.groupBox = QGroupBox(Change_password)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setAutoFillBackground(False)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cancel_button = QPushButton(self.groupBox)
        self.cancel_button.setObjectName(u"cancel_button")

        self.gridLayout_3.addWidget(self.cancel_button, 3, 1, 1, 1)

        self.error_label = QLabel(self.groupBox)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setEnabled(True)
        self.error_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_3.addWidget(self.error_label, 2, 0, 1, 2)

        self.change_password_button = QPushButton(self.groupBox)
        self.change_password_button.setObjectName(u"change_password_button")

        self.gridLayout_3.addWidget(self.change_password_button, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 2)


        self.retranslateUi(Change_password)

        QMetaObject.connectSlotsByName(Change_password)
    # setupUi

    def retranslateUi(self, Change_password):
        Change_password.setWindowTitle(QCoreApplication.translate("Change_password", u"Dialog", None))
        self.label_old.setText(QCoreApplication.translate("Change_password", u"Old password:", None))
        self.label_new.setText(QCoreApplication.translate("Change_password", u"New password:", None))
        self.groupBox.setTitle("")
        self.cancel_button.setText(QCoreApplication.translate("Change_password", u"Cancel", None))
        self.error_label.setText("")
        self.change_password_button.setText(QCoreApplication.translate("Change_password", u"Change password", None))
    # retranslateUi

