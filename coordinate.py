from turtle import *
bgcolor('black')
pencolor('lime')
pensize(8)

x1,y1 = 0, 100
x2,y2 = 100, 0
x3,y3 = 0, -100
x4,y4 = -100, 0

hideturtle()

penup()
goto(x1, y1)
pendown()
goto(x2, y2)
goto(x3, y3)
goto(x4, y4)
goto(x1, y1)

done()
