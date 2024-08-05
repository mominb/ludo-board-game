from game import Game
import unittest


class Test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game(4)

    def test_kill_pawns(self):
        self.game.players[1].pawn_positions_on_board()[0] = 5
        self.game.active_player.pawn_positions_on_board()[0] = 5
        self.game.kill_pawns()
        print(self.game.players[1].pawns[0].position)
