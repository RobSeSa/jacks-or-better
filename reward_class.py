# Rewards class
'''
- stores all of the static rewards
    - ex) pair = x2
        triple = x3
- computes reward for a given hand
    - input: Hand()
    - output: int for reward value
    - if verbose -> print what rewards were hit (pair, triple, full house, etc)
'''

'''
implementation
- create dictionary of rewards; key=name, value=amount reward
- create function to check each win type (pair, straight, etc)

Assume all inputs to indiv check functions are sorted integer version of hand
'''

import hand_class
import card_class
from card_class import int_to_card, card_to_int

REWARDS = {
    'pair':2,
    'triple':3
    }

print(int_to_card)
print(card_to_int)

def is_straight(hand):
    for i in range(len(hand)-1):
        if not hand[i] + 1== hand[i+1]:
            return False
    return True

def is_flush(hand):
    low_card = hand[0]
    high_card = hand[-1]

    spades = high_card <= 12
    hearts = low_card > 12 and high_card <= 25
    clubs = low_card > 25 and high_card <= 38
    diamonds = low_card > 38

    if spades or hearts or clubs or diamonds:
        return True
    return False

def compute_rewards(hand):
    # convert the hand from Card, Hand objects to raw ints
    print("Computing reward for:", hand)
    hand_as_nums = []
    for card in hand.hand:
        hand_as_nums.append(card.card_num)
    print("Numerical rep of hand:", hand_as_nums)
    hand_as_nums.sort()
    print("After sorting:", hand_as_nums)

    # check each win type