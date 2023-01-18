from tic_tac_toe.board import Coord
from tic_tac_toe.colors import Colors

class Player:
    
    def __init__(self, name: str, symbol:str):
        self._name = name
        self._symbol = symbol
        self._points = 0

    def __repr__(self):
        return f"<   Name: {self._name} - Symbol: {self._symbol} - Points: {self._points}   >"

    @property
    def name(self) -> str:
        """
        Return Player name.
        :return:
        """
        return self._name

    @property
    def symbol(self) -> str:
        """
        Return Player symbol eg. X or O
        :return:
        """
        return self._symbol

    @property
    def points(self) -> int:
        """
        Return Player score
        :return: int
        """
        return self._points


    def add_point(self) -> None:
        """
        Add one point to Player
        :return: None
        """
        self._points += 1

    def get_input(self) -> Coord:
        """
        Read user input for X and Y coordinates
        :return: namedtuple Coord(x,y)
        """
        pos_x:int=None
        pos_y:int=None

        while True: # Read X position
            try:
                pos_x = int(input(f'{Colors.lightblue}Enter X position: {Colors.reset}'))
            except ValueError:
                print(f'{Colors.purple}Invalid X value.{Colors.reset}')
            else:
                if pos_x < 1 or pos_x > 3:
                    print(f'{Colors.yellow}X position should be 1, 2 or 3{Colors.reset}')
                else:
                    break

        while True: # Read Y position
            try:
                pos_y = int(input(f'{Colors.lightblue}Enter Y position: {Colors.reset}'))
            except ValueError:
                print(f'{Colors.purple}Invalid Y value.{Colors.reset}')
            else:
                if pos_y < 1 or pos_y > 3:
                    print(f'{Colors.yellow}Y position should be 1, 2 or 3{Colors.reset}')
                else:
                    break
        x = pos_x - 1
        y = pos_y - 1
        return Coord(x, y)
            