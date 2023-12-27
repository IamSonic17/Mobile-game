
# Class for create object of player
class Player:
    def __init__(self, name=" ", choice=" ", score=0):
        self.name = name
        self.choice = choice
        self.score = score

    def __gt__(self, other) -> bool:
        return any((
            self.choice == 'Rock' and other.choice == 'Scissors',
            self.choice == 'Scissors' and other.choice == 'Paper',
            self.choice == 'Paper' and other.choice == 'Rock'
        ))

    def __eq__(self, other):
        return self.choice == other.choice

