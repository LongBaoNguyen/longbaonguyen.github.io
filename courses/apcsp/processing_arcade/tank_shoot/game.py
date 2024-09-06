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
        # TODO, set player's center to middle of screen
        self.player.center_x = WIDTH // 2
        self.player.center_y = HEIGHT // 2 
                
        # TODO, create empty brick_list and bullet_list
        self.brick_list = []
        self.bullet_list = []

        # TODO, create variable score, initialize to 0
        self.score = 0
 

        self.num_bricks = 10
        for i in range(self.num_bricks):
            # create a coin Sprite, add to list
            brick = arcade.Sprite("brick.png", 0.4)
            brick.center_x = random.randrange(WIDTH)
            brick.center_y = random.randrange(HEIGHT)
            self.brick_list.append(brick)
            

    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """    
        self.player.draw()
        
        # TODO, iterate through brick_list and draw 
        for brick in self.brick_list:
            brick.draw()
        
            
        # TODO, iterate through bullet_list and draw
        for bullet in self.bullet_list:
            bullet.draw()
        
            
        textSize(32)
        textAlign(LEFT, CENTER)
        fill(255,0,0) # for text color
        text("Score:" + str(self.score), 20, 40)

        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        # TODO, update player 
        self.player.update()
        
        # TODO, iterate through bullet_list, update each bullet(to move bullets)
        for bullet in self.bullet_list:
            bullet.update()    
        
        

        # TODO
        # for each bullet in bullet_list, 
        #   call check_for_collision_list with brick_list to get collision list
        #   if collision_list is not empty:
        #     remove bullet from bullet_list
        #     remove first element of collision_list from brick_list  
        #     update score
        #   if bullet leaves right side of screen
        #      remove bullet 
        
        for bullet in self.bullet_list:
            collision_list = self.check_for_collision_list(bullet, self.brick_list)
            if len(collision_list) != 0:
                self.bullet_list.remove(bullet)
                self.brick_list.remove(collision_list[0])
                self.score += 1
            if bullet.center_x > WIDTH:
                self.bullet_list.remove(bullet)
                

        

                
        
    def check_for_collision(self, sprite1, sprite2):
        """ Returns whether sprite1 and sprite2 intersect.(rectangle intersection)
        """
        # TODO
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
        
        # TODO
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
        bullet = arcade.Sprite("bullet.png")
        bullet.center_y = self.player.center_y


        # set left side of bullet to equal right side of player
        bullet.set_left(self.player.get_right())
        
        # set change_x to 10(velocity)
        bullet.change_x = 10
        
        # append to bullet_list
        self.bullet_list.append(bullet)
        
        
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
