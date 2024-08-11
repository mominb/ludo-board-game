from game import Game
import sys
import inflect

p = inflect.engine()


def main(): ...
def get_num_players():
    number = int(input("How many players? ").strip())


def ask_to_open():
    if game.active_player.pawn_positions_on_board == []:
        pawn_to_open = int(input("which pawn do you want to open? ").strip())
    else:
        open = input("would you like to open a pawn? ").strip().lower()
    if open == "yes":
        pawn_to_open = int(input("which pawn do you want to open? ").strip())
    else

def ask_to_roll(): ...
def run_game(): ...


if __name__ == "__main__":
    main()
