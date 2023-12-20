import random
from variants import Variants


# Class for create object of player
class Player:
    def __init__(self, name='Bot', choice=random.choice(list(Variants))):
        self.name = name
        self.choice = choice.value

    def __gt__(self, other) -> bool:
        return any((
            self.choice == 'rock' and other.choice == 'scissors',
            self.choice == 'scissors' and other.choice == 'paper',
            self.choice == 'paper' and other.choice == 'rock'
        ))

    def __eq__(self, other):
        return self.choice == other.choice
