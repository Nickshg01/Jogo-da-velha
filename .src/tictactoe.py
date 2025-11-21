from values import (HUMAN_PLAYER, AI_PLAYER)

# LÓGICA BACKEND

class TicTacToe:
    def __init__(self, gui):
        self.board = ['' for _ in range(9)]
        self.ai_turn = False
        self.gui = gui

    def _available_moves(self) -> list:
        '''Retorna quais espaços estão livres.'''
        return [i for i, spot in enumerate(self.board) if spot == '']
    
    def _is_board_full(self) -> bool:
        '''Verifica se o tabuleiro está cheio.'''
        return self._available_moves() == []
    
    def _make_move(self, position: int, player: str) -> bool:
        '''Faz um movimento caso o espaço estiver vazio e retorna True. Caso contrário, retorna False.'''
        if self.board[position] == '':
            self.board[position] = player
            self.gui._updateButtons()
            self.ai_turn = not self.ai_turn
            return True
        return False
    
    def _check_winner(self) -> str | None:
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
        return self._check_winner() is not None or self._is_board_full()
    
    def _minimax(self, depth: int, is_maximizing: bool):
        '''Algoritmo Minimax. Retorna a melhor pontuação possível para o tabuleiro atual.'''
        winner = self._check_winner()

        if winner == AI_PLAYER:
            return 1
        elif winner == HUMAN_PLAYER:
            return -1
        elif self._is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            
            for move in self._available_moves():
                self.board[move] = AI_PLAYER
                score = self._minimax(depth+1, False)
                self.board[move] = ''
                best_score = max(score, best_score)
            return best_score
        
        best_score = float('inf')
        for move in self._available_moves():
            self.board[move] = HUMAN_PLAYER
            score = self._minimax(depth+1, True)
            self.board[move] = ''
            best_score = min(score, best_score)
        return best_score

    def _get_best_move(self) -> int:
        '''Retorna o melhor movimento possível para a IA usando o algoritmo Minimax.'''
        best_score = float('-inf')
        best_move = None

        for move in self._available_moves():
            self.board[move] = AI_PLAYER
            score = self._minimax(0, False)
            self.board[move] = ''

            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play_game(self):
        '''Gerencia o movimento do jogo.'''        
        if not self._game_over():
            if self.ai_turn:
                self._make_move(self._get_best_move(), AI_PLAYER)
            return

        winner = self._check_winner()
        if winner == AI_PLAYER:
            print('Vitória da IA.')
        elif winner == HUMAN_PLAYER:
            # EM TEORIA, IMPOSSÍVEL
            print('Vitória do jogador.')
        else:
            print('Empate.')