class Duration:
    def __init__(self, duration):
        self.duration = duration

    def __str__(self):
        seconds_in_1min = 60
        seconds = self.duration
        minutes = seconds // seconds_in_1min
        seconds = seconds - (minutes * seconds_in_1min)
        return f"{minutes}:{seconds}"

    def value(self):
        return self.duration

class Track:
    def __init__(self, track_name, duration):
        self.track_name = track_name
        self.duration = Duration(duration)

    def get_track(self):
        return self.track_name

    def duration_seconds(self):
        return self.duration.value()

    def duration_string(self):
        return str(self.duration)



class Album:
    def __init__(self, artist, name, tracks):
        self.artist = artist
        self.name = name
        self.tracks = tracks

    def add_track(self, track_name, duration):
        track = Track(track_name, duration)
        self.tracks.append(track)

    def total_duration(self):
        total = 0
        for track in self.tracks:
            total += track.duration_seconds()
        return Duration(total)

    def __str__(self):
        return self.artist + ' - ' + self.name + ':  ' +  str(self.total_duration())

    # def list_tracks(self):
    #     for track in self.tracks:
    #         return track.

albums = [
    Album(artist = "Foals", name = "Holy Fire", tracks = [Track(track_name = "abc", duration = 145), Track(track_name = "def", duration = 123)]),
    Album(artist = "Bombay Bicycle Club", name = "I had the blues but i shook them loose", tracks = [])
    ]

# for album in albums:
#     for track in album.tracks:
#         print(track.get_track())


menu = {
    "1": "List Albums",
    "2": "Add Album",
    "3": "Update Album",
    "4": "Delete Album",
    "5": "List Albums By An Artist",
    "6": "List Album Tracks",
    "7": "Add Album Track",
    "8": "Exit"
}


def list_albums():
    for album in albums:
        print(album)


def add_album():
    artist = input("Please enter the artist: ")
    album_name = input("Please enter an album name: ")
    albums.append(Album(artist = artist, name = album_name))


def update_album():
    album_name_to_find = input("Which album would you like to update?: ")
    album_names = [album.name for album in albums]
    if album_name_to_find in album_names:
        position = album_names.index(album_name_to_find)
        del albums[position]
        album_name_to_update = input("Please enter the update to the album: ")
        artist_to_update = input("Please enter the update to the artist: ")
        albums.append(Album(artist = artist_to_update, name = album_name_to_update))
    else:
        print("Didn't find album")


def delete_album():
    album_delete = input("Which album would you like to delete?: ")
    album_names = [album.name for album in albums]
    if album_delete in album_names:
        position = album_names.index(album_delete)
        del albums[position]
    else:
        print("Album is not in list")


def albums_by_artist():
    artist = input("Please enter the artist: ")
    album_names = [album.artist for album in albums]
    if artist in album_names:
        return search_albums(artist)
    else:
        print("Artist does not exist")


def search_albums(artist):
    for album in albums:
        if album.artist == artist:
            print(album['Album Name'])


def list_album_tracks():
    album = input("Please enter the album name you would like to see the tracks for: ")
    album_names = [album.name for album in albums]
    if album in album_names:
        for album in albums:
            for track in album.tracks:
                print(track.get_track())
    else:
        print("Album does not exist")


def add_album_tracks():
    album = input("Please enter the album name you would like to add the track for: ")
    album_names = [album.name for album in albums]
    if album in album_names:
        track = input("Please enter the track: ")
        duration = input("Please enter the duration of this track in seconds")
        albums.append(Track(track_name = track, duration = duration))
    else:
        print("album does not exist")


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
        list_album_tracks()
    elif selection == "7":
        add_album_tracks()
    elif selection == "8":
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