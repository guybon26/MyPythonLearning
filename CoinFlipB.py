import random
coinSide = ['H', 'T']
iteration = int(input("Please type the number of iterations"))
capital = 1000
def firstCoin():
    return random.choices(coinSide, cum_weights=[0.91, 0.09], k=1)[0]

def secondCoin():
    return random.choices(coinSide, cum_weights=[0.26, 0.74], k=1)[0]

for i in range(iteration):
    reminder = capital % 3
    if reminder==0:
       if firstCoin() == 'T':
           capital+=1
       else:
           capital-=1
    else:
        if secondCoin() == 'T':
            capital+=1
        else:
            capital-=1


print(capital)