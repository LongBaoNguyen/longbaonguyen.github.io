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
    def setup(self):
        """ Initialize your variables. Call this setup method to reset your game. """
        self.player = arcade.Sprite("tank.png", 1.0, WIDTH/2, HEIGHT/2)
        self.player.center_x = 200
        self.player.center_y = 300

        self.brick_list = arcade.SpriteList()
        
        for x in range(100, 300, 64):
            brick = arcade.Sprite("brick.png", 0.5, x, width/2)
            self.brick_list.append(brick)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.brick_list)
        
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        self.brick_list.draw()
        self.player.draw()
        
    def on_update(self):
        """ Called automatically 60 times a second to update our objects."""
        self.physics_engine.update()

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
            self.player.angle += 90
        elif key == 's':
            self.player.angle += -90

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
