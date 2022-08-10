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
from hand_class import Hand
import card_class
from card_class import int_to_card, card_to_int
import numpy as np
from numpy import random

REWARDS = {
    'j_or_better':1,
    'two_pair':2,
    'triple':3,
    'straight':4,
    'flush':6,
    'full_house':9,
    'quad':25,
    'straight_flush':50,
    'royal_flush':800
    }

JACK_VALUE = card_to_int['J-spades']
ACE_VALUE = card_to_int['A-spades']
TEN_VALUE = card_to_int['10-spades']
'''
each function returns either name_reward, value_reward
    ex) 'royal_flush', 800
or '', 0 if no reward
'''


def get_nums_ignore_suits(hand):
    '''
    input: hand formatted as list of 5 nums (0-51)
    output: hand formatted as list of 5 nums (0-12)
    '''
    NUM_DIFF_CARDS = 13
    new_hand = [card % NUM_DIFF_CARDS for card in hand]
    return new_hand

def is_straight(hand):
    ace_straight = hand[0] == ACE_VALUE and hand[1] == TEN_VALUE
    other_straight = hand[0] == hand[-1] - 4
    if ace_straight or other_straight:
        return True
    else:
        return False

# https://codereview.stackexchange.com/questions/128702/poker-hands-in-python
def eval_hand(hand):
    values = get_nums_ignore_suits(hand)
    values.sort()

    straight = is_straight(values)

    # handle flush
    low_card = hand[0]
    high_card = hand[-1]

    spades = high_card <= 12
    hearts = low_card > 12 and high_card <= 25
    clubs = low_card > 25 and high_card <= 38
    diamonds = low_card > 38
    flush = spades or hearts or clubs or diamonds

    if straight and flush:
        if values[0] == ACE_VALUE and values[1] == TEN_VALUE:
            return 'royal_flush', REWARDS['royal_flush']
        else:
            return 'straight_flush', REWARDS['straight_flush']

    # check duplicates
    pairs = []
    pair_present = False
    three_of_a_kind = False
    three_value = None
    for v in set(values):
        if values.count(v) == 4:
            return 'quad', REWARDS['quad']
        if values.count(v) == 3:
            three_of_a_kind = True
            three_value = v
        if values.count(v) == 2:
            pair_present = True
            pairs.append(v)

    if three_of_a_kind and pair_present: return 'full_house', REWARDS['full_house']
    if flush: return 'flush', REWARDS['flush']
    if straight: return 'straight', REWARDS['straight']
    if three_of_a_kind: return 'triple', REWARDS['triple']
    if len(pairs) == 2: return 'two_pair', REWARDS['two_pair']
    if len(pairs) == 1 and (pairs[0] >= JACK_VALUE or pairs[0] == ACE_VALUE):
        return 'j_or_better', REWARDS['j_or_better']
    return None, 0

def compute_rewards(hand):
    # convert the hand from Card, Hand objects to raw ints
    print("Computing reward for:", hand)
    hand_as_nums = []
    for card in hand.hand:
        hand_as_nums.append(card.card_num)
    hand_as_nums.sort()

    # check each win type
    win_name, win_value = eval_hand(hand_as_nums)
    if win_name:
        print("Congratulations !!!\nYou got a", win_name, "for", win_value,"points!")
    else:
        print("Oh no! You didn't win anything!")
    return win_value



if __name__=='__main__':
    print(REWARDS)

    hands_to_try = {
        'straight 0-5':range(5),
        'straight 1-6':range(1,6),
        'random1':[4,5,10,42,51],
        'straight diff suit': [0,14,2,16,4],
        'straight ace high': [0,12,11,10,9],
        'pair 10': [0,1,2,9,22],
        '2 pair': [15, 28, 29, 10, 23],
        'Jacks': [14, 28, 29, 10, 23],
        'flush': [32,26,28,29,30],
        'royal_flush': [0,9,10,11,12],
        'non_spade_royal_flush': [26,35,36,37,38],
        'straight flush': [27,28,29,30,31],
        'quads': [3, 16, 29, 42, 50],
        'full_house': [3,16,29,50,24],
        'triple5': [4,17,30,6,49],
        'nothing': [4, 15, 19, 25, 40]
    }
    for name, hand in hands_to_try.items():
        print("\nTesting:", name)
        test_hand = Hand()
        for card_num in hand:
            test_hand.add_card(card_num)
        compute_rewards(test_hand)
