import random

coinSide = ('H', 'T')
capital = 1000
iteration = int(input("Please set the number of iterations: "))

def coinGameA():
    flipCoin = random.choices(coinSide, cum_weights=[0.49, 0.51], k=1)[0]
    if flipCoin == 'T':
        capital+=1

    else:
        capital-=1

def coinGameB():
     reminder = capital % 3
     if reminder == 0:
        flipCoin = random.choices(coinSide, cum_weights=[0.91, 0.09], k=1)[0]
        if flipCoin == 'T':
            capital+=1
            elif:
            capital-=1

        else:
        flipCoin = random.choices(coinSide, cum_weights=[0.26, 0.74], k=1)[0]
        if flipCoin == 'T':
            capital += 1
        else:
            capital -= 1

for i in range(iteration):
        if random.choice(coinSide)=='T':
          coinGameA()
          else:
          coinGameB()

print(capital)
