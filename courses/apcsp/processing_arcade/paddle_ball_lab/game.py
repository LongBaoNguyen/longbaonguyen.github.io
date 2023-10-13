"""
Ball and Paddle Lab. 

"""

from __future__ import division, print_function
from arcade import *

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
            
            Create Sprite object at the origin, default 1.0 scale.
            self.player = Sprite("tank.png")
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = Sprite("coin.png", 2.0, 200, 300)
        """
        
        # create two Sprite objects(paddle.png and ball.png, scaling = 0.2)
        # put paddle at y = 500

                
        # set change_x and change_y properties of ball object
        


                                                                                                                                        
    def on_draw(self):
        """ Called automatically 60 times a second to draw/update objects.
            Write code to draw/update all objects.
        """
        # draw paddle and ball


        # set paddle position to equal to follow mouseX but at fixed y position(500)


        # make ball move


        # if ball pass right screen or left screen, negate change_x 
        
        
        # if ball pass top screen or bottom screen, negate change_y 
        
        
        # make ball bounce off top of paddle(Hint: Use get_top(), get_right() etc.., see arcade.py)
   
   
   
   
    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. 
        Example:
          if key == LEFT:
              # code to respond to LEFT arrow key being pressed.
          elif key == RIGHT:
              # code to respond to RIGHT arrow key being pressed.
          elif key == UP:
              # code to respond to UP arrow key being pressed.
          elif key == DOWN:
              # code to respond to DOWN arrow key being pressed.
          elif key == 'a':
              # code to respond to 'a' key being pressed.
          elif key == 'b':
              # code to respond to 'b' key being pressed.
        """
        pass
        
    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        pass

    
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER
        """
        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
