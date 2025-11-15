from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton)
from PySide6.QtGui import QIcon
from values import ICON

# CRIA A INTERFACE PRINCIPAL

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(QWidget())
        self._layout = QGridLayout()
        self.centralWidget().setLayout(self._layout)
        self.setWindowTitle('Jogo da Velha')
        self.setWindowIcon(QIcon(str(ICON)))
