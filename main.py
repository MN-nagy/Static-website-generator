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
        if factored % i == 0:
            j = i
            while True:
                if not factored % j == 0:
                    break
                factored //= j
                factors.append(j)
    if factored > 2:
        factors.append(factored)
    return factors
