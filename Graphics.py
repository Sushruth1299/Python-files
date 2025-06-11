# Declare a variable called width
while True:
    try:
        while True:
            width = int(input("Please provide the width of rhombus between (0 - 1500)\n"))
            if width > 1500:
                print("ERR: width is greater than 1500\n")
            elif width < 0:
                print("ERR: width is a negative number\n")
            else:
                break
        break

    # values, symbols, etc, create a ValueError
    except ValueError:
        # Keeps program running 
        print("ERR: This isn't an integer!\n")

# Declare a variable called height
while True:
    try: 
        while True:
            height = int(input("Please provide the height of rhombus between (0 - 750)\n"))
            if height > 750:
                print('ERR: height is greater than 750\n')
            elif height < 0:
                print('ERR: height is a negative number\n')
            else:
                break
        break
    except ValueError:
        print("ERR: This isn't an integer!\n")

print()

x = width/2
y = height/2

from turtle import *

bgcolor('black')
pencolor('lime')
pensize(8)

x1, y1 = 0, y
x2, y2 = x, 0
x3, y3 = 0, -y
x4, y4 = -x, 0


penup()
goto(x1, y1)
pendown()
goto(x2, y2)
goto(x3, y3)
goto(x4, y4)
goto(x1, y1)
done()
