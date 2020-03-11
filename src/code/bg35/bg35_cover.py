from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        arrow1 =Arrow(2*UP+2*LEFT, 2*DOWN+2*RIGHT, color=RED)
        arrow2 =Arrow(2*DOWN+2*LEFT, 2*UP+2*RIGHT, color=RED)
        self.play(Write(arrow1), Write(arrow2))
        t = TextMobject('A', 'E', 'S')
        t.set_color(GREEN)
        t[1].set_color(BLUE)
        t.scale(3)
        self.play(Write(t))