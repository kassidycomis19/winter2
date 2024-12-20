import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("powderblue")  # Blue background

# Create a turtle for drawing snowflakes
flake = turtle.Turtle()
flake.speed(0)  # Fast drawing

# Function to draw a single snowflake
def draw_snowflake(size, num_points):
    for _ in range(num_points):
        for _ in range(3):
            flake.forward(size)
            flake.backward(size)
            flake.left(60)
        flake.right(360 / num_points)

# Function to scatter snowflakes across the screen
def draw_scattered_snowflakes(num_snowflakes, size, num_points):
    for _ in range(num_snowflakes):
        flake.penup()
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        flake.goto(x, y)  # Move to random position
        flake.pendown()
        draw_snowflake(size, num_points)

# Draw 20 snowflakes with size 50 and 6 points
draw_scattered_snowflakes(20, 50, 6)

flake.hideturtle()  # Hide turtle after drawing

# Keep the window open
turtle.done()
import turtle
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a turtle named "t"
t = turtle.Turtle()
t.shape("turtle")
t.speed(3)  # Set turtle drawing speed


def draw_tree(x, y):
    # Move to starting position without drawing
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw the tree trunk
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()


    t.color("green")
    t.begin_fill()
    t.setheading(60)
    for _ in range(3):
        t.forward(40)
        t.left(120)
    t.end_fill()



draw_tree(-100, -100)
draw_tree(50, -100)
draw_tree(200, -100)

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
turtle.done()
