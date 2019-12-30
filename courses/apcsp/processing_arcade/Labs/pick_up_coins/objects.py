"""
Pick Up Coins Lab

Do the following:

1) The player Sprite along with some other variables have already been created for you. 
2) In setup(), inititalize a SpriteList. Use a for loop to initialize coins at random positions 
on the screen. Use the imported random module and random.randrange(n) generates a random integer
from 0 to n - 1 (similar to range()) to initialize the positions of the coins. Add to the SpriteList.
3) Use arcade.check_for_collision_with_list to get a list of Sprites collided with player.
4) For each one in the list, update the number of coins collected and remove from SpriteList.
5) If all coins have been removed, display "You win! Press r to restart!". If the user presses "r",
reset the game.

"""

from __future__ import division, print_function
import arcade
from constants import *

import random

class Window:    
    def __init__(self):
        """ Declare the variables, set them to None. """
        self.player = None
        self.coin_list = None
        self.num_coins = None
        self.game_over = None
        self.total_coins = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)
        self.num_coins = 0
        self.total_coins = 5
        self.game_over = False
        # initialize a new empty SpriteList(self.coin_list)
        
        # Use a for loop to create self.total_coins
        # randomly placed on the screen. Add to SpriteList.
        
        
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()
        
        # draw coin_list
        
        # draw number of coins collected text.
        
        # draw game over message if it's game over.
        

    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        
        # if game is not over:
        # 1) update player  
        # 2) compute collision_list
        # 3) for each coin in collision_list, remove and update score
        # if all coins have been collected, then game over.  
        
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
        elif key == 'r' and self.game_over:
            self.setup()
        

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
            
            
        
        
    
