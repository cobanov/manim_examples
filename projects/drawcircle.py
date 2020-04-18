class TriangleScene(Scene):
    def construct(self):
        circle = Circle(radius=3)
        base_line = Line(ORIGIN,RIGHT*3,color=ORANGE)
        side_1 = Line(ORIGIN,RIGHT*3,color=BLUE)
        side_2 = Line(RIGHT*3,RIGHT*3,color=PURPLE)
        sides = VGroup(side_1,side_2)
        
        def triangle_update(mob):
            side_1,side_2 = mob
            new_side_1 = Line(ORIGIN,circle.points[-1],color=BLUE)
            new_side_2 = Line(RIGHT*3,circle.points[-1],color=PURPLE)
            side_1.become(new_side_1)
            side_2.become(new_side_2)

        sides.add_updater(triangle_update)
        self.add(base_line,sides)
        self.play(ShowCreation(circle,run_time=3))

        self.wait()