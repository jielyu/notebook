from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        t = TextMobject(*[c for c in 'requests'])
        t.scale(3)
        for idx, c in enumerate(t):
            if idx % 2 == 0:
                c.set_color(BLUE)
            else:
                c.set_color(GREEN)
        t.shift(UP)
        self.play(Write(t))

        rect = Rectangle(height=2, width=6)
        rect.move_to(t.get_center())
        rect.set_color(YELLOW)
        self.play(Write(rect))

        img = Image.open(os.path.expanduser(
            '~/VideoStudio/CNBlueGeek/article/icons8-python-480.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.move_to(t.get_center()+DOWN*2)
        #img_obj.scale(0.5)
        #img_obj.shift(2*DOWN)
        self.play(Write(t))
        self.play(Animation(img_obj))