# Python program to generate
# odd sized magic squares
# A function to generate odd
# sized magic squares
def magic_square(n):
    # 2D array with
    # all slots to set 0
    matrix = [[0 for a in range(n)]
              for b in range(n)]
    
    # initialize position of 1
    i = n//2
    j = n - 1

    # Fill the magic square
    # by placing in values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0
            
            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1
            
        if matrix[int(i)][int(j)] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            # Assign the current number to the matrix
            matrix[int(i)][int(j)] = num
            num = num + 1
        
        j = j + 1
        i = i + 1

    # Printing magic square
    print("magic square for n =", n)
    print("Sum of each row or column =", 
          n * (n * n + 1) // 2, "\n")
    
    for i in range(n):
        for j in range(n):
            print("%2d" % matrix[i][j],
                  end = " ")
        
        # To display output
        # in matrix form
        print()

y = 3
magic_square(y)