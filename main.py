from tic_tac_toe import Player
from tic_tac_toe import Game
from tic_tac_toe import Colors

def tic_tac_toe(player1_name:str, player2_name:str) -> None:
    """
    Main game loop
    :param player1_name: Player 1 Name
    :param player2_name: Player 2 Name
    """
    p1: Player = Player(name=f'{Colors.green}{player1_name}{Colors.reset}',
                        symbol=f'{Colors.green}X{Colors.reset}')
    p2: Player = Player(name=f'{Colors.red}{player2_name}{Colors.reset}',
                        symbol=f'{Colors.red}O{Colors.reset}')
    
    game = Game(player_1=p1,
                player_2=p2)
    print(f'\n{Colors.pink}{"*"*20}')
    print(f'*   {Colors.red}Tic {Colors.green} Tac {Colors.orange}Toe   {Colors.pink}*')
    print(f'{"*"*20}{Colors.reset}\n')
    while True: # Game loop
        winner: Player = game.run()
        if winner is not None:
            winner.add_point()
            print(f'\n{Colors.pink}***************************{Colors.reset}\n')
            print(f'{winner.name} Won!')
            print(f'\n{Colors.pink}*********** Socre *********\n{Colors.reset}')
            print(f'{p1.name}: {p1.points}')
            print(f'{p2.name}: {p2.points}')
            print(f'\n{Colors.pink}***************************{Colors.reset}\n')
        else:
            print(f'\n{Colors.pink}***************************{Colors.reset}\n')
            print(f'DRAW')
            print(f'\n{Colors.pink}*********** Socre *********\n{Colors.reset}')
            print(f'{p1.name}: {p1.points}')
            print(f'{p2.name}: {p2.points}')
            print(f'\n{Colors.pink}***************************{Colors.reset}\n')
        if input('Play again? (y/n) ').lower() == 'y':
            game.reset()
        else:
            print('\n\nGame Ended\n\n')
            break
            

if __name__ == '__main__': # Entry Point
    # Change here Player Names
    p1_name = 'Player 1'
    p2_name = 'Player_2'
    tic_tac_toe(player1_name=p1_name,
                player2_name=p2_name)


