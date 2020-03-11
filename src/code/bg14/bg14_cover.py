from manimlib.imports import *
from PIL import Image

class Cover(Scene):

    def construct(self):

        t = TextMobject('QR', 'code')
        t.scale(3)
        t[0].set_color(BLUE)
        t[1].set_color(GREEN)
        t.move_to(UP)

        img = Image.open(os.path.expanduser(
            '~/VideoStudio/CNBlueGeek/article/icons8-python-480.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.move_to(t.get_center())
        img_obj.shift(2*DOWN)
        self.play(Write(t))
        self.play(Animation(img_obj))