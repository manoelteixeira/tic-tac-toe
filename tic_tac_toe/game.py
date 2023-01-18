from random import seed
from random import choice

from tic_tac_toe.board import Board
from tic_tac_toe.board import Coord
from tic_tac_toe.player import Player
from tic_tac_toe.colors import Colors

class Game:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.board = Board()
        self.rounds = 0
        self.player_1 = player_1
        self.player_2 = player_2
        
    
    def _check_game(self) -> bool:
        """
        Check if any winning condition was met
        :return: True if winning condition is present or False otherwise.
        """
        winning_conditions: list = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], # Vertical Check
                                    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], # Horizontal Check
                                    [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]] # Diagonal Check

        current_board = self.board.get_board()
        for condition in winning_conditions:
            cell_1 = current_board[condition[0][0]][condition[0][1]]
            cell_2 = current_board[condition[1][0]][condition[1][1]]
            cell_3 = current_board[condition[2][0]][condition[2][1]]

            if cell_1 == cell_2 == cell_3 != ' ':  # Check to see if cells are marked with the same value.
                return True  # Winning condition was met
        return False  # Winning condition was not met
        
    def reset(self) -> None:
        """
        Reset Game variables
        """
        self.rounds = 0
        self.board.reset()
    

    def run(self) -> Player:
        """
        Run until winning conditions is meet or the board is filled.
        :return: Winner Player or None in case of a draw
        """
        seed()
        current_player = choice([self.player_1, self.player_2]) # Randomize which player makes the first move
        self.board.draw()
        while True:
            print(f"\nIt's {current_player.name} time to play.\n")
            move: Coord = current_player.get_input()
            try:
                self.board.mark_cell(mark=current_player.symbol,
                                     coord=move)
            except ValueError as err:
                print(f'\n{Colors.purple}{err}{Colors.reset}\n')
            else:
                self.board.draw()
                if self.rounds >= 4 and self._check_game(): # Check if current player move won the game
                    return current_player
                if self.rounds == 8: # Draw condition
                    return None
                if current_player == self.player_1:
                    current_player = self.player_2
                else:
                    current_player = self.player_1
                self.rounds += 1