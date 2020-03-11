from manimlib.imports import *

class Cover(Scene):
    def construct(self):

        t = TextMobject(*[c for c in 'KERAS'])
        t.scale(3)
        for idx, c in enumerate(t):
            if idx % 2 == 0:
                c.set_color(BLUE)
            else:
                c.set_color(GREEN)
        self.play(Write(t))