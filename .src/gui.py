from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton)
from PySide6.QtGui import QIcon
from values import (ICON, BUTTON_SIZE, BIG_FONT_SIZE)

# CRIA A INTERFACE PRINCIPAL

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(QWidget())
        self._layout = QGridLayout()
        self.centralWidget().setLayout(self._layout)
        self.setWindowTitle('Jogo da Velha')
        self.setWindowIcon(QIcon(str(ICON)))

        self._addButtons()
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

# PADRONIZA OS BOTÕES
    class Button(QPushButton):
        def __init__(self, text: str = ''):
            super().__init__(text)
            
            self.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
            if text == 'X':
                self.setStyleSheet(f'color: red; font-size: {BIG_FONT_SIZE}px')
            elif text == 'O':
                self.setStyleSheet(f'color: blue; font-size: {BIG_FONT_SIZE}px')

# ADICIONA OS BOTÕES AO LAYOUT
    def _addButtons(self):
        for i in range(3):
            for j in range(3):
                self._layout.addWidget(self.Button(), i, j)
