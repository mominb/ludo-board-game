from game import Game
import sys


def main():
    game = Game(get_players())
    run_game(game)

def get_players():
    try:
        num_of_players = int(input("How many players? ").strip())
        if num_of_players > 4:
            raise ValueError

    except ValueError:
        sys.exit("Value must be integer ranging from 1 - 4")
    return num_of_players
def run_game(game):
    print

if __name__ == "__main__":
    main()
