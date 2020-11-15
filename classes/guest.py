class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def customer_can_afford_entry(self, room):
        if self.wallet >= room.price:
            return True
        else:
            return False
    
    def pay_the_bill(self, amount):
        self.wallet -= amount