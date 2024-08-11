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

    if game.active_player.pawn_positions_on_board == []:
        pawn_to_open = int(input("which pawn do you want to open? \n").strip())
        game.active_player.pawns[pawn_to_open - 1].position = 1
    else:
        open = input("would you like to open a pawn? \n").strip().lower()
    if open == "yes":
        pawn_to_open = int(input("which pawn do you want to open? \n").strip())
        game.active_player.pawns[pawn_to_open - 1].position = 1





def roll(game):
    while game.dice.can_roll() and not game.dice.voided():
        _ = input("press Enter to roll dice\n").strip()

        num = game.dice.roll()
        print(f"You rolled a {p.number_to_words(num)} !!!\n")
    if game.dice.voided():
        print("Sorry you turn is voided")
        game.change_turn()

def run_game(game):
    print(f"Player # {p.number_to_words(game.active_player.number)}'s turn\n3")
    roll(game)


if __name__ == "__main__":
    main()
