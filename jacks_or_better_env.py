import gym
from gym import spaces

import reward_class
from reward_class import compute_rewards
from game_class import Game
import numpy as np

N_DISCRETE_ACTIONS = 2**5
NUM_CARDS = 5

class JacksOrBetterEnvironment(gym.Env):
    """Jacks or Better Environment that follows gym interface"""

    def __init__(self):
        super(JacksOrBetterEnvironment, self).__init__()
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(low=0, high=51, shape=(5,), dtype=np.uint8)
        self.game = Game()

    def get_indiv_actions(self, action):
        # convert integer (0-15) to list of 5 actions (1=KEEP,0=REPLACE)
        res = []
        for i in range(NUM_CARDS):
            res.append((action >> i) % 2)
        return res

    def step(self, action):
        # Execute one time step within the environment
        obs = self._take_action(action)
        reward = compute_rewards(self.game.hand)
        reward -= 1 # every time you play, you lose $1
        done = True
        return obs, reward, done, {}

    def _take_action(self, action):
        actions = self.get_indiv_actions(action)
        # debug print
        print("You are taking actions:")
        for i, action in enumerate(actions):
            if action:
                print("Keeping card", i)
            else:
                print("Replace card:", i)
        KEEP_CARD_VALUE = 1
        GET_NEW_CARD_VALUE = 0
        for i in range(NUM_CARDS):
            # keep or get new card for each
            if actions[i] == KEEP_CARD_VALUE:
                continue
            elif actions[i] == GET_NEW_CARD_VALUE:
                new_card_num = self.game.deck.get_one_card()
                self.game.hand.remove_card_by_index(i)
                self.game.hand.add_card_by_index(new_card_num=new_card_num, i=i)
            else:
                print("Error: got invalid action[i] value of:", action[i])

        # update the observation to the new hand
        hand_as_nums = [c.card_num for c in self.game.hand.hand]
        obs = np.asarray(hand_as_nums)
        return obs



    def reset(self):
        # Reset the state of the environment to a random hand
        self.game.reset()
        hand_as_nums = [c.card_num for c in self.game.hand.hand]
        obs = np.asarray(hand_as_nums)
        return obs

    def render(self, mode='human', close=False):
        # Render the environment to the screen
        print(self.game.hand)