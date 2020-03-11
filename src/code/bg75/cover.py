from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        t = TextMobject(*[str(x) for x in range(10)])
        t.arrange_submobjects(RIGHT, buff=MED_LARGE_BUFF)
        self.play(DrawBorderThenFill(t))
        rect = Rectangle(height=1.0, width=0.5, color=RED)
        rect.move_to(t[5].get_center())
        self.play(Write(rect))
        arrow = Arrow(rect.get_center()+2*UP, 
                      rect.get_center(),
                      color=YELLOW)
        self.play(Write(arrow))
        arrow = Arrow(t[6].get_center()+1.5*UP, 
                      t[6].get_center(),
                      color=YELLOW, 
                      fill_opacity=0.5)
        self.play(Write(arrow))
        arrow = Arrow(t[7].get_center()+1.*UP, 
                      t[7].get_center(),
                      color=YELLOW, 
                      fill_opacity=0.5)
        self.play(Write(arrow))
        arrow = Arrow(t[4].get_center()+1.5*UP, 
                      t[4].get_center(),
                      color=YELLOW, 
                      fill_opacity=0.5)
        self.play(Write(arrow))
        arrow = Arrow(t[3].get_center()+1.*UP, 
                      t[3].get_center(),
                      color=YELLOW, 
                      fill_opacity=0.5)
        self.play(Write(arrow))

        tt = TextMobject(*[x for x in 'itertools'])
        for idx, c in enumerate(tt):
            if idx % 2 == 0:
                c.set_color(GREEN)
            else:
                c.set_color(BLUE)
        tt.move_to(t[5].get_center() + DOWN)
        tt.scale(2)
        self.play(Write(tt))