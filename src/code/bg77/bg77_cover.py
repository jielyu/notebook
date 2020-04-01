from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        t = TextMobject('Functor')
        t.set_color(BLUE)
        t.shift(UP)
        t.scale(3)
        self.play(Write(t))

        r1 = Rectangle(height=1, width=3, color=GREEN)
        r1.shift(LEFT*3+DOWN)
        r2 = Rectangle(height=1, width=3, color=YELLOW)
        r2.shift(LEFT*1+DOWN+UP*0.1)
        r3 = Rectangle(height=1, width=6, color=RED)
        r3.shift(LEFT*0+DOWN)
        self.play(Write(r1),Write(r2),Write(r3))

        t = TextMobject('rm')
        t.set_color(YELLOW)
        self.play(Write(t))