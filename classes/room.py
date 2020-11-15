class Room:
    # - Constructor - songs_in_room and guests are lists which store the playlist and the guests information
    def __init__(self, name, price, room_theme):
        self.name = name
        self.price = price
        self.room_theme = room_theme
        self.songs_in_room = []
        self.guests = []

    # - Method adds a song to the playlist cue for the room

    def add_song_to_room(self, song_name):
        self.songs_in_room.append(song_name)
    
    # - Method checks in a guest to the room

    def check_in_guest(self, guest_name, price, wallet):
        self.guests.append(guest_name)

    # - Method checks out a guest from the room

    def check_out_guest(self, guest_name):
        self.guests.remove(guest_name)
        
    # - Method clears guests from the list 

    def empty_room(self):
        self.guests.clear()

    # - Method adds a song by its full title - i.e artist and genre, to the playlist

    def add_song_to_room_playlist(self, song_name):
        self.songs_in_room.append(song_name)

    # - Method retrieves the length of the playlist

    def get_song_list_length(self):
        return len(self.songs_in_room)


    



