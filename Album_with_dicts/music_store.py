###WITH A LIST OF DICTIONARIES
put albums in

konstructor method that takes these two properties in a class

albums = [
    {
        "Artist": "Foals",
        "Album Name": "Holy Fire"
    },
    {
        "Artist": "Bombay Bicycle Club",
        "Album Name": "I had the blues but i shook them loose"
    }
]


menu = {
    "1": "List Albums",
    "2": "Add Album",
    "3": "Update Album",
    "4": "Delete Album",
    "5": "List Albums By An Artist",
    "6": "Exit"
}



# This function lists all the Album Names in the music store. It iterates over each album in the store and returns each
# album name on a new line.
def list_albums():
    for album in albums:
        print(album["Album Name"],'-', album["Artist"])


# This function adds an album into the music store. It firstly asks for two inputs from the end user. The album name,
# which prompts the user to enter the name of the artist, followed by the album by the artist. This then appends a dictionary
# to the list of albums with each result of the input function assigned using a variable
def add_album():
    artist = input("Please enter the artist: ")
    album_name = input("Please enter an album name: ")
    albums.append({"Artist": artist, "Album Name": album_name})


# poss room for a bit of refactoring.
# This function updates a pre existing album in the music store. It firstly asks for an input from the end user assigned to a variable
# album name to find. This asks the user for the album they would like to update. An iteration of Album Name is then assigned to a variable
# album names which iterates over each album in the albums list of dictionaries, specifically hitting the album name.
# We then have an if else statement that checks that that album exists in the list. If it does exist, the position variable indexes within
# the album name variable with the result of the input function album name to find and finds the position of the input in the list.
# It then deletes the album at that position. There are then two further input functions, one that makes the update to the album and the other to the artist.
# It then appends the result of each input into a new dictionary.
# NEED TO FIND A WAY TO ONLY REPLACE ALBUM NAME, BUT UNSURE HOW TO DO THIS IN A LIST OF DICTIONARIES OR WHETHER ITS EVEN POSSIBLE
def update_album():
    album_name_to_find = input("Which album would you like to update?: ")
    album_names = [album["Album Name"] for album in albums]
    if album_name_to_find in album_names:
        position = album_names.index(album_name_to_find)
        del albums[position]
        album_name_to_update = input("Please enter the update to the album: ")
        artist_to_update = input("Please enter the update to the artist: ")
        albums.append({"Artist": artist_to_update, "Album Name": album_name_to_update})
    else:
        print("Didn't find album")


# This function deletes an album from albums. It firstly takes an input asking the end user which album they would like to delete
# it then iterates over each album in albums, specifying the album name key. If the inputted result is in album names which is the iteration,
# it finds the position of the album (dictionary) in the list and removes it. If it doesnt exist, it prints album is not in the list.
def delete_album():
    album_delete = input("Which album would you like to delete?: ")
    album_names = [album["Album Name"] for album in albums]
    if album_delete in album_names:
        position = album_names.index(album_delete)
        del albums[position]
    else:
        print("Album is not in list")


# This function lists each album by an artist. It firstly takes an input asking the end user for the name of the artist.
# It then iterates over each album in albums looking for the Artist key. This is assigned to a variable called album names.
# It then checks the value of artist matches up to the keys in albums. It will then return the function search albums, with artist
# passed in as the parameter. The search albums function essentially iterates over each album in albums again. Looks for the artist key
# in album and checks its equal to artist (checking that it exists). It then prints the album name from artist, so returns the album name
# associated with that artist in the dictionary.
def albums_by_artist():
    artist = input("Please enter the artist: ")
    album_names = [album["Artist"] for album in albums]
    if artist in album_names:
        return search_albums(artist)
    else:
        print("Artist does not exist")


def search_albums(artist):
    for album in albums:
        if album["Artist"] == artist:
            print(album['Album Name'])


def show_menu():
    for key, value in menu.items():
        print (key, value)


def handle_selection(selection):
    if selection == "1":
        list_albums()
    elif selection == "2":
        add_album()
    elif selection == "3":
        update_album()
    elif selection == "4":
        delete_album()
    elif selection == "5":
        albums_by_artist()
    elif selection == "6":
        exit()
    else:
        print("unknown option selected")


def main():
    while True:
        show_menu()
        selection=input("Please choose an option: ")
        handle_selection(selection)

if __name__ == "__main__":
    main()

