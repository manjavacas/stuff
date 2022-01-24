import pyglet

from road import Road, LINE_RGB_COLOR, lines_coordinates
from player import Player

PLAYER_POS_X = 1260
PLAYER_POS_Y = 830


class Game(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(fullscreen=True, *args, **kwargs)

        # Set batch and entities
        self.batch = pyglet.graphics.Batch()

        self.create_objects()

        # Set handlers
        self.push_handlers(self.player.key_handler)

        # Set frequence
        pyglet.clock.schedule_interval(self.update, 1/60.0)

    def create_objects(self):
        background = pyglet.graphics.OrderedGroup(0)
        foreground = pyglet.graphics.OrderedGroup(1)

        self.road = Road(x=0, y=0, batch=self.batch, group=background)
        self.player = Player(x=PLAYER_POS_X, y=PLAYER_POS_Y,
                             batch=self.batch, group=foreground)

        self.lines = []
        for coords in lines_coordinates:
            x0, y0, x1, y1 = coords
            self.lines.append(pyglet.shapes.Line(
                x0, y0, x1, y1))
            ## Uncomment for printing control lines
            # self.lines.append(pyglet.shapes.Line(
            #     x0, y0, x1, y1, color=LINE_RGB_COLOR, batch=self.batch, group=foreground))

    def update(self, dt):
        if not self.player.crashed:
            self.player.update(dt)
            self.player.check_collision()
            self.player.check_on_line(self.lines)
        else:
            self.player.reset()

        self.road.update(dt)

    def on_mouse_press(self, x, y, button, modifiers):
        print(x, y)

    def on_draw(self):
        self.clear()
        self.batch.draw()


if __name__ == '__main__':
    game = Game()
    pyglet.app.run()
