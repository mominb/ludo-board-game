from game import Game
import sys
import inflect

p = inflect.engine()


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

    print(f"Player # {game.active_player.number} please roll the dice")
    while game.dice.can_roll() and not game.dice.voided():
        _ = input("press Enter to roll").strip()

        num = game.dice.roll()
        print(f"You rolled a {p.number_to_words(num)} !!!")
    if

if __name__ == "__main__":
    main()
