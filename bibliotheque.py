# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bibliotheque.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#=====================================================================================================================
import menu
import data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Ui_MainWindow(object):
    """
    Class to load a the library of exercices
    """
   
    def setupUi(self, MainWindow):
        """
        Setup of the class that need to be use to load the library window
        """
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(746, 722)#=====================================================================================================================
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
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, 20, 50, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.base)
        self.label.setStyleSheet("font: 90 15pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_5 = QtWidgets.QLabel(self.base)
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.comboBox_membre = QtWidgets.QComboBox(self.base)
        self.comboBox_membre.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_membre.setObjectName("comboBox_membre")
        #self.comboBox_membre.addItem("") #=====================================================================================================================
        self.verticalLayout.addWidget(self.comboBox_membre)
        self.tableWidget_exo = QtWidgets.QTableWidget(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_exo.sizePolicy().hasHeightForWidth())
        self.tableWidget_exo.setSizePolicy(sizePolicy)
        self.tableWidget_exo.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_exo.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.tableWidget_exo.setObjectName("tableWidget_exo")
        self.tableWidget_exo.setColumnCount(1)
        self.tableWidget_exo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_exo.setHorizontalHeaderItem(0, item)
        self.tableWidget_exo.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget_exo)
        self.gridLayout_12.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(50, 50, 50, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.base)
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.gridWidget_camera = QtWidgets.QWidget(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_camera.sizePolicy().hasHeightForWidth())
        self.gridWidget_camera.setSizePolicy(sizePolicy)
        self.gridWidget_camera.setMinimumSize(QtCore.QSize(0, 300))
        self.gridWidget_camera.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(111, 111, 111, 255), stop:0.994318 rgba(156, 156, 156, 255));")
        self.gridWidget_camera.setObjectName("gridWidget_camera")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget_camera)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3.addWidget(self.gridWidget_camera)
        self.pushButton_replay = QtWidgets.QPushButton(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_replay.sizePolicy().hasHeightForWidth())
        self.pushButton_replay.setSizePolicy(sizePolicy)
        self.pushButton_replay.setObjectName("pushButton_replay")
        self.verticalLayout_3.addWidget(self.pushButton_replay, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, 50, 50, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.base)
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.textEdit_desc = QtWidgets.QTextEdit(self.base)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_desc.sizePolicy().hasHeightForWidth())
        self.textEdit_desc.setSizePolicy(sizePolicy)
        self.textEdit_desc.setMinimumSize(QtCore.QSize(0, 400))
        self.textEdit_desc.setMaximumSize(QtCore.QSize(200, 16777215))
        self.textEdit_desc.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit_desc.setObjectName("textEdit_desc")
        self.verticalLayout_5.addWidget(self.textEdit_desc)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.pushButton_suppr = QtWidgets.QPushButton(self.base)
        self.pushButton_suppr.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_suppr.sizePolicy().hasHeightForWidth())
        self.pushButton_suppr.setSizePolicy(sizePolicy)
        self.pushButton_suppr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_suppr.setObjectName("pushButton_suppr")
        self.gridLayout_2.addWidget(self.pushButton_suppr, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_back = QtWidgets.QPushButton(self.base)
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout_2.addWidget(self.pushButton_back, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.tab.addWidget(self.base, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.all, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
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
            self.comboBox_membre.addItem(part)
    
    def back(self,MainWindow):
        """Function to go to the previous view"""
        ui = menu.Ui_MainWindow()
        ui.setupUi(MainWindow)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    def retranslateUi(self, MainWindow):
        """
        Define retranslation
        """
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))#=====================================================================================================================
        self.label_3.setText(_translate("MainWindow", "Bibliothèque"))
        self.label.setText(_translate("MainWindow", "Selectionner un exercice"))
        self.label_5.setText(_translate("MainWindow", "Partie du corps"))
        #self.comboBox_membre.setItemText(0, _translate("MainWindow", "Membre supérieur")) #=====================================================================================================================
        item = self.tableWidget_exo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Exercice"))
        self.label_2.setText(_translate("MainWindow", "Séquence vidéo"))
        self.pushButton_replay.setText(_translate("MainWindow", "Rejouer"))
        self.label_4.setText(_translate("MainWindow", "Description"))
        self.pushButton_suppr.setText(_translate("MainWindow", "Supprimer exercice"))
        self.pushButton_back.setText(_translate("MainWindow", "Retour Menu"))


if __name__ == "__main__":
    """Load a library view"""
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
