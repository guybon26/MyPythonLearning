userNumber = input(" please provide the size of the pattern")
counter = int(userNumber)
row = 0
while row < counter:
    column = 0
    while column <= row:
        print(column+1, end=" ")
        column += 1
    print("")
    row += 1