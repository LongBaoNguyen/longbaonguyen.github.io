"""
Tank Shooting Lab

Tank shoots bullets whenever mouse is clicked. 
Place 10 bricks randomly on the screen. 
If bullet hits brick, both are removed. 
If bullet leaves the screen, it is removed. 
   
IMPLEMENT ALL PARTS LABELED "TODO".

Implement the methods in the following order:
1) __init__
2) on_mouse_press for shooting when mouse is clicked
3) on_draw
4) on_update


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
            self.player = Sprite("tank.png")
            
            Create Sprite object with 2.0 scale position at (200, 300)
            self.coin = Sprite("coin.png", 2.0, 200, 300)
        """
        
        self.player = Sprite("tank.png", 0.8)
        self.player.center_x = WIDTH // 2
        self.player.center_y = HEIGHT // 2

                                
        # TODO, create empty brick_list and bullet_list
   


        # TODO, create variable score, initialize to 0
 

        self.num_bricks = 10
        for i in range(self.num_bricks):
            brick = Sprite("brick.png", 0.4)
            brick.center_x = random.randrange(WIDTH)
            brick.center_y = random.randrange(HEIGHT)
            self.brick_list.append(brick)
            

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        self.player.draw()
        
        # TODO, iterate through brick_list and draw each brick 
        
            
        # TODO, iterate through bullet_list and draw
        
            
        # TODO, call move() on player object

                
        # TODO, iterate through bullet_list, move each bullet

                
        

        # TODO
        # for each bullet in bullet_list, 
        #   call check_for_collision_list with brick_list to get collision list
        #   if collision_list is not empty:
        #     remove bullet from bullet_list
        #     remove first element of collision_list from brick_list  
        #     update score
        #   if bullet leaves right side of screen
        #      remove bullet 
        
                

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
        if key == RIGHT:
            self.player.change_x = 5
        elif key == LEFT:
            self.player.change_x = -5
        elif key == UP:
            self.player.change_y = -5
        elif key == DOWN:
            self.player.change_y = 5
    
        

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        if key == RIGHT:
            self.player.change_x = 0
        elif key == LEFT:
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
        # TODO
        # create bullet Sprite
        # set center_y to equal player's center_y


        # set left side of bullet to equal right side of player
        # bullet.set_left(10) for example would move the bullet
        # so that the left side of the bullet = 10.
        # x = player.get_right() 
        # x is the position of the right side of the player.

        
        
        # set change_x to 10(velocity)

                
        # append to bullet_list
        
        
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
