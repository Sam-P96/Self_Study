d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon'] # fromkey is a way to make a new dict

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)
if "four" in values: # using this to find the key for four, its inefficient tho
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items(): #more efficient
    if value == "four":
        print(f"{d[key]} was found with the key {key}")

# # Code for the dict update method lecture.
# d2 = {
#     7: "lucky seven",
#     10:"ten",
#     3: "this is the new three"
# }
#
# d.update(d2) # updates the list, keeps the original positions
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)



# # Code for "The remaining `dict` methods lecture.
# # new_dict = dict.fromkeys(pantry_items, 0)
# # print(new_dict)
#
# keys = d.keys()
# print(keys)
#
# for item in d.keys():
#     print(item)

