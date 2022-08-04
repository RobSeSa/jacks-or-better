# Card class

import numpy as np
from numpy import random


SUITS = ['spades', 'hearts', 'clubs', 'diamonds']
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
ALL_CARDS = []
for suit in SUITS:
    for card in CARDS:
        ALL_CARDS.append(card+'-'+suit)

card_to_int = dict()
int_to_card = dict()

for num, card_name in enumerate(ALL_CARDS):
    card_to_int[card_name] = num
    int_to_card[num] = card_name

class Card():
    def __init__(self, card_num):
        self.card_num = card_num
        self.card_name = int_to_card[card_num]
    
    def print(self):
        print(self.card_name, end="")
        
    def __repr__(self):
        return self.card_name
    
    def __str__(self):
        return self.card_name

   
if __name__ == "__main__":
    print("Testing Card class")

    for _ in range(5):
        x = random.randint(0, 52)
        c = Card(x)
        print("random int:",x, "printed:")
        print(c)
