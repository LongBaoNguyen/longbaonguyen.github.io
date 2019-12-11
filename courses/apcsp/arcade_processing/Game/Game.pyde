from __future__ import division
import arcade


player = None
brick_list = None



def setup():
    global player, brick, brick_list
    size(800, 600)
    imageMode(CENTER)
    player = arcade.Sprite("tank.png", 1.0, width/2, height/2)
    brick_list = arcade.SpriteList()
    

    for x in range(100, 300, 64):
        brick = arcade.Sprite("brick.png", 0.5, x, width/2)
        brick_list.append(brick)
    

def draw():
    global player
    background(255)
    player.draw()
    
    for brick in brick_list:
        brick.draw()
    
    resolve_collision(player, brick_list)
 
def resolve_collision(sprite, sprite_list):
    sprite.center_x += sprite.change_x
    hit_list = arcade.check_for_collision_with_list(sprite, sprite_list)
    # If we hit a wall, move so the edges are at the same point
    if len(hit_list) > 0:
        if sprite.change_x > 0:
            for item in hit_list:
                sprite.set_right(min(item.get_left(),
                                            sprite.get_right()))
        elif sprite.change_x < 0:
            for item in hit_list:
                sprite.set_left(max(item.get_right(),
                                            sprite.get_left()))
        else:
            print("Error, collision while player wasn't moving.")
    
    # --- Move in the y direction
    sprite.center_y += sprite.change_y
    
    # Check for wall hit
    hit_list = arcade.check_for_collision_with_list(sprite, sprite_list)
    
    # If we hit a wall, move so the edges are at the same point
    if len(hit_list) > 0:
        if sprite.change_y < 0:
            for item in hit_list:
                sprite.set_top(max(item.get_bottom(), sprite.get_top()))
        elif sprite.change_y > 0:
            for item in hit_list:
                sprite.set_bottom(min(item.get_top(), sprite.get_bottom()))
        else:
            print("Error, collision while player wasn't moving.")    
    
    
         
def keyPressed():
    if keyCode == LEFT:
        player.change_x = -5
    elif keyCode == RIGHT:
        player.change_x = 5
    elif keyCode == UP:
        player.change_y = -5
    elif keyCode == DOWN:
        player.change_y = 5
    
def keyReleased():
    if keyCode == LEFT:
        player.change_x = 0
    elif keyCode == RIGHT:
        player.change_x = 0
    elif keyCode == UP:
        player.change_y = 0
    elif keyCode == DOWN:
        player.change_y = 0
    
