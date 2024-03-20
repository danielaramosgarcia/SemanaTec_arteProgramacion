# Daniela Ramos A01174259
# Jeannete 
# Gael 

"""
Catch Game

This is a game where letters fall from the top of the screen and the player needs to catch them to form words.

The objective of the game is to catch as many letters as possible and create as many words as you can within a given time limit.

Enjoy the challenge and have fun playing!

"""

from random import *
import turtle
from freegames import vector
import time

# Set up the screen
# Function to draw a rectangle
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Initialize the screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")  # Set sky color

pen = turtle.Turtle()
pen.speed(0)  # Set drawing speed to fastest

# Draw grass
draw_rectangle(pen, "lightgreen", -300, -100, 600, 200)

# Draw sun
pen.penup()
pen.goto(200, 150)
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()



