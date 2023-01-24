userNumber = input("please provide a number")
if userNumber.isnumeric():
    reverseNumber = userNumber[::-1]
    if reverseNumber==userNumber:
     print(userNumber, "is a palindrome")
else:
    print("please provide a valid number")