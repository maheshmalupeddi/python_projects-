from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from multiplicationFE import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.result.clicked.connect(self.calc)
        self.ui.reset.clicked.connect(self.reset)
    def reset(self):
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.ans.clear()
    def calc(self):
        a = float(self.ui.lineEdit_3.text())
        b = float(self.ui.lineEdit_4.text())
        c = a*b
        self.ui.ans.setText("{}".format(c))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())