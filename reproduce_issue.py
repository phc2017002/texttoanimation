from manim import *

class CircularConcept(Scene):
    def construct(self):
        # Title
        title = Text("The Circular Concept", color=BLUE).to_edge(UP)
        self.add(title)

        # Nodes
        c1 = Circle(radius=0.5, color=WHITE).shift(LEFT * 2 + DOWN * 0.5)
        t1 = Text("10", font_size=24).move_to(c1)
        
        c2 = Circle(radius=0.5, color=WHITE).shift(UP * 1.5)
        t2 = Text("20", font_size=24).move_to(c2)
        
        c3 = Circle(radius=0.5, color=WHITE).shift(RIGHT * 2 + DOWN * 0.5)
        t3 = Text("30", font_size=24).move_to(c3)
        
        g1 = VGroup(c1, t1)
        g2 = VGroup(c2, t2)
        g3 = VGroup(c3, t3)
        
        self.add(g1, g2, g3)
        
        # Arrows
        a1 = CurvedArrow(c1.get_top(), c2.get_left(), color=YELLOW)
        a2 = CurvedArrow(c2.get_right(), c3.get_top(), color=YELLOW)
        a3 = CurvedArrow(c3.get_bottom(), c1.get_bottom(), color=GREEN) # The bottom arrow
        
        self.add(a1, a2, a3)
        
        # Overlapping Text
        # Intentionally placed to overlap with the bottom arrow (a3)
        overlap_text = Text("Forms a Circle!", color=GREEN, font_size=24)
        overlap_text.move_to(a3.get_center()) # DIRECT OVERLAP
        
        self.add(overlap_text)
        self.wait(2)
