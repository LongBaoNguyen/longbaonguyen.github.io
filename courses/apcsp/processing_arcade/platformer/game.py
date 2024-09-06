"""
Simple Platformer Game

In this lab, you will need to fill in code for the following IN THIS ORDER:

FOR some of the functions, REMOVE THE WORD "pass" and fill in the code as directed.    
    
1) __init__
2) on_draw
3) resolve_collisions_platforms
4) on_update
5) is_on_platforms
6) on_key_press

Note that create_platforms function is given to you in its entirety and you'll need
to call it.

Complete all parts with "TODO" directions.

"""


from __future__ import division, print_function
import arcade
import random

WIDTH = 800 # width of screen in pixels
HEIGHT = 600 # height of screen in pixels

BACKGROUND_COLOR = color(255)  # 0(black), 255(white)

MOVE_SPEED = 4;
SPRITE_SCALE = 50.0/128;
SPRITE_SIZE = 50;
GRAVITY = .6;
JUMP_SPEED = 14; 


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
        # TODO call create_platforms with "map.csv" to create platform list
        # store returned platforms in variable self.platforms

                
        # initialize player
        self.player = arcade.Sprite("player.png", 0.8)
        self.player.center_x = 300
        self.player.center_y = 100
        

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        # TODO draw player

                
        # TODO draw platforms

        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        # TODO call resolve_collisions_platforms
        
        
    def resolve_collisions_platforms(self, sprite):
        pass
        # TODO add gravity to change_y of sprite
  
  
        # TODO move in y-direction by adding change_y to center_y to update y position.
  
  
        # TODO Now resolve any collision in the y-direction:
        # compute collision_list between sprite and walls(platforms).

                
        # TODO
        # if collision list is nonempty:
        #   get the first platform from collision list
        #   if sprite is moving down(change_y > 0)
        #     set bottom of sprite to equal top of platform
        #   else if sprite is moving up
        #     set top of sprite to equal bottom of platform
        #   set sprite's change_y to 0


                        

        # TODO move in x-direction by adding change_x to center_x to update x position.

    
        # TODO
        # Now resolve any collision in the x-direction:
        # compute collision_list between sprite and walls(platforms).

      
        # TODO
        # if collision list is nonempty:
        #   get the first platform from collision list
        #   if sprite is moving right
        #      set right side of sprite to equal left side of platform
        #   else if sprite is moving left
        #      set left side of sprite to equal right side of platform        
        

    
            
    def is_on_platforms(self, sprite):
        pass
        # TODO move down 5 pixels

                
        # TODO compute collision list between player with platforms

        # TODO move back up 5 pixels to restore original position

                
        # TODO return whether list is nonempty

                
    def check_for_collision(self, sprite1, sprite2):
        """ Returns whether sprite1 and sprite2 intersect.(rectangle intersection)
        """
        # follow intersection rules from lecture notes to implement collision detection
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
        
        # create empty list collision_list
        collision_list = []
        # for each sprite sp in sprite_list:
        for sp in sprite_list:
        #     if there's collision between sp and sprite 
            if self.check_for_collision(sp, sprite):
        #     add to collision_list 
                collision_list.append(sp)
        # remember to return collision_list
        return collision_list
        
    def create_platforms(self, filename):
        platforms = []
        lines = loadStrings(filename)
        for row, line in enumerate(lines):
            values = split(line, ",")
            for col, value in enumerate(values):
                if value == "1":
                    sprite = arcade.Sprite("red_brick.png", SPRITE_SCALE)
                    sprite.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
                    sprite.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
                    platforms.append(sprite)
                elif value == "2":
                    sprite = arcade.Sprite("tile.png", SPRITE_SCALE)
                    sprite.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
                    sprite.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
                    platforms.append(sprite)
                elif value == "3":
                    sprite = arcade.Sprite("brown_brick.png", SPRITE_SCALE)
                    sprite.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
                    sprite.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
                    platforms.append(sprite)
                elif value == "4":
                    sprite = arcade.Sprite("crate.png", SPRITE_SCALE)
                    sprite.center_x = SPRITE_SIZE/2 + col * SPRITE_SIZE;
                    sprite.center_y = SPRITE_SIZE/2 + row * SPRITE_SIZE;
                    platforms.append(sprite)
        return platforms
    
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
        # TODO
        # add and elif key pressed is 'a' and is_on_platforms returns True:
            # change player change_y to -JUMP_SPEED 
        

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
        
        # set change_x to 10(velocity)
        
        # append to bullet_list
        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
