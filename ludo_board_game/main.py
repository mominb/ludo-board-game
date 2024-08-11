from game import Game
import sys
import inflect

p = inflect.engine()


def main():
    game = Game(get_num_players())
    input("Press Enter to start game.\n")
    run_game(game)


def get_num_players():
    number = int(input("How many players? \n").strip())
    return number


def ask_to_open(game):
    if game.dice.can_open_pawn()

def roll(game):
    while game.dice.can_roll() and not game.dice.voided():
        input("\033[33mpress Enter to roll dice\033[0m\n")
        num = game.dice.roll()
        print(f"\033[32mYou rolled a {p.number_to_words(num)} !!!\033[0m\n")
    if game.dice.voided():
        print("\033[31mSorry your turn is voided 😔\033[0m\n\n\n")
        game.dice.reset()
        game.change_turn_voided()
        new_turn(game)
    else:
        ask_to_open(game)


def run_game(game):
    print(f"\033[33mPLAYER # {p.number_to_words(
        game.active_player.number).upper()}'S TURN\033[0m\n")
    roll(game)
    ask_to_open(game)


def new_turn(game):
    run_game(game)


if __name__ == "__main__":
    main()
