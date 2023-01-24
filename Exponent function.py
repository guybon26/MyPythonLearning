def expoCalc(base, exponent):
    result =1
    for i in range(exponent):
        result = result * base
    print(result)

expoCalc(2, 5)