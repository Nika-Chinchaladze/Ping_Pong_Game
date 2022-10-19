from turtle import Turtle


class Ball(Turtle):
    def __init__(self, color_type):
        super().__init__()
        self.shape("circle")
        self.color(color_type)
        self.penup()
        self.setposition(0, 0)
        self.x_step = 10
        self.y_step = 10
        self.current_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def change_bounce(self):
        self.y_step *= -1

    def change_direction(self):
        self.x_step *= -1
        self.current_speed *= 0.8

    def contrary_direction(self):
        self.goto(0, 0)
        self.x_step *= -1
        self.current_speed = 0.1

