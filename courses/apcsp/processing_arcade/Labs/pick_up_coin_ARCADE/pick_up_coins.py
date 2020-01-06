"""
Pick Up Coins Lab

Do the following:

1) The player Sprite along with some other variables have already been created for you. 
2) In setup(), inititalize a SpriteList. Use a for loop to initialize coins at random positions 
on the screen. Use the imported random module and random.randrange(n) generates a random integer
from 0 to n - 1 (similar to range()) to initialize the positions of the coins. Add to the SpriteList.
3) Use arcade.check_for_collision_with_list to get a list of Sprites collided with player.
4) For each one in the list, update the number of coins collected and remove from SpriteList.
5) If all coins have been removed, display "You win! Press r to restart!". If the user presses "r",
reset the game.

"""


import arcade

WIDTH = 800
HEIGHT = 600


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        

        


    def on_draw(self):
        """ Called automatically 60 times a second to draw objects."""
        arcade.start_render()
        
    
    def on_update(self, delta_time):
        """ Called automatically 60 times a second to update objects.
            delta_time is time since the last time on_update was called."""
        
        

        
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
    window = GameWindow(WIDTH, HEIGHT, "Pick Up Coins")
    arcade.run()


if __name__ == "__main__":
    main()




