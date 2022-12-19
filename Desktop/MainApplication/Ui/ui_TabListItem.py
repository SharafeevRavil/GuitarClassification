# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TabListItem.ui'
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

class Ui_TabListItem(object):
    def setupUi(self, TabListItem):
        if not TabListItem.objectName():
            TabListItem.setObjectName(u"TabListItem")
        TabListItem.resize(468, 114)
        self.gridLayout = QGridLayout(TabListItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(TabListItem)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_name = QLabel(self.frame)
        self.tab_name.setObjectName(u"tab_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.tab_name.setFont(font)

        self.gridLayout_2.addWidget(self.tab_name, 0, 0, 1, 1)

        self.author_name = QLabel(self.frame)
        self.author_name.setObjectName(u"author_name")

        self.gridLayout_2.addWidget(self.author_name, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.button_open = QPushButton(self.frame)
        self.button_open.setObjectName(u"button_open")

        self.gridLayout_2.addWidget(self.button_open, 2, 2, 1, 1)

        self.button_report_delete = QPushButton(self.frame)
        self.button_report_delete.setObjectName(u"button_report_delete")

        self.gridLayout_2.addWidget(self.button_report_delete, 2, 3, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(TabListItem)

        QMetaObject.connectSlotsByName(TabListItem)
    # setupUi

    def retranslateUi(self, TabListItem):
        TabListItem.setWindowTitle(QCoreApplication.translate("TabListItem", u"Form", None))
        self.tab_name.setText(QCoreApplication.translate("TabListItem", u"TextLabel", None))
        self.author_name.setText(QCoreApplication.translate("TabListItem", u"TextLabel", None))
        self.button_open.setText(QCoreApplication.translate("TabListItem", u"Open", None))
        self.button_report_delete.setText(QCoreApplication.translate("TabListItem", u"Report", None))
    # retranslateUi

