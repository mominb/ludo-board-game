from game import Game
import sys


def main():
    print(get_info())


def get_info():
    try:
        num_of_players = int(input('How many players? ').strip())
        if num_of_players > 4:
            raise ValueError

    except ValueError:
        sys.exit('Value must be integer ranging from 1 - 4')
    return num_of_players


if __name__ == '__main__':
    main()
