def factorial(n):
    if n <= 1:
        return 1
    result = 2
    for x in range(2 + 1, n + 1):
        result *= x
        print(x)
        print(result)

    return result

factorial(3)