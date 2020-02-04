"""
Tank Shooting Lab

Tank shoots bullets whenever mouse is clicked. Place 10 bricks randomly on the screen. 
If bullet hits brick, both are removed. If bullet leaves the screen, it is removed. 

Do the following. Make sure each part works before moving on the next part!

1) Initialize bullet_list(SpriteList) in setup
2) In on_mouse_press, each time mouse is pressed, create a bullet, initialize
   it to be at the location of the player(same center_y, but left side of bullet
   should be equal to right side of player)
   Set change_x of bullet to 10. Append to bullet_list.
   Update and draw bullet_list.
   If 1) and 2) works, you are now able to shoot each time mouse is clicked. 
3) In setup, create brick_list and randomly, placed 10 bricks in brick_list. 
   Draw them.
4) In update():
   for each bullet in bullet_list, call check_for_collision_with_list 
   with brick_list to get collision list
       if collision_list is not empty:
           remove bullet from bullet_list
           remove first element of collision_list from brick_list(or all of them , up to you) 
       if bullet leaves screen, it is removed  
5) Add a score variable to keep track of how many bricks are hit. Display score.

   

"""

import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.tank = None
        self.tank_list = None
        self.brick_list = None
        self.physics_engine = None

    def setup(self):

        self.tank = arcade.Sprite("images/tank.png", 0.5)
        self.tank_list = arcade.SpriteList()
        self.tank_list.append(self.tank)
        
        # initialize bullet list to empty SpriteList
        
        # create brick_list and randomly, placed 10 bricks in brick_list. 




    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        self.tank_list.draw()

        # draw bullet_list
        
        # draw brick_list
    
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update objects.
            delta_time is time since the last time on_update was called."""
        
        self.tank_list.update()

        # update bullet_list

                
        # for each bullet in bullet_list
        # call check_for_collision_with_list with brick_list to get collision list
        #     if collision_list is not empty:
        #           remove bullet from bullet_list
        #           remove first element of collision_list from brick_list    
        #            (to remove, use kill() or remove_from_sprite_lists()
        #            for example: bullet.kill())
        #     if bullet leaves screen, remove it

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse is pressed. """
        
        # create bullet Sprite
        
        # set center_y to equal player center_y
        
        # set left side of bullet to equal right side of player
        
        # set change_x to 10
        
        # append to bullet_list
        

        
    def on_key_press(self, key, modifiers):
        """ Called automatically whenever a key is pressed. """
        if key == arcade.key.LEFT:
            self.tank.change_x = -5
        elif key == arcade.key.RIGHT:
            self.tank.change_x = 5
        elif key == arcade.key.UP:
            self.tank.change_y = 5
        elif key == arcade.key.DOWN:
            self.tank.change_y = -5

    def on_key_release(self, key, modifiers):
        """ Called automatically whenever a key is released. """    
        if key == arcade.key.LEFT:
            self.tank.change_x = 0
        elif key == arcade.key.RIGHT:
            self.tank.change_x = 0
        elif key == arcade.key.UP:
            self.tank.change_y = 0
        elif key == arcade.key.DOWN:
            self.tank.change_y = 0
    
    
def main():
    """ Main method """
    window = GameWindow(WIDTH, HEIGHT, "Resolving Many-Wall Collisions with Engine")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




