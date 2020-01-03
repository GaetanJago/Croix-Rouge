# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#=====================================================================================================================
import creerExo
import bibliotheque
import patients
import os
import ctypes
import data
from data import AppData
from data import Patient
#=====================================================================================================================

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1200, 650)		#=====================================================================================================================
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.carre = QtWidgets.QWidget(self.centralwidget)
		self.carre.setAcceptDrops(False)
		self.carre.setStyleSheet("QWidget#carre{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(108, 219, 215, 255), stop:1 rgba(78, 144, 185, 255));\n"
"border-radius: 20px;\n"
"blur-raduis:5px;\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
" }\n"
"\n"
"QPushButton{font: 12pt \"MS Shell Dlg 2\";}\n"
"\n"
"\n"
"\n"
"\n"
"")
		self.carre.setObjectName("carre")
		self.gridLayout_5 = QtWidgets.QGridLayout(self.carre)
		self.gridLayout_5.setContentsMargins(40, 20, 40, 20)
		self.gridLayout_5.setObjectName("gridLayout_5")
		self.label_2 = QtWidgets.QLabel(self.carre)
		self.label_2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";\n"
"font-weight:bold;\n"
"")
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
		self.verticalFrame = QtWidgets.QFrame(self.carre)
		self.verticalFrame.setStyleSheet("QFrame{padding-left: 30px;\n"
"padding-right: 30px;\n"
"padding-bottom:10px;}\n"
"QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(153, 153, 153, 255));\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"padding : 8px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(157, 195, 255);\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"padding : 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(0, 85, 127);\n"
"border-width: 2px;\n"
"}\n"
"")
		self.verticalFrame.setObjectName("verticalFrame")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
		self.verticalLayout.setObjectName("verticalLayout")
		self.pushButton_creer = QtWidgets.QPushButton(self.verticalFrame)
		self.pushButton_creer.setObjectName("pushButton_creer")
		self.verticalLayout.addWidget(self.pushButton_creer)
		self.pushButton_lib = QtWidgets.QPushButton(self.verticalFrame)
		self.pushButton_lib.setObjectName("pushButton_lib")
		self.verticalLayout.addWidget(self.pushButton_lib)
		self.pushButton_gestion = QtWidgets.QPushButton(self.verticalFrame)
		self.pushButton_gestion.setObjectName("pushButton_gestion")
		self.verticalLayout.addWidget(self.pushButton_gestion)
		self.gridLayout_5.addWidget(self.verticalFrame, 2, 0, 1, 1)
		self.gridLayout.addWidget(self.carre, 0, 1, 1, 1)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setMinimumSize(QtCore.QSize(100, 50))
		self.label.setMaximumSize(QtCore.QSize(600, 300))
		self.label.setStyleSheet("")
		self.label.setText("")
		
		scriptDir = os.path.dirname(os.path.realpath(__file__))	
		self.label.setPixmap(QtGui.QPixmap(scriptDir + os.path.sep + 'images' + os.path.sep +'croix.png'))

		self.label.setScaledContents(False)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setWordWrap(False)
		self.label.setObjectName("label")
		self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem4, 2, 0, 1, 1)
		spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem5, 2, 2, 1, 1)
		spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem7, 1, 0, 1, 1)
		self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
		#=====================================================================================================================
		#Affectation des boutons
		def creer(self):
			ui = creerExo.Ui_MainWindow()
			ui.setupUi(MainWindow)
		def lib(self):
			ui = bibliotheque.Ui_MainWindow()
			ui.setupUi(MainWindow)
		def gestion(self):
			ui = patients.Ui_MainWindow()
			ui.setupUi(MainWindow)
		self.pushButton_creer.clicked.connect(creer)
		self.pushButton_gestion.clicked.connect(gestion)
		self.pushButton_lib.clicked.connect(lib)
		#=====================================================================================================================

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Application Croix Rouge"))
		self.label_2.setText(_translate("MainWindow", "Menu Principal"))
		self.pushButton_creer.setText(_translate("MainWindow", "Créer un exercice"))
		self.pushButton_lib.setText(_translate("MainWindow", "Bibliothèque d\'exercices"))
		self.pushButton_gestion.setText(_translate("MainWindow", "Gestion des programmes\n"
"thérapeuthiques"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)

	#=====================================================================================================================
	# set icon for window and for taskbar
	scriptDir = os.path.dirname(os.path.realpath(__file__))	
	app.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'images' + os.path.sep +'icon.png'))	
	myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	#=====================================================================================================================

	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()#=====================================================================================================================
	sys.exit(app.exec_())