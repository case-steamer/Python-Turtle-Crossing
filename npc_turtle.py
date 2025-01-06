import time
from turtle import Turtle
import random

COLORS = ["#d9d8ee", "#e2eed8", "#d8eed9", "#d8e2ee", "#d8edee", "#8FFFDD", "#B8FFEA", "#FFEEB8", "#FFDBB8", "#A3D6FF",
          "#A3E2FF", "#A3F6FF", "#B6ECED", "#B8FFE6", "#ECFFB8", "#FFE2A3", "#BBE386", "#FFFBB8", "#FFB8D3", "#F6D7FF"]
HEADINGS = [0, 180]
SCREENWIDTH = 600
SCREENHEIGHT = 600


class NPCTurtle(Turtle):
    def __init__(self, location, speed, color, spaces, heading):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(color)
        self.setheading(heading)
        self.resizemode("user")
        self.turtlesize(1.75, 1.75, 1)
        self.speed(speed)
        if heading == 0:
            self.x = (SCREENWIDTH/2) * (-1)
        else:
            self.x = SCREENWIDTH/2
        self.sety(location)
        self.increment = spaces

    def move(self):
        self.forward(5)






