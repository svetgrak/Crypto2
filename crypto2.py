import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog, QTableWidgetItem
from main_window import Ui_mainWindow

class MainWin(QMainWindow):

    def __init__(self):
        super(MainWin,self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

app = QApplication([])
application = MainWin()
application.show()

def msgShow(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

sys.exit(app.exec())
