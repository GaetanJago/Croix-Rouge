# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'programme.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#=====================================================================================================================
import patients
import data
import sys
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Ui_MainWindow(object):
	"""
    Class to load Program management view
    """
	def setupUi(self, MainWindow):
		"""
        Setup to load Program management view
        """
		MainWindow.setObjectName("MainWindow")
		#MainWindow.resize(720, 696)#=====================================================================================================================
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
		self.base.setStyleSheet("QLabel{\n"
	"font: 75 12pt \"MS Shell Dlg 2\";\n"
	"}\n"
	"\n"
	"QWidget#base{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(108, 219, 215, 255), stop:1 rgba(78, 144, 185, 255));\n"
	"border-style: solid;\n"
	"border-color: black;\n"
	"border-width: 2px;\n"
	"}\n"
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
	"\n"
	"")
		self.base.setObjectName("base")
		self.gridLayout_12 = QtWidgets.QGridLayout(self.base)
		self.gridLayout_12.setObjectName("gridLayout_12")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.pushButton_cancel = QtWidgets.QPushButton(self.base)
		self.pushButton_cancel.setObjectName("pushButton_cancel")
		self.horizontalLayout.addWidget(self.pushButton_cancel)
		self.pushButton_save = QtWidgets.QPushButton(self.base)
		self.pushButton_save.setObjectName("pushButton_save")
		self.horizontalLayout.addWidget(self.pushButton_save)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem1)
		self.gridLayout_12.addLayout(self.horizontalLayout, 1, 0, 1, 1)
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_patient = QtWidgets.QLabel(self.base)
		self.label_patient.setObjectName("label_patient")
		self.verticalLayout_3.addWidget(self.label_patient, 0, QtCore.Qt.AlignHCenter)
		self.horizontalWidget_2 = QtWidgets.QWidget(self.base)
		self.horizontalWidget_2.setObjectName("horizontalWidget_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.label_4 = QtWidgets.QLabel(self.horizontalWidget_2)
		self.label_4.setObjectName("label_4")
		self.horizontalLayout_2.addWidget(self.label_4)
		self.comboBox_repos = QtWidgets.QComboBox(self.horizontalWidget_2)
		self.comboBox_repos.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
		self.comboBox_repos.setObjectName("comboBox_repos")
		self.comboBox_repos.addItem("")
		self.horizontalLayout_2.addWidget(self.comboBox_repos)
		self.verticalLayout_3.addWidget(self.horizontalWidget_2, 0, QtCore.Qt.AlignHCenter)
		self.tableWidget_prog = QtWidgets.QTableWidget(self.base)
		self.tableWidget_prog.setObjectName("tableWidget_prog")
		self.tableWidget_prog.setColumnCount(3)
		self.tableWidget_prog.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.tableWidget_prog.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.tableWidget_prog.setHorizontalHeaderItem(1, item)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.tableWidget_prog.setHorizontalHeaderItem(2, item)
		self.tableWidget_prog.horizontalHeader().setStretchLastSection(True)
		self.verticalLayout_3.addWidget(self.tableWidget_prog)
		self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 2, 1, 1)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem2)
		self.pushButton_add = QtWidgets.QPushButton(self.base)
		self.pushButton_add.setObjectName("pushButton_add")
		self.verticalLayout.addWidget(self.pushButton_add)
		self.pushButton_suppr = QtWidgets.QPushButton(self.base)
		self.pushButton_suppr.setObjectName("pushButton_suppr")
		self.verticalLayout.addWidget(self.pushButton_suppr)
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem3)
		self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 1, 1)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(self.base)
		self.label.setObjectName("label")
		self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
		self.comboBox_part = QtWidgets.QComboBox(self.base)
		self.comboBox_part.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
		self.comboBox_part.setObjectName("comboBox_part")
		#self.comboBox_part.addItem("")	#=======================================================================================================================
		self.verticalLayout_2.addWidget(self.comboBox_part)
		self.tableWidget_lib = QtWidgets.QTableWidget(self.base)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tableWidget_lib.sizePolicy().hasHeightForWidth())
		self.tableWidget_lib.setSizePolicy(sizePolicy)
		self.tableWidget_lib.setMinimumSize(QtCore.QSize(150, 0))
		self.tableWidget_lib.setObjectName("tableWidget_lib")
		self.tableWidget_lib.setColumnCount(1)
		self.tableWidget_lib.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		item.setFont(font)
		self.tableWidget_lib.setHorizontalHeaderItem(0, item)
		self.tableWidget_lib.horizontalHeader().setStretchLastSection(True)
		self.verticalLayout_2.addWidget(self.tableWidget_lib)
		self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
		self.gridLayout_12.addLayout(self.gridLayout_2, 0, 0, 1, 1)
		self.tab.addWidget(self.base, 1, 0, 1, 1)
		self.gridLayout.addWidget(self.all, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		#=====================================================================================================================
		#Affectation des boutons
		self.pushButton_save.clicked.connect(lambda : self.back(MainWindow))
		self.pushButton_cancel.clicked.connect(lambda : self.back(MainWindow))

		#Affectation des categories
		cat = data.readAllParts()
		for part in cat:
			self.comboBox_part.addItem(part)

		#adjust column size
		header = self.tableWidget_prog.horizontalHeader()
		header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
		header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

	def back(self,MainWindow):
		"""Method to go to the preious view"""
		ui = patients.Ui_MainWindow()
		ui.setupUi(MainWindow)		
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	def retranslateUi(self, MainWindow):
		"""Method for the retranslation"""
		_translate = QtCore.QCoreApplication.translate
		#MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))#==============================================
		self.label_3.setText(_translate("MainWindow", "Gestion des programmes thérapeuthiques"))
		self.pushButton_cancel.setText(_translate("MainWindow", "Annuler"))
		self.pushButton_save.setText(_translate("MainWindow", "Sauvegarder"))
		self.label_patient.setText(_translate("MainWindow", "Programme de Jean S (78784)"))
		self.label_4.setText(_translate("MainWindow", "Temps de pause"))
		self.comboBox_repos.setItemText(0, _translate("MainWindow", "30s"))
		item = self.tableWidget_prog.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Exercice"))
		item = self.tableWidget_prog.horizontalHeaderItem(1)
		item.setText(_translate("MainWindow", "Nombre de répétitions"))
		item = self.tableWidget_prog.horizontalHeaderItem(2)
		item.setText(_translate("MainWindow", "Vitesse"))
		self.pushButton_add.setText(_translate("MainWindow", ">>"))
		self.pushButton_suppr.setText(_translate("MainWindow", "<<"))
		self.label.setText(_translate("MainWindow", "Choisir un exercice"))
		self.comboBox_part.setItemText(0, _translate("MainWindow", "Partie du corps"))
		item = self.tableWidget_lib.horizontalHeaderItem(0)
		item.setText(_translate("MainWindow", "Bibliothèque"))


if __name__ == "__main__":
	"""Launch program management view"""
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
