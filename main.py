from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()

##screen properties

screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

"""this line of code is for divide the screen into two parts"""
#####################################################################
paddle = Turtle(shape="classic")
paddle.color("white")
paddle.penup()
paddle.goto(0, 280)
paddle.pendown()
paddle.right(90)

for _ in range(15):
    paddle.forward(20)
    paddle.penup()
    paddle.forward(20)
    paddle.pendown()

paddle.hideturtle()
paddle.showturtle()
########################################################################

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    """detect collision with the wall"""
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    """detect collision with paddle"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    """Detect when you missed the paddle"""
    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
