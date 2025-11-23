from manim import *

class LayoutTest(Scene):
    def construct(self):
        # Test 1: Title Exclusion Zone Violation
        # This object is too high (Y=3.5) and should be capped
        high_object = Circle().move_to(UP * 3.5)
        
        # Test 2: Arrow Label Collision
        # This label is placed UP from the arrow, which hits the title
        arrow = Arrow(ORIGIN, UP)
        label = Text("z").next_to(arrow, UP)
        
        self.play(Create(high_object), Create(arrow), Write(label))
