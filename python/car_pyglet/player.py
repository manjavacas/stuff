import pyglet
import math

from road import Road

from pyglet.window import key
from physical_object import PhysicalObject

PLAYER_POS_X = 1210
PLAYER_POS_Y = 830

LINE_PROX_LOW = -2000
LINE_PROX_UP = 2000

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

player_img = pyglet.resource.image('car.png')
player_img.anchor_x = player_img.width // 2
player_img.anchor_y = player_img.height // 2


def limit(x, a, b):
    if x < a:
        return a
    elif x >= b:
        return b
    return x


class Player(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=player_img, *args, **kwargs)

        self.rotation = 0

        self.acceleration = 2000.0
        self.max_velocity = 3000.0
        self.rotate_speed = 150.0
        self.friction = .9

        self.crashed = False
        self.current_line = 0

        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            angle_rads = -math.radians(self.rotation)
            self.velocity_x += math.cos(angle_rads) * self.acceleration * dt
            self.velocity_y += math.sin(angle_rads) * self.acceleration * dt
        if self.key_handler[key.DOWN]:
            angle_rads = -math.radians(self.rotation)
            self.velocity_x -= math.cos(angle_rads) * \
                (self.acceleration/2) * dt
            self.velocity_y -= math.sin(angle_rads) * \
                (self.acceleration/2) * dt

        self.velocity_x = limit(
            self.velocity_x, -self.max_velocity, self.max_velocity) * self.friction
        self.velocity_y = limit(
            self.velocity_y, -self.max_velocity, self.max_velocity) * self.friction

    def check_collision(self):
        if not Road.on_road(self.x, self.y):
            self.crashed = True

    def check_on_line(self, lines):
        line = lines[self.current_line]

        v1 = (line.x2 - line.x, line.y2 - line.y)
        v2 = (line.x2 - self.x, line.y2 - self.y)

        cross_prod = v1[0] * v2[1] - v1[1] * v2[0]

        if LINE_PROX_LOW < cross_prod < LINE_PROX_UP:
            self.current_line = (self.current_line + 1) % len(lines)
            return True
        else:
            return False

    def reset(self):
        self.x = PLAYER_POS_X
        self.y = PLAYER_POS_Y
        self.velocity_x = 0
        self.velocity_y = 0
        self.rotation = 0
        self.crashed = False
        self.current_line = 0

    def delete(self):
        super(Player, self).delete()
