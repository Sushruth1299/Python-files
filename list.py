ROW, COLUMN = 5, 5

list = [[0 for i in range(COLUMN)]
        for i in range(ROW)]

for i in range(5):
    for i in range(5):
        print("\t", list[i])