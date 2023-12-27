import random

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.uix.gridlayout import GridLayout

from defs import who_wins
from player import Player


Window.size = (720, 1280)


class Container(GridLayout):
    bot = Player(name="Bot")
    user = Player(name='User')

    def play(self, var):
        variants = ['Rock', 'Scissors', 'Paper']
        result = ['Winner', 'Loser']
        self.bot.choice = random.choice(variants)
        self.user.choice = var
        if self.bot.score < 5 or self.user.score < 5:
            status = who_wins(self.bot, self.user)
            self.status.text = status
            self.bot_score.text = str(self.bot.score)
            self.user_score.text = str(self.user.score)
        if self.bot.score > 4 or self.user.score > 4:
            self.rock.disabled = True
            self.scissors.disabled = True
            self.paper.disabled = True
            self.play_again.disabled = False
            if self.bot.score < self.user.score:
                self.user_score.text = result[0]
                self.bot_score.text = result[1]
                self.status.text = str('Victory!')
            else:
                self.bot_score.text = result[0]
                self.user_score.text = result[1]
                self.status.text = str('Defeat')

    def reload(self):
        self.user.score = 0
        self.bot.score = 0
        self.rock.disabled = False
        self.scissors.disabled = False
        self.paper.disabled = False
        self.play_again.disabled = True
        self.status.text = 'What is in your hand?'
        self.bot_score.text = str(self.bot.score)
        self.user_score.text = str(self.user.score)


LabelBase.register(name='Playskool', fn_regular='PF Playskool Pro 3D Regular.ttf')


class RockScissorsPaperApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RockScissorsPaperApp().run()
