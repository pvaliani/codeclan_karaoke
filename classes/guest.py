class Guest:

    # - Constructor - defines a guest by their name and wallet value 

    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet

    
    # - Method checks whether a customer can afford entry by comparing their wallet to the entry price of the room

    def customer_can_afford_entry(self, room):
        if self.wallet >= room.price:
            return True
        else:
            return False
    

    # - Method to allow customer to pay a bill by an amount from their wallet 

    def pay_the_bill(self, amount):
        self.wallet -= amount
    
    # - Method to find guests favourite track from the list of tracks in the playlist
    
    def find_favourite_song(self, room):
        for song in room.songs_in_room:
            if self.favourite_song == song.name:
                return "This is my fave jam!"