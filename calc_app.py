from test import *

import sys

class CalcApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        # direct the signal to a method of the app class
        self.pushButton_2.clicked.connect(self.clickMe)
        #self.pushButton_2.connect(self.clickMe)
        self.pushButton_17.clicked.connect(self.clearMe)
        #self.pushButton.clicked.connect(self.showName)

    def clickMe(self):
        self.lcdNumber.setProperty("value", 1.0)
        print('1')

    def clearMe(self):
        self.lcdNumber.setProperty("value", 0.0)
        print('Cleared')

    def showName(self):
        pass

    
# Create an app
app = QtWidgets.QApplication(sys.argv)
# Create a window
MainWindow = QtWidgets.QMainWindow()

# Create an instance of the app
ui = CalcApp(MainWindow)

# show the window and start the app
MainWindow.show()
app.exec_()