"""
Resolving Collisions Lab

Do the following:

1) Create a SpriteList of "brick.png" Sprites. 
2) Initialize two rows of brick sprites. One with all adjacent bricks and one with spacing
enough for the tank to go in between. 
3) Use PhysicsEngineSimple class to detect/resolve collision! See the source code
https://github.com/pvcraven/arcade/blob/master/arcade/physics_engines.py
to see how to create an object of this class. Note: This part of the lab should only takes
2 lines of code!

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
        
        # declare the variables: brick_list, physics_engine

        self.brick_list = None
        self.physics_engine = None

    def setup(self):

        self.tank = arcade.Sprite("images/tank.png", 0.5)
        self.tank_list = arcade.SpriteList()
        self.tank_list.append(self.tank)
        
        # initialize brick_list as a SpriteList

        self.brick_list = arcade.SpriteList()
        # use a for loop to create a set of HORIZONTAL, ADJACENT "brick.png" Sprites.
        # Remember to add them to brick_list
        # Hint: Use for loop with range(begin, end, step)
        
        for x in range(100, 700, 64):
            brick = arcade.Sprite("images/brick.png", 0.5, center_x=x, center_y=200)
            self.brick_list.append(brick)



        # use a for loop to create a set of HORIZONTAL, "brick.png" Sprites
        # with spacing enough for tank to go between them.

        for x in range(100, 700, 200):
            brick = arcade.Sprite("images/brick.png", 0.5, center_x=x, center_y=400)
            self.brick_list.append(brick)


        # initialize physics_engine, see source code in link above
        # use PhysicsEngineSimple class.

        self.physics_engine = arcade.PhysicsEngineSimple(self.tank, self.brick_list)


    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        self.tank_list.draw()
        # draw brick_list
        self.brick_list.draw()
    
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update objects.
            delta_time is time since the last time on_update was called."""
        # update physics engine
        self.physics_engine.update()

        
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




