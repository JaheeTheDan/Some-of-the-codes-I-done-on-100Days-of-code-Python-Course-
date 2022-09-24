'''Sanke Class'''
from turtle import Turtle


class Snake():
    '''Sanke class that make a new snake every new game and can increase in lenth'''

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''Funtion that make the sanke's body'''
        x = 0
        for _ in range(3):
            self.add_segment(x, 0)
            x -= 20

    def add_segment(self, x, y):
        '''Add segment to the body'''
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)

    def extend_snake(self):
        '''Increase the number of segments on body by one'''
        x, y = self.segments[-1].pos()
        self.add_segment(x, y)

    def reset(self):
        '''Reset snake when the funtion is called'''
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        '''Funtion that allowed the sanke to move'''
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        '''Allows the sanke to move up'''
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        '''Allows the sanke to move down'''
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        '''Allows the sanke to move left'''
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        '''Allows the sanke to move right'''
        if self.head.heading() != 180:
            self.head.seth(0)
