"""
Placing Coins Away from Bricks and Other Coins

Do the following:

1) Use nested loop to create rows of bricks(e.g., 4 rows, each with 10 bricks).  
2) Use for loop to create set of coins where each coin is placed away from bricks and other coins.
Note: Each iteration of for loop, use while loop until a coin is placed successfully.
3) Use PhysicsEngineSimple class to detect/resolve brick collision.
4) In update(), use code from Pick Up Coins Lab to pick up coins. 


"""

from __future__ import division, print_function
import arcade
from constants import *

import random

class Window:    
    def __init__(self):
        """ Declare the variables, set them to None. """
        
        self.player = None
        self.brick_list = None
        self.coin_list = None
        self.physics_engine = None
        self.num_coins = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)
        self.num_coins = 30

        # Initialize brick_list as a SpriteList
        # Then use nested for loops to place rows of bricks. 
        # (Hint: Outer for loop is y coordinate skipping every 150 pixels
        #        Inner for loop is x coordinate skipping every 64 pixels)
        # Append bricks to brick_list




        
        # Initialize coin_list as a SpriteList
        self.coin_list = arcade.SpriteList()
        
        # PSEUDOCODE for how to place coins. 
        # for each i in range of number of coins 
        #       create coin Sprite
        #       set boolean variable successfully_placed to False
        #       while not successfully_placed
        #           set center_x and center_y randomly
        #           compute collision lists for coin with bricks
        #           AND coin with other coins (2 lists)
        #           if both lists have 0 length, then we have successfully placed the coin
        #                  add coin to coin_list
    
    
    
    
    
    
                
        # initialize physics_engine
        
        
            
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        # draw everything


    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        
        # update physics engine
        
        
        # use code from pick up coins lab to pick up coins
        # you don't need all of the code from that lab(no gameover or reset)
        
                
                                        
    def on_mouse_motion(self, x, y, dx, dy):        
        """ Called whenever the mouse moves. """
        # if x is within width of rectangle and y within height of rectangle
        # return True otherwise return False.
        pass
        
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. """

        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. """
        pass
                  
    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. """
        if key == LEFT:
            self.player.change_x = -5
        elif key == RIGHT:
            self.player.change_x = 5
        elif key == UP:
            self.player.change_y = -5 
        elif key == DOWN:
            self.player.change_y = 5
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. """
        if key == LEFT:
            self.player.change_x = 0
        elif key == RIGHT:
            self.player.change_x = 0
        elif key == UP:
            self.player.change_y = 0
        elif key == DOWN:
            self.player.change_y = 0
            
            
        
        
    
