def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*")
banner_text("BITCH")
banner_text("I SAID WHAT I SAID")
banner_text("something something instead...")
banner_text("*")

result = banner_text("Hi hi")
print(result) #There will be a "None" after the "Hi hi"

# All functions in python returns something, if there's nothing, it returns ''None''
# In this case, we just choose not to use the return feature, instead we make it do something

numbers = [4, 3, 6, 7, 9]
print(numbers.sort()) #None
#This will print out None, cus .sort sorts the numbers in place, it doesnt return a value
numbers.sort() # us it this way to sort the numbers
print(numbers)
