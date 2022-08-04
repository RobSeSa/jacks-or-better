# Jacks or Better Game class
'''
## Game Rules:
- you are dealt 5 cards
- you have the option to choose which cards to keep
- any cards you dont keep are replaced by new cards from the remaining deck
- rewards are given out based on your 5 card hand

Game:
- reset game (start game)
- deal cards
- keep X cards
- show rewards
    - must compute for a given hand
'''

import card_class
from card_class import Card
import hand_class
from hand_class import Hand
import deck_class
from deck_class import Deck
import reward_class

import numpy as np
from numpy import random

class Game():
    def __init__(self):
        '''
        - create deck of cards
        - create hand
        - add 5 random cards from deck of cards to hand
        '''
        self.deck = Deck()
        self.hand = Hand()

        # add 5 cards from deck to hand
        for _ in range(5):
            card_num = self.deck.get_one_card()
            self.hand.add_card(card_num)
    
    def reset(self):
        self.deck.reset()
        self.hand.reset()

        # add 5 cards from deck to hand
        for _ in range(5):
            card_num = self.deck.get_one_card()
            self.hand.add_card(card_num)
    
    def show_starting_cards(self):
        print("Your starting hand:")
        self.hand.show_hand()
    
    def ask_to_replace_cards(self):
        print("Enter \'y\' to keep card and \'n\' to replace")
        for i in range(5):
            print("Would you like to keep", self.hand.get_card_by_index(i), "? (y/n)")
            ans = input()
            invalid_answer = (not ans == 'y') and (not ans == 'n')
            while invalid_answer:
                print("Invalid reply.")
                print("Would you like to keep", self.hand.get_card_by_index(i), "? (y/n)")
                ans = input()
                invalid_answer = (not ans == 'y') and (not ans == 'n')

            if ans == 'y':
                #print("Keeping", self.hand.get_card_by_index(i))
                continue
            elif ans == 'n':
                new_card_num = self.deck.get_one_card()
                self.hand.remove_card_by_index(i)
                self.hand.add_card_by_index(new_card_num=new_card_num, i=i)
                #print("Replaced the card to:", self.hand.get_card_by_index(i))
            else:
                print("### Error replacing cards: Received response not y/n when keeping card")
    
    def get_game_results(self):
        pass
    
    # Printing functions
    def show_deck(self):
        self.deck.show()
    
    def show_hand(self):
        self.hand.show_hand()
    
    def show_all(self):
        self.show_deck()
        self.show_hand()



if __name__ == "__main__":
    print("Testing Game class")
    g = Game()
    g.show_all()

    g.show_starting_cards()

    g.reset()
    print("Showing game after reseting:")
    g.show_all()

    g.ask_to_replace_cards()
    print("Game after asking to replace:")
    g.show_all()

    print("Getting reward from final hand")
    reward_class.compute_rewards(g.hand)
