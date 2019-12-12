# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!


from __future__ import division, print_function

import main
import arcade
from constants import *

window = None

def setup():
    global window
    size(WIDTH, HEIGHT)
    rectMode(CENTER)
    imageMode(CENTER)
    window = main.Window()
    window.setup()
    

def draw():
    background(BACKGROUND_COLOR)
    window.on_draw()
    window.on_update()

def keyPressed():
    if key == CODED:
        window.on_key_press(keyCode)
    else:
        window.on_key_press(key)
    
def keyReleased():
    if key == CODED:
        window.on_key_release(keyCode)
    else:
        window.on_key_release(key)

def mouseMoved():
    window.on_mouse_motion(mouseX, mouseY, pmouseX, pmouseY)

def mousePressed():
    window.on_mouse_press(mouseX, mouseY, mouseButton)

def mouseReleased():
    window.on_mouse_release(mouseX, mouseY, mouseButton)
