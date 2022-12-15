# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Subscribe.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QWidget)

class Ui_Subscribe(object):
    def setupUi(self, Subscribe):
        if not Subscribe.objectName():
            Subscribe.setObjectName(u"Subscribe")
        Subscribe.resize(276, 388)
        self.gridLayout = QGridLayout(Subscribe)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(Subscribe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 3)

        self.label_2 = QLabel(Subscribe)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.textBrowser = QTextBrowser(Subscribe)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 5, 0, 1, 3)

        self.label = QLabel(Subscribe)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line = QFrame(Subscribe)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.button_cancel = QPushButton(Subscribe)
        self.button_cancel.setObjectName(u"button_cancel")

        self.gridLayout.addWidget(self.button_cancel, 9, 2, 1, 1)

        self.input_username = QLineEdit(Subscribe)
        self.input_username.setObjectName(u"input_username")

        self.gridLayout.addWidget(self.input_username, 0, 1, 1, 2)

        self.button_subsribe = QPushButton(Subscribe)
        self.button_subsribe.setObjectName(u"button_subsribe")

        self.gridLayout.addWidget(self.button_subsribe, 9, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 9, 1, 1, 1)

        self.widget = QWidget(Subscribe)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.combo_currency = QComboBox(self.widget)
        self.combo_currency.addItem("")
        self.combo_currency.addItem("")
        self.combo_currency.addItem("")
        self.combo_currency.setObjectName(u"combo_currency")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_currency.sizePolicy().hasHeightForWidth())
        self.combo_currency.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.combo_currency, 0, 2, 1, 1)

        self.label_price = QLabel(self.widget)
        self.label_price.setObjectName(u"label_price")

        self.gridLayout_2.addWidget(self.label_price, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.combo_period = QComboBox(self.widget)
        self.combo_period.addItem("")
        self.combo_period.addItem("")
        self.combo_period.addItem("")
        self.combo_period.setObjectName(u"combo_period")

        self.gridLayout_2.addWidget(self.combo_period, 1, 1, 1, 2)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 3)

        self.line_3 = QFrame(Subscribe)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 3, 0, 1, 3)

        self.label_error = QLabel(Subscribe)
        self.label_error.setObjectName(u"label_error")

        self.gridLayout.addWidget(self.label_error, 8, 0, 1, 1)


        self.retranslateUi(Subscribe)

        QMetaObject.connectSlotsByName(Subscribe)
    # setupUi

    def retranslateUi(self, Subscribe):
        Subscribe.setWindowTitle(QCoreApplication.translate("Subscribe", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Subscribe", u"Payment data:", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Subscribe", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">PLACEHOLDER</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Subscribe", u"Username:", None))
        self.button_cancel.setText(QCoreApplication.translate("Subscribe", u"Cancel", None))
        self.button_subsribe.setText(QCoreApplication.translate("Subscribe", u"Subscribe", None))
        self.label_3.setText(QCoreApplication.translate("Subscribe", u"Price:", None))
        self.combo_currency.setItemText(0, QCoreApplication.translate("Subscribe", u"Rub", None))
        self.combo_currency.setItemText(1, QCoreApplication.translate("Subscribe", u"Usd", None))
        self.combo_currency.setItemText(2, QCoreApplication.translate("Subscribe", u"Eur", None))

        self.label_price.setText(QCoreApplication.translate("Subscribe", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Subscribe", u"Period:", None))
        self.combo_period.setItemText(0, QCoreApplication.translate("Subscribe", u"Month", None))
        self.combo_period.setItemText(1, QCoreApplication.translate("Subscribe", u"HalfOfYear", None))
        self.combo_period.setItemText(2, QCoreApplication.translate("Subscribe", u"Year", None))

        self.label_error.setText("")
    # retranslateUi

