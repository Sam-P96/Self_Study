vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R1100",
    "er5": "Kawasaki ER5",
    "can-am": "Bombardier Can-Am 250",
    "virago": "Yamaha XV250",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "For Fiesta Chia 1.4",
    "roadster": "Triumph Street Triple" # insertion order changes the value
#you will get t warning
}


vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade Virago
vehicles["virago"] = "Yamaha XV353" #each key in the dict is unique

# for key in vehicles:
#     print(key, vehicles[key], sep = ", ")
for key, value in vehicles.items(): # .items() gives you the list of tuples
    print(key, value, sep = ", ")

