from turtle import Screen
from time import sleep
from Rockets_Section import Rockets
from Ball_Section import Ball
from Track_Score import ScoreBoard
from Border_Section import Border
from Winner_Section import Champion


# prepare screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# create rockets, ball, scoreboard
r_rocket = Rockets(350, 0, "khaki")
l_rocket = Rockets(-350, 0, "light blue")
ball = Ball("white")
winner = Champion()
r_score = ScoreBoard(50, 230)
l_score = ScoreBoard(-50, 230)
border = Border()
border.draw_raw()
border.draw_column()
border.draw_vertical()

try_again = True
while try_again:

    screen.listen()
    screen.onkey(l_rocket.move_up, "w")
    screen.onkey(l_rocket.move_down, "s")
    screen.onkey(r_rocket.move_up, "o")
    screen.onkey(r_rocket.move_down, "l")

    play = True
    while play:
        r_score.write_score()
        l_score.write_score()
        sleep(ball.current_speed)
        screen.update()
        ball.move_ball()

        if ball.ycor() > 260 or ball.ycor() < -250:
            ball.change_bounce()

        if (ball.distance(r_rocket) <= 70) and (ball.xcor() >= 330):
            ball.change_direction()
        elif (ball.distance(l_rocket) <= 70) and (ball.xcor() <= -330):
            ball.change_direction()

        if ball.xcor() > 390:
            ball.contrary_direction()
            l_score.score += 1
        elif ball.xcor() < -390:
            ball.contrary_direction()
            r_score.score += 1

        if l_score.score == 3:
            winner.declare_winner("Left Side")
            r_score.write_score()
            l_score.write_score()
            play = False
        elif r_score.score == 3:
            winner.declare_winner("Right Side")
            r_score.write_score()
            l_score.write_score()
            play = False

    will = screen.textinput(title="end/continue", prompt="Do You Want to Try Again? Yes/No ").lower()
    if will == "no":
        try_again = False
    else:
        r_score.score = 0
        l_score.score = 0
        winner.clear()


screen.exitonclick()
