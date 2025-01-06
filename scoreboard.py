from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("#FF2974")
        self.setx(x)
        self.sety(y)
        self.count = 0

    def lose_notice(self):
        self.write(f"""You Lose
""", font=("courier", 80, "normal"))
        self.write(f"Score: {self.count}", font=("courier", 40, "normal"))

    def win_notice(self):
        self.write(f"""You Win
""", font=("courier", 80, "normal"))
        self.write(f"Score: {self.count}", font=("courier", 40, "normal"))


