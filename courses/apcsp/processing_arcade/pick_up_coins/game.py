"""
Pick Up Coins Lab

Follow the instructions given by the comments below.
Tank moves about the screen and picks up coins. Text coin counter is updated appropriately.

IMPLEMENT ALL PARTS LABELED "TODO".
"""


from __future__ import division, print_function
from arcade import *
import random

WIDTH = 800 # width of screen in pixels
HEIGHT = 600 # height of screen in pixels

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
            self.player = Sprite("tank.png")
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = Sprite("coin.png", 2.0, 200, 300)
        """
        # create a player Sprite using "tank.png"
        
        # create empty list called self.coins
        self.coins = []
        self.num_coins = 20
        
        # use a loop to create coins(use self.num_coins)
            

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        # draw player and all coins
            
        # display text, left-center align    
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Coins:" + str(self.num_coins), 20, 40)

        
        self.player.update()
        
        # TODO
        # call check_for_collision_list and store result in collision_list variable
        # remember to use self.check_for_collision_list(...)

                                                                                                                                                                                                                                                                      
        # TODO
        # for each sprite in collision_list:
        #    remove it from self.coins
        #    update self.num_coins
            
                
        
        
    
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
        if key == RIGHT:
            self.player.change_x = 5
        elif key == LEFT:
            self.player.change_x = -5
        elif key == UP:
            self.player.change_y = -5
        elif key == DOWN:
            self.player.change_y = 5
    
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        if key == RIGHT:
            self.player.change_x = 0
        elif key == LEFT:
            self.player.change_x = 0
        elif key == UP:
            self.player.change_y = 0
        elif key == DOWN:
            self.player.change_y = 0
            
        
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
                  
      
        
        
    
