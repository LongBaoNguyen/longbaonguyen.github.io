# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!

# Useful classes: Sprite, SpriteList, PhysicsEngineSimple
# Useful functions: check_for_collision, check_for_collision_with_list


from __future__ import division, print_function

def draw_text(txt, x, y, clr=color(0), font_size=32, anchor_x=LEFT, anchor_y=BOTTOM):
    txt = str(txt)
    textSize(font_size)
    textAlign(anchor_x, anchor_y)
    fill(clr)
    text(txt, x, y)

def draw_circle_filled(center_x, center_y, radius, fill_clr=color(0), stroke_clr=color(0), line_width=1):
    fill(fill_clr)
    stroke(stroke_clr)
    strokeWeight(line_width)
    ellipse(center_x, center_y, 2 * radius, 2 * radius)

def draw_rectangle_filled(center_x, center_y, w, h, fill_clr=color(0), stroke_clr=color(0), line_width=1):
    fill(fill_clr)
    stroke(stroke_clr)
    strokeWeight(line_width)
    rect(center_x, center_y, w, h)
    
def draw_line(start_x, start_y, end_x, end_y, stroke_clr=color(0), line_width=1):
    stroke(stroke_clr)
    strokeWeight(line_width)
    line(start_x, start_y, end_x, end_y)
    
    
def load_texture(filename): 
    return loadImage(filename)   

def check_for_collision(sprite1, sprite2):
    no_x_overlap = sprite1.get_right() <= sprite2.get_left() or sprite2.get_right() <= sprite1.get_left()
    if no_x_overlap:
        return False
    no_y_overlap = sprite1.get_top() >= sprite2.get_bottom() or sprite2.get_top() >= sprite1.get_bottom()
    if no_y_overlap:
        return False
    return True

def check_for_collision_with_list(sprite, sprite_list):
    collision_list = [sprite2 for sprite2 in sprite_list 
                      if sprite is not sprite2 and check_for_collision(sprite, sprite2)]
    return collision_list


class Sprite(object):
    def __init__(self, filename, scale=1.0, center_x=0, center_y=0, angle=0, alpha=255):
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0
        self.texture = loadImage(filename)
        self.textures = [self.texture]
        self.cur_texture_index = 0
        self.scale = scale
        self.width = self.texture.width * self.scale
        self.height = self.texture.height * self.scale
        self.angle = angle  # in degrees
        self.change_angle = 0.0
        self.alpha = alpha # 255 is fully opaque, 0 is fully transparent
    def draw(self):
        pushMatrix();
        translate(self.center_x, self.center_y);
        rotate(radians(self.angle));
        tint(255, self.alpha);
        image(self.texture, 0, 0, self.width, self.height)
        tint(255, 255);
        popMatrix();
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
    def set_texture(self, index):
        self.texture = self.textures[index]
    def get_left(self):
        return self.center_x - self.width/2
    def set_left(self, l):
        self.center_x = l + self.width/2
    def get_right(self):
        return self.center_x + self.width/2
    def set_right(self, r):
        self.center_x = r - self.width/2
    def get_top(self):
        return self.center_y - self.height/2
    def set_top(self, t):
        self.center_y = t + self.height/2
    def get_bottom(self):
        return self.center_y + self.height/2
    def set_bottom(self, b):
        self.center_y = b - self.height/2

class SpriteList:
    def __init__(self):
        self.sprite_list = []
    def append(self, item):
        self.sprite_list.append(item)
    def remove(self, item):
        self.sprite_list.remove(item)
    def update(self):
        for sprite in self.sprite_list:
            sprite.update()
    def draw(self):
        for sprite in self.sprite_list:
            sprite.draw()
    def __getitem__(self, i):
        return self.sprite_list[i]
    def __len__(self):
        return len(self.sprite_list)
 
class PhysicsEngineSimple:
    """
    This class will move everything, and take care of collisions.
    """
    def __init__(self, player_sprite, walls):
        """
        Constructor.
        """
        self.player_sprite = player_sprite
        self.walls = walls

    def update(self):
        """
        Move everything and resolve collisions.
        """
        # --- Move in the x direction
        self.player_sprite.center_x += self.player_sprite.change_x

        # Check for wall hit
        hit_list = check_for_collision_with_list(self.player_sprite, self.walls)

        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            if self.player_sprite.change_x > 0:
                for item in hit_list:
                    self.player_sprite.set_right(min(item.get_left(),
                                                   self.player_sprite.get_right()))
            elif self.player_sprite.change_x < 0:
                for item in hit_list:
                    self.player_sprite.set_left(max(item.get_right(),
                                                  self.player_sprite.get_left()))
            else:
                print("Error, collision while player wasn't moving.")

        # --- Move in the y direction
        self.player_sprite.center_y += self.player_sprite.change_y

        # Check for wall hit
        hit_list = check_for_collision_with_list(self.player_sprite, self.walls)

        # If we hit a wall, move so the edges are at the same point
        if len(hit_list) > 0:
            if self.player_sprite.change_y < 0:
                for item in hit_list:
                    self.player_sprite.set_top(max(item.get_bottom(),
                                                 self.player_sprite.get_top()))
            elif self.player_sprite.change_y > 0:
                for item in hit_list:
                    self.player_sprite.set_bottom(min(item.get_top(),
                                                    self.player_sprite.get_bottom()))
            else:
                print("Error, collision while player wasn't moving.")
    
# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!
        
                      
    
    

 
