from turtle import Turtle


class Rockets(Turtle):
    def __init__(self, x_position, y_position, color_type):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=7, stretch_len=1, outline=1)
        self.color(color_type)
        self.penup()
        self.setposition(x_position, y_position)

    def move_up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)

    def move_down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)

