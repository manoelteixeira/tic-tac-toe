from collections import namedtuple
from tic_tac_toe.colors import Colors

# X, Y position
Coord = namedtuple(typename='Coord', field_names=['x','y'])


class Board:
    def __init__(self) -> None:
        self._board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]
    
    
    
    def get_board(self) -> list[list]:
        """
        Return current board in its current state
        :return:
        """
        return self._board
    
    # Mark cell if available
    def mark_cell(self, mark:str, coord:Coord) -> None:
        """
        Mark cell if it is available
        :param mark: player symbol e.g. X or O
        :param coord: namedtuple Coord(x,y)
        :return:
        """
        if self._board[coord.x][coord.y] != ' ': # Check if cell is already marked.
            raise ValueError('Position already Marked')
        self._board[coord.x][coord.y] = mark
        
    # Draw Board
    def draw(self) -> None:
        """
        Draw board in its current state.
        :return:
        """
        print(f'{Colors.orange}\n-=-=-=-=-=-=-=-=-=-=-=-=-\n{Colors.reset}')
        print('       1   2   3  \n')
        print(f'   1   {self._board[0][0]} | {self._board[0][1]} | {self._board[0][2]} ')
        print('      ---|---|--- ')
        print(f'   2   {self._board[1][0]} | {self._board[1][1]} | {self._board[1][2]} ')
        print('      ---|---|--- ')
        print(f'   3   {self._board[2][0]} | {self._board[2][1]} | {self._board[2][2]} ')
        print(f'{Colors.orange}\n-=-=-=-=-=-=-=-=-=-=-=-=-\n{Colors.reset}')

    
    def reset(self) -> None:
        """
        Clear the board.
        :return:
        """
        self._board = [[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']]