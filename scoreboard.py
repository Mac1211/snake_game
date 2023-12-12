from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Aerial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoring = 0
        with open('data.txt') as score_data:
            self.high_score = int(score_data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score : {self.scoring} High Score: {self.high_score}',move= False, align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.scoring > self.high_score:
            self.high_score = self.scoring
            with open('data.txt', 'w') as data:
                data.write(f'{self.high_score}')
        self.scoring = 0
        self.update_scoreboard()

    

    def score(self):
        self.scoring += 1
        self.update_scoreboard()