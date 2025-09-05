available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "HDMI cable",
                   "6": "DVD Drive"
                    }

current_choice = None
computer_parts = {}

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            del computer_parts[chosen_part]
        else:
            print(f"Adding {chosen_part}")
            computer_parts[chosen_part] = chosen_part
            print(f"Your list now contains: {chosen_part}")
    else:
        print("Pleas select a valid option:")
        for idx, item in available_parts.items():
            print(idx, item, sep = ": ")
        print("0: to finish")

    current_choice = input("> ")
