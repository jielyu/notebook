from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        t = TextMobject(*[str(x+1) for x in range(6)])
        t[1].move_to(t[0].get_center() + DL*1.5)
        t[2].move_to(t[0].get_center() + DR*1.5)
        arrow1 = Arrow(t[0].get_center(), t[1].get_center())
        arrow1.set_color(RED)
        arrow2 = Arrow(t[0].get_center(), t[2].get_center())
        t[3].move_to(t[1].get_center() + DL)
        t[4].move_to(t[1].get_center() + DR)
        t[5].move_to(t[2].get_center() + DL)
        arrow3 = Arrow(t[1].get_center(), t[3].get_center())
        arrow4 = Arrow(t[1].get_center(), t[4].get_center())
        arrow5 = Arrow(t[2].get_center(), t[5].get_center())
        tree = VGroup(t, arrow1, arrow2, arrow3, arrow4, arrow5)
        self.play(Write(tree))

        l1 = Line()
        l2 = Line()
        l2.move_to(l1.get_center())
        l2.rotate(90*DEGREES)
        cross = VGroup(l1, l2)
        cross.set_color(GREEN)
        cross.scale(0.4)
        cross.rotate(25*DEGREES)
        cross.move_to((t[0].get_center() + t[1].get_center())/2)
        self.play(Write(cross))

        t = TextMobject(r'Max\\ ', 'Product')
        t.scale(3)
        t.set_color(BLUE)
        t.shift(UP*1.5)
        self.play(Write(t))
        r = Rectangle(height=1.3, width=3.3)
        r.move_to(t[0].get_center())
        r.set_color(YELLOW)
        self.play(Write(r))

        tree = VGroup(tree, cross)
        tree.move_to(t.get_center()+DOWN*3.3)
        self.play(Write(tree))
