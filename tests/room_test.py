import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 45, "Wild West")
        self.guest_1 = Guest("Michael Jackson", 50)
        self.guest_2 = Guest("50 Cent", 150)
        self.song_1 = Song("Beautiful Day", "U2")
        self.song_2 = Song("Bunsen", "Frontierer")
        self.song_3 = Song("Axe To Fall", "Converge")

    
    # - This test determines that a room name exists by comparing the object self.room with attribute "name" to the value of "Room 1"

    # - self.room.name reads as self.room -> the room object from classes.room and .name is the attribute of the room as defined in the Room class

    def test_room_has_name(self):
        self.assertEqual(self.room.name, "Room 1")


    def test_room_has__no_song_in_playlist(self):
        self.assertEqual(self.room.songs_in_room, [])

    def test_room_has_no_guests_checked_in(self):
        self.assertEqual(self.room.guests, [])

    # def test_room_doesnt_have_guest_checked_out(self):
    #     self.assertEqual(check_out_guest(self, guest_name), "")

    def test_room_has_price(self):
        self.assertEqual(self.room.price, 45)

    def test_room_has_theme(self):
        self.assertEqual(self.room.room_theme, "Wild West")

    def test_room_has__song_in_playlist(self):
        self.song_1 = Song("My Plague", "Slipknot")
        self.assertEqual(self.song_1.name, "My Plague")

    def test_length_of_playlist_in_room(self):
        self.room.add_song_to_room_playlist(self.song_1)
        self.room.add_song_to_room_playlist(self.song_2)
        self.room.add_song_to_room_playlist(self.song_3)
        length = self.room.get_song_list_length()
        self.assertEqual(3, length)



        

