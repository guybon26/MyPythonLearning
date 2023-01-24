numbers_x = input("Please provide a set of numbers")
numbers_y = input("please provide another set of numbers")

lengthX = len(numbers_x)
lengthY = len(numbers_y)

if numbers_x[0]==numbers_x[-1]:
    print('X is true')
else:
    print ('X is false')

if numbers_y[0]==numbers_y[-1]:
    print('Y is True')
else:
    print('Y is False')
