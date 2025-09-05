def fizz_buzz(x: int) -> str:
    """
    the number entered is checked if it is divisible by both 3 & 5,
    or 5 or 3 alone, or neither.
    :param x: the number being checked
    :return: the corresponding answer or the number back out if
    it is neither divisible by 3 nor 5.
    """
    if x % 3 == 0 and x % 5 == 0:
        result = "fizz buzz"
    elif x % 5 == 0:
        result = "buzz"
    elif x % 3 == 0:
        result = "fizz"
    else:
        result = str(x)
    return result

for i in range(1,101):
    # print(fizz_buzz(i))
    if i % 2 == 0:
        p_g = input("Your Turn: ")
        if fizz_buzz(i) == p_g.casefold():
            continue
        else:
            print("YOU LOSE")
            break
    else:
        print(fizz_buzz(i))