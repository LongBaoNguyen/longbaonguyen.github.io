"""
Tank Shooting Lab

Tank shoots bullets whenever mouse is clicked. 
Place 10 bricks randomly on the screen. 
If bullet hits brick, both are removed. 
If bullet leaves the screen, it is removed. 

Do the following. Make sure each part works before moving on to the next part!

1) Initialize bullet_list(SpriteList) in setup
2) In on_mouse_press, each time mouse is pressed, create a bullet, initialize
   it to be at the location of the player(same center_y, but left side of bullet
   should be equal to right side of player)
   Set change_x of bullet to 10. Append to bullet_list.
   Update and draw bullet_list.
   If 1) and 2) works, you are now able to shoot each time mouse is clicked. 
3) In setup, create brick_list and randomly, placed 10 bricks in brick_list. 
   Draw them.
4) In update():
   for each bullet in bullet_list, call check_for_collision_with_list 
   with the bullet and the brick_list to get collision list of bricks
       if collision_list is not empty:
           remove bullet from bullet_list
           remove first element of collision_list from brick_list(or all of them, up to you)
       if bullet leaves screen, it is removed  
5) Add a score variable to keep track of how many bricks are hit. Display score.

   
"""

from __future__ import division, print_function
import arcade
from constants import *
import random

class Window:    
    def __init__(self):
        """ Declare the variables, set them to None. """
        self.player = None
        self.bullet_list = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player = arcade.Sprite("tank.png", 0.5)
        self.player.set_left(0)
        self.player.center_y = HEIGHT/2

        # initialize bullet list to empty SpriteList
        
        # create brick_list and randomly, placed 10 bricks in brick_list. 

        
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.player.draw()
        
        # draw bullet_list
        
        # draw brick_list


    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.player.update()
        
        # update bullet_list

                
        # for each bullet in bullet_list
        # call check_for_collision_with_list with brick_list to get collision list
        #     if collision_list is not empty:
        #           remove bullet from bullet_list
        #           remove first element of collision_list from brick_list    
        #     if bullet leaves screen, remove it

                        
    def on_mouse_motion(self, x, y, dx, dy):        
        """ Called whenever the mouse moves. """
        # if x is within width of rectangle and y within height of rectangle
        # return True otherwise return False.
        pass
        
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. """
        
        pass
        # create bullet Sprite
        
        # set center_y to equal player center_y
        
        # set left side of bullet to equal right side of player
        
        # set change_x to 10
        
        # append to bullet_list
        
        
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
            
            
        
        
    
