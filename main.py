"""1: the ball is an object created using the turtle class with logic for automatic movement and bouncing
2: the scoreboard is turtle printed text that clears and refreshes tracking the score as it's made
3: the paddles are two separate objects of the paddle class that take user input to move and interact with
the ball object
4: the dashed lines in the middle are drawn out by a 4th turtle object that will determine the zones for scoring
5: a screen object to contain all the above
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    # Ball hits top or bottom and bounces
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball hits paddle and bounces
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Ball scores in right goal
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Ball scores in left goal
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
