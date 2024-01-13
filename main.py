import random
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


Builder.load_string('''

<MyOwnLabel@Label>
    color: (0,0,0,1)
    font_size: '25sp'
    font_name:"Playskool"
    halign: 'center'
    valign: 'top'
    text_size: self.size

<Container>:

    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'backscreen.jpg'

    rows: 5
    bot_score: bot_score
    user_score: user_score
    user_name: user_name
    status: status
    bonus: bonus
    rock: rock
    scissors: scissors
    paper: paper
    play_again: play_again
    image_rock: image_rock
    image_scissors: image_scissors
    image_paper: image_paper

    AnchorLayout:
        anchor_y: 'top'
        size_hint: 0.1, 0.15

        GridLayout:
            cols: 2
            padding: [15, 20, 15, -30]

            BoxLayout:

                MyOwnLabel:
                    text: 'Bot ->'
                    id: bot_name

                MyOwnLabel:
                    text: '0'
                    id: bot_score


            BoxLayout:

                MyOwnLabel:
                    text: '0'
                    id: user_score

                MyOwnLabel:
                    text: '<- User'
                    id: user_name

    Label:
        text: 'What is in your hand?'
        color: (0,0,0,1)
        font_size: '35sp'
        font_name:"Playskool"
        size_hint: 0.1, 0.4
        halign: 'center'
        valign: 'center'
        text_size: self.size
        id: status
    Label:
        text: 'Choose!'
        color: (1,0,0,1)
        font_size: '45sp'
        font_name:"Playskool"
        size_hint: 0.1, 0.4
        halign: 'center'
        valign: 'center'
        text_size: self.size
        id: bonus

    BoxLayout:
        size_hint: 0.1, 0.75
        padding: [30, 20, 30, 20]

        Button:
            text: ''
            font_size: '25sp'
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_color: 255,254,223,0
            id: rock
            disabled: False
            on_press:
                root.press_button('image_rock')
            on_release:
                root.release_button('image_rock')
                root.play('Rock')
            Image:
                id: image_rock
                source: 'rock_button.png'
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: 250, 130

        Button:
            text: ''
            font_size: '25sp'
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_color: 255,254,223,0
            id: scissors
            disabled: False
            on_press:
                root.press_button('image_scissors')
            on_release:
                root.release_button('image_scissors')
                root.play('Scissors')
            Image:
                id: image_scissors
                source: 'scissors_button.png'
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: 250, 140

        Button:
            text: ''
            font_size: '25sp'
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            background_color: 255,254,223,0
            id: paper
            disabled: False
            on_press:
                root.press_button('image_paper')
            on_release:
                root.release_button('image_paper')
                root.play('Paper')
            Image:
                id: image_paper
                source: 'paper_button.png'
                center_x: self.parent.center_x
                center_y: self.parent.center_y
                size: 250, 130

    BoxLayout:
        size_hint: 0.1, 0.2
        padding: [0, 0, 0, 0]

        Button:
            text: 'Начать заново'
            id: play_again
            disabled: True
            on_release:
                root.reload()

''')


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
        self.bonus.text = 'Choose!'
        self.bot_score.text = str(self.bot.score)
        self.user_score.text = str(self.user.score)

    def press_button(self, name):
        if name == 'image_rock':
            return setattr(self.image_rock, 'size', (200, 80))
        elif name == 'image_scissors':
            return setattr(self.image_scissors, 'size', (200, 80))
        else:
            return setattr(self.image_paper, 'size', (200, 70))

    def release_button(self, name):
        if name == 'image_rock':
            return setattr(self.image_rock, 'size', (250, 130))
        elif name == 'image_scissors':
            return setattr(self.image_scissors, 'size', (250, 140))
        else:
            return setattr(self.image_paper, 'size', (250, 130))


def who_wins(first, second):
    if first == second:
        answer = [f"({first.choice} vs {second.choice})", "Draw"]
    elif first > second:
        answer = [f"({first.choice} vs {second.choice})", "Bot win"]
        first.score = int(first.score) + 1
    else:
        answer = [f"({first.choice} vs {second.choice})", "User win"]
        second.score = int(second.score) + 1

    return answer


LabelBase.register(name='Playskool', fn_regular='Playskool.ttf')


class RockScissorsPaperApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    RockScissorsPaperApp().run()
