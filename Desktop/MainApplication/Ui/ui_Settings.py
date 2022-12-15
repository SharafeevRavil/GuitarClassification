# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(400, 364)
        self.gridLayout = QGridLayout(Settings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line = QFrame(Settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.widget = QWidget(Settings)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_apply = QPushButton(self.widget)
        self.button_apply.setObjectName(u"button_apply")

        self.gridLayout_2.addWidget(self.button_apply, 0, 1, 1, 1)

        self.button_ok = QPushButton(self.widget)
        self.button_ok.setObjectName(u"button_ok")

        self.gridLayout_2.addWidget(self.button_ok, 0, 0, 1, 1)

        self.button_cancel = QPushButton(self.widget)
        self.button_cancel.setObjectName(u"button_cancel")

        self.gridLayout_2.addWidget(self.button_cancel, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.microphone_combo_box = QComboBox(Settings)
        self.microphone_combo_box.setObjectName(u"microphone_combo_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.microphone_combo_box.sizePolicy().hasHeightForWidth())
        self.microphone_combo_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.microphone_combo_box, 0, 1, 1, 1)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Settings", u"Microphone:", None))
        self.button_apply.setText(QCoreApplication.translate("Settings", u"Apply", None))
        self.button_ok.setText(QCoreApplication.translate("Settings", u"Ok", None))
        self.button_cancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
    # retranslateUi

