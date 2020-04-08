from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        ct_list = []
        for i in range(4):
            c = Circle()
            c.scale(0.7)
            t = TextMobject(str(i+1)).move_to(c.get_center())
            t.scale(2)
            t.set_color(BLUE)
            ct = VGroup(c,t)
            ct_list.append(ct)

        
        ct_list[0].shift(UL*2)
        ct_list[1].shift(UR*2)
        ct_list[2].shift(DR*2)
        ct_list[3].shift(DL*2)

        self.play(*[Write(x) for x in ct_list])

        line_list = []
        line = Line(ct_list[0].get_center()+RIGHT*0.7, ct_list[1].get_center()+LEFT*0.7)
        line.set_color(GREEN)
        line_list.append(line)

        line = Line(ct_list[0].get_center()+DR*0.5, ct_list[2].get_center()+UL*0.5)
        line.set_color(GREEN)
        line_list.append(line)

        line = Line(ct_list[0].get_center()+DOWN*0.7, ct_list[3].get_center()+UP*0.7)
        line.set_color(GREEN)
        line_list.append(line)

        line = Line(ct_list[1].get_center()+DL*0.5, ct_list[3].get_center()+UR*0.5)
        line.set_color(GREEN)
        line_list.append(line)

        self.play(*[Write(x) for x in line_list])