animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals.copy() # This is a shallow copy, so if you make changes
#to the original dict, when you use .copy(), it wont change accordingly.
animals["teddy"] = "toy"
print(things["teddy"])

