"""
Name: 

Title of Create Task:     
   
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
    
    
    def sub_algorithm_1(self, a, b):
        """ Rename this subalgorithm 1 and modify its parameters. 
            Modify this comment to reflect your subalgorithm.
        """
        pass
        
                        

    def sub_algorithm_2(self, a, b):     
        """ Rename this subalgorithm 1 and modify its parameters. 
            Modify this comment to reflect your subalgorithm.
        """
        pass
    

        
    def on_key_press(self, key, modifiers):
        """ Called automatically whenever a key is pressed. """
        #if key == arcade.key.LEFT:
        #    self.tank.change_x = -5
        #elif key == arcade.key.RIGHT:
        #    self.tank.change_x = 5
        
    def on_key_release(self, key, modifiers):
        """ Called automatically whenever a key is released. """    
        #if key == arcade.key.LEFT:
        #    self.tank.change_x = -5
        #elif key == arcade.key.RIGHT:
        #    self.tank.change_x = 5
    
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse is pressed. """
        
        pass    
    
def main():
    """ Main method """
    window = GameWindow(WIDTH, HEIGHT, "Create Task")
    arcade.run()


if __name__ == "__main__":
    main()




