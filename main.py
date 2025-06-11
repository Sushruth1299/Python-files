from turtle import *

bgcolor('black')

pencolor('blue')
pensize(2)
speed(0)
pensize(2)



def drawcircle(radius):
    for i in range(10):
        circle(radius)
        radius -= 4

def drawdesign() :
    for i in range(20):

        drawcircle(150)
        right(18)

drawdesign()
done()