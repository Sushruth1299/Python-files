from turtle import *

import colorsys



bgcolor('black')
speed(0)
pensize(2)


hue = 0.0


for i in range(282):
    cl = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(cl)
    hue += 0.005
    right(i)
    circle(50, i)
    forward(i)
    left(91)
penup()
color('silver', 'silver')
goto(0, 300)
write("Python Turtle Graphics", False, 'center', ('Times new Roman', 30, 'bold'))

hideturtle()
done()