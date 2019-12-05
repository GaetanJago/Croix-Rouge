# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creeExo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import menu




class Ui_MainWindow(object):

    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(893, 669)
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
        self.textEdit = QtWidgets.QTextEdit(self.verticalWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setTabStopWidth(80)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.label_12 = QtWidgets.QLabel(self.verticalWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_6)
        self.label_6 = QtWidgets.QLabel(self.verticalWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_3.addWidget(self.textEdit_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.gridLayout_8.addWidget(self.verticalWidget, 1, 1, 1, 1)
        self.gridWidget = QtWidgets.QWidget(self.base)
        self.gridWidget.setStyleSheet("border-style: solid;\n"
"border-color: black;\n"
"border-width: 2px;\n"
"border-top-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(111, 111, 111, 255), stop:0.994318 rgba(156, 156, 156, 255));")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_8.addWidget(self.gridWidget, 1, 0, 1, 1)
        self.gridWidget_3 = QtWidgets.QWidget(self.base)
        self.gridWidget_3.setStyleSheet("")
        self.gridWidget_3.setObjectName("gridWidget_3")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridWidget_3)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_7 = QtWidgets.QLabel(self.gridWidget_3)
        self.label_7.setStyleSheet("font: 75 25pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_8.addWidget(self.gridWidget_3, 0, 0, 1, 1)
        self.gridWidget_2 = QtWidgets.QWidget(self.base)
        self.gridWidget_2.setStyleSheet("\n"
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
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem1, 0, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_9.addWidget(self.pushButton_15, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.gridWidget_2, 2, 0, 1, 1)
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

        self.pushButton_6.clicked.connect(self.retour)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Créer un exercice"))
        self.label_5.setText(_translate("MainWindow", "Nom de l\'exercice"))
        self.label_12.setText(_translate("MainWindow", "Partie du corps"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Membre supérieur"))
        self.label_6.setText(_translate("MainWindow", "Description"))
        self.pushButton_4.setText(_translate("MainWindow", "Commencer \n"
" l\'enregistrement"))
        self.pushButton_5.setText(_translate("MainWindow", "Ajouter dans la\n"
" bibliothèque"))
        self.pushButton_6.setText(_translate("MainWindow", "Retour Menu"))
        self.label_7.setText(_translate("MainWindow", "Calibration en cours... Veuillez étirez les bras "))
        self.pushButton_15.setText(_translate("MainWindow", "Rejoué"))

    def retour(self):
        ui = menu.Ui_MainWindow()
        ui.setupUi(MainWindow)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

