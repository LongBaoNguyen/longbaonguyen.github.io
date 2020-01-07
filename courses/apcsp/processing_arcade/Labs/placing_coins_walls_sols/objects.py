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
        
        # declare the variables: player, brick_list
        self.player = None
        self.brick_list = None
        self.coin_list = None
        self.physics_engine = None
        self.num_coins = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)
        self.num_coins = 30

        # initialize brick_list as a SpriteList
        self.brick_list = arcade.SpriteList()
        for y in range(50, HEIGHT, 150):
            for x in range(100, WIDTH - 100, 64):
                brick = arcade.Sprite("brick.png", 0.5)
                brick.center_x = x
                brick.center_y = y
                self.brick_list.append(brick)
        
        self.coin_list = arcade.SpriteList()
        
        for i in range(self.num_coins):
            coin = arcade.Sprite("coin.png", 0.5)
            successfully_placed = False
            
            while not successfully_placed:
                coin.center_x = random.randrange(WIDTH)
                coin.center_y = random.randrange(HEIGHT)
                brick_collision = arcade.check_for_collision_with_list(coin, self.brick_list)
                coin_collision = arcade.check_for_collision_with_list(coin, self.coin_list)
                if len(brick_collision) == 0 and len(coin_collision) == 0:
                    successfully_placed = True
                    self.coin_list.append(coin)
            
                
        # initialize physics_engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.brick_list)
            
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()
        self.brick_list.draw()
        self.coin_list.draw()


    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.physics_engine.update()
        collision_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        if len(collision_list) > 0:
            for coin in collision_list:
                self.num_coins += 1
                self.coin_list.remove(coin)
        
                                        
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
            
            
        
        
    
