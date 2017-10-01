from turtle import *
import math as m

def draw_flag(height):
    up()
    goto(-0.75 * height, 0.5 * height)
    down()
    color('red', 'red')
    setheading(0)
    begin_fill()
    fd(1.5 * height)
    right(90)
    fd(height)
    right(90)
    fd(1.5 * height)
    right(90)
    fd(height)
    end_fill()

def draw_star(center, beginning):
    up()
    goto(center)
    goto(beginning)
    down()
    color('yellow', 'yellow')
    radius = distance(center)
    setheading(0)
    left(towards(center) + 18)
    begin_fill()
    while True:
        fd(2 * radius * m.cos(m.pi / 10))
        right(144)
        if distance(beginning) < 1:
            break
    end_fill()
    
def node_little_star(center_little_star, radius):
    center_big_star = (-10 * x, 5 * x)
    up()
    goto(center_big_star)
    goto(center_little_star)
    setheading(0)
    left(towards(center_big_star))
    fd(radius)
    node = pos()
    return node

speed(7)
height = 640
draw_flag(height)
x = height / 20

draw_star((-10 * x, 5 * x), (-10 * x, 8 * x))

draw_star((-5 * x, 8 * x), node_little_star((-5 * x, 8 * x), x))
draw_star((-3 * x, 6 * x), node_little_star((-3 * x, 6 * x), x))
draw_star((-3 * x, 3 * x), node_little_star((-3 * x, 3 * x), x))
draw_star((-5 * x, 1 * x), node_little_star((-5 * x, 1 * x), x))

hideturtle()
