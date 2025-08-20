print("Please choose your option from the list below: \n 1. Learn Python \n 2. Learn Java \n 3. Go Swimming \n 4. Have Dinner \n 5. Go to bed \n 0. Exit")
user_input = int(input("Choose your option here:"))
while user_input != 0:
    if user_input >=1 and user_input <=5:
        print("Congratulations, you chose to do {}! \n Please choose another option from the list below: \n 1. Learn Python \n 2. Learn Java \n 3. Go Swimming \n 4. Have Dinner \n 5. Go to bed \n 0. Exit".format(user_input))
        user_input = int(input(("Make your choice here:")))
        continue
    else:
        user_input = int(input("Please choose a valid option"))
        continue
else:
    print("You have chosen to exit, goodbye.")