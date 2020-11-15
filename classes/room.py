class Room:
    def __init__(self, name, song_in_room, guests, price, room_theme):
        self.name = name
        self.song_in_room = song_in_room
        self.guests = guests
        self.price = price
        self.room_theme = room_theme

    def add_song_to_room(self, song_name):
        self.song_in_room.append(song_name)

    def check_in_guest(self, guest_name):
        self.guests.append(guest_name)

    def check_out_guest(self, guest_name):
        self.guests.remove(guest_name)

