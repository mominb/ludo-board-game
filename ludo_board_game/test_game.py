from game import Game
import unittest


class Test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game(4)

    def test_kill_pawns(self):
        self.game.players[1].pawn_positions_on_board()[0] = 5
        self.game.active_player.pawn_positions_on_board()[0] = 5
        self.game.kill_pawns()
        assert self.game.players[1].pawns[0].position == 0

    def test_move(self):
        print(len(self.game.players))
        with self.assertRaises(ValueError):
            self.game.move(self.game.players[0].pawns[0], 10)

    def test_turn_completed(self):
        self.game.dice.can_roll = False
        self.game.dice.results_used = True
        assert self.game.turn_completed() == True
        self.game.dice.results_used = False
        assert self.game.turn_completed() == False

    def test_change_turn(self):
        self.game.active_player = self.game.players[0]
        self.game.dice.can_roll = False
        self.game.dice.results_used = True
        self.game.change_turn()

    def test_find_non_active_pawns_at(self):
        self.game.active_player = self.game.players[0]
