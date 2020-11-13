import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", "Beautiful Day by U2", "Pedram Valiani")
    
    # - This test determines that a room name exists by comparing the object self.room with attribute "name" to the value of "Room 1"

    # - self.room.name reads as self.room -> the room object from classes.room and .name is the attribute of the room as defined in the Room class

    def test_room_has_name(self):
        self.assertEqual(self.room.name, "Room 1")

    # - This test checks that the room has a song by comparing the self.room instance object with the 2nd parameter of the room instance

    def test_room_has_song(self):
        self.assertEqual(self.room.song_in_room, "Beautiful Day by U2")

    # - This test checks that the room has a guest by comparing the self.guest instance object with the 3rd parameter of the room instance

    def test_room_has_guest(self):
        self.assertEqual(self.room.guests_in_room, "Pedram Valiani")
        

