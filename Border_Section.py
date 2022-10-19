from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.setposition(-330, 290)

    def draw_raw(self):
        self.shapesize(1)
        self.color("yellow green")
        self.setheading(0)
        self.stamp()
        for i in range(33):
            self.forward(20)
            self.stamp()
        self.setposition(-330, -280)
        self.setheading(0)
        self.stamp()
        for i in range(33):
            self.forward(20)
            self.stamp()

    def draw_column(self):
        self.shapesize(3)
        self.color("saddle brown")
        self.setposition(-370, 270)
        self.setheading(270)
        self.stamp()
        for j in range(9):
            self.forward(60)
            self.stamp()
        self.setposition(370, 270)
        self.setheading(270)
        self.stamp()
        for j in range(9):
            self.forward(60)
            self.stamp()

    def draw_vertical(self):
        self.shapesize(2)
        self.pensize(5)
        self.setposition(0, 265)
        self.setheading(270)
        for k in range(9):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(20)

