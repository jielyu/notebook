from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        t = TextMobject(r'map\\', r'filter\\', 'zip')
        t.set_color(BLUE)
        t[1].set_color(GREEN)
        t.scale(3)
        t[0].shift(LEFT)
        t[2].shift(RIGHT)
        self.play(Write(t))
