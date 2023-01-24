userString = input("please provide a sentence")
str_x = userString.split()
counter = 0


for i in str_x:
    if i=="Emma":
        counter+=1


print("Emma appear", counter, "times")