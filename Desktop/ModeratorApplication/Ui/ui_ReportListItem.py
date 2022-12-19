# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReportListItem.ui'
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

class Ui_ReportListItem(object):
    def setupUi(self, ReportListItem):
        if not ReportListItem.objectName():
            ReportListItem.setObjectName(u"ReportListItem")
        ReportListItem.resize(483, 114)
        self.gridLayout = QGridLayout(ReportListItem)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(ReportListItem)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_profile = QPushButton(self.frame)
        self.button_profile.setObjectName(u"button_profile")

        self.gridLayout_2.addWidget(self.button_profile, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(184, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.label_from = QLabel(self.frame)
        self.label_from.setObjectName(u"label_from")

        self.gridLayout_2.addWidget(self.label_from, 1, 1, 1, 1)

        self.button_tab = QPushButton(self.frame)
        self.button_tab.setObjectName(u"button_tab")

        self.gridLayout_2.addWidget(self.button_tab, 2, 4, 1, 1)

        self.button_viewed = QPushButton(self.frame)
        self.button_viewed.setObjectName(u"button_viewed")

        self.gridLayout_2.addWidget(self.button_viewed, 2, 5, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_reported = QLabel(self.frame)
        self.label_reported.setObjectName(u"label_reported")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_reported.setFont(font)

        self.gridLayout_2.addWidget(self.label_reported, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(ReportListItem)

        QMetaObject.connectSlotsByName(ReportListItem)
    # setupUi

    def retranslateUi(self, ReportListItem):
        ReportListItem.setWindowTitle(QCoreApplication.translate("ReportListItem", u"Form", None))
        self.button_profile.setText(QCoreApplication.translate("ReportListItem", u"Open Profile", None))
        self.label_from.setText(QCoreApplication.translate("ReportListItem", u"TextLabel", None))
        self.button_tab.setText(QCoreApplication.translate("ReportListItem", u"Open Tab", None))
        self.button_viewed.setText(QCoreApplication.translate("ReportListItem", u"Mark as Viewed", None))
        self.label.setText(QCoreApplication.translate("ReportListItem", u"reported by", None))
        self.label_reported.setText(QCoreApplication.translate("ReportListItem", u"TextLabel", None))
    # retranslateUi

