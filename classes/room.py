class Room:
    def __init__(self, name, song_in_room, guests_in_room):
        self.name = name
        self.song_in_room = song_in_room
        self.guests_in_room = guests_in_room

    def add_song_to_room(self, song_name):
        self.song_in_room.append(song_name)

    def add_guest_to_room(self, guest_name):
        self.guests_in_room.append(guest_name)
