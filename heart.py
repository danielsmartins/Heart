import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.hideturtle()


def heart_points(t):
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    return x, y


def draw_heart_lines():
    angles = list(range(0, 360, 1))  
    random.shuffle(angles)  

    for t in angles:
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        x, y = heart_points(math.radians(t))
        pen.goto(x * 20, y * 20)

draw_heart_lines()

turtle.done()
