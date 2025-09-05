def factorial(n: int) -> int:
    if n <= 1:
        return 1
    result = 2
    for x in range(2 + 1, n + 1):
        result *= x

    return result


for i in range(36):
    print(i, factorial(i))


# think of factorial multiplying the factors from low to high, its easer to understand