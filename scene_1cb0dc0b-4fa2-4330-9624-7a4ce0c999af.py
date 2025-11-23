from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Introduction
        self.introduction()
        
        # Wave functions
        self.explain_wave_functions()
        
        # The Schrödinger equation
        self.show_schrodinger_equation()
        
        # Time-independent version
        self.time_independent_schrodinger()
        
        # Probability density
        self.explain_probability_density()
        
        # Physical interpretation
        self.physical_interpretation()
        
        # Example: Particle in a box
        self.particle_in_box_example()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of the Schrödinger equation, one of the most fundamental equations in quantum mechanics.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE, weight=BOLD)
            subtitle = Text("Wave Functions and Probability Density", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
            self.wait(1)
        
        with self.voiceover(text="This equation describes how quantum states evolve over time and forms the foundation of quantum mechanics.") as tracker:
            self.wait(2)
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def explain_wave_functions(self):
        with self.voiceover(text="Before we dive into the equation itself, let's understand what a wave function is.") as tracker:
            title = Text("What is a Wave Function?", font_size=40, color=YELLOW)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="A wave function, denoted by the Greek letter psi, is a mathematical function that describes the quantum state of a particle.") as tracker:
            psi_definition = MathTex(r"\Psi(x, t)", font_size=60, color=GREEN)
            psi_definition.shift(UP * 1)
            self.play(Write(psi_definition))
            
        with self.voiceover(text="It depends on position x and time t. The wave function itself is a complex-valued function.") as tracker:
            description = Text("Complex-valued function of position and time", font_size=24)
            description.next_to(psi_definition, DOWN, buff=0.8)
            self.play(FadeIn(description))
            self.wait(1)
        
        with self.voiceover(text="Let's visualize what a wave function might look like. Here's a simple example of a wave packet.") as tracker:
            self.play(FadeOut(psi_definition), FadeOut(description))
            
            # Create axes for wave function
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=10,
                y_length=4,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes.shift(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label(r"\Psi(x)", direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="This wave packet represents the real part of a wave function. It shows the wavelike nature of quantum particles.") as tracker:
            # Create a wave packet
            wave_function = axes.plot(
                lambda x: np.exp(-x**2 / 2) * np.cos(4 * x),
                color=YELLOW,
                x_range=[-4, 4]
            )
            self.play(Create(wave_function), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(wave_function))

    def show_schrodinger_equation(self):
        with self.voiceover(text="Now, let's introduce the time-dependent Schrödinger equation in its full glory.") as tracker:
            title = Text("The Schrödinger Equation", font_size=40, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="Here it is: i times the reduced Planck constant times the partial derivative of psi with respect to time equals the Hamiltonian operator acting on psi.") as tracker:
            schrodinger_eq = MathTex(
                r"i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi",
                font_size=50,
                color=YELLOW
            )
            schrodinger_eq.shift(UP * 0.5)
            self.play(Write(schrodinger_eq), run_time=3)
            self.wait(1)
        
        with self.voiceover(text="Let's break down each component of this equation to understand what it means.") as tracker:
            self.wait(1)
        
        with self.voiceover(text="The left side represents the time evolution of the wave function. The i is the imaginary unit, and h-bar is the reduced Planck constant.") as tracker:
            # left_box = SurroundingRectangle(schrodinger_eq[0][0:7], color=RED, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            left_label = Text("Time evolution", font_size=24, color=RED)
            # left_label.next_to(left_box, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(left_box), FadeIn(left_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
        
        with self.voiceover(text="The right side contains the Hamiltonian operator, which represents the total energy of the system.") as tracker:
            # self.play(FadeOut(left_box), FadeOut(left_label))  # Auto-disabled: uses disabled SurroundingRectangle
            
            # right_box = SurroundingRectangle(schrodinger_eq[0][8:], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            right_label = Text("Total energy (Hamiltonian)", font_size=24, color=GREEN)
            # right_label.next_to(right_box, DOWN, buff=0.5)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(right_box), FadeIn(right_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
        
        # self.play(FadeOut(right_box), FadeOut(right_label))  # Auto-disabled: uses disabled SurroundingRectangle
        
        with self.voiceover(text="The Hamiltonian operator can be expanded into kinetic energy and potential energy terms.") as tracker:
            hamiltonian_expansion = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=45,
                color=GREEN
            )
            hamiltonian_expansion.next_to(schrodinger_eq, DOWN, buff=1)
            self.play(Write(hamiltonian_expansion), run_time=2)
            self.wait(1)
        
        with self.voiceover(text="The first term is the kinetic energy operator, and the second term V of x is the potential energy.") as tracker:
            # kinetic_box = SurroundingRectangle(hamiltonian_expansion[0][2:12], color=ORANGE, buff=0.08)  # Auto-disabled: indexed SurroundingRectangle
            kinetic_label = Text("Kinetic energy", font_size=20, color=ORANGE)
            # kinetic_label.next_to(kinetic_box, DOWN, buff=0.3)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # potential_box = SurroundingRectangle(hamiltonian_expansion[0][13:], color=PURPLE, buff=0.08)  # Auto-disabled: indexed SurroundingRectangle
            potential_label = Text("Potential energy", font_size=20, color=PURPLE)
            # potential_label.next_to(potential_box, DOWN, buff=0.3)  # Auto-disabled: uses disabled SurroundingRectangle
            
            # self.play(Create(kinetic_box), FadeIn(kinetic_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(0.5)
            # self.play(Create(potential_box), FadeIn(potential_label))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
        
        self.play(
            FadeOut(title), FadeOut(schrodinger_eq), FadeOut(hamiltonian_expansion),
            # FadeOut(kinetic_box), FadeOut(kinetic_label), FadeOut(potential_box), FadeOut(potential_label)  # Auto-disabled: uses disabled SurroundingRectangle
        )

    def time_independent_schrodinger(self):
        with self.voiceover(text="For many applications, we use the time-independent Schrödinger equation, which applies to stationary states.") as tracker:
            title = Text("Time-Independent Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="In this case, we can separate the wave function into a spatial part and a time part.") as tracker:
            separation = MathTex(
                r"\Psi(x,t) = \psi(x) \cdot e^{-iEt/\hbar}",
                font_size=45,
                color=YELLOW
            )
            separation.shift(UP * 1.5)
            self.play(Write(separation))
            self.wait(1)
        
        with self.voiceover(text="This leads to the time-independent form: the Hamiltonian acting on psi equals E times psi, where E is the energy eigenvalue.") as tracker:
            time_independent_eq = MathTex(
                r"\hat{H}\psi(x) = E\psi(x)",
                font_size=50,
                color=GREEN
            )
            time_independent_eq.shift(DOWN * 0.2)
            self.play(Write(time_independent_eq), run_time=2)
            self.wait(1)
        
        with self.voiceover(text="Or, writing out the Hamiltonian explicitly, we get this form with the second derivative and potential energy.") as tracker:
            expanded_form = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)",
                font_size=42,
                color=ORANGE
            )
            expanded_form.shift(DOWN * 1.8)
            self.play(Write(expanded_form), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(title), FadeOut(separation), FadeOut(time_independent_eq), FadeOut(expanded_form))

    def explain_probability_density(self):
        with self.voiceover(text="Now let's explore one of the most important concepts: probability density.") as tracker:
            title = Text("Probability Density", font_size=40, color=PURPLE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="According to the Born interpretation, the square of the absolute value of the wave function gives us the probability density of finding the particle at a given position.") as tracker:
            born_rule = MathTex(
                r"P(x) = |\Psi(x,t)|^2 = \Psi^*(x,t) \Psi(x,t)",
                font_size=48,
                color=YELLOW
            )
            born_rule.shift(UP * 1.2)
            self.play(Write(born_rule), run_time=2)
            self.wait(1)
        
        with self.voiceover(text="This is a probability density, meaning the probability of finding the particle in a small interval is P of x times delta x.") as tracker:
            probability_text = MathTex(
                r"\text{Probability in } [x, x+dx] = P(x) \, dx",
                font_size=38,
                color=WHITE
            )
            probability_text.next_to(born_rule, DOWN, buff=0.8)
            self.play(Write(probability_text))
            self.wait(1)
        
        with self.voiceover(text="Let's visualize this relationship. First, we'll show a wave function.") as tracker:
            self.play(FadeOut(born_rule), FadeOut(probability_text))
            
            # Create axes
            axes_psi = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.2, 1.2, 0.5],
                x_length=9,
                y_length=3,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes_psi.shift(UP * 1.2)
            
            psi_label = axes_psi.get_axis_labels(x_label="x", y_label=r"\Psi(x)")
            
            self.play(Create(axes_psi), Write(psi_label))
        
        with self.voiceover(text="Here's our wave function, oscillating with a Gaussian envelope.") as tracker:
            wave_func = axes_psi.plot(
                lambda x: np.exp(-x**2 / 2) * np.cos(5 * x),
                color=YELLOW,
                x_range=[-3, 3]
            )
            wave_label = Text("Wave function ψ(x)", font_size=24, color=YELLOW)
            wave_label.next_to(axes_psi, RIGHT, buff=0.3)
            
            self.play(Create(wave_func), Write(wave_label))
            self.wait(1)
        
        with self.voiceover(text="Now, when we take the absolute value squared, we get the probability density shown below.") as tracker:
            # Create axes for probability density
            axes_prob = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 1.2, 0.5],
                x_length=9,
                y_length=3,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes_prob.shift(DOWN * 1.8)
            
            prob_label = axes_prob.get_axis_labels(x_label="x", y_label=r"|\Psi(x)|^2")
            
            self.play(Create(axes_prob), Write(prob_label))
        
        with self.voiceover(text="Notice how the probability density is always positive and shows where the particle is most likely to be found.") as tracker:
            prob_density = axes_prob.plot(
                lambda x: np.exp(-x**2),
                color=RED,
                x_range=[-3, 3]
            )
            prob_density_label = Text("Probability density |ψ(x)|²", font_size=24, color=RED)
            prob_density_label.next_to(axes_prob, RIGHT, buff=0.3)
            
            self.play(Create(prob_density), Write(prob_density_label), run_time=2)
            self.wait(2)
        
        with self.voiceover(text="The total probability of finding the particle anywhere must equal one. This is called normalization.") as tracker:
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\Psi(x,t)|^2 \, dx = 1",
                font_size=40,
                color=GREEN
            )
            normalization.to_edge(DOWN, buff=0.3)
            self.play(Write(normalization))
            self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(axes_psi), FadeOut(psi_label), FadeOut(wave_func), FadeOut(wave_label),
            FadeOut(axes_prob), FadeOut(prob_label), FadeOut(prob_density), FadeOut(prob_density_label),
            FadeOut(normalization)
        )

    def physical_interpretation(self):
        with self.voiceover(text="Let's discuss the physical interpretation and what the Schrödinger equation tells us about quantum mechanics.") as tracker:
            title = Text("Physical Interpretation", font_size=40, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="First, the Schrödinger equation is deterministic. If we know the wave function at one time, we can calculate it at any other time.") as tracker:
            point1 = Text("1. Deterministic evolution of ψ", font_size=30, color=YELLOW)
            point1.shift(UP * 1.5)
            self.play(FadeIn(point1))
            self.wait(1)
        
        with self.voiceover(text="However, the outcome of measurements is probabilistic. We can only predict probabilities, not certainties.") as tracker:
            point2 = Text("2. Probabilistic measurement outcomes", font_size=30, color=YELLOW)
            point2.next_to(point1, DOWN, buff=0.6)
            self.play(FadeIn(point2))
            self.wait(1)
        
        with self.voiceover(text="Third, particles exhibit wave-particle duality. They show wave-like behavior through interference and diffraction.") as tracker:
            point3 = Text("3. Wave-particle duality", font_size=30, color=YELLOW)
            point3.next_to(point2, DOWN, buff=0.6)
            self.play(FadeIn(point3))
            self.wait(1)
        
        with self.voiceover(text="Finally, there's the uncertainty principle. We cannot simultaneously know the exact position and momentum of a particle.") as tracker:
            point4 = Text("4. Heisenberg uncertainty principle", font_size=30, color=YELLOW)
            point4.next_to(point3, DOWN, buff=0.6)
            self.play(FadeIn(point4))
            
            uncertainty = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=45,
                color=RED
            )
            uncertainty.next_to(point4, DOWN, buff=0.8)
            self.play(Write(uncertainty))
            self.wait(2)
        
        self.play(FadeOut(title), FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4), FadeOut(uncertainty))

    def particle_in_box_example(self):
        with self.voiceover(text="Let's apply the Schrödinger equation to a classic example: a particle confined in a one-dimensional box.") as tracker:
            title = Text("Example: Particle in a Box", font_size=40, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="Imagine a particle trapped between two infinitely high potential walls at x equals zero and x equals L.") as tracker:
            # Draw the box
            box_axes = Axes(
                x_range=[-1, 5, 1],
                y_range=[0, 4, 1],
                x_length=8,
                y_length=3,
                axis_config={"color": BLUE}
            )
            box_axes.shift(DOWN * 0.5)
            
            # Potential walls
            left_wall = Line(start=box_axes.c2p(0, 0), end=box_axes.c2p(0, 3.5), color=RED, stroke_width=8)
            right_wall = Line(start=box_axes.c2p(4, 0), end=box_axes.c2p(4, 3.5), color=RED, stroke_width=8)
            
            bottom_line = Line(start=box_axes.c2p(0, 0), end=box_axes.c2p(4, 0), color=WHITE, stroke_width=4)
            
            zero_label = MathTex("0", font_size=28).next_to(box_axes.c2p(0, 0), DOWN)
            L_label = MathTex("L", font_size=28).next_to(box_axes.c2p(4, 0), DOWN)
            
            v_label = MathTex("V = 0", font_size=28, color=GREEN).move_to(box_axes.c2p(2, 0.5))
            
            self.play(Create(box_axes))
            self.play(Create(left_wall), Create(right_wall), Create(bottom_line))
            self.play(Write(zero_label), Write(L_label), Write(v_label))
            self.wait(1)
        
        with self.voiceover(text="Inside the box, the potential energy is zero, so the Schrödinger equation simplifies significantly.") as tracker:
            schrodinger_box = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi",
                font_size=40,
                color=YELLOW
            )
            schrodinger_box.to_edge(UP, buff=1.5)
            self.play(Write(schrodinger_box))
            self.wait(1)
        
        with self.voiceover(text="The solutions are standing waves, similar to waves on a string. The wave function must be zero at the walls.") as tracker:
            self.play(FadeOut(schrodinger_box), FadeOut(v_label))
            
            # Show first three energy levels
            n1_wave = box_axes.plot(
                lambda x: np.sin(PI * x / 4),
                color=YELLOW,
                x_range=[0, 4]
            )
            n1_label = MathTex("n=1", font_size=24, color=YELLOW).next_to(box_axes.c2p(4.5, 0.7), RIGHT)
            
            self.play(Create(n1_wave), Write(n1_label))
            self.wait(1)
        
        with self.voiceover(text="Higher energy states have more nodes. Here's the second energy level with two half-wavelengths.") as tracker:
            n2_wave = box_axes.plot(
                lambda x: np.sin(2 * PI * x / 4),
                color=GREEN,
                x_range=[0, 4]
            )
            n2_label = MathTex("n=2", font_size=24, color=GREEN).next_to(box_axes.c2p(4.5, 1.5), RIGHT)
            
            self.play(Create(n2_wave), Write(n2_label))
            self.wait(1)
        
        with self.voiceover(text="And the third energy level with three half-wavelengths fits in the box.") as tracker:
            n3_wave = box_axes.plot(
                lambda x: np.sin(3 * PI * x / 4),
                color=ORANGE,
                x_range=[0, 4]
            )
            n3_label = MathTex("n=3", font_size=24, color=ORANGE).next_to(box_axes.c2p(4.5, 2.3), RIGHT)
            
            self.play(Create(n3_wave), Write(n3_label))
            self.wait(1)
        
        with self.voiceover(text="The energy levels are quantized, meaning only certain discrete energy values are allowed. The energy of each state is proportional to n squared.") as tracker:
            energy_formula = MathTex(
                r"E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}, \quad n = 1, 2, 3, ...",
                font_size=38,
                color=PURPLE
            )
            energy_formula.to_edge(DOWN, buff=0.5)
            self.play(Write(energy_formula))
            self.wait(2)
        
        self.play(
            FadeOut(title), FadeOut(box_axes), FadeOut(left_wall), FadeOut(right_wall), FadeOut(bottom_line),
            FadeOut(zero_label), FadeOut(L_label), FadeOut(n1_wave), FadeOut(n1_label),
            FadeOut(n2_wave), FadeOut(n2_label), FadeOut(n3_wave), FadeOut(n3_label),
            FadeOut(energy_formula)
        )

    def conclusion(self):
        with self.voiceover(text="Let's summarize what we've learned about the Schrödinger equation.") as tracker:
            title = Text("Summary", font_size=44, color=BLUE, weight=BOLD)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="The Schrödinger equation is the fundamental equation of quantum mechanics that describes how wave functions evolve in time.") as tracker:
            summary1 = Text("• Fundamental equation of quantum mechanics", font_size=28, color=WHITE)
            summary1.shift(UP * 1.2)
            self.play(FadeIn(summary1))
            self.wait(1)
        
        with self.voiceover(text="Wave functions contain all information about a quantum system, but they are complex-valued and not directly observable.") as tracker:
            summary2 = Text("• Wave functions describe quantum states", font_size=28, color=WHITE)
            summary2.next_to(summary1, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(FadeIn(summary2))
            self.wait(1)
        
        with self.voiceover(text="Probability densities, obtained by squaring the wave function, tell us where we're likely to find particles.") as tracker:
            summary3 = Text("• Probability density = |ψ|² gives measurement outcomes", font_size=28, color=WHITE)
            summary3.next_to(summary2, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(FadeIn(summary3))
            self.wait(1)
        
        with self.voiceover(text="Energy levels are often quantized, meaning only discrete values are allowed, as we saw in the particle in a box.") as tracker:
            summary4 = Text("• Quantized energy levels in bound systems", font_size=28, color=WHITE)
            summary4.next_to(summary3, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(FadeIn(summary4))
            self.wait(1)
        
        with self.voiceover(text="This equation revolutionized physics and opened the door to understanding atoms, molecules, and the quantum world.") as tracker:
            summary5 = Text("• Foundation for understanding the quantum world", font_size=28, color=WHITE)
            summary5.next_to(summary4, DOWN, buff=0.5, aligned_edge=LEFT)
            self.play(FadeIn(summary5))
            self.wait(1)
        
        with self.voiceover(text="Thank you for joining me on this journey through the Schrödinger equation. Keep exploring quantum mechanics!") as tracker:
            final_equation = MathTex(
                r"i\hbar \frac{\partial \Psi}{\partial t} = \hat{H} \Psi",
                font_size=50,
                color=YELLOW
            )
            final_equation.to_edge(DOWN, buff=1)
            self.play(Write(final_equation))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

# Instructions to run:
# manim -pql schrodinger_explanation.py SchrodingerEquationExplanation
# For high quality: manim -pqh schrodinger_explanation.py SchrodingerEquationExplanation
