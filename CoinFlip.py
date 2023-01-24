import random
capital = 1000
coinSide = ('H', 'T')
iterations = int(input("Enter number of iterations"))

def flipCoin():
    return random.choices(coinSide, cum_weights=[0.49, 0.51], k=1)[0]

for i in range(iterations):
    if flipCoin() == 'T':
        capital += 1
    else:
        capital -= 1
print(capital)
