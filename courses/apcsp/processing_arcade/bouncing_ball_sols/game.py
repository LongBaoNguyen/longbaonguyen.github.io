"""
This lab introduces you to how to animate a bouncing ball.


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
        
        # create variables: x, y, change_x, change_y and radius for the ball.
        self.x = 200
        self.y = 300
        self.change_x = 5
        self.change_y = 3
        self.radius = 50
                
    def on_draw(self):
        """ Called automatically 60 times a second to draw and update objects.
            Write code to draw and update all objects.
        """
        # set the fill to red. Call fill(red, green, blue).
        # Then call ellipse(x, y, width, height)
        # to draw ellipse centered at (self.x, self.y) with diameter = 2 * self.radius
        
        fill(255, 0, 0)
        ellipse(self.x, self.y, 2 * self.radius, 2 * self.radius)
        
        
        # update position by adding change_x and change_y to x and y  
        self.x += self.change_x
        self.y += self.change_y

        
        # if right edge of ball passes right side of screen or 
        # left edge of ball passes left side of screen, negate change_x to change direction
        # Note: use radius in the conditional so that the ball bounces exactly at edge.
        if self.x + self.radius > width or self.x - self.radius < 0:
            self.change_x *= -1
        
        # if top edge of ball passes top side of screen or 
        # bottom edge of ball passes bottom side of screen, negate change_y to change direction
        # Note: use radius in the conditional so that the ball bounces exactly at edge.

        if self.y + self.radius > height or self.y - self.radius < 0:
            self.change_y *= -1

    
        
    
