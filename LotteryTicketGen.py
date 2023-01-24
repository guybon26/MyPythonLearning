import random

population = range(1000)

N = int(input('Please type a number of tickets to generate'))

print(random.sample(population, N))
