"""
AI Tic Tac Toe Lab

Most of the code is given including all code to play 
the game manually(must implement legalMoves() first before playing).


To complete this project, complete the following code from the files in this recommended
order:


In this file(game.py), you only need to go to 

Look for "TODO".

IMPLEMENT ALL PARTS LABELED "TODO".
"""


from __future__ import division, print_function
from state import *
from player import *
from train import *

import random

WIDTH = 600 # width of screen in pixels
HEIGHT = 600 # height of screen in pixels
SIZESQUARE = WIDTH // 3

BACKGROUND_COLOR = color(255)  # 0(black), 255(white)


class Window:    
    def __init__(self):
        """ Declare and initialize your variables. 
            When declaring/initializing a global variable that is used throughout 
            the game, use self and the dot notation.
            For example:
            self.lives = 3
            self.score = 0
        """
        self.set_up()
        
        
    def set_up(self):
        # Human Player: Player 1, AI Player: Player 2
        
        # if not yet trained, call self.train_play
        # otherwise call self.load_policy_play
        
        #self.train_play()
        self.load_policy_play()
        
    def train_play(self):
        # only run this the first time; subsequent runs do not require retraining:
        # call load_policy_play below to load the trained model and play
        ai_trainer = TrainAI(100000)
        self.load_policy_play()

    def load_policy_play(self):
        self.current_player = 1
        self.game_over = False
        self.winner = None
        self.current_state = State()
        self.ai_player = Player(symbol=-1, epsilon=0)
        self.ai_player.load_policy()
        self.ai_player.set_state(self.current_state)
        print(len(self.ai_player.estimations))
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
    
        strokeWeight(8)
        fill(255, 0, 0)
        for i in range(1, 3):
            line(i*SIZESQUARE, 0, i*SIZESQUARE, HEIGHT)
        for i in range(1, 3):
            line(0, i*SIZESQUARE, WIDTH, i*SIZESQUARE)
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.current_state.data[i][j] == -1:
                    noFill()
                    ellipse(100+j*200,100+i*200,200,200)
                if self.current_state.data[i][j] == 1:
                    line(j*200, i*200,(j+1)*200,(i+1)*200);
                    line(j*200, (i+1)*200, (j+1)*200, i*200);    
                      
        if self.current_player == -1 and not self.game_over:
            row, col, symbol = self.ai_player.act()
            next_state_hash = self.current_state.next_state(row, col, -1).hash()
            self.current_state, is_end = all_states[next_state_hash]
            self.ai_player.set_state(self.current_state)
            if is_end:
                self.winner = self.current_state.winner
                self.game_over = True
            self.current_player *= -1
        if self.winner is not None:
            self.game_over = True
        if self.game_over:
            fill(0);
            textSize(30);
            if self.winner == 0:
                text("Draw", width/2, height/2);
            elif self.winner == 1:
                text("X player win!", width/2, height/2);
            elif self.winner == -1:
                text("O player win!", width/2, height/2);

    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. 
        Example:
          if key == LEFT:
              # code to respond to LEFT arrow key being pressed.
          elif key == RIGHT:
              # code to respond to RIGHT arrow key being pressed.
          elif key == UP:
              # code to respond to UP arrow key being pressed.
          elif key == DOWN:
              # code to respond to DOWN arrow key being pressed.
          elif key == 'a':
              # code to respond to 'a' key being pressed.
          elif key == 'b':
              # code to respond to 'b' key being pressed.
        """
        if key == 'r':
            self.set_up()
            
        # TODO: 
        # if key == 's:
        #    set ai_mode to True
        #    initialize new variable self.search_problem to = EightPuzzleSearchProblem with current puzzle
        #    initialize self.solution_path to returned path given by graphSearch()

            
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        pass
            
  
    def on_mouse_clicked(self, x, y, button):
        """ Called whenever the mouse is pressed. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER
        """
        if self.current_player == 1 and not self.game_over:
            row = mouseY // SIZESQUARE
            col = mouseX // SIZESQUARE
            next_state_hash = self.current_state.next_state(row, col, 1).hash()
            self.current_state, is_end = all_states[next_state_hash]
            self.ai_player.set_state(self.current_state)
            if is_end:
                self.winner = self.current_state.winner
                self.game_over = True
            self.current_player *= -1
  
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER
        """
        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
