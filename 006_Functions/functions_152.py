# # def multiply(x, y):
# #     result = x * y
# #     return result
# #
#
# def is_palindrome(string):
#     """
#     Checks if a `str` is a palindrome. Works only on singular words.
#         Function is not case-sensitive
#
#     :param string: Enter a `str` to check if it is a palindrome.
#     :return: True or False value
#     """
#     # backwards = string[::-1]
#     # return backwards == string (This is a little long, here's a shoter ver:
#     return string[::-1].casefold() == string.casefold()
#
#
# def palindrome_sentence(sentence):
#     """
#     A palindrome sentence checker. palindrome_sentence will not take
#         space and _ like fullstops and commas into consideration
#         when checking the palindrome. Function is not case-sensitive.
#
#     :param sentence: Enter a `str` in the form of a word or a sentence.
#     :return: True or False value
#     """
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string +=char
#
#     # return string[::-1].casefold() == string.casefold()
#     return is_palindrome(string)
#
#
# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome" )
#
# # answer = multiply(18,3)
# print(answer)


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None #Here we put result = None cus result doesnt have a value yet
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

for i in range(36):
    print(i, fibonacci(i))