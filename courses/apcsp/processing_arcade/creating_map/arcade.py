# DO NOT MODIFY THIS FILE!!!!!!!!
# DO NOT MODIFY THIS FILE!!!!!!!!


from __future__ import division, print_function

# all sprites are 50 pixels x 50 pixels(can be adjusted for different images)
TANK_SCALE = 50.0/92
BRICK_SCALE = 50.0/128
COIN_SCALE = 50.0/64
SPRITE_SIZE = 50;


def read_map(csv_filename):
    """ csv_filename is a comma separated file which contains numbers(2D) indicating 
        objects on a map. For example: "0" is empty space, "1" is a brick, "2" is a coin.
        The function returns a tuple of two lists: (bricks, coins)
        You can modify this function to fit your own game. 
        Scaling factors: TANK_SCALE, BRICK_SCALE can be adjusted according to the images. 
        Here: Every image is scale to 50 x 50. 
    """
    bricks = []
    coins = []
    lines = loadStrings(csv_filename)
    for i in range(len(lines)):
        values = split(lines[i], ",")
        for j in range(len(values)):
            if values[j] == "1":
                sprite = Sprite("red_brick.png", BRICK_SCALE)
                sprite.center_x = SPRITE_SIZE/2 + j * SPRITE_SIZE
                sprite.center_y = SPRITE_SIZE/2 + i * SPRITE_SIZE;
                bricks.append(sprite)
            elif values[j] == "2":
                sprite = Sprite("coin.png", COIN_SCALE)
                sprite.center_x = SPRITE_SIZE/2 + j * SPRITE_SIZE
                sprite.center_y = SPRITE_SIZE/2 + i * SPRITE_SIZE;
                coins.append(sprite)
    return bricks, coins

                

    
    




# class for creating Sprites
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
