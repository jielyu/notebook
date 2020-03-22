from manimlib.imports import *

class Cover(Scene):

    def construct(self):

        img = Image.open(os.path.expanduser(
            '~/VideoStudio/CNBlueGeek/article/icons8-python-480.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.move_to(UP)
        img_obj.scale(1.5)
        #img_obj.shift(2*DOWN)
        self.play(Animation(img_obj))

        t = TextMobject(*[c for c in ['unit', 'test']])
        t.scale(3.5)
        for idx, c in enumerate(t):
            if idx % 2 == 0:
                c.set_color(BLUE)
            else:
                c.set_color(GREEN)
        t.shift(DOWN)
        self.play(Write(t))