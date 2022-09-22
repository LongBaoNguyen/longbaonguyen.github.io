"""
This lab introduces you to how to create instance variables 
and update them in each frame of animation. 

Objective: 
    Draw a red circle and make it move to the right. 
    
    Drawing API:
    ellipse(x, y, width, height): (x, y) center of ellipse.
    rect(x, y, width, height): (x, y) top left corner of rectangle.
    line(x1, y1, x2, y2): line connecting (x1, y1) and (x2, y2)

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
        # create two variable x and y for the center of the circle.
        # Don't forget to prefix it with "self."!

                                
    def on_draw(self):
        """ Called automatically 60 times a second to draw and update all objects.
            Write code to draw/update all objects.
        """
        # set the fill to red. Call fill(red, green, blue).

        # Then call ellipse(x, y, width, height)
        # to draw ellipse centered in the 
        # middle of the screen at (WIDTH//2, HEIGHT//2) with diameter 300
                
                
        # update the center by adding 5 pixels to x every frame(use self. notation) 
        
        
   
    
        
    
