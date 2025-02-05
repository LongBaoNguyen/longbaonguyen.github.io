# IMPLEMENT the check_for_collision_list function below

from __future__ import division, print_function


def check_for_collision(sprite1, sprite2):
    """ Returns whether sprite1 and sprite2 intersect.(rectangle intersection)
    """
    # follow intersection rules from lecture notes to implement collision detection
    # see this link to see the math:
    # https://longbaonguyen.github.io/courses/apcsp/processing_arcade/processing4.pdf
    
    x_overlap = sprite1.get_right() > sprite2.get_left() and sprite1.get_left() < sprite2.get_right()
    y_overlap = sprite1.get_bottom() > sprite2.get_top() and sprite1.get_top() < sprite2.get_bottom()
    return x_overlap and y_overlap 


def check_for_collision_list(sprite, sprite_list):
    """ Returns list of sprites in sprite_list which intersect with sprite.
        MUST Call check_for_collision function above.         
    """
    # TODO
    # create empty list collision_list
    # for each sprite sp in sprite_list:
    #     if there's collision between sp and sprite 
    #     add to collision_list 
    # remember to return collision_list

        
            
            
        
    
                





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
    def move(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle
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
