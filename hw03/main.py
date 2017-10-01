from turtle import *
import math as m
def draw_flag(height):
    #Draw a rectangle centered on the origin as flag
    up()
    goto(-0.75 * height, 0.5 * height)
    down()
    color('#f40002', '#f40002')
    setheading(0)
    begin_fill()
    for i in range(2):
        fd(1.5 * height)
        right(90)
        fd(height)
        right(90)
    end_fill()
def draw_star(center, radius):
    #Input the center and radius to draw a star
    center_big_star = (-10 * x, 5 * x)
    up()
    goto(center_big_star)
    goto(center)
    setheading(0)
    if center == center_big_star:
        angle = 90
    else:
        angle = towards(center_big_star)
    #The 'angle' means the orientation of star
    #It's according to the relationship with the big star
    left(angle)       
    fd(radius)
    right(162)
    down()
    beginning = pos()
    color('#faf408', '#faf408')    
    begin_fill()
    while True:
        fd(2 * radius * m.cos(m.pi / 10))
        right(144)
        if distance(beginning) < 1:
            break
    end_fill()   
height = 460 #Set the height of the flag
x = height / 20 #The x represents a unit length
speed(7)
draw_flag(height)
draw_star((-10 * x, 5 * x), 3 * x)
draw_star((-5 * x, 8 * x), x)
draw_star((-3 * x, 6 * x), x)
draw_star((-3 * x, 3 * x), x)
draw_star((-5 * x, 1 * x), x)
hideturtle()
