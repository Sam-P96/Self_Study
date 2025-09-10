lion_list = ["scary", "big", "cat"]
ele_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": ele_list,
    "teddy": teddy_list,
}

# things = animals.copy() # This is a shallow copy, so if you make changes
#to the original dict, when you use .copy(), it wont change accordingly.
things = { # this is what .copy is doing
    "lion": lion_list,
    "elephant": ele_list,
    "teddy": teddy_list,
}

print(things["teddy"])
print(animals["teddy"])

print()

teddy_list.append("toy")
animals["teddy"].append("either list we append to")
things["teddy"].append("it will append to the same list in .copy")
print(things["teddy"])
print(animals["teddy"])
