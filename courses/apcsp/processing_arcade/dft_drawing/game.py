"""
DFT Drawings

IMPLEMENT ALL PARTS LABELED "TODO".
"""
from __future__ import division, print_function
from utility import *
import random

WIDTH = 800 # width of screen in pixels
HEIGHT = 600 # height of screen in pixels

BACKGROUND_COLOR = color(255)  # 0(black), 255(white)

TIME = 2 * PI

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
        points = read_points("pi.csv")
        self.time = 0
        self.y = []
        self.epi = True
        self.path = []
        for x, y in points:
            pt = Complex(x, y)
            self.y.append(pt)
        self.Y = dft(self.y)
        print(self.Y)
        self.Y.sort(key=lambda t: t[1], reverse=True)
        print(self.Y)
        
    def on_draw(self):
        """ Called automatically 60 times a second to draw objects.
            Write code to draw all objects.
        """  
        vector = self.draw_circles(WIDTH//2, HEIGHT//2, 0, self.Y)
        self.path.insert(0, vector)
        noFill()
        stroke(0)
        beginShape()
        for i in range(len(self.path)):
            vertex(self.path[i].x, self.path[i].y)
        endShape()
        self.time += TIME / len(self.Y)
        
        if self.time > TIME:
            self.time = 0
            self.path = []
        
    def draw_circles(self, x, y, rot, Y):
        N = len(Y)
        for i in range(N):
            prevx, prevy = x, y
            freq, radius, phase = Y[i]
            radius = radius / N
            x += radius * cos(freq * self.time + phase + rot) 
            y += radius * sin(freq * self.time + phase + rot) 
            if self.epi:
                stroke(255, 100, 100);
                noFill();
                ellipse(prevx, prevy, radius * 2, radius * 2);
                stroke(255);
                line(prevx, prevy, x, y);
        return PVector(x, y)


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
        pass


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
                  
      
        
        
    
