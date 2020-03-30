from manimlib.imports import *

class Cover(Scene):
    CONFIG={
		"camera_config": {
			"background_color": "#F6F6F6",
		},
	}
    def construct(self):
        t = TextMobject(*[c for c in [r'Github\\', 'Action']])
        t.scale(3)
        for idx, c in enumerate(t):
            if idx % 2 == 0:
                c.set_color(BLUE)
            else:
                c.set_color(GREEN)
        t.shift(UP)
        t[0].shift(LEFT)
        t[1].shift(RIGHT)
        self.play(Write(t))

        rect = Rectangle(height=1.5, width=5)
        rect.move_to(t[1].get_center())
        rect.set_color(RED)
        self.play(Write(rect))

        rect = Rectangle(height=1.7, width=5.2)
        rect.move_to(t[1].get_center())
        rect.set_color(BLACK)
        self.play(Write(rect))

        icon_path = '~/VideoStudio/CNBlueGeek/notebook/src/images/bg76/github-icon.jpg'
        img = Image.open(os.path.expanduser(icon_path))
        img = np.asarray(img)
        img_obj = ImageMobject(img)
        img_obj.move_to(t.get_center()+DOWN*3+LEFT)
        #img_obj.scale(0.5)
        #img_obj.shift(2*DOWN)
        self.play(Write(t))
        self.play(Animation(img_obj))