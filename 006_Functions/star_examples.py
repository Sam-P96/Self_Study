numbers = (0, 1, 2, 3, 4, 5)
numbers2 = 0, 1, 2, 3, 4, 5

# print(numbers)
# print(*numbers)
# print(0, 1, 2, 3, 4, 5) #same as this, it unpacks it


def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0, 1, 2, 3, 4, 5)
print()

test_star()
# # You can use * to unpack something, but you might never use it
# print(numbers, sep="; ")
# print(*numbers, sep="; ")
# print(0, 1, 2, 3, 4, 5, sep="; ")

