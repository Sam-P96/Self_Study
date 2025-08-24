welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imdelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightning", "Metallica", 1984)

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

#in tuples, parenthesis are optional, but it's a good habit to use it
#indexing a tuple is similar to indexing a list, you use []
#Tuples doesn't support assigning a list, hence metallica[0] = "Master of Puppets" doesn't work
#creating a list (metallica2) allows us assigning something to the list
#Using a tuple for things that shouldn't change can help prevent bugs
#Yes, it might crash the code, but it'll be something we spot when testing the code