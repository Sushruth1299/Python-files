from time import *
print("Draw Colorful Spiral Web using Turtle Graphics in Python\n")
sleep(3)

from turtle import *
bgcolor('black')
speed(0)
pensize(3)

title('Draw Colorful Spiral Web using Turtle Graphics in Python')

colors = ['red', 'yellow', 'lime', 'purple', 'blue', 'orange']

for i in range(200):
    pencolor(colors[i%6])
    width(i/100 + 1)
    forward(i)
    left(59)
done()
