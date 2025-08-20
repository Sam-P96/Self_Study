panagram = """The quick brown 
fox jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036, 854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']

values = "".join(generated_list)
print(values)

value_list = values.split()
print(value_list)

# int_list = []
# for numbers in values_list:
#     num = int(numbers)
#     int_list.append(num)
#
# print(int_list)

#One way is to replace the values in place
for index in range(len(value_list)):
    value_list[index] = int(value_list[index])

print(value_list)


# Notes from 0000_doodle_0000

# You have this generated list from some function I dont remember:

# generated_list = ['9', ' ',
#                   '2', '2', '3', ' ',
#                   '3', '7', '2', ' ',
#                   '0', '3', '6', ' ',
#                   '8', '5', '4', ' ',
#                   '7', '7', '5', ' ',
#                   '8', '0', '7']
#
# print(generated_list)
#
# values = "".join(generated_list)
# print(values)
#
# # The .join method is used to concatenate all the elements in a list into a single string
#
# value_list = values.split()
# print(value_list)
#
# # The .split function turns it into a str list
#
# value_list_int = []
# # We create an empty list, assigning a name to it and use an empty []
#
# for numbers in value_list:
#     value_list_int.append(int(numbers))
#
# # A for loop was use to go through the list, turning all the str in the list
# # into int
#
# print(value_list_int)
