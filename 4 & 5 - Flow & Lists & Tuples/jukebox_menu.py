from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exist):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, title))
    choice = int(input("Select: "))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        print("="*10 + "Invalid selection" + "="*10)
        continue

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        print("="*10 + "Invalid selection" + "="*10)
        continue

    print("Playing: {}".format(title))
    print("="*40)

# Another way to write the for loop
#     for index, value in enumerate(albums):
#         title, artist, year, songs = value
#         print(index + 1, title, artist, year, songs)
# if 1 <= choice <= len(albums) is read as ''if choice is greater than
# or equal to 1, and smaller than or equal to length of albums''
# songs_list = albums[choice -1][3] [edited to better understand index for layman][the 4th choice, so the song list]
# SONG_LIST_INDEX is written in all caps to represent a constant, it's just a variable
# It's written like that to mark it as a constant, its kind of like a tradition
# Not an actual feature or function, but it represents a value that shouldn't be changed
