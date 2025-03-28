"""
You will use a list of tuples to store a list of circles. 

Objective: Create a list of circles randomly on the screen.

"""
from __future__ import division, print_function
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
        """
        # create an empty list called self.circles
        self.circles = []

        # loop 10 times to create 10 circles: each circle is a tuple of 
        # (x, y, diameter) where each of the value is randomized:
        # Use random.randrange(start, stop, step) to generate random numbers
        # append each circle tuple to self.circles
        for i in range(10):
            x = random.randrange(0, WIDTH)
            y = random.randrange(0, HEIGHT)
            diameter = random.randrange(10, 80)
            r = random.randrange(0, 255)
            g = random.randrange(0, 255)
            b = random.randrange(0, 255)
            circle = (x, y, diameter, r, g, b)
            self.circles.append(circle)
            
            

                                
    def on_draw(self):
        """ Called automatically 60 times a second to draw and update all objects.
            Write code to draw/update all objects.
        """
        # loop through self.circles and draw each(use tuple unpacking)
        # use fill(r, g, b) and ellipse(x, y, diameter, diameter)
        for x, y, diameter, r, g, b in self.circles:
            fill(r, g, b)
            ellipse(x, y, diameter, diameter)    
        
   
    
        
    
