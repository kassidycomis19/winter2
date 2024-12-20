import turtle




screen = turtle.Screen()


screen.setup(500, 500)


screen.bgcolor('Indigo')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)


t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Kassidy Comis", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")

import turtle


screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
star = turtle.Turtle()
star.shape("turtle")
star.color("blue")


star.speed(5)


def draw_star(size):
    for _ in range(5):
        star.forward(size)
        star.right(144)


draw_star(100)


star.hideturtle()


screen.exitonclick()

