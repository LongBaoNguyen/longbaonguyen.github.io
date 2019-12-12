"""
In Rectangle? Lab

This is similar to the previous lab. Draw a rectangle in the middle of the screen of 
some width and height and color.
If the mouse enters the rectangle, change color. If the mouse leaves the rectangle,
reset to original color.

"""

from __future__ import division, print_function
import arcade
from constants import *

class Window:    
    def __init__(self):
        """ Declare the variables, set them to None. """

        pass

    def setup(self):
        """ Set up the game and initialize the variables. """

        pass
        

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        pass

    def on_update(self):
        """ Called to update our objects. Happens approximately 60 times per second."""
        
        pass



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
        # use UP,DOWN,LEFT,RIGHT  (different than original Arcade library)
        if key == LEFT:
            pass
        elif key == RIGHT:
            pass        
            
        # for letter keys, use 'a', 'b', etc..(also different)
        elif key == 'a':
            pass
            
    def on_key_release(self, key):
        """ Called automatically whenever a key is released. """
        pass
            
            
        
        
    
