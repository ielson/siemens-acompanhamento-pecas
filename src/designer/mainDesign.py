# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 905)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setToolTip("")
        self.run_button.setObjectName("run_button")
        self.gridLayout.addWidget(self.run_button, 5, 1, 1, 1)
        self.path_button = QtWidgets.QPushButton(self.centralwidget)
        self.path_button.setObjectName("path_button")
        self.gridLayout.addWidget(self.path_button, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.gridLayout.addWidget(self.stop_button, 6, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio1.setObjectName("radio1")
        self.horizontalLayout.addWidget(self.radio1)
        self.radio2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio2.setObjectName("radio2")
        self.horizontalLayout.addWidget(self.radio2)
        self.radio3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio3.setObjectName("radio3")
        self.horizontalLayout.addWidget(self.radio3)
        self.radio4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio4.setObjectName("radio4")
        self.horizontalLayout.addWidget(self.radio4)
        self.radio5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio5.setObjectName("radio5")
        self.horizontalLayout.addWidget(self.radio5)
        self.radio6 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio6.setObjectName("radio6")
        self.horizontalLayout.addWidget(self.radio6)
        self.radio7 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radio7.setObjectName("radio7")
        self.horizontalLayout.addWidget(self.radio7)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)
        self.simulacaoCB = QtWidgets.QCheckBox(self.centralwidget)
        self.simulacaoCB.setObjectName("simulacaoCB")
        self.gridLayout.addWidget(self.simulacaoCB, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(1000, 300, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 32))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Acompanhamento de Peças"))
        self.run_button.setText(_translate("MainWindow", "Iniciar"))
        self.path_button.setText(_translate("MainWindow", "Selecionar Caminho"))
        self.label.setText(_translate("MainWindow", "Acompanhamento de Peças"))
        self.label_3.setText(_translate("MainWindow", "Envio de e-mails"))
        self.label_2.setText(_translate("MainWindow", "Arquivo de Histórico"))
        self.stop_button.setText(_translate("MainWindow", "Cancelar"))
        self.groupBox.setTitle(_translate("MainWindow", "Regional"))
        self.radio1.setText(_translate("MainWindow", "&NOR"))
        self.radio2.setText(_translate("MainWindow", "CAM"))
        self.radio3.setText(_translate("MainWindow", "CEN"))
        self.radio4.setText(_translate("MainWindow", "S&UP"))
        self.radio5.setText(_translate("MainWindow", "RIO"))
        self.radio6.setText(_translate("MainWindow", "SU&L"))
        self.radio7.setText(_translate("MainWindow", "CCC"))
        self.simulacaoCB.setText(_translate("MainWindow", "Sim"))
        self.label_4.setText(_translate("MainWindow", "Simulacao"))
