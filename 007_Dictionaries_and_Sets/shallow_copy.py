import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# things = animals.copy() # was performing a shallow copy

things = copy.deepcopy(animals) # performs deep copy

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
