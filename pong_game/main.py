from turtle import Screen, Turtle
from day22_pong_game.paddles import Paddle
from day22_pong_game.ball import Ball
from day22_pong_game.scoreboard import Scoreboard
from time import sleep


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

score_r = Scoreboard((200, 250))
score_l = Scoreboard((-200, 250))
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkeypress(paddle_right.go_up, 'w')
screen.onkeypress(paddle_right.go_down, 's')

screen.onkeypress(paddle_left.go_up, 'Up')
screen.onkeypress(paddle_left.go_down, 'Down')

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detecting collision with wall
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()

    # detecting collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        print('right lose')
        score_l.l_score()
        ball.reset_game()
        sleep(1)

    if ball.xcor() < -390:
        print('left lose')
        score_r.r_score()
        ball.reset_game()
        sleep(1)


screen.exitonclick()