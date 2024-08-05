import random


class Dice:
    def __init__(self):
        self.roll_results = []

    def __str__(self):
        (rolls, sixes) = self._stats()

        return f"rollCount: {rolls}, sixes:{sixes}"

    def _stats(self):
        rolls = len(self.roll_results)
        sixes = list(map(result, self.roll_results)).count(6)

        return (rolls, sixes)

    def can_roll(self):
        (rolls, sixes) = self._stats()

        return rolls < 3 and sixes == rolls

    def voided(self):
        (rolls, sixes) = self._stats()

        return rolls == 3 and sixes == 3

    def roll(self):
        if not self.can_roll():
            raise ValueError("Cannot roll because stats", self._stats())

        number = random.randint(1, 6)

        self.roll_results.append(RollResult(number))

        return number

    def results_used(self):
        usedCount = list(map(lambda r: r.used, self.roll_results)).count(True)

        return len(self.roll_results) == usedCount

    def reset(self):
        self.roll_results = []


class RollResult:
    def __init__(self, result):
        self.result = result
        self.used = False


def result(rollResult):
    return rollResult.result
