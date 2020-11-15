import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Beautiful Day", "U2")

    # - This test determines that a song exists by comparing the object self.song with attribute "name" to the value of "Beautiful Day by U2"

    # - self.song.name reads as self.song -> the song object from classes.song and .name is the attribute of the song as defined in the Song class

    def test_song_has_name(self):
        self.assertEqual(self.song.name, "Beautiful Day")

    # check that the song has an artist

    def test_song_has_artist(self):
        self.assertEqual(self.song.artist, "U2")

