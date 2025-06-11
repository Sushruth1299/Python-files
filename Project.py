from random import *

while True:
        try:
            side = int(input("Enter the sidelength of the rhombus between (0 - 750): "))
            if side > 750:
                print("ERR: sidelength is larger than 750. Try again\n")
            elif side < 0:
                print("ERR: sidelength is negative. Try again\n")
            else:
                break
        except ValueError:
            print("ERR: Value isn't a number! Try again!\n")

print()
print("Enter values of both angles")
print("Make sure they both equal 180 degrees!\n")

while True:
    while True:
        try:
            angle1 = int(input("Enter the angle of the rhombus's side between (0 - 179)"))
            if angle1 > 179:
                print('ERR: The angle value is greater than 179. Try again!\n')
            elif angle1 < 0:
                print('ERR: angle value is negative. Try again!\n')
            else:
                break
        except ValueError:
            print("ERR: Value isn't a number! Try again!\n")
    while True:
        try:
            angle2 = int(input("Enter the angle of the rhombus's top end between (0 - 179)"))
            if angle2 > 179:
                print('ERR: The angle value is greater than 179. Try again!\n')
            elif angle2 < 0:
                print('ERR: angle value is negative. Try again!\n')
            else:
                break
        except ValueError:
            print("ERR: Value isn't a number! Try again!\n")
    
    if angle1 + angle2 == 180:
        break
    else:
        print("ERR: The sum of the angles do not equal 180! Try again!\n")

print()

y = angle1/2
x = angle2/2

colors = ['red' ,'yellow', 'blue', 'lime', 'orange', 'magenta']

from turtle import *
bgcolor('black')
pencolor(choice(colors))
pensize(8)

penup()
left(90)
pendown()

left(angle2/2)
for i in range(2):
    forward(side)
    right(angle1)
    forward(side)
    right(angle2)

hideturtle()
done()