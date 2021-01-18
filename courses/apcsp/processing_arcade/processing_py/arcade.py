# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!

# Useful classes: Sprite, SpriteList
# Useful functions: check_for_collision, check_for_collision_with_list


from __future__ import division, print_function

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
