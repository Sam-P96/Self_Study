menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    while "spam" in meal:
        meal.remove("spam")
for meal in menu:
    print(meal)

menu_2 = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "spam", "spam", "bacon", "spam"],
]

for meal_2 in menu_2:
    meal_2 = [item for item in meal_2 if item != "spam"]
    print(meal_2)