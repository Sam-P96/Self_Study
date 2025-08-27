
string = "go go power rangers"
string_2 = []
string_3 = []

for c in string:
    string_2 += c

for c in string_2:
    if c != " ":
        string_3 += c

print(string_2)
print(string_3.join(""))