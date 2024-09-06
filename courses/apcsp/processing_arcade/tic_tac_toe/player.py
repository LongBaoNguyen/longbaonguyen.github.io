import random
from state import *


class Player:
    # @step_size: the step size to update values
    # @epsilon: the probability to explore
    def __init__(self, symbol=1, step_size=0.1, epsilon=0.1):
        self.estimations = dict()
        self.step_size = step_size
        self.epsilon = epsilon
        self.states = []
        self.greedy = []
        self.symbol = symbol

    def reset(self):
        self.states = []
        self.greedy = []

    def set_state(self, state):
        self.states.append(state)
        self.greedy.append(True)

    def init_estimations(self):
        for hash_val in all_states:
            state, is_end = all_states[hash_val]
            if is_end:
                if state.winner == self.symbol:
                    self.estimations[hash_val] = 1.0
                elif state.winner == 0:
                    # we need to distinguish between a tie and a lose
                    self.estimations[hash_val] = 0.5
                else:
                    self.estimations[hash_val] = 0
            else:
                self.estimations[hash_val] = 0.5

    # update value estimations
    def backup(self):
        states = [state.hash() for state in self.states]

        for i in reversed(range(len(states) - 1)):
            state = states[i]
            td_error = self.greedy[i] * (
                self.estimations[states[i + 1]] - self.estimations[state]
            )
            self.estimations[state] += self.step_size * td_error

    # choose an action based on the state
    def act(self):
        state = self.states[-1]
        next_states = []
        next_positions = []
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if state.data[i][j] == 0:
                    next_positions.append([i, j])
                    next_states.append(state.next_state(
                        i, j, self.symbol).hash())

        if random.random() < self.epsilon:
            action = next_positions[random.randrange(len(next_positions))]
            action.append(self.symbol)
            self.greedy[-1] = False
            return action

        values = []
        for hash_val, pos in zip(next_states, next_positions):
            values.append((self.estimations[hash_val], pos))
        # to select one of the actions of equal value at random due to Python's sort is stable
        random.shuffle(values)
        values.sort(key=lambda x: x[0], reverse=True)
        action = values[0][1]
        action.append(self.symbol)
        return action

    def save_policy(self):
        save_p = ""
        for k, v in self.estimations.items():
            save_p += (str(k) + "," + str(v) + " ")
        save_p.rstrip()
        l = split(save_p, ' ');
        if self.symbol == 1:
            saveStrings("data/datap1.txt", l)
        elif self.symbol == -1:
            saveStrings("data/datap2.txt", l)

        
    def load_policy(self):
        if self.symbol == 1:
            lines = loadStrings("data/datap1.txt")
        elif self.symbol == -1:
            lines = loadStrings("data/data_p2_100k.txt")
        for i in range(len(lines)):
            data = split(lines[i], ',');
            try:
                h, v = int(float(data[0])), float(data[1])
                self.estimations[h] = v
            except:
                print("error reading from file")
    

        
