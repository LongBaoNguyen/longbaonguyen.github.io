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
        self.coin_list = arcade.SpriteList()
        self.num_coins = 0
        self.total_coins = 5
        self.game_over = False
        for i in range(self.total_coins):
            coin = arcade.Sprite("coin.png", 0.5)
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)
            self.coin_list.append(coin)
            
            
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text("Coins: " + str(self.num_coins), 50, HEIGHT - 50)
        if self.game_over:
            arcade.draw_text("You win! Press r to restart!", WIDTH/2 - 200, HEIGHT/2)


    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        
        if not self.game_over:
            self.player.update()
            collision_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
            if len(collision_list) > 0:
                for coin in collision_list:
                    self.num_coins += 1
                    self.coin_list.remove(coin)
                
            if self.num_coins == self.total_coins:
                self.game_over = True
                
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
            
            
        
        
    
