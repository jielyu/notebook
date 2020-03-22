from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        tf_text = TextMobject('TF', '2.0')
        tf_text.shift(UP)
        tf_text[0].set_color(BLUE)
        tf_text[1].set_color(YELLOW)
        tf_text.scale(3.0)

        np_text = TextMobject(*[c for c in 'NUMPY'])
        for idx, c in enumerate(np_text):
            if idx % 2 == 0:
                c.set_color(BLUE)
            else:
                c.set_color(GREEN)
        np_text.shift(0.5*DOWN)
        np_text.scale(0.6)
        self.play(Write(tf_text))
        self.play(Write(np_text))

        c = Circle()
        c.shift(0.5*DOWN)
        c.scale(0.8)
        self.play(Write(c))