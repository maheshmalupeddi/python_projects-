# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Multiplication_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 781, 551))
        self.frame.setStyleSheet("background-color: rgb(6, 6, 6);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 40, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 140, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(13, 255, 1);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 210, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(13, 255, 1);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(270, 160, 91, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 220, 91, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 330, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(240, 320, 81, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 781, 551))
        self.frame_2.setStyleSheet("background-color: rgb(6, 6, 6);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(220, 40, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.Avalue = QtWidgets.QLabel(self.frame_2)
        self.Avalue.setGeometry(QtCore.QRect(100, 140, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Avalue.setFont(font)
        self.Avalue.setStyleSheet("color: rgb(13, 255, 1);")
        self.Avalue.setObjectName("Avalue")
        self.Bvalue = QtWidgets.QLabel(self.frame_2)
        self.Bvalue.setGeometry(QtCore.QRect(100, 210, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Bvalue.setFont(font)
        self.Bvalue.setStyleSheet("color: rgb(13, 255, 1);")
        self.Bvalue.setObjectName("Bvalue")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.result = QtWidgets.QPushButton(self.frame_2)
        self.result.setGeometry(QtCore.QRect(110, 330, 93, 28))
        self.result.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.result.setObjectName("result")
        self.ans = QtWidgets.QLabel(self.frame_2)
        self.ans.setGeometry(QtCore.QRect(240, 320, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ans.setFont(font)
        self.ans.setStyleSheet("color: rgb(255, 255, 255);")
        self.ans.setText("")
        self.ans.setObjectName("ans")
        self.reset = QtWidgets.QPushButton(self.frame_2)
        self.reset.setGeometry(QtCore.QRect(110, 390, 93, 28))
        self.reset.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.reset.setObjectName("reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Multiplication App"))
        self.label_2.setText(_translate("MainWindow", "Enter A Value:"))
        self.label_3.setText(_translate("MainWindow", "Enter B Value:"))
        self.pushButton.setText(_translate("MainWindow", "Result"))
        self.label_5.setText(_translate("MainWindow", "Multiplication App"))
        self.Avalue.setText(_translate("MainWindow", "Enter A Value:"))
        self.Bvalue.setText(_translate("MainWindow", "Enter B Value:"))
        self.result.setText(_translate("MainWindow", "Result"))
        self.reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
