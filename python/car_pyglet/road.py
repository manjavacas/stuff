import pyglet

from physical_object import PhysicalObject

ROAD_RGB_COLOR = [95, 109, 95]
LINE_RGB_COLOR = (210, 30, 26)

pyglet.resource.path = ['./resources']
pyglet.resource.reindex()

road_img = pyglet.resource.image('road.png')

lines_coordinates = [(1321, 908, 1320, 760),
                     (1487, 890, 1444, 748),
                     (1696, 798, 1617, 672),
                     (1710, 547, 1854, 589),
                     (1712, 388, 1859, 383),
                     (1689, 254, 1801, 153),
                     (1575, 319, 1524, 181),
                     (1339, 337, 1295, 194),
                     (1086, 316, 1181, 429),
                     (992, 357, 944, 497),
                     (914, 270, 782, 338),
                     (705, 184, 755, 48),
                     (550, 192, 520, 46),
                     (329, 109, 416, 229),
                     (166, 292, 302, 350),
                     (133, 561, 279, 532),
                     (251, 774, 348, 659),
                     (447, 839, 463, 691),
                     (674, 650, 735, 785),
                     (960, 622, 902, 758),
                     (1093, 708, 1030, 840),
                     (1210, 763, 1166, 902)]


class Road(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Road, self).__init__(img=road_img, *args, **kwargs)

    def update(self, dt):
        super(Road, self).update(dt)

    @staticmethod
    def on_road(x, y):
        img_data = road_img.get_region(int(x), int(y), 1, 1).get_image_data()
        data = img_data.get_data('RGB', 3 * img_data.width)
        return list(data) == ROAD_RGB_COLOR
