"""
This lab introduces you to the basics of Processing including drawing
simple shapes, text and animation.  

See the following slides for an intro to Processing. 
https://longbaonguyen.github.io/courses/apcsp/processing_arcade/processing1.pdf

To do: 
    1) Draw a rectangle with center at (100, 400) and width = 50, height = 10
    2) Draw a line connecting the top left corner and bottom right corner. 
    3) Display some text on the screen. Use the text() method.
    4) Print out some text on the console. Use the print() method. 
    4) Draw a small red circle with radius 20 and make it move to the right. 
    
    Drawing API:
    ellipse(x, y, width, height): (x, y) center of ellipse.
    rect(x, y, width, height): (x, y) top left corner of rectangle.
    line(x1, y1, x2, y2): line connecting (x1, y1) and (x2, y2)
    text(str, x, y): display str at location (x, y).

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
        # Note: We need to initialize any variables that need to be changed(in draw below) 
        # throughout the course of running the program.
        self.x = 100
        self.y = 200
                                
    def draw(self):
        """ Called automatically 60 times a second to draw and update all objects.
            Write code to draw/update all objects.
        """
        # draw a blue rectangle center at (100, 400) and width = 50, height = 100
        # Call fill(red, green, blue).

        fill(0, 0, 255)
        strokeWeight(2)
        rect(100, 400, 50, 100)
        
        # draw a line connecting the top left corner and bottom right corner. 
        strokeWeight(3)
        line(0, 0, 800, 600)
        
        # display some text on the screen. Use the text() method.
        textSize(32)
        fill(0) # black
        text("Processing!", 400, 50)
        

        # print out some text on the console. Use the print() method. 
        print("Hello, world!")

        # set the fill to red. Call fill(red, green, blue).
        # Then call ellipse(x, y, width, height)
        # to draw circle centered at (self.x, self.y) with diameter 20
        fill(255, 0, 0)
        strokeWeight(1)
        ellipse(self.x, self.y, 20, 20)
                
        # update the center by adding 5 pixels to x every frame(use self. notation) 
        self.x += 5
        
   
    
        
    
