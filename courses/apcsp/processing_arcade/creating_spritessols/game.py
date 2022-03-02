"""
This lab introduces you to how to create sprites, draw and update them. 
We will also learn how to control a Sprite using the keyboard.
"""

from __future__ import division, print_function
import arcade

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
        # create a Sprite called self.player using "tank.png", place it in the middle of the screen
        self.player = arcade.Sprite("tank.png")
        self.player.center_x = WIDTH//2
        self.player.center_y = HEIGHT//2
        
        # create an empty list called self.coins
        self.coins = []
        
        # use a for loop to populate self.coins with 10 "coin.png" Sprites placed randomly on the screen
        # Hint: coin.center_x = random(0, WIDTH)
        for i in range(10):
            coin = arcade.Sprite("coin.png")
            coin.center_x = random(0, WIDTH)
            coin.center_y = random(0, HEIGHT)
            self.coins.append(coin)
        
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """
        # draw self.player
        self.player.draw()
        
        # loop through self.coins and draw each Sprite
        for coin in self.coins:
            coin.draw()
        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        # call update on self.player
        self.player.update()
        
   
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
                  
      
        
        
    
