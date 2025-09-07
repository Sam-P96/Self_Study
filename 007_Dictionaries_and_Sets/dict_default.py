from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken {chicken_quantity}")

#the setdefault method returns the value, it behaves like get
# but it will return 0 if ti doesnt eixsts

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}") #we get 0 cus its not in the dict)

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}") # get the same result here, BUT it doesn't add the key to the dict

z_quantity = pantry.setdefault("Zucchini", "eight")

print(f"zucchini: {z_quantity}")
print()
print("Pantry now contains..")

for key, value in sorted(pantry.items()):
    # Notice how beans added the key, but ketchup is not added
    print(key, value)






