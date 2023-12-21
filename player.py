from variants import Variants


# Class for create object of player
class Player:
    def __init__(self, name=" ", choice=" ", score=0):
        self.name = name
        self.choice = choice
        self.score = score

    def __gt__(self, other) -> bool:
        return any((
            self.choice == Variants.ROCK and other.choice == Variants.SCISSORS,
            self.choice == Variants.SCISSORS and other.choice == Variants.PAPER,
            self.choice == Variants.PAPER and other.choice == Variants.ROCK
        ))

    def __eq__(self, other):
        return self.choice == other.choice

