from manim import *

class ParticleInABox(Scene):
    def construct(self):
        # Title and Equation - FIXED OVERLAP
        title = Text("Particle in a Box", color=TEAL).to_edge(UP)
        
        # Placing equation below title with proper spacing to avoid overlap
        equation = MathTex(r"E_n = \frac{n^2 h^2}{8mL^2}").next_to(title, DOWN, buff=0.5)
        
        self.add(title, equation)
        
        # Box and Graph
        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN * 0.5)
        
        # Box walls
        left_wall = Line(axes.c2p(0, -1.5), axes.c2p(0, 1.5), stroke_width=4)
        right_wall = Line(axes.c2p(1, -1.5), axes.c2p(1, 1.5), stroke_width=4)
        bottom_wall = Line(axes.c2p(0, -1.5), axes.c2p(1, -1.5), stroke_width=4)
        box = VGroup(left_wall, right_wall, bottom_wall)
        
        # Wave functions
        n1_func = lambda x: np.sin(1 * np.pi * x)
        n3_func = lambda x: np.sin(3 * np.pi * x)
        
        graph1 = axes.plot(n1_func, color=GREEN)
        graph3 = axes.plot(n3_func, color=ORANGE)
        
        # Labels
        label1 = MathTex("n=1", color=GREEN).next_to(graph1, RIGHT).shift(UP * 1)
        label3 = MathTex("n=3", color=ORANGE).next_to(graph3, RIGHT).shift(UP * 0.5)
        
        self.add(axes, box, graph1, graph3, label1, label3)
        self.wait(2)