from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(x_position, y_position)
        self.score = 0

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 30, "bold"))
