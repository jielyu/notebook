from manimlib.imports import *

class Cover(Scene):

    def construct(self):
        img_dir = os.path.expanduser(
            '~/VideoStudio/CNBlueGeek/notebook/src/images/bg80')
    
        img = Image.open(os.path.join(img_dir, 'python-core-program.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.shift(LEFT*4.5)
        img_obj.scale(4)
        img_obj.rotate(20*DEGREES)
        self.play(Animation(img_obj))

        img = Image.open(os.path.join(img_dir, 'effective-python.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.shift(LEFT*0.5)
        img_obj.scale(4)
        self.play(Animation(img_obj))

        img = Image.open(os.path.join(img_dir, 'python-cookbook.png'))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.shift(RIGHT*4.5)
        img_obj.scale(4)
        img_obj.rotate(-20*DEGREES)
        self.play(Animation(img_obj))