"""
Pick Up Coins Lab

Follow the instructions given by the comments below.
Tank moves about the screen and picks up coins. Text coin counter is updated appropriately.

IMPLEMENT ALL PARTS LABELED "TODO".
"""


from __future__ import division, print_function
import arcade
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
        
        self.player = arcade.Sprite("tank.png", 0.8)
        self.player.center_x = WIDTH/2
        self.player.center_y = HEIGHT/2
        
        
        self.coins = []
        self.num_coins = 20
        for i in range(self.num_coins):
            # create a coin Sprite, add to list
            coin = arcade.Sprite("coin.png", 0.8)
            coin.center_x = random.randrange(WIDTH)
            coin.center_y = random.randrange(HEIGHT)
            self.coins.append(coin)
            

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        self.player.draw()
        for coin in self.coins:
            coin.draw()
            
        # display text, left-center align    
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Coins:" + str(self.num_coins), 20, 40)

        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        self.player.update()
        
        # TODO
        # call check_for_collision_list and store result in collision_list variable
        collision_list = self.check_for_collision_list(self.player, self.coins)                     
                                                                                                                                   
        # TODO
        # for each sprite in collision_list:
        #    remove it from self.coins
        #    update self.num_coins
        for sprite in collision_list:
            self.coins.remove(sprite)
            self.num_coins -= 1
            
                
        
        
    def check_for_collision(self, sprite1, sprite2):
        """ Returns whether sprite1 and sprite2 intersect.(rectangle intersection)
        """
        # TODO
        # follow intersection rules from lecture notes to implement collision detection
        # see this link to see the math:
        # https://longbaonguyen.github.io/courses/apcsp/processing_arcade/processing3.pdf
        x_overlap = sprite2.get_right() > sprite1.get_left() and sprite2.get_left() < sprite1.get_right() 
        y_overlap = sprite2.get_bottom() > sprite1.get_top() and sprite2.get_top() < sprite1.get_bottom()
        return x_overlap and y_overlap
        
      
    def check_for_collision_list(self, sprite, sprite_list):
        """ Returns list of sprites in sprite_list which intersect with sprite.
            Call check_for_collision method above. Use self and dot notation.
            For example:
                
            if self.check_for_collision(sprite1, sprite2):
                # do something here.
        """
        
        # TODO
        # create empty list collision_list
        collision_list = []
        
        # for each sprite sp in sprite_list:
        #     if there's collision between sp and sprite 
        #     add to collision_list 
        for sp in sprite_list:
            if self.check_for_collision(sp, sprite):
                collision_list.append(sp)
        return collision_list
            
        
        
        # remember to return collision_list
        
        
        



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
        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
