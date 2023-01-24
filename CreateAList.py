userList1 = input("please provide the first list of numbers")
userList2 = input("please provide the 2nd list of numbers")

list1 = list(map(int, userList1.split()))
list2 = list(map(int, userList2.split()))
combinedList =[]
for i in range(len(list1)):
    if list1[i] % 2 !=0:
        combinedList.append(list1[i])
    if list2[i] % 2 ==0:
        combinedList.append(list2[i])
print(combinedList)

\