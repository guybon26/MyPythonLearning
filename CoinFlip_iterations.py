import random
def simulate_coin_flip(iterations):
    capital = 1000
    coinSide = ('H', 'T')

    def flipCoin():
        return random.choices(coinSide, cum_weights=[0.49, 0.51], k=1)[0]

    for i in range(iterations):
        if flipCoin() == 'T':
            capital += 1
        else:
            capital -= 1
    print(capital)

simulate_coin_flip(1000)
