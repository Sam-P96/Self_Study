vehicles = {
    "dream": "Honda 250T",
    "er5": "Kawasaki ER5",
    "can-am": "Bombardier Can-Am 250",
    "virago": "Yamaha XV250",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "For Fiesta Chia 1.4",
    "roadster": "Triumph Street Triple",
}


vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade Virago
vehicles["virago"] = "Yamaha XV353" #each key in the dict is unique

del vehicles["starfighter"]
# del vehicles["f1"] #since f1 doesnt exist, it will crash
result = vehicles.pop("f1", "The great revolution starts today")
print(result)
print()
vehicles.pop("f1", None) # pop method removes an item and returns the value, if
#the key doesnt exist, then it will return what you passed as the default instead

plane = vehicles.pop("learjet")
print(plane)
print()
bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# for key in vehicles:
#     print(key, vehicles[key], sep = ", ")
for key, value in vehicles.items(): # .items() gives you the list of tuples
    print(key, value, sep = ", ")

