import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Pedram Valiani")

    # - This test determines that a song exists by comparing the object self.guest with attribute "name" to the value of "Pedram Valiani"

    # - self.guest.name reads as self.guest -> the guest object from classes.guest and .name is the attribute of the song as defined in the Guest class
    
    def test_guest_has_name(self):
        self.assertEqual(self.guest.name, "Pedram Valiani")

