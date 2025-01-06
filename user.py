from turtle import Turtle


class UserTurtle(Turtle):
    def __init__(self, x, y, direction):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("#d8eee4")
        self.resizemode("user")
        self.turtlesize(1.75, 1.75, 1)
        self.setx(x)
        self.sety(y)
        self.setheading(direction)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)

    def move_right(self):
        new_x = self.xcor() + 20
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() - 20
        new_y = self.ycor()
        self.goto(new_x, new_y)
