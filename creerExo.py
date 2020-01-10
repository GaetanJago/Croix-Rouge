# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creerExo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!




#=====================================================================================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import menu
import data
import cv2
#=====================================================================================================================

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		#MainWindow.resize(893, 669)#=====================================================================================================================
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.all = QtWidgets.QWidget(self.centralwidget)
		self.all.setStyleSheet("QWidget#all{border-radius: 20px;\n"
"blur-raduis:5px;\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"pading:50px;\n"
"}")
		self.all.setObjectName("all")
		self.tab = QtWidgets.QGridLayout(self.all)
		self.tab.setContentsMargins(0, 0, 0, 20)
		self.tab.setSpacing(0)
		self.tab.setObjectName("tab")
		self.head = QtWidgets.QWidget(self.all)
		self.head.setStyleSheet("/*QWidget#head{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(192, 192, 192, 255));\n"
"    border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-radius: 20px;\n"
"}*/")
		self.head.setObjectName("head")
		self.gridLayout_10 = QtWidgets.QGridLayout(self.head)
		self.gridLayout_10.setObjectName("gridLayout_10")
		self.label_3 = QtWidgets.QLabel(self.head)
		self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
		self.label_3.setObjectName("label_3")
		self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
		self.tab.addWidget(self.head, 0, 0, 1, 1)
		self.base = QtWidgets.QWidget(self.all)
		self.base.setStyleSheet("QWidget#base{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(108, 219, 215, 255), stop:1 rgba(78, 144, 185, 255));\n"
"border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"}\n"
"")
		self.base.setObjectName("base")
		self.gridLayout_8 = QtWidgets.QGridLayout(self.base)
		self.gridLayout_8.setObjectName("gridLayout_8")
		self.verticalWidget = QtWidgets.QWidget(self.base)
		self.verticalWidget.setMaximumSize(QtCore.QSize(200, 16777215))
		self.verticalWidget.setStyleSheet("QLabel,QComboBox{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton{font: 12pt \"MS Shell Dlg 2\";}\n"
"\n"
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
		self.verticalWidget.setObjectName("verticalWidget")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_5 = QtWidgets.QLabel(self.verticalWidget)
		self.label_5.setStyleSheet("")
		self.label_5.setObjectName("label_5")
		self.verticalLayout_3.addWidget(self.label_5)
		self.textEdit_name = QtWidgets.QTextEdit(self.verticalWidget)
		self.textEdit_name.setMaximumSize(QtCore.QSize(16777215, 30))
		self.textEdit_name.setTabStopWidth(80)
		self.textEdit_name.setObjectName("textEdit_name")
		self.verticalLayout_3.addWidget(self.textEdit_name)
		self.label_Part = QtWidgets.QLabel(self.verticalWidget)
		self.label_Part.setObjectName("label_Part")
		self.verticalLayout_3.addWidget(self.label_Part)
		self.comboBox_Part = QtWidgets.QComboBox(self.verticalWidget)
		self.comboBox_Part.setObjectName("comboBox_Part")
		#self.comboBox_Part.addItem("")	#=====================================================================================================================
		self.verticalLayout_3.addWidget(self.comboBox_Part)
		self.label_6 = QtWidgets.QLabel(self.verticalWidget)
		self.label_6.setObjectName("label_6")
		self.verticalLayout_3.addWidget(self.label_6)
		self.textEdit_desc = QtWidgets.QTextEdit(self.verticalWidget)
		self.textEdit_desc.setMaximumSize(QtCore.QSize(200, 16777215))
		self.textEdit_desc.setObjectName("textEdit_desc")
		self.verticalLayout_3.addWidget(self.textEdit_desc)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem)
		self.gridLayout_8.addWidget(self.verticalWidget, 1, 1, 1, 1)


		# ------ Modification ------ #
		self.fps = 24
		self.cap = cv2.VideoCapture(0)
		self.cameraWidget = QtWidgets.QLabel(self.base)
		self.cameraWidget.setAlignment(Qt.AlignCenter)
		self.isCapturing = False
		self.ith_frame = 1
		self.start()

		"""
		self.cameraWidget = QtWidgets.QWidget(self.base)
		self.cameraWidget.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-top-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(111, 111, 111, 255), stop:0.994318 rgba(156, 156, 156, 255));")
		"""
		# ------ Modification ------ #

		self.cameraWidget.setObjectName("cameraWidget")
		self.gridLayout_6 = QtWidgets.QGridLayout(self.cameraWidget)
		self.gridLayout_6.setObjectName("gridLayout_6")
		self.gridLayout_8.addWidget(self.cameraWidget, 1, 0, 1, 1)
		self.indicationWidget = QtWidgets.QWidget(self.base)
		self.indicationWidget.setStyleSheet("")
		self.indicationWidget.setObjectName("indicationWidget")
		self.gridLayout_11 = QtWidgets.QGridLayout(self.indicationWidget)
		self.gridLayout_11.setObjectName("gridLayout_11")
		self.label_indication = QtWidgets.QLabel(self.indicationWidget)
		self.label_indication.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
		self.label_indication.setObjectName("label_indication")
		self.gridLayout_11.addWidget(self.label_indication, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
		self.gridLayout_8.addWidget(self.indicationWidget, 0, 0, 1, 1)
		self.rejoueWidget = QtWidgets.QWidget(self.base)
		self.rejoueWidget.setStyleSheet("\n"
"QPushButton{font: 12pt \"MS Shell Dlg 2\";}\n"
"\n"
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
		self.rejoueWidget.setObjectName("rejoueWidget")
		self.gridLayout_9 = QtWidgets.QGridLayout(self.rejoueWidget)
		self.gridLayout_9.setObjectName("gridLayout_9")
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_9.addItem(spacerItem1, 0, 4, 1, 1)
		spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_9.addItem(spacerItem2, 0, 2, 1, 1)
		self.pushButton_replay = QtWidgets.QPushButton(self.rejoueWidget)
		self.pushButton_replay.setObjectName("pushButton_replay")
		self.gridLayout_9.addWidget(self.pushButton_replay, 0, 3, 1, 1)
		self.pushButton_Begin = QtWidgets.QPushButton(self.rejoueWidget)
		self.pushButton_Begin.setObjectName("pushButton_Begin")
		self.gridLayout_9.addWidget(self.pushButton_Begin, 0, 1, 1, 1)
		self.pushButton_add = QtWidgets.QPushButton(self.rejoueWidget)
		self.pushButton_add.setObjectName("pushButton_add")
		self.gridLayout_9.addWidget(self.pushButton_add, 0, 5, 1, 1)
		spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_9.addItem(spacerItem3, 0, 0, 1, 1)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_9.addItem(spacerItem4, 0, 6, 1, 1)
		self.gridLayout_8.addWidget(self.rejoueWidget, 2, 0, 1, 1)
		self.pushButton_back = QtWidgets.QPushButton(self.base)
		self.pushButton_back.setStyleSheet("\n"
"QPushButton{font: 12pt \"MS Shell Dlg 2\";}\n"
"\n"
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
		self.pushButton_back.setObjectName("pushButton_back")
		self.gridLayout_8.addWidget(self.pushButton_back, 2, 1, 1, 1)
		self.tab.addWidget(self.base, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.all, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		#=====================================================================================================================
		#Affectation des boutons
		self.pushButton_back.clicked.connect(lambda : self.back(MainWindow))

		#Affectation catégories
		cat = data.readAllParts()
		for part in cat:
			self.comboBox_Part.addItem(part)
			
		#=====================================================================================================================

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		#MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))#=====================================================================================================================
		self.label_3.setText(_translate("MainWindow", "Créer un exercice"))
		self.label_5.setText(_translate("MainWindow", "Nom de l\'exercice"))
		self.label_Part.setText(_translate("MainWindow", "Partie du corps"))
		#self.comboBox_Part.setItemText(0, _translate("MainWindow", "Membre supérieur"))
		self.label_6.setText(_translate("MainWindow", "Description"))
		self.label_indication.setText(_translate("MainWindow", "Prêt à la capture "))
		self.pushButton_replay.setText(_translate("MainWindow", "Rejouer"))
		self.pushButton_Begin.setText(_translate("MainWindow", "Commencer \n"
		" l\'enregistrement"))
		self.pushButton_add.setText(_translate("MainWindow", "Ajouter dans la\n"
		" bibliothèque"))
		self.pushButton_back.setText(_translate("MainWindow", "Retour Menu"))


	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	def back(self,MainWindow):
		ui = menu.Ui_MainWindow()
		ui.setupUi(MainWindow)
		self.timer.stop()
		self.cap.release()
	
	def setFPS(self, fps):
		self.fps = fps

	def nextFrameSlot(self):
		ret, frame = self.cap.read()

		# ------ Modification ------ #
		# Save images if isCapturing
		if self.isCapturing:
			cv2.imwrite('img_%05d.jpg'%self.ith_frame, frame)
			self.ith_frame += 1
		# ------ Modification ------ #

		# My webcam yields frames in BGR format
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
		pix = QPixmap.fromImage(img)
		self.cameraWidget.setPixmap(pix)

	def start(self):
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.nextFrameSlot)
		self.timer.start((1000 / self.fps))
		
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
	
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
