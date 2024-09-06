"""
Multiplication Table

"""


from __future__ import division, print_function
from arcade import *
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
        self.screen = 1
        self.level = 1
        
    
    def restart(self):
        self.first_try = True
        self.answer = ""
        self.num_corr = 0
        self.num_incorr = 0
        if self.level == 1:
            self.problems = level_1[:]
        elif self.level == 2:
            self.problems = level_2[:]
        elif self.level == 3:
            self.problems = level_3[:]
        elif self.level == 4:
            self.problems = level_4[:]

        random.shuffle(self.problems)
        self.problem = self.problems.pop()
        self.correct_answer = table[self.problem]
        self.remaining = len(self.problems)
        self.feedback = ""
        self.game_over = False
        self.reading_input = True
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """ 
        if self.screen == 1:
            textSize(42)
            textAlign(LEFT, CENTER)
            fill(0,0,0) # for text color
            text("Multiplication Table Quiz", 20, 50)
            textSize(32)

            fill(0,0,0) # for text color
            text("Pick a level. Press arrow keys to change: ", 20, 150)
            fill(255,0,0) # for text color
            text(str(self.level), 660, 150)
            fill(0, 0, 0)
            text("Level 1. {1,2,3,4,5} x {1,2,3,4,5}", 20, 230)
            text("Level 2. {1,2,3,4,5} x {6,7,8,9,10}", 20, 260)
            text("Level 3. {6,7,8,9,10} x {6,7,8,9,10}", 20, 290)
            text("Level 4. 1 - 10", 20, 320)

            textSize(42)
            textAlign(LEFT, CENTER)
            fill(0,0,0) # for text color
            text("Press 'r' anytime to reset.", 20, 400)


        elif self.screen == 2:
        
            # display text, left-center align    
            textSize(32)
            textAlign(LEFT, CENTER)
            fill(0,0,0) # for text color
            text("Level: " + str(self.level), 20, 40)
            fill(0,255,0) # for text color
            text("Correct: " + str(self.num_corr), 20, 500)
            fill(255,0,0) # for text color
            text("Incorrect: " + str(self.num_incorr), 20, 550)
            
            fill(0,255,255) # for text color
            text("Remaining Problems: " + str(self.remaining), 20, 450)
    
    
            textSize(52)
            fill(0,0,255) # for text color
            text(self.problem + " = " + self.answer, 50, 250)
            
            textSize(32)
            fill(255,0,0) # for text color
            text(self.feedback, 50, 300)
            
            if self.game_over:
                fill(0,0,0) # for text color
                textSize(30)
                text("All done! Good job!", 50, 80)
                text("Press 'r' to restart.", 50, 100)

    



        
    def on_update(self):
        """ Called to update our objects about 60 times per second.
            Write code to update all objects(for animation).
        """
        
        
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
        if key == 'r':
            self.screen = 1
            self.level = 1
            self.restart()
        if self.screen == 1:
            if key == RIGHT:
                self.level += 1
                if self.level == 5:
                    self.level = 1
            elif key == LEFT:
                self.level -= 1
                if self.level == 0:
                    self.level = 4
            elif key == ENTER or key == RETURN:
                self.screen = 2
                self.restart()
        elif self.screen == 2:           
            if self.reading_input:
                if key in "1234567890":
                    self.answer += key
                if key == DELETE or key == BACKSPACE:
                    self.answer = self.answer[:-1]
        
                if key == ENTER or key == RETURN:
                    if self.answer != "" and self.correct_answer == int(self.answer):
                        self.num_corr += 1
                        self.feedback = "Correct!"
                        self.reading_input = False

                    elif self.first_try and self.answer != "" and self.correct_answer != int(self.answer):
                        self.feedback = "Incorrect! Try again."
                        self.first_try = False
                    else:
                        self.num_incorr += 1
                        self.feedback = "Incorrect! The answer is " + str(self.correct_answer) + "."
                        self.problems.append(self.problem)
                        random.shuffle(self.problems)
                        self.reading_input = False
            if key == " ":
                if len(self.problems) == 0:
                    self.game_over = True
                else:
                    self.problem = self.problems.pop()
                    self.correct_answer = table[self.problem]
                    self.answer = ""
                    self.feedback = ""
                    self.remaining = len(self.problems)
                    self.reading_input = True
                    self.first_try = True
        
    def on_key_release(self, key):
        """ Called automatically whenever a key is released. 
        """
        pass
        
        
    def on_mouse_press(self, x, y, button):
        """ Called whenever the mouse is pressed. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER
        """
        pass
        
    def on_mouse_release(self, x, y, button):
        """ Called whenever the mouse is released. 
            Parameters: x, y location of the mouse
                        button: LEFT, RIGHT, CENTER

        """
        pass
                  
      
        
        
    
