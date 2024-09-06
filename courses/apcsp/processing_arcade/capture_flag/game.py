"""
Capture the Flag

Follow the instructions given by the comments below.


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
                        
            Create Sprite object at the origin, default 1.0 scale.
            self.player = arcade.Sprite("tank.png")
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = arcade.Sprite("coin.png", 2.0, 200, 300)
        """
        # create a player Sprite using "player.png"
        self.player = Sprite("player.png", 1.0, 200, 300)

        
        # create a flag Sprite using "flag.png"
        self.flag = Sprite("flag.png", 1.0)
        
        
        # randomize position of flag
        # for example: x = random.randrange(100)
        # x is a random value from 0 to 100(exclusive)
        self.flag.center_x = random.randrange(WIDTH)
        self.flag.center_y = random.randrange(HEIGHT)

        
        # inititalize score
        self.score = 0


    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        # draw player and move player
        self.player.draw()
        self.player.move()

                
        # draw flag

                
        # if player and flag intersect:
        #     update score
        #     randomize position of flag(center_x, center_y)\
        collided = check_for_collision(self.flag, self.player)
        if collided:
            self.score += 1
            self.flag.center_x = random.randrange(WIDTH)
            self.flag.center_y = random.randrange(HEIGHT)
        
        
        # display text, left-center align  
        # TODO: Display score  
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Score:" + str(self.score), 20, 40)

        
        
        
      
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
        if key == LEFT:
            self.player.change_x = -5
    
        

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
                  
      
        
        
    
