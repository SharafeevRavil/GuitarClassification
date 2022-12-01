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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew_from_audio_file = QAction(MainWindow)
        self.actionNew_from_audio_file.setObjectName(u"actionNew_from_audio_file")
        self.actionNew_from_real_time = QAction(MainWindow)
        self.actionNew_from_real_time.setObjectName(u"actionNew_from_real_time")
        self.actionLocal = QAction(MainWindow)
        self.actionLocal.setObjectName(u"actionLocal")
        self.actionOwned = QAction(MainWindow)
        self.actionOwned.setObjectName(u"actionOwned")
        self.actionGlobal = QAction(MainWindow)
        self.actionGlobal.setObjectName(u"actionGlobal")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionLogin = QAction(MainWindow)
        self.actionLogin.setObjectName(u"actionLogin")
        self.actionRegister = QAction(MainWindow)
        self.actionRegister.setObjectName(u"actionRegister")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionAll = QAction(MainWindow)
        self.actionAll.setObjectName(u"actionAll")
        self.actionBanned = QAction(MainWindow)
        self.actionBanned.setObjectName(u"actionBanned")
        self.actionLogin_2 = QAction(MainWindow)
        self.actionLogin_2.setObjectName(u"actionLogin_2")
        self.actionLogout_2 = QAction(MainWindow)
        self.actionLogout_2.setObjectName(u"actionLogout_2")
        self.actionLogout_3 = QAction(MainWindow)
        self.actionLogout_3.setObjectName(u"actionLogout_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(220, 70, 391, 311))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuUsers = QMenu(self.menubar)
        self.menuUsers.setObjectName(u"menuUsers")
        self.menuProfile = QMenu(self.menubar)
        self.menuProfile.setObjectName(u"menuProfile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuUsers.menuAction())
        self.menubar.addAction(self.menuProfile.menuAction())
        self.menuView.addAction(self.actionLocal)
        self.menuView.addAction(self.actionOwned)
        self.menuUsers.addAction(self.actionAll)
        self.menuUsers.addAction(self.actionBanned)
        self.menuProfile.addAction(self.actionLogin_2)
        self.menuProfile.addAction(self.actionLogout_2)
        self.menuProfile.addAction(self.actionLogout_3)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_from_audio_file.setText(QCoreApplication.translate("MainWindow", u"New from audio file", None))
        self.actionNew_from_real_time.setText(QCoreApplication.translate("MainWindow", u"New from real time", None))
        self.actionLocal.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.actionOwned.setText(QCoreApplication.translate("MainWindow", u"Repoted", None))
        self.actionGlobal.setText(QCoreApplication.translate("MainWindow", u"Global", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.actionRegister.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionAll.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.actionBanned.setText(QCoreApplication.translate("MainWindow", u"Banned", None))
        self.actionLogin_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionLogout_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.actionLogout_3.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:8pt; font-weight:600; color:#666666;\">Welcome</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Helvetica'; font-size:8pt; color:#666666;\">Dori me Interimo, adapare Dori me Ameno, Ameno Latire Latirem"
                        "o Dori me Ameno Omenare imperavi ameno Dimere, dimere matiro Matiremo Ameno Omenare imperavi emulari, ameno Omenare imperavi emulari, ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me am Ameno Omenare imperavi ameno Dimere dimere matiro Matiremo Ameno Omenare imperavi emulari, ameno Omenare imperavi emulari, ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me Ameno dori me Ameno dori me Dori me (dori me, dori me, dori me) (Dori me, dori me, dori me) Ameno Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me Ameno dori me Dori me dom Ameno dore Ameno dori me Ameno dori me Ameno dom Dori me reo Ameno dori me</span></p></body></html>", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuUsers.setTitle(QCoreApplication.translate("MainWindow", u"Users", None))
        self.menuProfile.setTitle(QCoreApplication.translate("MainWindow", u"Profile", None))
    # retranslateUi

