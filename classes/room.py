class Room:
    def __init__(self, name, price, room_theme):
        self.name = name
        self.price = price
        self.room_theme = room_theme
        self.songs_in_room = []
        self.guests = []


    def add_song_to_room(self, song_name):
        self.songs_in_room.append(song_name)

    def check_in_guest(self, guest_name, price, wallet):
        self.guests.append(guest_name)

    def check_out_guest(self, guest_name):
        self.guests.remove(guest_name)

    def add_song_to_room_playlist(self, song_name):
        self.songs_in_room.append(song_name)

    def get_song_list_length(self):
        return len(self.songs_in_room)



