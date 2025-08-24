albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

# for album in albums:
#     name, artist, year = album
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(name, artist, year))
# This one has the advantage of having ''album'' in the reference, but the other one is just more efficient.

for name, artist, year in albums:
    print("Album: {}, Artist {}, Year: {}"
          .format(name, artist, year))
# This one is preferable to the first one