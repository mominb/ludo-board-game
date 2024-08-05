from dice import Dice
from pawn import Pawn
from color import Color
from functools import reduce


class Player:
    player_count = 0
    colors = [color for color in Color]
    dice = Dice()

    def __init__(self):
        Player.player_count = self.number = Player.player_count + 1

        if Player.player_count > 4:
            raise ValueError("Cannot have more than 4 players")

        self.color = Player.colors[self.number - 1]
        self.win_position = None
        self.pawns = []
        for _ in range(4):
            self.pawns.append(Pawn(self))

    def __str__(self):
        return f"Player # {self.number} having a color of {self.color}"

    def pawn_positions_on_board(self):
        return reduce(lambda list, pawn: list + [pawn.board_position()], self.pawns, [])

    def pawns_at(self, pawn_position):
        pawns = []

        for my_pawn_index, my_pawn_position in enumerate(self.pawn_positions_on_board()):
            if pawn_position == my_pawn_position:
                pawns.append(self.pawns[my_pawn_index])

        return pawns

    def has_won(self):
        count = 0
        for pawn in self.pawns:
            if pawn.has_finished():
                count += 1

        return count >= 4
