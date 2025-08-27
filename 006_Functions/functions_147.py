def palindrome_sent(string):
    string_2 = ""
    for c in string:
        if c.casefold() in "abcdefghijklmnopqrstuvwxyz":
            string_2 += c
    return string_2[::-1].casefold() == string_2.casefold()

word = input("Please enter a sentence to check: ")
if palindrome_sent(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome" )