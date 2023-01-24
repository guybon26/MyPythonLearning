userNumber = input('please provide a list of numbers')
num = list(map(int, userNumber.split()))
length = len(num)
counter = 0
sum = 0
step = num[1]-num[0]
while counter < length:
    sum = num[counter] * (num[counter]+step)/2
    counter+=1

average = sum/ length

print('sum is', sum)
print('average is', average)