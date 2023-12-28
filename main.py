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
            self.status.text = status[0]
            self.bonus.text = status[1]
            self.bot_score.text = str(self.bot.score)
            self.user_score.text = str(self.user.score)
        if self.bot.score > 4 or self.user.score > 4:
            self.play_again.disabled = False
            self.rock.disabled = True
            self.scissors.disabled = True
            self.paper.disabled = True
            if self.bot.score < self.user.score:
                self.user_score.text = result[0]
                self.bot_score.text = result[1]
                self.bonus.text = str('Victory!')
            else:
                self.bot_score.text = result[0]
                self.user_score.text = result[1]
                self.bonus.text = str('Defeat')

    def reload(self):
        self.user.score = 0
        self.bot.score = 0
        self.play_again.disabled = True
        self.rock.disabled = False
        self.scissors.disabled = False
        self.paper.disabled = False
        self.status.text = 'What is in your hand?'
        self.bot_score.text = str(self.bot.score)
        self.user_score.text = str(self.user.score)

    def press_button(self, name):
        if name == 'image_rock':
            return setattr(self.image_rock, 'size', (500, 150))
        elif name == 'image_scissors':
            return setattr(self.image_scissors, 'size', (500, 150))
        else:
            return setattr(self.image_paper, 'size', (500, 120))

    def release_button(self, name):
        if name == 'image_rock':
            return setattr(self.image_rock, 'size', (500, 220))
        elif name == 'image_scissors':
            return setattr(self.image_scissors, 'size', (500, 200))
        else:
            return setattr(self.image_paper, 'size', (500, 170))


LabelBase.register(name='Playskool', fn_regular='PF Playskool Pro 3D Regular.ttf')


class RockScissorsPaperApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RockScissorsPaperApp().run()
