"""
Top-Down Games. Resolve top-down collision.
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
        # create a Sprite called self.player using "tank.png", 
        # place it in the middle of the screen
        
        self.player = Sprite("tank.png", TANK_SCALE)
        self.player.center_x = WIDTH//2
        self.player.center_y = HEIGHT//2
        
        
        # call read_map with "map.csv" to return list of bricks
        # and store in self.bricks variable
        self.bricks = read_map("map.csv")
        
        
        
    
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """
        # draw self.player
        self.player.draw()

                
        # loop through self.bricks and draw each Sprite
        for brick in self.bricks:
            brick.draw()


        
        # call resolve_top_down_collision on player and bricks
        # to both move and resolve player's collision with bricks
        resolve_top_down_collision(self.player, self.bricks)

        
        

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
        # write code to control self.player
        # Hint: if key pressed is LEFT, set Sprite's change_x to -5
        # Then under on_key_release below, if the same LEFT key is pressed, set change_x back to 0
        # similarly for other keys and directions. 
        if key == LEFT:
            self.player.change_x = -5
        elif key == RIGHT:
            self.player.change_x = 5
        elif key == UP:
            self.player.change_y = -5
        elif key == DOWN:
            self.player.change_y = 5

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        # See comment above in on_key_press: if LEFT key is pressed, set change_x back to 0

        if key == LEFT:
            self.player.change_x = 0
        elif key == RIGHT:
            self.player.change_x = 0
        elif key == UP:
            self.player.change_y = 0
        elif key == DOWN:
            self.player.change_y = 0
            
        
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
                  
      
        
        
    
