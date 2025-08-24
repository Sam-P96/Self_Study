number = input("Enter 3 numbers in the format \"a,b,c\"")

number_split = number.split(",")
# print(number_split)

number_int = []
for num in number_split:
    number_int.append(int(num))

# print(number_int)
jolly = number_int[0] + number_int[1] - number_int[2]
print(jolly)