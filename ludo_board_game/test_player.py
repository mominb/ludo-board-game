from game import Game
import unittest


class Test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game(4)

    def test_pawn_positions_on_board(self):
        self.game.players[0].pawns[2].position = 17
        self.assertEqual(
            self.game.players[0].pawn_positions_on_board(), [0, 0, 17, 0])
