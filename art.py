from turtle import *

import colorsys


bgcolor('black')
speed(0)
pensize(3)


hue = 0.0


for i in range(300):
    pen = colorsys.hsv_to_rgb(hue, 1 ,1)
    color(pen, pen)
    hue += 0.005
    right(i)
    circle(50, i)
    forward(i)
    left(91)

penup()
goto(1000, 0)
done()