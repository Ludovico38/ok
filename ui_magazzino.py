# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'magazzino.ui'
#
# Created: Mon Jun  1 19:49:06 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 456)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/magazzino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.scaffLineEdit = QtGui.QLineEdit(self.tab)
        self.scaffLineEdit.setObjectName("scaffLineEdit")
        self.horizontalLayout.addWidget(self.scaffLineEdit)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addscaffPushButton = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/add2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addscaffPushButton.setIcon(icon1)
        self.addscaffPushButton.setObjectName("addscaffPushButton")
        self.horizontalLayout_4.addWidget(self.addscaffPushButton)
        self.delscaffPushButton = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delscaffPushButton.setIcon(icon2)
        self.delscaffPushButton.setObjectName("delscaffPushButton")
        self.horizontalLayout_4.addWidget(self.delscaffPushButton)
        self.scaffFirstPushButton = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaffFirstPushButton.setIcon(icon3)
        self.scaffFirstPushButton.setObjectName("scaffFirstPushButton")
        self.horizontalLayout_4.addWidget(self.scaffFirstPushButton)
        self.scaffPrevPushButton = QtGui.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaffPrevPushButton.setIcon(icon4)
        self.scaffPrevPushButton.setObjectName("scaffPrevPushButton")
        self.horizontalLayout_4.addWidget(self.scaffPrevPushButton)
        self.scaffNextPushButton = QtGui.QPushButton(self.tab)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaffNextPushButton.setIcon(icon5)
        self.scaffNextPushButton.setObjectName("scaffNextPushButton")
        self.horizontalLayout_4.addWidget(self.scaffNextPushButton)
        self.scaffLastPushButton = QtGui.QPushButton(self.tab)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/last.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaffLastPushButton.setIcon(icon6)
        self.scaffLastPushButton.setObjectName("scaffLastPushButton")
        self.horizontalLayout_4.addWidget(self.scaffLastPushButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(33, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.sTableView = QtGui.QTableView(self.tab)
        self.sTableView.setObjectName("sTableView")
        self.gridLayout_4.addWidget(self.sTableView, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.adddettPushButton = QtGui.QPushButton(self.tab)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adddettPushButton.setIcon(icon7)
        self.adddettPushButton.setObjectName("adddettPushButton")
        self.horizontalLayout_3.addWidget(self.adddettPushButton)
        self.deldettPushButton = QtGui.QPushButton(self.tab)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deldettPushButton.setIcon(icon8)
        self.deldettPushButton.setObjectName("deldettPushButton")
        self.horizontalLayout_3.addWidget(self.deldettPushButton)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(295, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.findLineEdit = QtGui.QLineEdit(self.tab_2)
        self.findLineEdit.setMinimumSize(QtCore.QSize(178, 0))
        self.findLineEdit.setObjectName("findLineEdit")
        self.horizontalLayout_6.addWidget(self.findLineEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.findPushButton = QtGui.QPushButton(self.tab_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.findPushButton.setIcon(icon9)
        self.findPushButton.setObjectName("findPushButton")
        self.horizontalLayout_2.addWidget(self.findPushButton)
        self.gSearchPushButton = QtGui.QPushButton(self.tab_2)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gSearchPushButton.setIcon(icon10)
        self.gSearchPushButton.setObjectName("gSearchPushButton")
        self.horizontalLayout_2.addWidget(self.gSearchPushButton)
        self.createFilterPushButton = QtGui.QPushButton(self.tab_2)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.createFilterPushButton.setIcon(icon11)
        self.createFilterPushButton.setObjectName("createFilterPushButton")
        self.horizontalLayout_2.addWidget(self.createFilterPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.fTableView = QtGui.QTableView(self.tab_2)
        self.fTableView.setObjectName("fTableView")
        self.gridLayout_3.addWidget(self.fTableView, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.prtTitleLineEdit = QtGui.QLineEdit(self.tab_4)
        self.prtTitleLineEdit.setObjectName("prtTitleLineEdit")
        self.horizontalLayout_7.addWidget(self.prtTitleLineEdit)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.prtDateLineEdit = QtGui.QLineEdit(self.tab_4)
        self.prtDateLineEdit.setObjectName("prtDateLineEdit")
        self.horizontalLayout_8.addWidget(self.prtDateLineEdit)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(214, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 1, 1, 1)
        self.printPushButton = QtGui.QPushButton(self.tab_4)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/fileprint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printPushButton.setIcon(icon12)
        self.printPushButton.setObjectName("printPushButton")
        self.gridLayout_5.addWidget(self.printPushButton, 1, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 276, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem3, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.saveWinPosCheckBox = QtGui.QCheckBox(self.tab_3)
        self.saveWinPosCheckBox.setObjectName("saveWinPosCheckBox")
        self.gridLayout_2.addWidget(self.saveWinPosCheckBox, 0, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(348, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 2, 1)
        self.saveTableGeometryCheckBox = QtGui.QCheckBox(self.tab_3)
        self.saveTableGeometryCheckBox.setObjectName("saveTableGeometryCheckBox")
        self.gridLayout_2.addWidget(self.saveTableGeometryCheckBox, 1, 0, 1, 2)
        spacerItem5 = QtGui.QSpacerItem(20, 229, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 23))
        self.menubar.setObjectName("menubar")
        self.menuF_ile = QtGui.QMenu(self.menubar)
        self.menuF_ile.setObjectName("menuF_ile")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New_File = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/filenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New_File.setIcon(icon13)
        self.action_New_File.setObjectName("action_New_File")
        self.action_Load_File = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Load_File.setIcon(icon14)
        self.action_Load_File.setObjectName("action_Load_File")
        self.action_Save_database = QtGui.QAction(MainWindow)
        self.action_Save_database.setObjectName("action_Save_database")
        self.actionA_bout = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionA_bout.setIcon(icon15)
        self.actionA_bout.setObjectName("actionA_bout")
        self.actionE_xit = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionE_xit.setIcon(icon16)
        self.actionE_xit.setIconVisibleInMenu(True)
        self.actionE_xit.setObjectName("actionE_xit")
        self.menuF_ile.addAction(self.action_New_File)
        self.menuF_ile.addSeparator()
        self.menuF_ile.addAction(self.action_Load_File)
        self.menuF_ile.addAction(self.actionE_xit)
        self.menu_Help.addAction(self.actionA_bout)
        self.menubar.addAction(self.menuF_ile.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label.setBuddy(self.scaffLineEdit)
        self.label_2.setBuddy(self.findLineEdit)
        self.label_3.setBuddy(self.prtTitleLineEdit)
        self.label_4.setBuddy(self.prtDateLineEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionE_xit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gestione Magazzino", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "&Scaffale:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "&Add/Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "&Cerca:", None, QtGui.QApplication.UnicodeUTF8))
        self.findPushButton.setText(QtGui.QApplication.translate("MainWindow", "Appl&yFlt", None, QtGui.QApplication.UnicodeUTF8))
        self.gSearchPushButton.setText(QtGui.QApplication.translate("MainWindow", "&GlobalFind", None, QtGui.QApplication.UnicodeUTF8))
        self.createFilterPushButton.setText(QtGui.QApplication.translate("MainWindow", "&CreateFlt", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Titolo:", None, QtGui.QApplication.UnicodeUTF8))
        self.prtTitleLineEdit.setText(QtGui.QApplication.translate("MainWindow", "Situazione Magazzino TIME di Stefano Zamprogno anno 2008", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.prtDateLineEdit.setText(QtGui.QApplication.translate("MainWindow", "31/12/2008", None, QtGui.QApplication.UnicodeUTF8))
        self.printPushButton.setText(QtGui.QApplication.translate("MainWindow", "P&rint", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "&Print", None, QtGui.QApplication.UnicodeUTF8))
        self.saveWinPosCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Store Window position", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTableGeometryCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Save Tables Geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuF_ile.setTitle(QtGui.QApplication.translate("MainWindow", "F&ile", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New_File.setText(QtGui.QApplication.translate("MainWindow", "&New database", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Load_File.setText(QtGui.QApplication.translate("MainWindow", "&Load database", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save_database.setText(QtGui.QApplication.translate("MainWindow", "&Save database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_bout.setText(QtGui.QApplication.translate("MainWindow", "A&bout", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_bout.setToolTip(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_bout.setStatusTip(QtGui.QApplication.translate("MainWindow", "About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionE_xit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
