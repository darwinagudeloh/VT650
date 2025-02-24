# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guioeMTrk.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        self.action25_Hz = QAction(MainWindow)
        self.action25_Hz.setObjectName(u"action25_Hz")
        self.action25_Hz.setCheckable(True)
        self.action50_Hz = QAction(MainWindow)
        self.action50_Hz.setObjectName(u"action50_Hz")
        self.action50_Hz.setCheckable(True)
        self.action150_Hz = QAction(MainWindow)
        self.action150_Hz.setObjectName(u"action150_Hz")
        self.action150_Hz.setCheckable(True)
        self.action200_Hz = QAction(MainWindow)
        self.action200_Hz.setObjectName(u"action200_Hz")
        self.action200_Hz.setCheckable(True)
        self.action100_Hz = QAction(MainWindow)
        self.action100_Hz.setObjectName(u"action100_Hz")
        self.action100_Hz.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 515, 40))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cbserial = QComboBox(self.frame)
        self.cbserial.setObjectName(u"cbserial")
        self.cbserial.setGeometry(QRect(75, 8, 160, 24))
        self.lserial = QLabel(self.frame)
        self.lserial.setObjectName(u"lserial")
        self.lserial.setGeometry(QRect(10, 10, 70, 20))
        self.bconfig = QPushButton(self.frame)
        self.bconfig.setObjectName(u"bconfig")
        self.bconfig.setGeometry(QRect(245, 8, 80, 24))
        self.bstart = QPushButton(self.frame)
        self.bstart.setObjectName(u"bstart")
        self.bstart.setEnabled(False)
        self.bstart.setGeometry(QRect(335, 8, 80, 24))
        self.bstop = QPushButton(self.frame)
        self.bstop.setObjectName(u"bstop")
        self.bstop.setEnabled(False)
        self.bstop.setGeometry(QRect(425, 8, 80, 24))
        self.bstop.setAutoDefault(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 515, 40))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 8, 501, 27))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.lpressure = QLabel(self.layoutWidget)
        self.lpressure.setObjectName(u"lpressure")

        self.gridLayout.addWidget(self.lpressure, 0, 0, 1, 1)

        self.lepression = QLineEdit(self.layoutWidget)
        self.lepression.setObjectName(u"lepression")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lepression.sizePolicy().hasHeightForWidth())
        self.lepression.setSizePolicy(sizePolicy)
        self.lepression.setText(u"")
        self.lepression.setFrame(True)
        self.lepression.setReadOnly(True)

        self.gridLayout.addWidget(self.lepression, 0, 1, 1, 1)

        self.lflow = QLabel(self.layoutWidget)
        self.lflow.setObjectName(u"lflow")

        self.gridLayout.addWidget(self.lflow, 0, 2, 1, 1)

        self.leflow = QLineEdit(self.layoutWidget)
        self.leflow.setObjectName(u"leflow")
        sizePolicy.setHeightForWidth(self.leflow.sizePolicy().hasHeightForWidth())
        self.leflow.setSizePolicy(sizePolicy)
        self.leflow.setReadOnly(True)

        self.gridLayout.addWidget(self.leflow, 0, 3, 1, 1)

        self.lvolume = QLabel(self.layoutWidget)
        self.lvolume.setObjectName(u"lvolume")

        self.gridLayout.addWidget(self.lvolume, 0, 4, 1, 1)

        self.levol = QLineEdit(self.layoutWidget)
        self.levol.setObjectName(u"levol")
        self.levol.setDragEnabled(False)
        self.levol.setReadOnly(True)

        self.gridLayout.addWidget(self.levol, 0, 5, 1, 1)

        self.gvdata = QGraphicsView(self.centralwidget)
        self.gvdata.setObjectName(u"gvdata")
        self.gvdata.setGeometry(QRect(10, 110, 780, 590))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 710, 780, 40))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.lsfile = QLabel(self.frame_3)
        self.lsfile.setObjectName(u"lsfile")
        self.lsfile.setGeometry(QRect(10, 10, 60, 20))
        self.lefilename = QLineEdit(self.frame_3)
        self.lefilename.setObjectName(u"lefilename")
        self.lefilename.setGeometry(QRect(80, 8, 600, 24))
        sizePolicy.setHeightForWidth(self.lefilename.sizePolicy().hasHeightForWidth())
        self.lefilename.setSizePolicy(sizePolicy)
        self.lefilename.setText(u"")
        self.lefilename.setFrame(True)
        self.lefilename.setReadOnly(True)
        self.bsgrap = QPushButton(self.frame_3)
        self.bsgrap.setObjectName(u"bsgrap")
        self.bsgrap.setEnabled(False)
        self.bsgrap.setGeometry(QRect(690, 8, 80, 24))
        self.gvlogo = QGraphicsView(self.centralwidget)
        self.gvlogo.setObjectName(u"gvlogo")
        self.gvlogo.setGeometry(QRect(535, 10, 255, 90))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 110, 781, 591))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuConfig = QMenu(self.menubar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuSample_rate = QMenu(self.menuConfig)
        self.menuSample_rate.setObjectName(u"menuSample_rate")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuConfig.addSeparator()
        self.menuConfig.addAction(self.menuSample_rate.menuAction())
        self.menuSample_rate.addAction(self.action25_Hz)
        self.menuSample_rate.addAction(self.action50_Hz)
        self.menuSample_rate.addAction(self.action100_Hz)
        self.menuSample_rate.addAction(self.action150_Hz)
        self.menuSample_rate.addAction(self.action200_Hz)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FLUKE\u00ae\ufe0f VT650", None))
        self.action25_Hz.setText(QCoreApplication.translate("MainWindow", u"25 Hz", None))
        self.action50_Hz.setText(QCoreApplication.translate("MainWindow", u"50 Hz", None))
        self.action150_Hz.setText(QCoreApplication.translate("MainWindow", u"150 Hz", None))
        self.action200_Hz.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.action100_Hz.setText(QCoreApplication.translate("MainWindow", u"100 Hz", None))
        self.lserial.setText(QCoreApplication.translate("MainWindow", u"Serial Port:", None))
        self.bconfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.bstart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.bstop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.lpressure.setText(QCoreApplication.translate("MainWindow", u"Pressure:", None))
        self.lflow.setText(QCoreApplication.translate("MainWindow", u"Flow:", None))
        self.lvolume.setText(QCoreApplication.translate("MainWindow", u"Volume:", None))
        self.lsfile.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.bsgrap.setText(QCoreApplication.translate("MainWindow", u"Save graph", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuSample_rate.setTitle(QCoreApplication.translate("MainWindow", u"Sample rate", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

