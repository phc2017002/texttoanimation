from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplainer(VoiceoverScene):
    def construct(self):
        # Initialize speech service with a specific voice
        self.set_speech_service(ElevenLabsService(voice_id="Josh"))

        # 1. Introduction to Quantum States
        self.intro_scene()
        
        # 2. The Equation Breakdown
        self.equation_breakdown()
        
        # 3. Wave Function and Probability
        self.wave_function_interpretation()
        
        # 4. The Hamiltonian (Kinetic + Potential)
        self.hamiltonian_breakdown()
        
        # 5. Particle in a Box application
        self.particle_in_a_box()
        
        # 6. Conclusion
        self.conclusion_scene()

    def intro_scene(self):
        with self.voiceover(text="Welcome. Today, we dive into the heart of quantum mechanics: The Schrödinger Equation. In classical physics, we describe a ball by its position and momentum.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE)
            self.play(Write(title))
            self.wait(1)
            
        with self.voiceover(text="But in the quantum world, objects like electrons are not just particles; they are described by a mathematical object called a Wave Function, denoted by the Greek letter Psi.") as tracker:
            self.play(FadeOut(title))
            psi_symbol = MathTex(r"\Psi(x, t)").scale(2).set_color(YELLOW)
            label = Text("The Wave Function", font_size=24).next_to(psi_symbol, DOWN, buff=0.5)
            self.play(Write(psi_symbol), Write(label))
            
        self.play(FadeOut(psi_symbol), FadeOut(label))

    def equation_breakdown(self):
        # The main equation
        tdse = MathTex(
            r"i\hbar", r"\frac{\partial}{\partial t}", r"\Psi", r"=", r"\hat{H}", r"\Psi"
        ).scale(1.5)
        
        with self.voiceover(text="This is the Time-Dependent Schrödinger Equation. It tells us how the wave function changes over time. Let's break it down piece by piece.") as tracker:
            self.play(Write(tdse))
            self.wait(1)
            
        # Shift up for explanation
        self.play(tdse.animate.to_edge(UP))
        
        # Explain i h-bar
        with self.voiceover(text="First, we have i, the imaginary unit, and h-bar, the reduced Planck's constant. These constants scale the equation, linking energy to frequency.") as tracker:
            # frame_ihbar = SurroundingRectangle(tdse[0], color=YELLOW, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # label_ihbar = Text("Constants", font_size=24, color=YELLOW).next_to(frame_ihbar, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(frame_ihbar), Write(label_ihbar))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(frame_ihbar), FadeOut(label_ihbar))  # Auto-disabled: uses disabled SurroundingRectangle

        # Explain Time Derivative
        with self.voiceover(text="Next is the partial derivative with respect to time. This represents the rate of change of the system's state.") as tracker:
            # frame_dt = SurroundingRectangle(tdse[1], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # label_dt = Text("Change in Time", font_size=24, color=GREEN).next_to(frame_dt, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(frame_dt), Write(label_dt))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(frame_dt), FadeOut(label_dt))  # Auto-disabled: uses disabled SurroundingRectangle
            
        # Explain Hamiltonian
        with self.voiceover(text="On the right side, we have H-hat, the Hamiltonian operator. This represents the total energy of the system: kinetic plus potential energy.") as tracker:
            # frame_ham = SurroundingRectangle(tdse[4], color=RED, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # label_ham = Text("Total Energy Operator", font_size=24, color=RED).next_to(frame_ham, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(frame_ham), Write(label_ham))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(frame_ham), FadeOut(label_ham))  # Auto-disabled: uses disabled SurroundingRectangle
            
        self.play(FadeOut(tdse))

    def wave_function_interpretation(self):
        # Visualization of Psi vs |Psi|^2
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"color": GREY},
            tips=False
        ).shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label("x").shift(RIGHT*0.2)
        y_label = axes.get_y_axis_label(r"\Psi", direction=LEFT).shift(LEFT*0.4)
        
        # Gaussian wave packet
        def wave_func(x):
            return np.exp(-x**2 / 2) * np.cos(3*x)

        graph_psi = axes.plot(wave_func, color=BLUE)
        label_psi = MathTex(r"\Psi(x)").set_color(BLUE).to_corner(UL)
        
        with self.voiceover(text="But what is Psi? Physically, it's a complex probability amplitude. It can be positive, negative, or even imaginary. Here is a real part visualization.") as tracker:
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(graph_psi), Write(label_psi))
            
        # Born Rule
        prob_density = axes.plot(lambda x: (np.exp(-x**2 / 2) * np.cos(3*x))**2, color=ORANGE)
        label_prob = MathTex(r"|\Psi(x)|^2").set_color(ORANGE).next_to(label_psi, DOWN, buff=0.4)
        
        with self.voiceover(text="The quantity that we actually measure is the absolute square of Psi. This is the Probability Density function.") as tracker:
            self.play(
                Transform(graph_psi, prob_density),
                Write(label_prob)
            )
            # Update y-axis label conceptually
            new_y_label = axes.get_y_axis_label(r"P(x)", direction=LEFT).shift(LEFT*0.4)
            self.play(Transform(y_label, new_y_label))

        with self.voiceover(text="Where the graph is high, the probability of finding the particle is high. Where it is zero, the particle will never be found.") as tracker:
            # Highlight a peak area
            area = axes.get_area(prob_density, x_range=[-0.5, 0.5], color=ORANGE, opacity=0.5)
            self.play(FadeIn(area))
            self.wait(1)
            
        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label), 
            FadeOut(graph_psi), FadeOut(label_psi), 
            FadeOut(label_prob), FadeOut(area)
        )

    def hamiltonian_breakdown(self):
        # Expanding the Hamiltonian
        h_eq = MathTex(
            r"\hat{H}", r"=", r"-\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2}", r"+", r"V(x)"
        ).scale(1.2)
        
        with self.voiceover(text="To solve the equation, we must expand the Hamiltonian operator. It consists of two main parts.") as tracker:
            self.play(Write(h_eq))
            self.wait(1)
            
        with self.voiceover(text="The first term represents Kinetic Energy. It relates to the curvature of the wave function.") as tracker:
            # frame_kin = SurroundingRectangle(h_eq[2], color=BLUE, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # label_kin = Text("Kinetic Energy", font_size=24, color=BLUE).next_to(frame_kin, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(frame_kin), Write(label_kin))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(frame_kin), FadeOut(label_kin))  # Auto-disabled: uses disabled SurroundingRectangle
            
        with self.voiceover(text="The second term, V of x, is the Potential Energy. This describes the external forces acting on the particle, like an electric field or a box.") as tracker:
            # frame_pot = SurroundingRectangle(h_eq[4], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # label_pot = Text("Potential Energy", font_size=24, color=GREEN).next_to(frame_pot, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(frame_pot), Write(label_pot))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(frame_pot), FadeOut(label_pot))  # Auto-disabled: uses disabled SurroundingRectangle

        self.play(FadeOut(h_eq))

    def particle_in_a_box(self):
        title = Text("Particle in a Box", font_size=36).to_edge(UP)
        
        with self.voiceover(text="Let's apply this to a classic example: The Particle in a Box. Imagine an electron trapped in a region with infinite walls.") as tracker:
            self.play(Write(title))

        # Setup visualization
        axes = Axes(
            x_range=[0, 1, 0.5],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": False, "color": GREY}, # Clean axes
            tips=False
        ).shift(DOWN * 0.5)
        
        wall_left = Line(axes.c2p(0, -2), axes.c2p(0, 2), color=WHITE, stroke_width=5)
        wall_right = Line(axes.c2p(1, -2), axes.c2p(1, 2), color=WHITE, stroke_width=5)
        floor = Line(axes.c2p(0, -2), axes.c2p(1, -2), color=GREY)
        
        walls = VGroup(wall_left, wall_right, floor)
        
        with self.voiceover(text="Inside the box, the potential is zero. Outside, it is infinite. The wave function must be zero at the walls.") as tracker:
            self.play(Create(axes), Create(walls))

        # n=1 State
        def psi_n1(x):
            if 0 <= x <= 1:
                return np.sin(1 * np.pi * x)
            return 0
        
        graph_n1 = axes.plot(psi_n1, color=YELLOW)
        label_n1 = MathTex("n=1").next_to(graph_n1, UP, buff=0.2)

        with self.voiceover(text="The lowest energy state, or ground state, looks like half a sine wave. This is n equals 1.") as tracker:
            self.play(Create(graph_n1), Write(label_n1))
            self.wait(1)
            
        # n=2 State
        def psi_n2(x):
            if 0 <= x <= 1:
                return np.sin(2 * np.pi * x)
            return 0

        graph_n2 = axes.plot(psi_n2, color=RED)
        label_n2 = MathTex("n=2").next_to(axes, UP, buff=0.2).set_x(axes.c2p(0.75,0)[0]) # Manual placement to avoid overlap with title

        with self.voiceover(text="At higher energy, n equals 2, the wave gains a full cycle. Notice the point in the middle where the wave function is zero. This is called a node.") as tracker:
            self.play(Transform(graph_n1, graph_n2), Transform(label_n1, label_n2))
            
        # n=3 State
        def psi_n3(x):
            if 0 <= x <= 1:
                return np.sin(3 * np.pi * x)
            return 0

        graph_n3 = axes.plot(psi_n3, color=GREEN)
        label_n3 = MathTex("n=3").next_to(axes, UP, buff=0.2).set_x(axes.c2p(0.5,0)[0])

        with self.voiceover(text="As we increase energy to n equals 3, the number of nodes increases. The curvature increases, which implies higher kinetic energy.") as tracker:
            self.play(Transform(graph_n1, graph_n3), Transform(label_n1, label_n3))
            
        self.play(FadeOut(walls), FadeOut(axes), FadeOut(graph_n1), FadeOut(label_n1), FadeOut(title))

    def conclusion_scene(self):
        main_text = Text("Quantum Reality", font_size=40, color=BLUE)
        sub_text = Text("Governed by Probability", font_size=30).next_to(main_text, DOWN, buff=0.5)
        
        with self.voiceover(text="The Schrödinger equation changed our understanding of reality. It replaced specific trajectories with evolving probabilities.") as tracker:
            self.play(Write(main_text))
            self.play(Write(sub_text))
            
        final_eq = MathTex(r"\hat{H}\Psi = E\Psi", color=YELLOW).scale(1.5).next_to(sub_text, DOWN, buff=1.0)
        
        with self.voiceover(text="Whether it's understanding atoms, designing lasers, or building quantum computers, it all starts with this beautiful equation.") as tracker:
            self.play(Write(final_eq))
            self.wait(2)
            
        self.play(FadeOut(main_text), FadeOut(sub_text), FadeOut(final_eq))
        self.wait(1)
