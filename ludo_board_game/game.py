from dice import Dice, result
from player import Player
from functools import reduce


class Game:
    SAFE_POSITIONS = [1, 9, 14, 22, 27, 35, 40, 48]

    def __init__(self, playerCount):
        self.players = []
        self.number_of_players = playerCount
        for _ in range(playerCount):
            self.players.append(Player())

        self.active_player = self.players[0]
        self.dice = Dice()

    def non_active_players(self):
        return list(
            filter(lambda p: p.number != self.active_player.number, self.players)
        )

    def find_non_active_pawns_at(self, board_position):
        return reduce(lambda list, player: list + player.pawns_at(board_position), self.non_active_players(), [])

    def kill_pawns(self):
        active_player_positions = self.active_player.pawn_positions_on_board()

        for active_pawn_position in active_player_positions:
            if active_pawn_position > 0 and not active_pawn_position in Game.SAFE_POSITIONS:
                pawns_to_kill = self.find_non_active_pawns_at(
                    active_pawn_position)
                if len(pawns_to_kill) == 1:
                    pawns_to_kill[0].position = 0

    def move(self, pawn, steps):
        if pawn.has_finished():
            raise ValueError("pawn already at home")
        if not pawn.has_started():
            raise ValueError("pawn not open")
        if pawn.has_started() == True:
            pawn.position += steps
            pawn.board_position += steps

    def turn_completed(self):
        if not self.dice.can_roll and self.dice.results_used:
            return True
        else:
            return False

    def active_player_index(self):
        for index, player in enumerate(self.players):
            if player.number == self.active_player.number:
                return index

    def change_turn(self):
        if self.turn_completed():
            self.active_player = self.players[self.active_player_index() + 1]

    def change_turn_voided(self):
        index = self.active_player_index()
        if index == len(self.players) - 1:
            self.active_player = self.players[0]
        else:
            self.active_player = self.players[self.active_player_index() + 1]
