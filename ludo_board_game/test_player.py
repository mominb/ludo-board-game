from game import Game
import unittest

class Test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game(4)
    def test_pawns_at(self):
        print(self.game.players[0].pawns_at(13))
