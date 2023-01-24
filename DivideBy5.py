userGivenList = input("please provide a list of numbers")
userList = list(map(int, userGivenList.split()))
length = len(userList)

for i in range(length):
    if userList[i] % 5 == 0:
        print(userList[i])

