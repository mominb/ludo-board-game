class Pawn:
    MAX_STEPS_TO_HOME = 57
    MAX_STEPS_ON_BOARD = MAX_STEPS_TO_HOME - 6

    def __init__(self, player):
        self.number = len(player.pawns) + 1
        self.owner = player
        self.position = 0

    def __str__(self):
        return (
            f"Pawn # {self.number} owned by {
                self.owner} has position {self.position}"
        )

    def has_started(self):
        return self.position >= 1

    def has_finished(self):
        return self.position >= Pawn.MAX_STEPS_TO_HOME

    def on_board(self):
        return self.has_started() and self.position <= Pawn.MAX_STEPS_ON_BOARD

    def on_path_to_home(self):
        return self.has_started() and self.position > Pawn.MAX_STEPS_ON_BOARD

    def board_position(self):
        if self.on_board():
            return (self.owner.number - 1) * 13 + self.position

        return 0

    def start(self):
        self.position = 1
