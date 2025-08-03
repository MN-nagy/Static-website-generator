import math


def prime_factors(n):
    factors = []
    factored = n
    while True:
        if factored % 2 != 0:
            break
        factored //= 2
        factors.append(2)
    for i in range(3, int(math.sqrt(factored)) + 1):
        while factored % i == 0:
            factored //= i
            factors.append(i)
    if factored > 2:
        factors.append(factored)
    return factors
