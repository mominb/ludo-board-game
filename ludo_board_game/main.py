from game import Game
import sys
import inflect

p = inflect.engine()


def main():

    input("Press Enter to start game. To quit a game, press 'ctrl + D' ")
    game = Game(get_num_players())


def get_num_players():
    number = int(input("How many players? ").strip())
    return number


def ask_to_open():
    if game.active_player.pawn_positions_on_board == []:
        pawn_to_open = int(input("which pawn do you want to open? ").strip())
        game.active_player.pawns[pawn_to_open - 1].position = 1
    else:
        open = input("would you like to open a pawn? ").strip().lower()
    if open == "yes":
        pawn_to_open = int(input("which pawn do you want to open? ").strip())
        game.active_player.pawns[pawn_to_open - 1].position = 1


def ask_to_roll(): ...
def run_game(): ...


if __name__ == "__main__":
    main()
