"""
Placing Coins Away from Bricks and Other Coins

Do the following:

1) Use nested loop to create rows of bricks(e.g., 4 rows, each with 10 bricks).  
2) Use for loop to create set of coins where each coin is placed away from bricks and other coins.
Note: Each iteration of for loop, use while loop until a coin is placed successfully.
3) Use PhysicsEngineSimple class to detect/resolve brick collision.
4) In update(), use code from Pick Up Coins Lab to pick up coins. 

"""

import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        
        self.tank = None
        self.brick_list = None
        self.coin_list = None
        self.physics_engine = None
        self.num_coins = None

    def setup(self):

        self.tank = arcade.Sprite("images/tank.png", 0.5)
        self.tank_list = arcade.SpriteList()
        self.tank_list.append(self.tank)

        self.num_coins = 30
        
        # Initialize brick_list as a SpriteList
        # Then use nested for loops to place rows of bricks. 
        # (Hint: Outer for loop is y coordinate skipping every 150 pixels
        #        Inner for loop is x coordinate skipping every 64 pixels)
        # Append bricks to brick_list


        # Initialize coin_list as a SpriteList


        # PSEUDOCODE for how to place coins. 
        # for each i in range of number of coins 
        #       create coin Sprite
        #       set boolean variable successfully_placed to False
        #       while not successfully_placed
        #           set center_x and center_y randomly
        #           compute collision lists for coin with bricks
        #           AND coin with other coins (2 lists)
        #           if both lists have 0 length, then we have successfully placed the coin
        #                  add coin to coin_list
    




        # initialize physics_engine



    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        # draw everything



    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update objects.
            delta_time is time since the last time on_update was called."""
        # update physics engine
        
        
        # use code from pick up coins lab to pick up coins
        # you don't need all of the code from that lab(no gameover or reset)

        
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




