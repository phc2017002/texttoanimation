from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Introduction
        self.introduction()
        
        # The Schrödinger Equation
        self.show_schrodinger_equation()
        
        # Wave Functions
        self.explain_wave_functions()
        
        # Probability Density
        self.explain_probability_density()
        
        # Time Evolution
        self.show_time_evolution()
        
        # Physical Interpretation
        self.physical_interpretation()
        
        # Real Example: Particle in a Box
        self.particle_in_box_example()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. This equation describes how quantum systems evolve over time and is the cornerstone of our understanding of the microscopic world.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE, weight=BOLD)
            subtitle = Text("Wave Functions and Probability Density", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
            self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def show_schrodinger_equation(self):
        with self.voiceover(text="Let's begin with the time-dependent Schrödinger equation in its most general form. This elegant equation connects the energy of a quantum system to its wave function.") as tracker:
            section_title = Text("The Schrödinger Equation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="Here is the equation: i times h-bar times the partial derivative of psi with respect to time equals the Hamiltonian operator acting on psi.") as tracker:
            # The time-dependent Schrödinger equation
            equation = MathTex(
                r"i\hbar\frac{\partial \psi}{\partial t} = \hat{H}\psi",
                font_size=50
            )
            equation.shift(UP * 0.5)
            self.play(Write(equation))
            
        with self.voiceover(text="Let's break down each component of this equation. First, we have i, the imaginary unit, which indicates that quantum mechanics fundamentally involves complex numbers.") as tracker:
            # Highlight i
            # i_box = SurroundingRectangle(equation[0][0], color=YELLOW, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            i_label = Text("Imaginary unit", font_size=24, color=YELLOW)
            # i_label.next_to(i_box, LEFT, buff=0.3)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(i_box), Write(i_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(i_box), FadeOut(i_label))  # Auto-disabled: uses disabled SurroundingRectangle
            
        with self.voiceover(text="Next is h-bar, the reduced Planck constant, which connects the quantum world to our macroscopic measurements. Its value is approximately 1.054 times 10 to the minus 34 joule seconds.") as tracker:
            # Highlight ℏ
            # hbar_box = SurroundingRectangle(equation[0][1], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            hbar_label = MathTex(r"\hbar = \frac{h}{2\pi} \approx 1.054 \times 10^{-34} \text{ J·s}", 
                                font_size=28, color=GREEN)
            # hbar_label.next_to(hbar_box, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(hbar_box), Write(hbar_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(hbar_box), FadeOut(hbar_label))  # Auto-disabled: uses disabled SurroundingRectangle
            
        with self.voiceover(text="Psi is the wave function, which contains all the information about the quantum state of our system. This is what we're solving for.") as tracker:
            # Highlight ψ
            # psi_box = SurroundingRectangle(equation[0][3], color=RED, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            psi_label = Text("Wave function", font_size=24, color=RED)
            # psi_label.next_to(psi_box, RIGHT, buff=0.3)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(psi_box), Write(psi_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
            # self.play(FadeOut(psi_box), FadeOut(psi_label))  # Auto-disabled: uses disabled SurroundingRectangle
            
        with self.voiceover(text="The Hamiltonian operator H-hat represents the total energy of the system, including both kinetic and potential energy. For a particle, it takes this form.") as tracker:
            # Highlight Ĥ and show expanded form
            # h_box = SurroundingRectangle(equation[0][7:9], color=PURPLE, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            
            hamiltonian = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=40,
                color=PURPLE
            )
            hamiltonian.next_to(equation, DOWN, buff=1)
            
            ke_label = Text("Kinetic Energy", font_size=20, color=ORANGE)
            pe_label = Text("Potential Energy", font_size=20, color=TEAL)
            ke_label.next_to(hamiltonian, DOWN, buff=0.3).shift(LEFT * 2)
            pe_label.next_to(hamiltonian, DOWN, buff=0.3).shift(RIGHT * 2)
            
            # self.play(Create(h_box), Write(hamiltonian))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(0.5)
            self.play(Write(ke_label), Write(pe_label))
            
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def explain_wave_functions(self):
        with self.voiceover(text="Now let's explore wave functions in detail. The wave function psi is a complex-valued function that describes the quantum state of a particle.") as tracker:
            section_title = Text("Wave Functions", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="A wave function can be written as psi of x and t, which depends on both position and time. Let's visualize what this looks like.") as tracker:
            psi_def = MathTex(r"\psi(x,t)", font_size=45)
            psi_def.next_to(section_title, DOWN, buff=0.8)
            self.play(Write(psi_def))
            
        with self.voiceover(text="Since the wave function is complex, we can separate it into real and imaginary parts. Here we show a simple example: a traveling wave packet.") as tracker:
            self.play(psi_def.animate.shift(UP * 1.5).scale(0.7))
            
            # Create axes for wave function
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=10,
                y_length=4,
                axis_config={"color": WHITE, "include_tip": True},
            )
            axes.shift(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT, buff=0.2)
            y_label = axes.get_y_axis_label(r"\psi(x)", edge=UP, direction=UP, buff=0.2)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
        with self.voiceover(text="The blue curve represents the real part of the wave function, while the red curve shows the imaginary part. Notice how they oscillate together, creating a complex wave.") as tracker:
            # Plot real and imaginary parts
            real_part = axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                color=BLUE,
                stroke_width=3
            )
            imag_part = axes.plot(
                lambda x: np.exp(-x**2/2) * np.sin(3*x),
                color=RED,
                stroke_width=3
            )
            
            real_label = Text("Re(ψ)", font_size=24, color=BLUE)
            imag_label = Text("Im(ψ)", font_size=24, color=RED)
            real_label.next_to(axes, RIGHT, buff=0.3).shift(UP * 0.5)
            imag_label.next_to(real_label, DOWN, buff=0.3)
            
            self.play(Create(real_part), Write(real_label))
            self.play(Create(imag_part), Write(imag_label))
            
        with self.voiceover(text="An important property of wave functions is that they must be normalized. This means the total probability of finding the particle somewhere in space must equal one.") as tracker:
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x,t)|^2 dx = 1",
                font_size=35
            )
            normalization.to_edge(DOWN, buff=0.5)
            self.play(Write(normalization))
            
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def explain_probability_density(self):
        with self.voiceover(text="The wave function itself is not directly observable, but its square modulus gives us the probability density. This is one of the most important concepts in quantum mechanics.") as tracker:
            section_title = Text("Probability Density", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="The probability density is defined as the absolute square of the wave function. Mathematically, we write it as psi star times psi, or the magnitude of psi squared.") as tracker:
            prob_density_eq = MathTex(
                r"P(x,t) = |\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t)",
                font_size=42
            )
            prob_density_eq.next_to(section_title, DOWN, buff=0.7)
            self.play(Write(prob_density_eq))
            
        with self.voiceover(text="Let's visualize this concept. Here we show the wave function on top and the corresponding probability density below.") as tracker:
            # Create two sets of axes
            axes_wave = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1, 1, 0.5],
                x_length=9,
                y_length=2.5,
                axis_config={"color": WHITE},
            )
            axes_wave.shift(UP * 1.2 + LEFT * 0.5)
            
            axes_prob = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 1, 0.5],
                x_length=9,
                y_length=2.5,
                axis_config={"color": WHITE},
            )
            axes_prob.shift(DOWN * 1.8 + LEFT * 0.5)
            
            wave_label = Text("ψ(x)", font_size=24, color=YELLOW)
            wave_label.next_to(axes_wave, LEFT, buff=0.2)
            
            prob_label = Text("|ψ(x)|²", font_size=24, color=GREEN)
            prob_label.next_to(axes_prob, LEFT, buff=0.2)
            
            self.play(prob_density_eq.animate.scale(0.7).to_edge(RIGHT).shift(UP * 2))
            self.play(
                Create(axes_wave), 
                Create(axes_prob),
                Write(wave_label),
                Write(prob_label)
            )
            
        with self.voiceover(text="For this Gaussian wave packet, the wave function oscillates both positively and negatively. However, the probability density is always positive, as it must be, since probabilities cannot be negative.") as tracker:
            # Wave function (complex, showing real part)
            wave_func = axes_wave.plot(
                lambda x: 0.8 * np.exp(-x**2/2) * np.cos(4*x),
                color=BLUE,
                stroke_width=3
            )
            
            # Probability density
            prob_func = axes_prob.plot(
                lambda x: 0.64 * np.exp(-x**2),
                color=GREEN,
                stroke_width=3
            )
            
            # Fill under probability curve
            area = axes_prob.get_area(
                prob_func,
                x_range=[-4, 4],
                color=GREEN,
                opacity=0.3
            )
            
            self.play(Create(wave_func))
            self.play(Create(prob_func), FadeIn(area))
            
        with self.voiceover(text="The area under the probability density curve represents the probability of finding the particle in a given region. The shaded green area shows where the particle is most likely to be found.") as tracker:
            # Highlight a region
            region_line_left = DashedLine(
                axes_prob.c2p(-1, 0),
                axes_prob.c2p(-1, 0.5),
                color=YELLOW,
                stroke_width=3
            )
            region_line_right = DashedLine(
                axes_prob.c2p(1, 0),
                axes_prob.c2p(1, 0.5),
                color=YELLOW,
                stroke_width=3
            )
            
            region_area = axes_prob.get_area(
                prob_func,
                x_range=[-1, 1],
                color=YELLOW,
                opacity=0.5
            )
            
            region_label = MathTex(
                r"P(-1 < x < 1) = \int_{-1}^{1} |\psi(x)|^2 dx",
                font_size=28,
                color=YELLOW
            )
            region_label.next_to(axes_prob, DOWN, buff=0.4)
            
            self.play(
                Create(region_line_left),
                Create(region_line_right),
                FadeIn(region_area),
                Write(region_label)
            )
            
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def show_time_evolution(self):
        with self.voiceover(text="One of the most fascinating aspects of quantum mechanics is how wave functions evolve in time. Let's see this evolution in action.") as tracker:
            section_title = Text("Time Evolution of Wave Functions", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="For a free particle, the wave function spreads out over time. This is called wave packet spreading and is a purely quantum mechanical phenomenon with no classical analog.") as tracker:
            # Create axes
            axes = Axes(
                x_range=[-6, 6, 2],
                y_range=[0, 1, 0.5],
                x_length=11,
                y_length=4,
                axis_config={"color": WHITE},
            )
            axes.shift(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=RIGHT)
            y_label = axes.get_y_axis_label(r"|\psi(x,t)|^2", edge=UP, direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
        with self.voiceover(text="At time t equals zero, we start with a narrow wave packet centered at the origin. Watch what happens as time progresses.") as tracker:
            # Initial wave packet
            t0_curve = axes.plot(
                lambda x: np.exp(-x**2/0.5),
                color=RED,
                stroke_width=3
            )
            t0_label = MathTex("t = 0", font_size=30, color=RED)
            t0_label.next_to(axes, RIGHT, buff=0.3).shift(UP * 1.5)
            
            self.play(Create(t0_curve), Write(t0_label))
            self.wait(1)
            
        with self.voiceover(text="As time increases, the wave packet spreads out and becomes wider. The particle becomes delocalized, with increasing uncertainty in its position.") as tracker:
            # Later time wave packets
            t1_curve = axes.plot(
                lambda x: 0.7 * np.exp(-x**2/1.5),
                color=ORANGE,
                stroke_width=3
            )
            t1_label = MathTex("t = t_1", font_size=30, color=ORANGE)
            t1_label.next_to(t0_label, DOWN, buff=0.3)
            
            t2_curve = axes.plot(
                lambda x: 0.5 * np.exp(-x**2/3),
                color=YELLOW,
                stroke_width=3
            )
            t2_label = MathTex("t = t_2", font_size=30, color=YELLOW)
            t2_label.next_to(t1_label, DOWN, buff=0.3)
            
            self.play(
                Transform(t0_curve.copy(), t1_curve),
                Write(t1_label)
            )
            self.wait(0.5)
            self.play(
                Transform(t1_curve.copy(), t2_curve),
                Write(t2_label)
            )
            
        with self.voiceover(text="This spreading is governed by the Heisenberg uncertainty principle. As the wave packet spreads in position, the momentum uncertainty increases correspondingly.") as tracker:
            uncertainty = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=38
            )
            uncertainty.to_edge(DOWN, buff=0.5)
            self.play(Write(uncertainty))
            
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        with self.voiceover(text="Let's discuss the physical interpretation of the Schrödinger equation and what it tells us about the quantum world.") as tracker:
            section_title = Text("Physical Interpretation", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="The Schrödinger equation is a wave equation, similar to the equations describing sound waves or water waves. However, it describes probability waves rather than physical waves.") as tracker:
            comparison = VGroup(
                Text("Classical Waves:", font_size=28, color=GREEN),
                Text("• Physical displacement", font_size=22),
                Text("• Water, sound, light", font_size=22),
                Text("", font_size=22),
                Text("Quantum Waves:", font_size=28, color=PURPLE),
                Text("• Probability amplitude", font_size=22),
                Text("• Matter waves", font_size=22),
                Text("• ψ(x,t) complex-valued", font_size=22),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            comparison.shift(LEFT * 2)
            
            self.play(Write(comparison))
            
        with self.voiceover(text="Unlike classical particles which have definite positions and momenta, quantum particles are described by wave functions that give probabilities for different measurement outcomes.") as tracker:
            # Classical vs Quantum
            classical_side = VGroup()
            classical_title = Text("Classical Particle", font_size=24, color=ORANGE)
            classical_dot = Dot(color=ORANGE, radius=0.15)
            classical_label = Text("Definite position", font_size=18)
            classical_side.add(classical_title, classical_dot, classical_label)
            classical_side.arrange(DOWN, buff=0.4)
            classical_side.shift(RIGHT * 3.5 + UP * 1)
            
            quantum_side = VGroup()
            quantum_title = Text("Quantum Particle", font_size=24, color=BLUE)
            
            # Small axes for quantum wave
            mini_axes = Axes(
                x_range=[-2, 2, 1],
                y_range=[0, 1, 1],
                x_length=3,
                y_length=1.5,
                axis_config={"color": WHITE, "stroke_width": 2},
            )
            quantum_wave = mini_axes.plot(
                lambda x: np.exp(-x**2),
                color=BLUE,
                stroke_width=2
            )
            quantum_label = Text("Probability distribution", font_size=18)
            quantum_side.add(quantum_title, VGroup(mini_axes, quantum_wave), quantum_label)
            quantum_side.arrange(DOWN, buff=0.3)
            quantum_side.shift(RIGHT * 3.5 + DOWN * 1.2)
            
            self.play(
                comparison.animate.shift(LEFT * 0.5),
                Write(classical_side),
                Write(quantum_side)
            )
            
        self.wait(1)
        self.play(FadeOut(*self.mobjects))

    def particle_in_box_example(self):
        with self.voiceover(text="Let's examine a concrete example: the particle in a box. This is one of the most important exactly solvable problems in quantum mechanics.") as tracker:
            section_title = Text("Example: Particle in a Box", font_size=36, color=BLUE)
            section_title.to_edge(UP)
            self.play(Write(section_title))
            
        with self.voiceover(text="Imagine a particle confined between two infinitely high potential walls. The particle can only exist between x equals zero and x equals L, where L is the width of the box.") as tracker:
            # Draw the box
            box_axes = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 3, 1],
                x_length=9,
                y_length=4,
                axis_config={"color": WHITE},
            )
            box_axes.shift(DOWN * 0.3)
            
            # Potential walls
            left_wall = Line(
                box_axes.c2p(1, 0),
                box_axes.c2p(1, 2.5),
                color=RED,
                stroke_width=8
            )
            right_wall = Line(
                box_axes.c2p(4, 0),
                box_axes.c2p(4, 2.5),
                color=RED,
                stroke_width=8
            )
            
            box_label_0 = MathTex("x=0", font_size=26)
            box_label_0.next_to(left_wall, DOWN, buff=0.2)
            box_label_L = MathTex("x=L", font_size=26)
            box_label_L.next_to(right_wall, DOWN, buff=0.2)
            
            v_inf_left = MathTex("V=\infty", font_size=24, color=RED)
            v_inf_left.next_to(left_wall, LEFT, buff=0.3)
            v_inf_right = MathTex("V=\infty", font_size=24, color=RED)
            v_inf_right.next_to(right_wall, RIGHT, buff=0.3)
            
            self.play(
                Create(box_axes),
                Create(left_wall),
                Create(right_wall),
                Write(box_label_0),
                Write(box_label_L),
                Write(v_inf_left),
                Write(v_inf_right)
            )
            
        with self.voiceover(text="The solutions to the Schrödinger equation in this case are standing waves, similar to the modes of a vibrating string. The wave functions are given by sine functions.") as tracker:
            solution_eq = MathTex(
                r"\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)",
                font_size=36
            )
            solution_eq.to_edge(UP, buff=1.5)
            self.play(Write(solution_eq))
            
        with self.voiceover(text="Here is the ground state, where n equals one. This is the lowest energy state the particle can have.") as tracker:
            # Ground state (n=1)
            n1_wave = box_axes.plot(
                lambda x: 1.2 * np.sin(np.pi * (x - 1) / 3) if 1 <= x <= 4 else 0,
                color=BLUE,
                stroke_width=3
            )
            n1_label = MathTex("n=1", font_size=28, color=BLUE)
            n1_label.next_to(box_axes, RIGHT, buff=0.5).shift(UP * 1)
            
            self.play(Create(n1_wave), Write(n1_label))
            self.wait(1)
            
        with self.voiceover(text="The first excited state has n equals two, with one node in the middle. Notice how the wave function goes to zero at the walls, satisfying the boundary conditions.") as tracker:
            # First excited state (n=2)
            n2_wave = box_axes.plot(
                lambda x: 1.2 * np.sin(2 * np.pi * (x - 1) / 3) if 1 <= x <= 4 else 0,
                color=GREEN,
                stroke_width=3
            )
            n2_label = MathTex("n=2", font_size=28, color=GREEN)
            n2_label.next_to(n1_label, DOWN, buff=0.3)
            
            self.play(Create(n2_wave), Write(n2_label))
            self.wait(1)
            
        with self.voiceover(text="And here is the n equals three state, with two nodes. Each successive state has higher energy and more nodes.") as tracker:
            # Second excited state (n=3)
            n3_wave = box_axes.plot(
                lambda x: 1.2 * np.sin(3 * np.pi * (x - 1) / 3) if 1 <= x <= 4 else 0,
                color=YELLOW,
                stroke_width=3
            )
            n3_label = MathTex("n=3", font_size=28, color=YELLOW)
            n3_label.next_to(n2_label, DOWN, buff=0.3)
            
            self.play(Create(n3_wave), Write(n3_label))
            
        with self.voiceover(text="The corresponding energies are quantized, meaning they can only take certain discrete values. This is given by the formula E sub n equals n squared times h-bar squared pi squared over two m L squared.") as tracker:
            energy_eq = MathTex(
                r"E_n = \frac{n^2\hbar^2\pi^2}{2mL^2}, \quad n = 1, 2, 3, ...",
                font_size=34
            )
            energy_eq.to_edge(DOWN, buff=0.5)
            self.play(Write(energy_eq))
            
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Let's summarize what we've learned about the Schrödinger equation and its profound implications for our understanding of nature.") as tracker:
            conclusion_title = Text("Summary", font_size=40, color=BLUE, weight=BOLD)
            conclusion_title.to_edge(UP, buff=0.5)
            self.play(Write(conclusion_title))
            
        with self.voiceover(text="First, the Schrödinger equation is the fundamental equation of quantum mechanics. It describes how quantum systems evolve in time through their wave functions.") as tracker:
            point1 = VGroup(
                Text("1. The Schrödinger Equation", font_size=28, color=YELLOW, weight=BOLD),
                MathTex(r"i\hbar\frac{\partial \psi}{\partial t} = \hat{H}\psi", font_size=35),
                Text("Governs all quantum systems", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point1.shift(UP * 1.5 + LEFT * 3)
            
            self.play(Write(point1))
            
        with self.voiceover(text="Second, wave functions contain all information about a quantum system, but they are complex-valued probability amplitudes, not directly measurable quantities.") as tracker:
            point2 = VGroup(
                Text("2. Wave Functions", font_size=28, color=GREEN, weight=BOLD),
                MathTex(r"\psi(x,t) \in \mathbb{C}", font_size=32),
                Text("Probability amplitudes", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point2.next_to(point1, DOWN, buff=0.6, aligned_edge=LEFT)
            
            self.play(Write(point2))
            
        with self.voiceover(text="Third, the probability density, given by the absolute square of the wave function, tells us where we're likely to find a particle when we measure its position.") as tracker:
            point3 = VGroup(
                Text("3. Probability Density", font_size=28, color=ORANGE, weight=BOLD),
                MathTex(r"P(x,t) = |\psi(x,t)|^2", font_size=35),
                Text("Observable predictions", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point3.next_to(point2, DOWN, buff=0.6, aligned_edge=LEFT)
            
            self.play(Write(point3))
            
        with self.voiceover(text="Finally, quantum mechanics fundamentally differs from classical physics. Particles don't have definite properties until measured, and observation plays a crucial role in determining outcomes.") as tracker:
            point4 = VGroup(
                Text("4. Quantum vs Classical", font_size=28, color=PURPLE, weight=BOLD),
                Text("• Superposition of states", font_size=22),
                Text("• Measurement affects system", font_size=22),
                Text("• Inherent uncertainty", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            point4.next_to(point3, DOWN, buff=0.6, aligned_edge=LEFT)
            
            self.play(Write(point4))
            
        with self.voiceover(text="The Schrödinger equation has been incredibly successful, explaining phenomena from atomic spectra to chemical bonding, semiconductor physics, and even the behavior of exotic materials. It remains one of the cornerstones of modern physics and technology.") as tracker:
            self.wait(2)
            
        with self.voiceover(text="Thank you for watching this exploration of the Schrödinger equation. The quantum world is strange and counterintuitive, but also beautiful and mathematically elegant.") as tracker:
            final_message = Text(
                "Thank you for watching!",
                font_size=36,
                color=BLUE,
                weight=BOLD
            )
            final_message.to_edge(DOWN, buff=1)
            self.play(Write(final_message))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))


# Run the animation
if __name__ == "__main__":
    scene = SchrodingerEquationExplanation()
    scene.render()
