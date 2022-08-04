# Deck class
'''
- create deck class
    - list of ints from 0-51
    - reset = reset to 0-51
    - get_one_card = remove 1 number from the current list randomly
'''

from numpy import random

class Deck():
    def __init__(self):
        # initialize to 0-51 inclusive
        self.deck = [x for x in range(52)]

    def reset(self):
        self.deck = [x for x in range(52)]
    
    def get_one_card(self):
        assert len(self.deck) > 0, "Deck is out of cards; cannot get_one_card"
        # from the deck of cards, get a random card (number from list)
        card_num = self.deck.pop(random.randint(len(self.deck)))
        return card_num
    
    def show(self):
        print("Deck contents:", self.deck)

if __name__ == "__main__":
    print("Testing Deck class")
    d = Deck()
    d.show()

    c = d.get_one_card()
    print("Removed card:",c)
    d.show()

    d.reset()
    print("Reset deck")
    d.show()
    
        