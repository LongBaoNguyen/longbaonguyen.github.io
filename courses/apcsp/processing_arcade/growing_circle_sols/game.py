"""
This lab introduces you to how to create instance variables 
and update them in each frame of animation. 

Objective: 
    Draw a red circle that grows larger and larger. 

"""
from __future__ import division, print_function


WIDTH = 1000 # width of screen in pixels
HEIGHT = 800 # height of screen in pixels

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
        self.diameter = 100
                                
    def on_draw(self):
        """ Called automatically 60 times a second to draw and update objects.
            Write code to draw and update all objects.
        """
        # set the fill to red. Call fill(red, green, blue).
        # Then call ellipse(x, y, width, height)
        # to draw ellipse centered in the 
        # middle of the screen at (WIDTH//2, HEIGHT//2) with self.diameter 
        fill(255, 0, 0)
        ellipse(WIDTH // 2, HEIGHT // 2, self.diameter , self.diameter) 
        
        
        # update diameter by adding 1 
        self.diameter += 1
        
        
        # if diameter is >= 300, reset it to 0. 
        if self.diameter >= 300:
            self.diameter = 0

    
        
    
