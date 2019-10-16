# 1. Convert albums from a dict {} to a list []
# 2. Model an album as a dict { 'name': 'Holy Fire', 'artist': 'Foals'}
# intialize  function that saves the albums and prepopulates the albums


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


def list_albums():
    for album in albums:
        print(album["Name"],'-', album["Artist"])


def add_album():
    album_name = input("Please enter an album name: ")
    artist = input("Please enter the artist: ")
    albums.append({"Artist": artist, "Name": album_name})


def update_album():
    # 1) Ask user for the name of the album to update.
    album_name_to_find = input("Which album would you like to update?: ")

    # 2) See if album exists in music store.
    album_names = [album["Name"] for album in albums]
    if album_name_to_find in album_names:
        print("Found Album")



    else:
        print("Didn't find album")


    # 3) If album does exist, then ask user for the update they would like to make to the album name.
    # 4) If the album does not exist, tell the user, album does not exist in store.


    # if album_update_question in albums[values]:
    #     position = album_names.index(album_update_question)
    #     del albums[position]
    #     album_update_modify = input("Please enter the update you would like to make: ")
    #     albums.insert(position, (album_update_modify))
    # else:
    #     print("Album does not exist")


# def delete_album():
#     album_delete = input("Which album would you like to delete?: ")
#     if album_delete i
#         position = album_names.index(album_delete)
#         del albums[position]
#     else:
#         print("Specified album not in stock")


def albums_by_artist():
    artist = input("Please enter the artist: ")
    for key,value in dict in albums:
        if value == artist:
            print(value)
        else:
            print("Specified album not in stock")
    # if artists exist as key in albums
    # retrieve value of the artist
    # if not, print a string saying this inputted artist is not currently in stock.


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

