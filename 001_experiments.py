
string = "A man, a plan, a canal, Panama"
string_2 = ""

for c in string:
    if c.casefold() in "abcdefghijklmnopqrstuvwxyz":
        string_2 += c


print(string_2)
print(string_2[::-1])