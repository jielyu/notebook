from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        t = TextMobject(r'C++\\', 'Swig')
        t.scale(4)
        t[0].set_color(GREEN)
        t[1].set_color(BLUE)
        t[0].shift(UP)
        t[1].shift(DOWN)
        self.play(Write(t))

        img = Image.open(os.path.expanduser(
            '~/VideoStudio/CNBlueGeek/article/icons8-python-480.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.move_to(t.get_center())
        #img_obj.scale(0.5)
        #img_obj.shift(2*DOWN)
        self.play(Write(t))
        self.play(Animation(img_obj))