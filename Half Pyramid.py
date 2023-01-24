counter = int(input("please provide the size of the pyramid"))
for i in range(counter):
    for j in range(i+1):
        print("*", end="")
    i-=1
    print()
