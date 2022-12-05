# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuitarCog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        self.action_new_from_file = QAction(MainWindow)
        self.action_new_from_file.setObjectName(u"action_new_from_file")
        self.action_new_from_realtime = QAction(MainWindow)
        self.action_new_from_realtime.setObjectName(u"action_new_from_realtime")
        self.action_view_local = QAction(MainWindow)
        self.action_view_local.setObjectName(u"action_view_local")
        self.action_view_owned = QAction(MainWindow)
        self.action_view_owned.setObjectName(u"action_view_owned")
        self.action_view_global = QAction(MainWindow)
        self.action_view_global.setObjectName(u"action_view_global")
        self.action_open_profile = QAction(MainWindow)
        self.action_open_profile.setObjectName(u"action_open_profile")
        self.action_login = QAction(MainWindow)
        self.action_login.setObjectName(u"action_login")
        self.action_register = QAction(MainWindow)
        self.action_register.setObjectName(u"action_register")
        self.action_logout = QAction(MainWindow)
        self.action_logout.setObjectName(u"action_logout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.gridLayout = QGridLayout(self.page_welcome)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_welcome = QLabel(self.page_welcome)
        self.label_welcome.setObjectName(u"label_welcome")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_welcome.setFont(font)
        self.label_welcome.setTextFormat(Qt.AutoText)
        self.label_welcome.setScaledContents(False)
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_welcome, 0, 0, 1, 1)

        self.label_welcome_text = QLabel(self.page_welcome)
        self.label_welcome_text.setObjectName(u"label_welcome_text")
        self.label_welcome_text.setTextFormat(Qt.AutoText)
        self.label_welcome_text.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_welcome_text.setWordWrap(True)

        self.gridLayout.addWidget(self.label_welcome_text, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_welcome)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_options = QMenu(self.menubar)
        self.menu_options.setObjectName(u"menu_options")
        self.menu_profile = QMenu(self.menubar)
        self.menu_profile.setObjectName(u"menu_profile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_profile.menuAction())
        self.menu_file.addAction(self.action_new_from_file)
        self.menu_file.addAction(self.action_new_from_realtime)
        self.menu_view.addAction(self.action_view_local)
        self.menu_view.addAction(self.action_view_owned)
        self.menu_view.addAction(self.action_view_global)
        self.menu_profile.addAction(self.action_open_profile)
        self.menu_profile.addAction(self.action_login)
        self.menu_profile.addAction(self.action_register)
        self.menu_profile.addAction(self.action_logout)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_new_from_file.setText(QCoreApplication.translate("MainWindow", u"New from audio file", None))
        self.action_new_from_realtime.setText(QCoreApplication.translate("MainWindow", u"New from real time", None))
        self.action_view_local.setText(QCoreApplication.translate("MainWindow", u"Local", None))
        self.action_view_owned.setText(QCoreApplication.translate("MainWindow", u"Owned", None))
        self.action_view_global.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.action_open_profile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.action_register.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.action_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.label_welcome_text.setText(QCoreApplication.translate("MainWindow", u"Dori me Interimo, adapare Dori me Ameno, Ameno Latire Latiremo Dori me Ameno Omenare imperavi ameno Dimere, dimere matiro Matiremo Ameno Omenare imperavi emulari, ameno Omenare imperavi emulari, ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me am Ameno Omenare imperavi ameno Dimere dimere matiro Matiremo Ameno Omenare imperavi emulari, ameno Omenare imperavi emulari, ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me Ameno dori me Ameno dori me Dori me (dori me, dori me, dori me) (Dori me, dori me, dori me) Ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me dom Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menu_options.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menu_profile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

