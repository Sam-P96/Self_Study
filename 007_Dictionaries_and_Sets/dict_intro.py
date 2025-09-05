vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R1100",
    "er5": "Kawasaki ER5",
    "can-am": "Bombardier Can-Am 250",
    "virago": "Yamaha XV250",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "For Fiesta Chia 1.4",
}

my_car = vehicles["fiesta"]
print(my_car)

computer = vehicles["virago"]
print(computer)

learner = vehicles.get("er5") # .get("ER5") would return None, indexing would crash the program
print(learner)

#indexing would be faster, but sometimes you want to get an error instead of process
# bad data


