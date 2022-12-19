# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuitarCog_Moderator.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStackedWidget, QStatusBar,
    QWidget)

class Ui_GuitarCogModerator(object):
    def setupUi(self, GuitarCogModerator):
        if not GuitarCogModerator.objectName():
            GuitarCogModerator.setObjectName(u"GuitarCogModerator")
        GuitarCogModerator.resize(989, 600)
        self.action_view_all = QAction(GuitarCogModerator)
        self.action_view_all.setObjectName(u"action_view_all")
        self.action_view_reported = QAction(GuitarCogModerator)
        self.action_view_reported.setObjectName(u"action_view_reported")
        self.action_users_all = QAction(GuitarCogModerator)
        self.action_users_all.setObjectName(u"action_users_all")
        self.action_users_banned = QAction(GuitarCogModerator)
        self.action_users_banned.setObjectName(u"action_users_banned")
        self.actionOpen = QAction(GuitarCogModerator)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionLogin = QAction(GuitarCogModerator)
        self.actionLogin.setObjectName(u"actionLogin")
        self.actionLogout = QAction(GuitarCogModerator)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionCreate = QAction(GuitarCogModerator)
        self.actionCreate.setObjectName(u"actionCreate")
        self.action_reports_all = QAction(GuitarCogModerator)
        self.action_reports_all.setObjectName(u"action_reports_all")
        self.action_reports_new = QAction(GuitarCogModerator)
        self.action_reports_new.setObjectName(u"action_reports_new")
        self.centralwidget = QWidget(GuitarCogModerator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName(u"page_welcome")
        self.stackedWidget.addWidget(self.page_welcome)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        GuitarCogModerator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GuitarCogModerator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 989, 22))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuUsers = QMenu(self.menubar)
        self.menuUsers.setObjectName(u"menuUsers")
        self.menuProfile = QMenu(self.menubar)
        self.menuProfile.setObjectName(u"menuProfile")
        self.menuReports = QMenu(self.menubar)
        self.menuReports.setObjectName(u"menuReports")
        GuitarCogModerator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GuitarCogModerator)
        self.statusbar.setObjectName(u"statusbar")
        GuitarCogModerator.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuUsers.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())
        self.menuView.addAction(self.action_view_all)
        self.menuUsers.addAction(self.action_users_all)
        self.menuUsers.addAction(self.action_users_banned)
        self.menuProfile.addAction(self.actionOpen)
        self.menuProfile.addAction(self.actionLogin)
        self.menuProfile.addAction(self.actionLogout)
        self.menuProfile.addAction(self.actionCreate)
        self.menuReports.addAction(self.action_reports_all)
        self.menuReports.addAction(self.action_reports_new)

        self.retranslateUi(GuitarCogModerator)

        QMetaObject.connectSlotsByName(GuitarCogModerator)
    # setupUi

    def retranslateUi(self, GuitarCogModerator):
        GuitarCogModerator.setWindowTitle(QCoreApplication.translate("GuitarCogModerator", u"MainWindow", None))
        self.action_view_all.setText(QCoreApplication.translate("GuitarCogModerator", u"All", None))
        self.action_view_reported.setText(QCoreApplication.translate("GuitarCogModerator", u"Reported", None))
        self.action_users_all.setText(QCoreApplication.translate("GuitarCogModerator", u"All", None))
        self.action_users_banned.setText(QCoreApplication.translate("GuitarCogModerator", u"Banned", None))
        self.actionOpen.setText(QCoreApplication.translate("GuitarCogModerator", u"Open", None))
        self.actionLogin.setText(QCoreApplication.translate("GuitarCogModerator", u"Login", None))
        self.actionLogout.setText(QCoreApplication.translate("GuitarCogModerator", u"Logout", None))
        self.actionCreate.setText(QCoreApplication.translate("GuitarCogModerator", u"Create", None))
        self.action_reports_all.setText(QCoreApplication.translate("GuitarCogModerator", u"All", None))
        self.action_reports_new.setText(QCoreApplication.translate("GuitarCogModerator", u"New", None))
        self.menuView.setTitle(QCoreApplication.translate("GuitarCogModerator", u"View", None))
        self.menuUsers.setTitle(QCoreApplication.translate("GuitarCogModerator", u"Users", None))
        self.menuProfile.setTitle(QCoreApplication.translate("GuitarCogModerator", u"Profile", None))
        self.menuReports.setTitle(QCoreApplication.translate("GuitarCogModerator", u"Reports", None))
    # retranslateUi

