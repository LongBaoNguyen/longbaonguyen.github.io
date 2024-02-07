"""
Eight Puzzle Lab

Follow the instructions given by the comments below.

IMPLEMENT ALL PARTS LABELED "TODO".
"""


from __future__ import division, print_function
from node import *
from state import *
from problem import *
from search import *
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
                        
            Create Sprite object at the origin, default 1.0 scale.
            self.player = arcade.Sprite("tank.png")
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = arcade.Sprite("coin.png", 2.0, 200, 300)
        """
        self.puzzle = createRandomEightPuzzle(20)
        #self.puzzle = EightPuzzleState([8,6,7,2,5,4,3,0,1])

        self.game_over = False
        self.search_problem = EightPuzzleSearchProblem(self.puzzle)
        self.solution_path = graphSearch(self.search_problem)


    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        self.draw_puzzle()
        if self.puzzle.isGoal():
            self.game_over = True
        if frameCount % 60 == 0 and len(self.solution_path) != 0:
            self.puzzle = self.puzzle.result(self.solution_path.pop(0))
        
        if self.game_over:
            fill(0, 0, 255);
            textSize(40);
            text("You win!", 10, height/2 - 40);
            text("Press 'r' to reset!", 10, height/2+60);
            
            
        
        
    def draw_puzzle(self):
        strokeWeight(8)
        fill(255, 0, 0)
        for i in range(1, 3):
            line(i*SIZESQUARE, 0, i*SIZESQUARE, HEIGHT)
        for i in range(1, 3):
            line(0, i*SIZESQUARE, WIDTH, i*SIZESQUARE)
        for i in range(3):
            for j in range(3):
                if self.puzzle.cells[i][j] != 0:
                    fill(255, 0, 0)
                    textSize(80)
                    text(self.puzzle.cells[i][j], 100+j*200 - 20, 100+i*200 + 20)
    
    
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
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
            
        
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
                  
      
        
        
    
