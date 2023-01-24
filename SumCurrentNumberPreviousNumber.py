userList = input("please type a list of 10 numbers")
num = list(map(int, userList.split()))
length = len(num)
sum = 0
for i in range(1,length):
    sum = num[i] + num[i-1]
    print(sum)
