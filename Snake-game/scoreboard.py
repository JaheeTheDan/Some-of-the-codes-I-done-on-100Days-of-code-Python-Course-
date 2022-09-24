'''Scoreboard Class'''
from turtle import Turtle

FONT = ('Agency FB', 20, 'normal')

class ScoreBoard(Turtle):
    '''Show info on screen like point gain and high sroce'''
    def __init__(self):
        self.score = 0
        #high_score_data.txt file that contain high score data
        try:
            with open ('high_score_data.txt','r',encoding='utf-8') as data:
                self.high_score = int(data.read())
        #if txt file is not found, then a new one is create
        except FileNotFoundError:
            with open ('high_score_data.txt','x',encoding='utf-8') as data:
                data.write('0')
                self.high_score = 0

        super().__init__()
        self.penup()
        self.ht()
        self.speed(0)
        self.color('white')

        #Show game score
        self.show_score()


    def show_score(self):
        '''Show the current score on top of sceen'''
        self.change_high_score()
        self.clear()
        self.goto(0,270)
        self.write(f'Score: {self.score} High Score: {self.high_score}',
                            move=False, align='center', font=FONT)

    def add_score(self):
        '''Increase the point scores'''
        self.score += 1
        self.show_score()

    def change_high_score(self):
        '''Change high score when it's beaten'''
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        '''Reset the point scores to 0 and change high score in the data.txt file'''
        with open('high_score_data.txt','w',encoding='utf-8') as data:
            data.write(str(self.high_score))
        self.score = 0
        self.show_score()

    def game_over(self):
        '''Show when funtion is called'''
        self.clear()
        text = f'   GAME OVER!\nYour score is {self.score}\nHigh Score is {self.high_score}'
        self.goto(0,0)
        self.write(text, move=False, align='center', font=FONT)
