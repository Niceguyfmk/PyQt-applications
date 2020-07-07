import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        """
        set size and position of window
        win.setGeometry(xpos, ypos, width, height) 
        win.setGeometry(0, 0, width, height)
        ^ window shows up on top left handcorner of screen

        """
        self.setGeometry(200,200, 300, 300) 
        self.setWindowTitle("PyQt Tutorial with Faiz!")
        self.initUI()

    def initUI(self):
        #adding a label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label!")
        self.label.move(50,50)
        
        #adding buttons
        self.buttonA=QtWidgets.QPushButton(self)
        self.buttonA.setText("Click here")
        #connecting button click event with clicked function
        self.buttonA.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You clicked the button")
        self.update()
    
    #to change the size of label to fit any updated text
    def update(self):
        self.label.adjustSize()    


#function to make a button do something on click
def clicked():
    print("clicked")

#main window function
def window():
    #passing the command line arguments to the Qt Application
    app = QApplication(sys.argv)
    #create widget
    win = MyWindow()
    #Make window Visible
    win.show()
    sys.exit(app.exec_())


window()