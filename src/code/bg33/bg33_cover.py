from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        t = TextMobject('Py', 'Torch')
        t[0].set_color(BLUE)
        t[1].set_color(GREEN)
        t.scale(3)
        self.play(Write(t))