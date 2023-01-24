userIncome = int(input("please enter the amount for tax calculation"))

if userIncome <= 10000:
    print("no tax required for", userIncome)

elif userIncome > 10000 and userIncome <=20000:
    rateTax1 = (userIncome - 10000) * 0.1
    print("your tax is 10000*0% +", rateTax1, "*10% =",rateTax1)

elif userIncome > 20000:
    rateTax1 = 1000
    rateTax2 = (userIncome - 20000) * 0.2
    rate20 = userIncome - 20000
    sum = rateTax1 + rateTax2
    print("your tax is 10000*0% + 10000*10% +", rate20, "*20% = ",sum )




