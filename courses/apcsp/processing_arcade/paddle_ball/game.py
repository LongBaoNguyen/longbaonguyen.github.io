"""
This lab introduces you to how to animate a ball bouncing off a paddle.
The code for the bouncing ball which bounces off the top, right and bottom
side are already given.

1) Add in a paddle(rectangle) which is controlled by the 
position of the mouse. Hint: mouseX and mouseY are variables already
created that keep track of the position of the mouse. Your paddle
should be a fixed distance from the left side of the screen(e.g. 50).

Note: In this lab, use rect(x, y, width, height) to draw rectangle;
(x, y) is the TOP LEFT corner of the rectangle. 

2) Add in collision code similar to the bouncing ball lab to bounce off
the paddle. 

3) If ball passes paddle, reset the ball to the middle of the screen.

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
        self.radius = 20
        
        # width and height of paddle(rectangle)
        self.paddle_width = 40
        self.paddle_height = 100
        
                
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

        # if top edge of ball passes top side of screen or 
        # bottom edge of ball passes bottom side of screen, negate change_y to change direction

        if self.y + self.radius > height or self.y - self.radius < 0:
            self.change_y *= -1

        
        # if right edge of ball passes left side of screen negate change_x to change direction
        if self.x + self.radius > width:
            self.change_x *= -1
            
        # YOUR CODE STARTS HERE
        # first add in a paddle the follows the position of your mouse. 
        # Then modify it so that it is 50 pixels from the left side of screen 
        # and controlled by the position of the mouse. 
        # Use self.paddle_width and self.paddle_height.
        # use rect(x, y, width, height) to draw rectangle;
        # (x, y) is the TOP LEFT corner of the rectangle.(2 lines of code)
        
        
        fill(0) # grayscale
        rect(50, mouseY, self.paddle_width, self.paddle_height)
        
        # fill in the code below for sides of paddle(3 lines)
        right_side_paddle = 50 + self.paddle_width
        top_side_paddle = mouseY
        bottom_side_paddle = mouseY + self.paddle_height
        
        # fill in code for sides of ball(3 lines)
        left_side_ball = self.x - self.radius
        top_side_ball = self.y - self.radius
        bottom_side_ball = self.y + self.radius
        
        
        # ball hits paddle if:
        # 1) left side of ball is less than right side of paddle
        # 2) top side of ball is greater than top side of paddle(y-axis inverted)
        # 3) bottom side of ball is less than bottom side of paddle
        # change x direction if all above are true. (2 lines)
        right = left_side_ball <= right_side_paddle
        top = top_side_ball >= top_side_paddle
        bottom = bottom_side_ball <= bottom_side_paddle
        if right and top and bottom:
            self.change_x *= -1
        elif right:
            self.x = WIDTH//2
            self.y = HEIGHT//2
            
        
        
        # else if ball passes without hitting paddle, reset position of ball
        # to middle of screen.(2 lines)
