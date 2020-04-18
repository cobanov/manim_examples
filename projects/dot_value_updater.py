from manimlib.imports import *

class DrawCircle(Scene):


    def construct(self):
        coords = [(0,-1,0), (-2,-1,0), (2,-1,0)]

        line = Line()
        decimal_x = DecimalNumber().move_to(UP)
        decimal_y = DecimalNumber().next_to(decimal_x, DOWN)

        
        dot = Dot(color=YELLOW)

        def line_updater(obj):
            line2 = Line(ORIGIN, dot.get_center())
            line.become(line2)

        def set_value_decimal_x(obj):
            obj.set_value(dot.get_center()[0])

        def set_value_decimal_y(obj):
            obj.set_value(dot.get_center()[1])

        
        decimal_x.add_updater(set_value_decimal_x)
        decimal_y.add_updater(set_value_decimal_y)

        line.add_updater(line_updater)
        
        self.add(decimal_x, decimal_y, dot, line)

        for coord in coords:
            self.play(ApplyMethod(dot.move_to, coord))
            self.wait(0.5)

        
        self.wait(2)

