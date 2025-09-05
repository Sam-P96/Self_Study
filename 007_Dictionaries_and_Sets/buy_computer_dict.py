available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "HDMI cable",
                   "6": "DVD Drive"
                    }

current_choice = None
while current_choice != 0:
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print("Pleas select a valid option:")
        for idx, item in available_parts.items():
            print(idx, item, sep = ": ")
        print("0: to finish")

    current_choice = input("> ")
