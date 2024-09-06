# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!


from __future__ import division, print_function


level_1 = []
for i in range(2, 6):
    for j in range(2, 6):
        value = str(i) + " x " + str(j)
        level_1.append(value)

level_2 = []
for i in range(2, 6):
    for j in range(6, 11):
        value = str(i) + " x " + str(j)
        level_2.append(value)
    
level_3 = []
for i in range(6, 8):
    for j in range(6, 11):
        value = str(i) + " x " + str(j)
        level_3.append(value)

level_4 = []
for i in range(8, 11):
    for j in range(6, 11):
        value = str(i) + " x " + str(j)
        level_4.append(value)

level_5 = level_1 + level_2 + level_3 + level_4

table = {}

for x in level_1:
    value = int(x[0]) * int(x[4])
    table[x] = value

for x in level_2:
    if len(x) == 5:
        value = int(x[0]) * int(x[4])
    elif len(x) == 6:
        value = int(x[0]) * int(x[4:])
    else:
        value = int(x[0:2]) * int(x[5:])

    table[x] = value
    
for x in level_3:
    if len(x) == 5:
        value = int(x[0]) * int(x[4])
    else:
        value = int(x[0]) * int(x[4:])
    table[x] = value


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
