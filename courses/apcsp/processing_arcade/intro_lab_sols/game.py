"""
This lab introduces you to how to create sprites and move them.
In particular, we will see the difference between:
    - creating several variables(e.g. position, velocity) to keep
    track of an object(ball)
    - (object-oriented programming)creating an object from a class(Sprite) that already has
    all the necessary variables associated with it(position, velocity).

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
        
        # Remember to use self. notation to create variables.
        # initialize three variables(center_x, center_x, speed)
        self.center_x = 100
        self.center_y = 400
        self.speed = 5
        
        # create the Sprite object called player(see data folder for image)
        # located at (100, 200).
        self.player = Sprite("player.png", 1.0, 100, 200)
        
        # set player's change_x property to 5(use dot notation)
        self.player.change_x = 5
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw/update objects.
            Write code to draw/update all objects.
        """
        # draw red circle located at center_x, center_y with radius 50 
        fill(255, 0, 0) 
        ellipse(self.center_x, self.center_y, 100, 100)
        
        
        # draw player
        self.player.draw()
        
        # move ball by adding speed to center_x
        self.center_x += self.speed
        
        
        # move player by calling move() on player object(dot notation)
        self.player.move()
    
        
        # optional: Can you figure out how to make the sprite rotate
        # by changing one of its property?(see arcade.py)
   
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
                  
      
        
        
    
