import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from defs import who_wins
from player import Player


class Container(GridLayout):
    bot = Player(name="Bot")
    user = Player(name='User')
    bot_score = 0
    user_score = 0

    def play(self, var):
        variants = ['rock', 'scissors', 'paper']
        self.bot.choice = random.choice(variants)
        self.user.choice = var
        who_wins(self.bot, self.user)
        self.bot_score.text = str(self.bot.score)
        self.user_score.text = str(self.user.score)
        if self.bot.score != 5 and self.user.score != 5:
            pass
        else:
            if self.bot.score < self.user.score:
                self.user_score.text = str('Win!')
                self.bot_score.text = str('Lose!')
            else:
                self.bot_score.text = str('Win!')
                self.user_score.text = str('Lose!')


class RockScissorsPaperApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RockScissorsPaperApp().run()
