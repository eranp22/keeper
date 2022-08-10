import os
import time
import pyautogui
from PyQt6 import QtWidgets, uic
import sys

while True:
    pyautogui.press('volumedown')
    time.sleep(1)
    pyautogui.press('volumeup')
    time.sleep(5)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('keeper.ui', self) # Load the .ui file
        self.show() # Show the GUI


app = QApplication(sys.argv)
window = UI()
app.exec_()
