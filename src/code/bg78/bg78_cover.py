from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        t = TextMobject('?', r' \% 3 = 0')
        t[0].set_color(RED)
        t.scale(3)
        t.shift(UP*2.0)
        self.play(Write(t))

        ct = []
        for i in range(3):
            c1 = Circle()
            t1 = TextMobject(str(i))
            t1.move_to(c1.get_center())
            ct1 = VGroup(c1, t1)
            ct1.shift(DOWN*0.3)
            ct.append(ct1)
        ct[0].shift((LEFT+DOWN)*1.414)
        ct[2].shift((RIGHT+DOWN)*1.414)
        ct[1].set_color(GREEN)
        ct[2].set_color(BLUE)
        self.play(*[Write(x) for x in ct])
