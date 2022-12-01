import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt
from ui_GuitarCog import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("GuitarCog")
        
if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())