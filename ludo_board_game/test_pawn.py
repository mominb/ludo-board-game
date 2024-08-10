
from pawn import Pawn
import unittest


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.pawn = Pawn("momin")

    def test_has_started(self):
        self.assertEqual(self.pawn.has_started(), False)
        self.pawn.position = 0
        self.assertEqual(self.pawn.has_started(), True)

    def test_has_finished(self):
        self.assertEqual(self.pawn.has_finished(), False)
        self.pawn.position = 56
        self.assertEqual(self.pawn.has_finished(), True)


if __name__ == '__main__':
    unittest.main()
