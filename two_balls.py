from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("linen")
screen.tracer(0)


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x = 10
        self.y = 9
        self.goto(position)

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

        if self.xcor() > 130 or self.xcor() < -130:
            self.bounce_x()

        if self.ycor() > 130 or self.ycor() < -130:
            self.bounce_y()

    def bounce_x(self):
        self.x *= -1

    def bounce_y(self):
        self.y *= -1


line = Turtle()
line.hideturtle()
line.color("red")
line.pensize(5)
ball1 = Ball((125, 0))
ball2 = Ball((0, 125))


def square(n):
    for __ in range(4):
        line.forward(n)
        line.right(90)


action = True
while action:
    screen.update()
    time.sleep(0.1)
    line.penup()
    line.goto(-150, 150)
    line.pendown()
    square(300)

    ball1.move()
    ball2.move()


screen.mainloop()
