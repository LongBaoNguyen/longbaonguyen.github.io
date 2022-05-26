"""
This lab introduces you to how to create instance variables 
and update them in each frame of animation. 

Objective: 
    Draw a red circle and the grows larger and larger. 
    You only have to write four lines of code!

"""
from __future__ import division, print_function


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
        """
        
        # create a variable called diameter. Don't forget to prefix it with "self."!
        self.diameter = 10
                
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """
        # set the fill to red. Call fill(red, green, blue).
        # Then call ellipse(x, y, length, width)
        # to draw ellipse centered in the 
        # middle of the screen at (WIDTH//2, HEIGHT//2) with diameter 300
        
        fill(255, 0, 0)
        ellipse(WIDTH//2, HEIGHT//2, self.diameter, self.diameter)
        
        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        # update diameter by adding 1 
        self.diameter += 1
        
   
    
        
    
