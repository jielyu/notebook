from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        r1 = Rectangle(height=1.6, width=4.2)
        t1 = TextMobject(r'DNS\\', 'Poisoning')
        t1[0].scale(3)
        t1[1].scale(1.5)
        t1[1].shift(DOWN*0.7)
        t1[0].set_color(BLUE)
        t1[1].set_color(GREEN)
        r1.move_to(t1[0].get_center())
        r1.set_color(YELLOW)
        self.play(Write(r1), Write(t1))

        