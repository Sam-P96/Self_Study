def sum_eo(n, t):
    total = 0
    if t == "e":
        for i in range(1,int(n)):
            if i % 2 == 0:
                total += i

    elif t == "o":
        for i in range(1,int(n)):
            if i % 2 != 0:
                total += i
    else:
        return -1

    return total


# n = int(input("Enter a number: "))
# t = input("Enter e for even or o for odd: ")
n = 10
t = "e"
print(sum_eo(n, t))
