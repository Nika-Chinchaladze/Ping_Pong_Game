from turtle import Turtle


class Champion(Turtle):
    def __init__(self):
        super().__init__()
        self.color("khaki")
        self.hideturtle()
        self.penup()
        self.setposition(0, 0)

    def declare_winner(self, side):
        self.clear()
        self.write(f"{side} is Winner!", align="center", font=("Courier", 38, "bold"))
