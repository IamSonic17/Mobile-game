import random
from defs import ask_user, who_wins
from player import Player
from variants import Variants

username = str(input('Type your name: '))

bot_score = 0
user_score = 0

for i in range(5):
    bot = Player(name="Bot", choice=random.choice(list(Variants)), score=bot_score)
    user = Player(username, ask_user(), score=user_score)
    who_wins(bot, user)
    bot_score = bot.score
    user_score = user.score

print(f"Bot: {bot_score}, {username}: {user_score}")
