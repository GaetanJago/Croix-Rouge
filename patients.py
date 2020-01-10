# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patients.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

#=====================================================================================================================
import menu
import programme
import data
import sys
from data import AppData
from data import Patient

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Ui_MainWindow(object):
    """
    Class to load patient management view
    """
    def setupUi(self, MainWindow):
        """
        Setup to load patient management view
        """
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(904, 696)#=====================================================================================================================
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
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_gestion = QtWidgets.QPushButton(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gestion.sizePolicy().hasHeightForWidth())
        self.pushButton_gestion.setSizePolicy(sizePolicy)
        self.pushButton_gestion.setObjectName("pushButton_gestion")
        self.verticalLayout_2.addWidget(self.pushButton_gestion, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_res = QtWidgets.QPushButton(self.base)
        self.pushButton_res.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_res.sizePolicy().hasHeightForWidth())
        self.pushButton_res.setSizePolicy(sizePolicy)
        self.pushButton_res.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_res.setObjectName("pushButton_res")
        self.verticalLayout_2.addWidget(self.pushButton_res, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_back = QtWidgets.QPushButton(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout_2.addWidget(self.pushButton_back, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(50, 50, 50, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.addWidget = QtWidgets.QWidget(self.base)
        self.addWidget.setMaximumSize(QtCore.QSize(300, 500))
        self.addWidget.setStyleSheet("QWidget#addWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(254, 254, 254, 255), stop:1 rgba(216, 216, 216, 255));\n"
"border-radius : 15px;\n"
"}")
        self.addWidget.setObjectName("addWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.addWidget)
        self.verticalLayout_5.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.addWidget)
        self.label_2.setStyleSheet("\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.addWidget)
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_name = QtWidgets.QLineEdit(self.addWidget)
        self.lineEdit_name.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout_5.addWidget(self.lineEdit_name)
        self.label_8 = QtWidgets.QLabel(self.addWidget)
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.lineEdit_ipp = QtWidgets.QLineEdit(self.addWidget)
        self.lineEdit_ipp.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_ipp.setObjectName("lineEdit_ipp")
        self.verticalLayout_5.addWidget(self.lineEdit_ipp)
        self.pushButton_add = QtWidgets.QPushButton(self.addWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_5.addWidget(self.pushButton_add, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.addWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, 20, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.base)
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tableWidget = QtWidgets.QTableWidget(self.base)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 500))
        self.tableWidget.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_12.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tab.addWidget(self.base, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.all, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
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
        self.pushButton_gestion.clicked.connect(lambda : self.prog(MainWindow))
        self.pushButton_add.clicked.connect(lambda : self.addPatient(self.lineEdit_name.text(),self.lineEdit_ipp.text()))

        #sync data dans le tableau and ajustement des tailles des colonnes
        self.syncData()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

    def addPatient(self,name,ipp):
        """Method to add and save a new patient using the fields"""
        #Confirmation message
        qm = QtWidgets.QMessageBox()
        reply = qm.question(MainWindow, 'Continuer ?','Voulez vraiment ajouter ' + name + "(" + ipp + ") ?", qm.Yes, qm.No)
        if reply == qm.Yes:
            new = data.deserialize()
            new.getListPatient().append(Patient(name , ipp))
            data.seralize(new)
            self.syncData()

            #Clear fields
            self.lineEdit_name.setText("")
            self.lineEdit_ipp.setText("")
    
    def syncData(self):
        """Sync tabView with patients data"""
        self.tableWidget.setRowCount(0) #clean before
        d = data.deserialize()
        i = 0
        for p in d.getListPatient() :
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(p.getName()))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(p.getIpp()))
    
    def back(self,MainWindow):
        """Method to go to the preious view"""
        ui = menu.Ui_MainWindow()
        ui.setupUi(MainWindow)
    def prog(self,MainWindow):
        """Method to change view to manage program of patient"""
        ui = programme.Ui_MainWindow()
        ui.setupUi(MainWindow)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    

    def retranslateUi(self, MainWindow):
        """Method for the retranslation"""
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))#==================================================================
        self.label_3.setText(_translate("MainWindow", "Gestion des programmes thérapeuthiques"))
        self.pushButton_gestion.setText(_translate("MainWindow", "Gestion du programme thérapeuthique"))
        self.pushButton_res.setText(_translate("MainWindow", "Résultat du patient"))
        self.pushButton_back.setText(_translate("MainWindow", "Retour Menu"))
        self.label_2.setText(_translate("MainWindow", "Ajouter un patient"))
        self.label_4.setText(_translate("MainWindow", "Nom"))
        self.label_8.setText(_translate("MainWindow", "Numéro IPP"))
        self.pushButton_add.setText(_translate("MainWindow", "Ajouter"))
        self.label.setText(_translate("MainWindow", "Choisir un patient"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Numéro IPP"))


if __name__ == "__main__":
    """Launch patient management view"""
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
