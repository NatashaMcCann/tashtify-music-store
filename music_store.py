albums = [
    {
        "Artist": "Foals",
        "Name": "Holy Fire"
    },
    {
        "Artist": "Bombay Bicycle Club",
        "Name": "I had the blues but i shook them loose"
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


#DONE
def list_albums():
    for album in albums:
        print(album["Name"],'-', album["Artist"])


#DONE
def add_album():
    album_name = input("Please enter an album name: ")
    artist = input("Please enter the artist: ")
    albums.append({"Artist": artist, "Name": album_name})


#DONE
def update_album():
    album_name_to_find = input("Which album would you like to update?: ")
    album_names = [album["Name"] for album in albums]
    if album_name_to_find in album_names:
        position = album_names.index(album_name_to_find)
        del albums[position]
        album_name_to_update = input("Please enter the update to the album: ")
        artist_to_update = input("Please enter the update to the artist: ")
        albums.append({"Artist": artist_to_update, "Name": album_name_to_update})
    else:
        print("Didn't find album")


#DONE
def delete_album():
    album_delete = input("Which album would you like to delete?: ")
    album_names = [album["Name"] for album in albums]
    if album_delete in album_names:
        position = album_names.index(album_delete)
        del albums[position]
    else:
        print("Album is not in list")


def albums_by_artist():
    artist = input("Please enter the artist: ")
  


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

