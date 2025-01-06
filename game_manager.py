import random

class GameManager:
    def __init__(self, SCREENWIDTH, SCREENHEIGHT):
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT
        self.COLORS = [
            "#d9d8ee", "#e2eed8", "#d8eed9", "#d8e2ee", "#d8edee", "#8FFFDD", "#B8FFEA", "#FFEEB8",
                       "#FFDBB8", "#A3D6FF", "#A3E2FF", "#A3F6FF", "#B6ECED", "#B8FFE6", "#ECFFB8", "#FFE2A3",
                       "#BBE386", "#FFFBB8", "#FFB8D3","#F6D7FF"
        ]
        self.HEADINGS = [0, 180]
        self.y_loc = ((self.SCREENHEIGHT / 2) * (-1))
        self.lane_num = int((self.SCREENHEIGHT - 80) / 80)
        self.lanes = []
        self.npcs = []

    def generate_lanes(self):
        lane_loc = self.y_loc + 80
        speed = random.uniform(1, 2)
        color = random.choice(self.COLORS)
        spaces = random.randint(100, 200)
        heading = random.choice(self.HEADINGS)
        number = random.randint(4, 7)
        return lane_loc, speed, color, spaces, heading, number

    def call_npcs(self, npc_list):
        order = []
        for n in npc_list:
            number = n[-1]
            order.append(number)
        return order

    def sense(self, player, npcs):
        for n in npcs:
            if abs(player.ycor() - n.ycor()) <= 35:
                ydist = abs(player.ycor() - n.ycor())
            else:
                ydist = None
            if abs(player.xcor() - n.xcor()) <= 35:
                xdist = abs(player.xcor() - n.xcor())
            else:
                xdist = None

            if ydist is None or xdist is None:
                ret_var = None
            elif ydist <= 35 and xdist <= 35:
                ret_var = True

            if ret_var == True:
                return True



