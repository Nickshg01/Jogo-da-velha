import math
from values import (HUMAN_PLAYER, AI_PLAYER)

# LÓGICA DE PROGRAMAÇÃO

class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)]

    def _avaliable_moves(self) -> list:
        '''Retorna quais espaços estão livres.'''
        return [i for i, spot in enumerate(self.board) if spot == '']
    
    def _make_move(self, position, player) -> bool:
        '''Faz um movimento caso o espaço estiver vazio e retorna True. Caso contrário, retorna False.'''
        if self.board[position] == '':
            self.board[position] = player
            return True
        return False
    
    def _winner_check(self) -> str | None:
        '''Verifica se há um vencedor no jogo. Retorna o vencedor ou None.'''
        # LINHAS
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != '':
                return self.board[i]
        # COLUNAS
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != '':
                return self.board[i]
        # DIAGONAIS
        if self.board[0] == self.board[4] == self.board[8] != '' or self.board[2] == self.board[4] == self.board[6] != '':
            return self.board[4]
        return None
    
    def _game_over(self) -> bool:
        '''Verifica se o jogo encerrou.'''
        return self._winner_check() is not None or self._avaliable_moves() == []
