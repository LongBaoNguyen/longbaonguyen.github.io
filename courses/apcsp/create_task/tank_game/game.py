"""
Create Task Example

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
        """
        
        self.player = arcade.Sprite("tank.png", 0.8)
        self.player.set_left(0)
        self.player.set_bottom(HEIGHT/2)
        
        
        # create empty brick_list and bullet_list
        self.brick_list = []
        self.bullet_list = []
        # create variable score, initialize to 0
        self.score = 0

        self.num_bricks = 10
        for i in range(self.num_bricks):
            # create a brick Sprite, add to list
            brick = arcade.Sprite("brick.png", 0.4)
            brick.center_x = random.randrange(WIDTH)
            brick.center_y = random.randrange(HEIGHT)
            self.brick_list.append(brick)
        
        self.coins = []
        self.score_coins = 0
        self.num_coins = 10
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
        
        # iterate through brick_list and draw 
        for brick in self.brick_list:
            brick.draw()
            
        for coin in self.coins:
            coin.draw()

        # iterate through bullet_list and draw
        for bullet in self.bullet_list:
            bullet.draw()
            
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Score:" + str(self.score), 20, 40)
        fill(255,0,0) # for text color
        text("Coins:" + str(self.score_coins), 20, 100)

        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        # update player 
        self.player.update()
        
        # iterate through bullet_list, update each bullet(to move bullets)
        for bullet in self.bullet_list:
            bullet.update()
            
        collision_coins = self.check_for_collision_list(self.player, self.coins)
        for sp in collision_coins:
            self.coins.remove(sp)
            self.score_coins += 1

        
        for bullet in self.bullet_list:
            collision_list = self.check_for_collision_list(bullet, self.brick_list)
            if len(collision_list) > 0:
                self.bullet_list.remove(bullet)
                self.brick_list.remove(collision_list[0])
                self.score += 1
            if bullet.get_left() > WIDTH:
                self.bullet_list.remove(bullet)
        
                
        
    def check_for_collision(self, sprite1, sprite2):
        """ Returns whether sprite1 and sprite2 intersect.(rectangle intersection)
        """
        x_overlap = sprite2.get_right() > sprite1.get_left() and sprite2.get_left() < sprite1.get_right() 
        y_overlap = sprite2.get_bottom() > sprite1.get_top() and sprite2.get_top() < sprite1.get_bottom()
        return x_overlap and y_overlap
        
      
    def check_for_collision_list(self, sprite, sprite_list):
        """ Returns list of sprites in sprite_list which intersect with sprite.
            Call check_for_collision method above. Use self and dot notation.                
        """
        collision_list = []
        for sp in sprite_list:
        #     if there's collision between sp and sprite 
            if self.check_for_collision(sp, sprite):
        #     add to collision_list 
                collision_list.append(sp)
        return collision_list
        
    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. 
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

        bullet = arcade.Sprite("bullet.png", 0.5)
        bullet.center_y = self.player.center_y
        bullet.center_x = self.player.center_x
        bullet.change_x = 15
        self.bullet_list.append(bullet)
        
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
