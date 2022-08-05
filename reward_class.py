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

REWARDS = {
    'j_or_better':1,
    'pair':2,
    'triple':3,
    'straight':4,
    'flush':6,
    'full_house':9,
    'quad':25,
    'straight_flush':50,
    'royal_flush':800
    }
'''
each function returns either name_reward, value_reward
    ex) 'royal_flush', 800
or '', 0 if no reward
'''

#print(int_to_card)
#print(card_to_int)

def check_flushes(hand):
    # handles flush, straight flush and royal flush
    low_card = hand[0]
    high_card = hand[-1]

    spades = high_card <= 12
    hearts = low_card > 12 and high_card <= 25
    clubs = low_card > 25 and high_card <= 38
    diamonds = low_card > 38
    is_flush = spades or hearts or clubs or diamonds

    if is_flush:
        straight_val = is_straight_flush(hand) # 0 = not straight, 1 = straight flush, 2 = royal straight flush
        if straight_val == 0:
            return 'flush', REWARDS['flush']
        elif straight_val == 1:
            return 'straight_flush', REWARDS['straight_flush']
        elif straight_val == 2:
            return 'royal_flush', REWARDS['royal_flush']
        else:
            print("\n\n Error checking is_flush in reward_class.compute_rewards\nReceived straight_val:", straight_val)
    return '', 0

def is_straight_flush(hand):
    # 0 = not straight, 1 = straight flush, 2 = royal straight flush

    if hand[-1] - hand[0] == 4: # if max card is 4+ min card (2,3,4,5,6)
        return 1
    # check if royal flush straight: 0,9,10,11,12
    spades = hand == [0,9,10,11,12]
    hearts = hand == [13,22,23,24,25]
    clubs = hand == [26,35,36,37,38]
    diamonds = hand == [39,48,49,50,51]
    if spades or hearts or clubs or diamonds:
        return 2
    return 0



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
    print(is_straight_flush(hand_as_nums))



if __name__=='__main__':
    # Test straights
    straight_2_6 = Hand()
    for card_num in range(1,6):
        straight_2_6.add_card(card_num)
    print(straight_2_6)
    compute_rewards(straight_2_6)


    straight_A_5 = Hand()
    for card_num in range(5):
        straight_A_5.add_card(card_num)
    print(straight_A_5)
    compute_rewards(straight_A_5)