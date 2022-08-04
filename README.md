# Jacks or Better

Goal: Create an AI to figure out optimal strategy for the casino game Jacks or Better


## Game Rules:
- you are dealt 5 cards
- you have the option to choose which cards to keep
- any cards you dont keep are replaced by new cards from the remaining deck
- rewards are given out based on your 5 card hand

Details:
- 52 card (A-K, spade, heart, club, diamond deck)
- cards are dealt *without replacements*



## Main Components
### Classes
- game
- deck
- hand
- cards

### Functions
Game:
- reset game (start game)
- deal cards
- keep X cards
- show rewards
    - must compute for a given hand

Deck:
- reset deck
- get 1 card

Hand:
- show hand
- remove card
- add card
- reset hand

Cards:
- print card (mapping from int to K-spade, 10-heart, etc)
- get card (from int)
- get int (from card)


## Implementation Plan
- create the cards class
    - store card mappings as a dictionary
        - 0 -> A-spade ... 51 -> K-diamond
- create hand class
    - list of 5 Cards
    - add card (as int)
    - remove card (by index)
    - remove card (by int)
    - show hand (print Cards)
- create deck class
    - list of ints from 0-51
    - reset = reset to 0-51
    - get_one_card = remove 1 number from the current list randomly
- create game class
    - reset game
        - get new deck
        - 5x get_one_card
            - add these cards to hand class
- create rewards class
    - stores all of the static rewards
        - ex) pair = x2
              triple = x3
    - computes reward for a given hand
        - input: Hand()
        - output: int for reward value
        - if verbose -> print what rewards were hit (pair, triple, full house, etc)

## Progress
- finished card_class
- finished hand_class
- finished deck_class
- finished starting game and asking to replace cards in game_class
- started computing rewards
