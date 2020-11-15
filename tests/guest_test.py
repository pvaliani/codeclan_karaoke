import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Pedram Valiani", 50)

    # - This test determines that a song exists by comparing the object self.guest with attribute "name" to the value of "Pedram Valiani"

    # - self.guest.name reads as self.guest -> the guest object from classes.guest and .name is the attribute of the song as defined in the Guest class
    
    def test_guest_has_name(self):
        self.assertEqual(self.guest.name, "Pedram Valiani")
    
    # - Check that the guest has money in their wallet to pay a bill

    def test_guest_has_wallet_money(self):
        self.assertEqual(self.guest.wallet, 50)

    # - Check that a guest can pay a bill - use the entry as an example

    def test_customer_can_afford_entry(self):
        self.guest.pay_the_bill(3)
        self.assertEqual(47, self.guest.wallet)



