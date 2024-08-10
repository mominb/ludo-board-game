from player import Player

import unittest


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_has_started(self):
        self.assertEqual(self.player.pawns[0].has_started(), False)
        self.player.pawns[0].position = 1
        self.assertEqual(self.player.pawns[0].has_started(), True)

    def test_has_finished(self):
        self.assertEqual(self.player.pawns[0].has_finished(), False)
        self.player.pawns[0].position = 57
        self.assertEqual(self.player.pawns[0].has_finished(), True)


if __name__ == '__main__':
    unittest.main()
