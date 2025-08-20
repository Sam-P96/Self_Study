print("This is a Celsius Fahrenheit converter")
program_select = input("""Please enter \"CF\" convert Celsius to Fahrenheit
Or enter \"FC\" convert Fahrenheit to Celsius""")

if program_select == "CF":
    celsius_input = int(input("Please enter the temperature in celsius:"))
    F_C = (celsius_input * 9 / 5) + 32
    print("The temperature in Fahrenheit is: {}".format(F_C))
elif program_select == "FC":
    fahrenheit_input = int(input("Please enter the temperature in fahrenheit:"))
    C_F = (fahrenheit_input - 32) * 5/9
    print("The temperature in Celsius is: {}".format(C_F))

#You can use float(input("....")) instead in the future so there's an option for decimal numbers