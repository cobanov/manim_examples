from manimlib.imports import *

class UpdaterFunc(Scene):

    def construct(self):

        dot = Dot()
        number_x = DecimalNumber( include_sign=True).next_to(dot)
        number_y = DecimalNumber( include_sign=True).next_to(number_x, DOWN)

        def update_number_x(obj):
            obj.next_to(dot)
            
            obj.set_value(dot.get_center()[0])

        def update_number_y(obj):
            obj.next_to(dot)
            obj.next_to(number_x,DOWN)
            obj.set_value(dot.get_center()[1])

        number_x.add_updater(update_number_x)
        number_y.add_updater(update_number_y)

        self.add(dot, number_x, number_y)
        self.play(dot.shift, RIGHT, DOWN, run_time=2)
        self.play(Rotate(dot), about_point=ORIGIN, run_time=2)

        self.wait()
