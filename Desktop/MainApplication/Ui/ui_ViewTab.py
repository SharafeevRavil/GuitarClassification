# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewTab.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ViewTab(object):
    def setupUi(self, ViewTab):
        if not ViewTab.objectName():
            ViewTab.setObjectName(u"ViewTab")
        ViewTab.resize(687, 413)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewTab.sizePolicy().hasHeightForWidth())
        ViewTab.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ViewTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.button_return = QPushButton(ViewTab)
        self.button_return.setObjectName(u"button_return")

        self.gridLayout.addWidget(self.button_return, 3, 2, 1, 1)

        self.webEngineView = QWebEngineView(ViewTab)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy1)
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.gridLayout.addWidget(self.webEngineView, 2, 0, 1, 3)

        self.label_tab_name = QLabel(ViewTab)
        self.label_tab_name.setObjectName(u"label_tab_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_tab_name.setFont(font)
        self.label_tab_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_tab_name, 0, 0, 1, 3)

        self.label_author_name = QLabel(ViewTab)
        self.label_author_name.setObjectName(u"label_author_name")
        self.label_author_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_author_name, 1, 0, 1, 3)


        self.retranslateUi(ViewTab)

        QMetaObject.connectSlotsByName(ViewTab)
    # setupUi

    def retranslateUi(self, ViewTab):
        ViewTab.setWindowTitle(QCoreApplication.translate("ViewTab", u"Form", None))
        self.button_return.setText(QCoreApplication.translate("ViewTab", u"Return", None))
        self.label_tab_name.setText(QCoreApplication.translate("ViewTab", u"TextLabel", None))
        self.label_author_name.setText(QCoreApplication.translate("ViewTab", u"TextLabel", None))
    # retranslateUi

