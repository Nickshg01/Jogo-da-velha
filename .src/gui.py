from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton)
from PySide6.QtGui import QIcon
from values import (ICON, BUTTON_SIZE, BIG_FONT_SIZE, HUMAN_PLAYER)
from tictactoe import TicTacToe

# CRIA A INTERFACE PRINCIPAL

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game = TicTacToe()
        self._layout = QGridLayout()
        self._buttons = []

        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self._layout)
        self.setWindowTitle('Jogo da Velha')
        self.setWindowIcon(QIcon(str(ICON)))

        self._updateButtons()
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

# PADRONIZA OS BOTÕES
    class _Button(QPushButton):
        def __init__(self, text: str = '', i: int = None, window = None):
            super().__init__(text)

            self.mainWindow = window
            self.index = i
            self.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)

            if text == 'X':
                self.setStyleSheet(f'color: red; font-size: {BIG_FONT_SIZE}px')
            elif text == 'O':
                self.setStyleSheet(f'color: blue; font-size: {BIG_FONT_SIZE}px')
            elif text == '':
                self.clicked.connect(lambda: self._player_clicked())

        def _player_clicked(self):
            self.mainWindow.game._make_move(self.index, HUMAN_PLAYER)
            self.mainWindow._updateButtons()

    def _updateButtons(self):
        '''Atualiza os botões do layout.'''
        self._buttons = []
        for i, spot in enumerate(self.game.board):
            self._buttons.append(self._Button(spot, i, self))

        c = 0
        for i in range(3):
            for j in range(3):
                self._layout.addWidget(self._buttons[c], i, j)
                c += 1
