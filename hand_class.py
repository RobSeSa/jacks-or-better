# Hand class

import card_class 
from card_class import Card
import numpy as np
from numpy import random

class Hand():
    def __init__(self):
        self.hand = []

    def reset(self):
        self.hand = []
    
    def add_card(self, card_num):
        assert len(self.hand) < 5, "Length of hand >= 5 when adding new card"
        assert card_num >= 0 and card_num < 52, f"{card_num} not a valid card number (0-51 inclusive)"
        for card in self.hand:
            if card.card_num == card_num:
                print("Error:", card_class.int_to_card[card_num], "already in hand")
                self.show_hand()
                return
        self.hand.append(Card(card_num))

    def add_card_by_index(self, new_card_num, i):
        assert len(self.hand) < 5, "Length of hand >= 5 when adding new card"
        for card in self.hand:
            if card.card_num == new_card_num:
                print("Error:", card_class.int_to_card[new_card_num], "already in hand when adding")
                self.show_hand()
                return
        self.hand.insert(i, Card(new_card_num))

    def get_card_by_index(self, i):
        assert len(self.hand) > 0, "Cannot get card from empty hand"
        assert i >= 0 and i < 5, f"Index {i} to get card from hand is invalid"
        return self.hand[i]
    
    def remove_card_by_index(self, i):
        assert len(self.hand) > 0, "Cannot remove card from empty hand"
        assert i >= 0 and i < 5, f"Index {i} to remove card from hand is invalid"
        self.hand.pop(i)
    
    def remove_card_by_card_num(self, card_num):
        assert len(self.hand) > 0, "Cannot remove card from empty hand"
        for i, card in enumerate(self.hand):
            if card.card_num == card_num:
                self.hand.pop(i)
                return
        assert False, f"Error: {card_num} not found in hand"
    
    def show_hand(self):
        print("Hand: ", end="")
        for card in self.hand:
            card.print()
            print(" ", end="")
        print()
    
    def __repr__(self):
        res = "Hand: "
        for card in self.hand:
            res += str(card)
            res += ' '
        return res
    
    def __str__(self):
        res = "Hand: "
        for card in self.hand:
            res += str(card)
            res += ' '
        return res
   
if __name__ == "__main__":
    print("Testing Hand class")

    h = Hand()
    h.add_card(4)
    #h.add_card(-1)
    h.add_card(50)
    h.show_hand()
    
    print("\nRemoving 50 or", card_class.int_to_card[50])
    h.remove_card_by_card_num(50)
    h.show_hand()

    h.add_card(5)
    h.add_card(6)
    h.add_card(8)
    h.show_hand()
            
    print("\nRemoving index 1")
    h.remove_card_by_index(1)
    h.show_hand()