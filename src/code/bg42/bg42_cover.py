from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        tf_text = TextMobject('TF', '2.0')
        tf_text.shift(UP)
        tf_text[0].set_color(BLUE)
        tf_text[1].set_color(YELLOW)
        tf_text.scale(3.0)

        csv_text = TexMobject('C', 'S', 'V')
        csv_text.set_color(GREEN)
        csv_text[1].set_color(BLUE)
        csv_text.shift(0.5*DOWN)
        self.play(Write(tf_text))
        self.play(Write(csv_text))

        c = Circle()
        c.shift(0.5*DOWN)
        c.scale(0.8)
        self.play(Write(c))