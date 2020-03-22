from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        t = TextMobject('分词工具')
        t.scale(2)
        #t.shift(UP)
        t.set_color(BLUE)
        self.play(Write(t))

        name = TextMobject('jieba')
        name.shift(2*UL)
        name.scale(2)
        name.set_color(GREEN)
        c = Circle()
        c.move_to(name)
        self.play(Write(name),Write(c))

        name = TextMobject('SnowNLP')
        name.shift(2*UR)
        name.scale(2)
        name.set_color(GREEN)
        c = Circle()
        c.move_to(name)
        self.play(Write(name),Write(c))

        name = TextMobject('thulac')
        name.shift(2*DL)
        name.scale(2)
        name.set_color(GREEN)
        c = Circle()
        c.move_to(name)
        self.play(Write(name),Write(c))

        name = TextMobject('pyltp')
        name.shift(2*DR)
        name.scale(2)
        name.set_color(GREEN)
        c = Circle()
        c.move_to(name)
        self.play(Write(name),Write(c))