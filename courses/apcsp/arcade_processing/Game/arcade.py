from __future__ import division


class Sprite:
    def __init__(self, filename, scale=1.0, center_x=0, center_y=0):
        self.texture = loadImage(filename)
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0
        self.width = self.texture.width*scale
        self.height = self.texture.height*scale
        #print(self.width)
    def draw(self):
        image(self.texture, self.center_x, self.center_y, self.width, self.height)
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
    def get_left(self):
        return self.center_x - self.width/2
    def set_left(self, l):
        self.center_x = l + self.width/2
    def get_right(self):
        return self.center_x + self.width/2
    def set_right(self, r):
        self.center_x = r - self.width/2
    def get_top(self):
        return self.center_y - self.width/2
    def set_top(self, t):
        self.center_y = t + self.width/2
    def get_bottom(self):
        return self.center_y + self.width/2
    def set_bottom(self, b):
        self.center_y = b - self.width/2

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

    
    

 
