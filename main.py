from turtle import Screen
from npc_turtle import NPCTurtle
from user import UserTurtle
from game_manager import GameManager
from scoreboard import Scoreboard
import random
import time


game_is_on = True
game = GameManager(600, 600)
score = Scoreboard(-250, 0)
score.count = 0
g_300 = True  # Does an initial check to make sure that npcs are not out of the scope of the screen
condition_1 = False
condition_2 = False
# initialize screen
screen = Screen()
screen.setup(width=game.SCREENWIDTH, height=game.SCREENHEIGHT)
screen.bgcolor("#140C17")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

# initialize user
user = UserTurtle(0, -300, 90)
screen.onkey(user.move_up, "Up")
screen.onkey(user.move_right, "Right")
screen.onkey(user.move_left, "Left")
og_y = user.ycor()


for number in range(game.lane_num):
    lane = game.generate_lanes()
    game.lanes.append(lane)
    game.y_loc += 100

order_ticket = game.call_npcs(game.lanes)


for lane in game.lanes:
    for i in range(lane[-1]):
        n = NPCTurtle(*lane[:5])
        game.npcs.append(n)
        for c in range(len(game.npcs)):
            n.setx(game.npcs[c - 1].xcor() - random.randrange(0, 300, 50))

while game_is_on:
    for n in range(len(game.npcs)):
        while g_300 is True:
            for o in range(len(game.npcs)):
                if 300 < game.npcs[o].xcor() or -300 > game.npcs[o].xcor():
                    condition_1 = False
                    game.npcs[o].setx(random.randint(-300, 300))
                    condition_1 = True
                    if condition_1 is True and condition_2 is True:
                        g_300 = False
                elif (game.npcs[o].xcor() - game.npcs[o - 1].xcor() <= 40 or
                        game.npcs[o - 1].xcor() - game.npcs[0].xcor() <= 40):
                    condition_2 = False
                    game.npcs[o].setx(game.npcs[o - 1].xcor() - 41)
                    condition_2 = True
                    if condition_1 is True and condition_2 is True:
                        g_300 = False
    for n in game.npcs:
        if n.xcor() < game.SCREENWIDTH/(-2) and n.heading() == 180:
            n.setx(300)
        elif n.xcor() > game.SCREENWIDTH/2 and n.heading() == 0:
            n.setx(-300)
        n.move()
    tap = game.sense(user, game.npcs)
    if tap:
        game_is_on = False
        score.lose_notice()
    if user.ycor() > og_y:
        score.count += 1
        og_y = user.ycor()
    if user.ycor() > 300:
        game_is_on = False
        score.win_notice()
    time.sleep(.2)
    screen.update()


screen.exitonclick()
