import turtle


screen = turtle.Screen()
screen.bgcolor("sky blue")


pen = turtle.Turtle()
pen.speed(1)
pen.color("black")
pen.hideturtle()


pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.write("Merry Christmas!", align="center", font=("Arial", 24, "bold"))


pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.color("red")
pen.begin_fill()


for _ in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()


pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.color("green")
pen.width(5)


pen.forward(100)

pen.penup()
pen.goto(0, -50)
pen.pendown()


pen.setheading(90)
pen.forward(100)


turtle.done()
