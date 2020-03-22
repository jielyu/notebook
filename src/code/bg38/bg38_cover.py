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

        t = TextMobject('文件系统')
        t.scale(2)
        t.shift(DOWN)
        t.set_color(BLUE)
        self.play(Write(t))