'''Food Class'''
from random import randint
from turtle import Turtle


class Food(Turtle):
    '''Food class that show food randomly on the screen'''

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('yellow')
        self.speed(0)
        self.refresh()

    def refresh(self):
        '''Place food at a random position on screen'''
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
