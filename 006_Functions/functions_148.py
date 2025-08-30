def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string (This is a little long, here's a shoter ver:
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string +=char

    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome" )