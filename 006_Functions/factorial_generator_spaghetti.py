def list_maker(x):
    list_m = []
    for i in range(x):
        if i != 0:
            list_m.append(i)

    return list_m

print(list_maker(6))

def factorial_1(x):
    num = 1
    list1 = list_maker(x)
    for number in list1:
        num *= number

    return num

print(factorial_1(6))

def factorial(x: int) -> str:
    """
    prints out multiple lines of a number and its factorial.
    :param x: number'th to factorial
    :return: None
    """
    for i in range(x):
        print(i, factorial_1(i))

factorial(6)

