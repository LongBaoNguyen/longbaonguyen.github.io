# YOU MAY MODIFY THIS FILE.
# The Window class here is very similar to the arcade.Window class.
# PUT ALL OF YOUR CLASSES/FUNCTIONS HERE.

from __future__ import division
import arcade
from constants import *

class Window:
    def __init__(self):
        """ Declare your variables. """
        self.player = None
        self.brick_list = None
        self.physics_engine = None
        self.num_coins = 0
    def setup(self):
        """ Initialize your variables. Call this setup method to reset your game. """
        self.player = Player("right_tank.png", 1.0)
        print(self.player.cur_texture_index)

        self.brick_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        for x in range(100, 300, 64):
            brick = arcade.Sprite("brick.png", 0.5, x, height/2)
            self.brick_list.append(brick)
        
        for x in range(100, 800, 100):
            coin = arcade.Sprite("coin.png", 0.5, x, height/4)
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.brick_list)
        
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.brick_list.draw()
        self.player.draw()
        self.coin_list.draw()
        arcade.draw_text("hi", 50, HEIGHT - 100)
        arcade.draw_text("Coins: " + str(self.num_coins), 50, HEIGHT - 50)
        
    def on_update(self):
        """ Called automatically 60 times a second to update our objects."""

        self.physics_engine.update()
        self.player.update()
        
        collision_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        if len(collision_list) > 0:
            for coin in collision_list:
                self.coin_list.remove(coin)
                self.num_coins += 1
            

    def on_mouse_motion(self, x, y, dx, dy):        
        """ Called whenever the mouse moves. """
        pass    
    
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. """

        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. """
        pass
                  
    def on_key_press(self, key):
        """ Called automatically whenever a key is pressed. """
        if key == LEFT:
            self.player.change_x = -5
        elif key == RIGHT:
            self.player.change_x = 5
        elif key == UP:
            self.player.change_y = -5 
        elif key == DOWN:
            self.player.change_y = 5
        elif key == 'a':
            self.player.set_texture(1)

    def on_key_release(self, key):
        """ Called automatically whenever a key is released. """
        if key == LEFT:
            self.player.change_x = 0
        elif key == RIGHT:
            self.player.change_x = 0
        elif key == UP:
            self.player.change_y = 0
        elif key == DOWN:
            self.player.change_y = 0
            
            
class Player(arcade.Sprite):
    def __init__(filename, scale):
        super().__init__(filename, scale)
        texture = arcade.load_texture("left_tank.png")
        self.textures.append(texture)
        print(len(self.textures))
        self.set_texture(0)
    def update(self):
        super().update()
        if self.change_x > 0:
            self.texture = self.textures[0]
        if self.change_x < 0:
            self.texture = self.textures[1]
        

        
        
    
