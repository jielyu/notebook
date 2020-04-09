from manimlib.imports import *

class Cover(Scene):
    CONFIG={
		"camera_config": {
			"background_color": "#F6F6F6",
		},
	}
    def construct(self):

        icon_path = '~/VideoStudio/CNBlueGeek/notebook/src/images/bg76/github-icon.jpg'
        img = Image.open(os.path.expanduser(icon_path))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.scale(3)
        self.play(Animation(img_obj))

        t = TextMobject('FREE')
        t.move_to(img_obj.get_center())
        t.set_color(BLUE)
        t.scale(2)
        self.play(Write(t))