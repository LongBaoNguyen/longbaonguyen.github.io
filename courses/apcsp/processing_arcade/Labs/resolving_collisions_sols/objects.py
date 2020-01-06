"""
Resolving Collisions Lab

Do the following:

1) Create a SpriteList of "brick.png" Sprites. 
2) Initialize two rows of brick sprites. One with all adjacent bricks and one with spacing
enough for the tank to go in between. 
3) Use PhysicsEngineSimple class to detect/resolve collision! 
See the arcade.py for the source code. Note: This part will only require 2 lines of code!


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
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)

        # initialize brick_list as a SpriteList
        self.brick_list = arcade.SpriteList()

        # use a for loop to create a set of HORIZONTAL, ADJACENT "brick.png" Sprites.
        # Remember to add them to brick_list
        # Hint: Use for loop with range(begin, end, step)
        for i in range(100, 500, 64):
            brick = arcade.Sprite("brick.png", 0.5)
            brick.center_x = i
            brick.center_y = HEIGHT/4
            self.brick_list.append(brick)
        
        
        # use a for loop to create a set of HORIZONTAL, "brick.png" Sprites
        # with spacing enough for tank to go between them.

        
            
        for i in range(100, 600, 200):
            brick = arcade.Sprite("brick.png", 0.5)
            brick.center_x = i
            brick.center_y = HEIGHT/2
            self.brick_list.append(brick)
            
        # initialize physics_engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.brick_list)
            
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()
        self.brick_list.draw()


    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.physics_engine.update()
        
                                        
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
            
            
        
        
    
