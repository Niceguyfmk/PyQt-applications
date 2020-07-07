from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    #passing the command line arguments to the Qt Application
    app = QApplication(sys.argv)
    #create widget
    win = QMainWindow()
    #set size and position of window
    #win.setGeometry(xpos, ypos, width, height) 
    #win.setGeometry(0, 0, width, height)
    # ^ window shows up on top left handcorner of screen
    win.setGeometry(200, 200, 300, 300) 
    win.setWindowTitle("PyQt Tutorial with Faiz!")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    
    #Make window Visible
    win.show()
    sys.exit(app.exec_())


window()