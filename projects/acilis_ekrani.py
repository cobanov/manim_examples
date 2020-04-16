from manimlib.imports import *


class MoveText(Scene):
	def construct(self):

		circle = Circle(color=BLUE)
		circle.move_to(0.5*UP)
		circle.scale(1.7)

		circle2 = Circle(radius=1, color=BLUE)
		circle2.move_to(0.5*UP)
		circle2.scale(1)
		
		text = TextMobject("Mert Cobanov")
		text.scale(0.7)
		text.to_corner(DR)

		text2 = TextMobject("Data Science")
		text2.scale(2)
		text2.move_to(2*DOWN)
		
		jf = ImageMobject("C:\\manim\\assets\\jf.png")
		jf.scale(1.7)
		jf.move_to(UP)

		# michel = ImageMobject("C:\\manim\\assets\\michel.png")
		# michel.scale(1.7)
		# michel.move_to(UP)

		self.play(Write(circle), FadeIn(jf), Write(text2), Write(text),  run_time=2)
		self.play(FadeOut(jf),FadeOut(text),FadeOut(text2))
		self.play(ReplacementTransform(circle, circle2), run_time=0.7)
		
		self.wait()