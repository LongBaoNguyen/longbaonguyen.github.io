from state import *
from player import *

class TrainAI:
    # @player1: the player who will move first, its chessman will be 1
    # @player2: another player with a chessman -1
    def __init__(self, epochs, print_every_n=500):
        self.p1 = Player(symbol=1, epsilon=0.01)
        self.p2 = Player(symbol=-1, epsilon=0.01)

        self.p1.init_estimations()
        self.p2.init_estimations()

        player1_win = 0.0
        player2_win = 0.0
        
        for i in range(1, epochs + 1):
            winner = self.play(print_state=False)
            if winner == 1:
                player1_win += 1
            if winner == -1:
                player2_win += 1
            if i % print_every_n == 0:
                print('Epoch %d, player 1 winrate: %.02f, player 2 winrate: %.02f' % (i, player1_win / i, player2_win / i))
            self.p1.backup()
            self.p2.backup()
        self.p1.save_policy()
        self.p2.save_policy()

        

    def reset(self):
        self.p1.reset()
        self.p2.reset()
        

    def alternate(self):
        while True:
            yield self.p1
            yield self.p2

    # @print_state: if True, print each board during the game
    def play(self, print_state=False):
        alternator = self.alternate()
        self.reset()
        current_state = State()
        self.p1.set_state(current_state)
        self.p2.set_state(current_state)
        if print_state:
            current_state.print_state()
        while True:
            player = next(alternator)
            i, j, symbol = player.act()
            next_state_hash = current_state.next_state(i, j, symbol).hash()
            current_state, is_end = all_states[next_state_hash]
            self.p1.set_state(current_state)
            self.p2.set_state(current_state)
            if print_state:
                current_state.print_state()
            if is_end:
                return current_state.winner
