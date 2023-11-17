"""
Capture the Flags

Randomize a list of flags on the screen. Player collects flags and score is updated.


1) Implement check_for_collision_list in the arcade.py file.
2) Follow the instructions given by the comments below.


"""


from __future__ import division, print_function
from arcade import *
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
                        
            Create Sprite object at the origin, 0.5 scale.
            self.player = Sprite("tank.png", 0.5)
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = Sprite("coin.png", 2.0, 200, 300)
        """
        # create a player Sprite using "player.png"

        
        # create a empty list for flag Sprites 

                
        # number of flags
        self.num_flags = 10 
        
        # use for loop to repeat num_flags times:
        #       create a flag Sprite using "flag.png" add to list
        #       initialize center_x and center_y attributes of flag Sprite
        #       use random.randrange(n)
        #       then append to flags list
        
        
        
        # inititalize score


    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        # draw player and move player


        # use for each loop to loop through flags list and draw each flag

                
                
        # TODO
        # call check_for_collision_list and store result in collision variable

                
        
        # TODO
        # for each sprite in collision list:
        #    remove it from flags list(for example, lst.remove(flag))
        #    update score

        
                        
        # display text, left-center align  
        # TODO: Display score  
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Score:" + str(1), 20, 40)

        
        
        
      
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
    
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """

            
        
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
                  
      
        
        
    
