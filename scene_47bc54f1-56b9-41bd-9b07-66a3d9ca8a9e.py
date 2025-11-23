# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text

# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text

from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Section 1: Introduction and Title
        self.introduction()
        
        # Section 2: Historical Context
        self.historical_context()
        
        # Section 3: The Equation Itself
        self.show_main_equation()
        
        # Section 4: Understanding the Wave Function
        self.explain_wave_function()
        
        # Section 5: Term by Term Analysis
        self.term_by_term_analysis()
        
        # Section 6: Probability Density
        self.explain_probability_density()
        
        # Section 7: Simple Example - Particle in a Box
        self.particle_in_box_example()
        
        # Section 8: Wave Function Evolution
        self.wave_function_evolution()
        
        # Section 9: Physical Interpretation
        self.physical_interpretation()
        
        # Section 10: Conclusion and Summary
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. This equation revolutionized our understanding of the microscopic world and laid the foundation for modern quantum theory.") as tracker:
            title = Text("The Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("Wave Functions and Probability Density", font_size=24, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.8)
            self.play(FadeIn(subtitle))
        
        with self.voiceover(text="In the next five minutes, we will dive deep into what this equation means, how it describes quantum systems, and why the wave function is so central to quantum mechanics. We'll explore probability densities, examine concrete examples, and build an intuitive understanding of this elegant mathematical framework.") as tracker:
            quantum_symbol = MathTex(r"\hbar", font_size=36, color=GREEN)
            quantum_symbol.move_to(DOWN * 1.0)
            self.play(Create(quantum_symbol))
            self.play(Rotate(quantum_symbol, angle=2*PI), run_time=2)
        
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="In nineteen twenty-six, Austrian physicist Erwin Schrödinger published his groundbreaking wave equation. At the time, physicists were struggling to understand the dual nature of matter and energy, which seemed to behave both as particles and as waves.") as tracker:
            title = Text("Historical Context", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            timeline = NumberLine(x_range=[1900, 1930, 10], length=10, include_numbers=True)
            timeline.move_to(DOWN * 0.5)
            self.play(Create(timeline))
            
            marker = Dot(color=RED)
            marker.move_to(timeline.n2p(1926))
            label = Text("1926", font_size=20, color=RED)
            label.next_to(marker, UP)
            self.play(FadeIn(marker), Write(label))
        
        with self.voiceover(text="Schrödinger's equation provided a mathematical framework to describe how quantum states evolve over time. It was inspired by de Broglie's hypothesis that matter has wave-like properties, and it unified many puzzling experimental observations into a coherent theory.") as tracker:
            wave_particle = VGroup(
                Circle(radius=0.4, color=YELLOW),
                self.create_wave_graphic()
            ).arrange(RIGHT, buff=1.5)
            wave_particle.move_to(DOWN * 2.0)
            self.play(Create(wave_particle))
        
        self.play(FadeOut(*self.mobjects))

    def create_wave_graphic(self):
        wave = FunctionGraph(
            lambda x: 0.3 * np.sin(3 * x),
            x_range=[-1, 1],
            color=BLUE
        )
        return wave

    def show_main_equation(self):
        with self.voiceover(text="Here is the time-dependent Schrödinger equation in its full glory. This is the master equation that governs how quantum systems evolve. On the left side, we have i times h-bar times the partial derivative of the wave function with respect to time.") as tracker:
            title = Text("The Schrödinger Equation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(
                r"i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi",
                font_size=36
            )
            equation.move_to(UP * 0.5)
            self.play(Write(equation))
        
        with self.voiceover(text="On the right side, we have the Hamiltonian operator acting on the wave function. The Hamiltonian represents the total energy of the system. For a particle in a potential, the Hamiltonian can be expanded into kinetic and potential energy terms.") as tracker:
            expanded = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=32
            )
            expanded.move_to(DOWN * 1.0)
            self.play(Write(expanded))
            
            # # kinetic_box = SurroundingRectangle(expanded[0][0:8], color=GREEN, buff=0.8)  # Auto-disabled: indexed SurroundingRectangle  # Auto-disabled: indexed SurroundingRectangle
            # # potential_box = SurroundingRectangle(expanded[0][9:], color=ORANGE, buff=0.8)  # Auto-disabled: indexed SurroundingRectangle  # Auto-disabled: indexed SurroundingRectangle
            
            # self.play(Create(kinetic_box))  # Auto-disabled: uses disabled SurroundingRectangle
            # self.play(Create(potential_box))  # Auto-disabled: uses disabled SurroundingRectangle
        
        with self.voiceover(text="Putting it all together, we get the complete time-dependent Schrödinger equation. This beautiful equation tells us how the wave function psi evolves in time, given the system's Hamiltonian. Every quantum phenomenon, from atomic spectra to quantum tunneling, emerges from solutions to this equation.") as tracker:
            full_equation = MathTex(
                r"i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2} + V(x)\psi",
                font_size=30
            )
            full_equation.move_to(DOWN * 2.5)
            self.play(Write(full_equation))
        
        self.play(FadeOut(*self.mobjects))

    def explain_wave_function(self):
        with self.voiceover(text="The wave function, denoted by the Greek letter psi, is the heart of quantum mechanics. It is a complex-valued function that contains all the information about a quantum system. Unlike classical physics where we describe particles with definite positions and velocities, the wave function gives us probabilities.") as tracker:
            title = Text("The Wave Function ψ", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            psi_def = MathTex(r"\psi(x,t) \in \mathbb{C}", font_size=32)
            psi_def.move_to(UP * 0.5)
            self.play(Write(psi_def))
        
        with self.voiceover(text="Let's visualize a simple wave function. The real part oscillates like a wave, and the imaginary part does too, but shifted in phase. Together, they form a complex wave that propagates through space. This wave-like nature is what gives quantum mechanics its strange and counterintuitive properties.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
            real_wave = axes.plot(lambda x: np.cos(2*x) * np.exp(-x**2/8), color=BLUE)
            imag_wave = axes.plot(lambda x: np.sin(2*x) * np.exp(-x**2/8), color=RED)
            
            real_label = Text("Re(ψ)", font_size=20, color=BLUE).move_to(axes.c2p(3, 0.8))
            imag_label = Text("Im(ψ)", font_size=20, color=RED).move_to(axes.c2p(3, -0.8))
            
            self.play(Create(real_wave), Write(real_label))
            self.play(Create(imag_wave), Write(imag_label))
        
        self.play(FadeOut(*self.mobjects))

    def term_by_term_analysis(self):
        with self.voiceover(text="Let's break down each term in the Schrödinger equation to understand what it represents physically. First, we have i times h-bar, where i is the imaginary unit and h-bar is the reduced Planck constant. This constant connects the microscopic quantum world to our macroscopic measurements.") as tracker:
            title = Text("Term-by-Term Analysis", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            term1 = MathTex(r"i\hbar", font_size=36, color=YELLOW)
            term1.move_to(UP * 0.5)
            self.play(Write(term1))
            
            explanation1 = VGroup(
                MathTex(r"i = \sqrt{-1}", font_size=24),
                MathTex(r"\hbar = \frac{h}{2\pi} = 1.055 \times 10^{-34} \text{ J·s}", font_size=20)
            ).arrange(DOWN, buff=0.8)
            explanation1.move_to(DOWN * 0.5)
            self.play(Write(explanation1))
        
        with self.voiceover(text="The time derivative term tells us how the wave function changes from one moment to the next. This is the dynamic part of quantum mechanics. The partial derivative with respect to time captures the evolution of the quantum state.") as tracker:
            self.play(FadeOut(term1), FadeOut(explanation1))
            
            term2 = MathTex(r"\frac{\partial\psi}{\partial t}", font_size=36, color=GREEN)
            term2.move_to(UP * 0.5)
            self.play(Write(term2))
            
            explanation2 = Text("Rate of change\nof wave function", font_size=22, color=GREEN)
            explanation2.move_to(DOWN * 0.5)
            self.play(Write(explanation2))
        
        with self.voiceover(text="The kinetic energy term contains the second spatial derivative of the wave function. This term describes how the wave function curves in space. A highly curved wave function corresponds to high kinetic energy, just as a tightly confined particle must have high momentum due to the uncertainty principle.") as tracker:
            self.play(FadeOut(term2), FadeOut(explanation2))
            
            term3 = MathTex(r"-\frac{\hbar^2}{2m}\frac{\partial^2\psi}{\partial x^2}", font_size=32, color=BLUE)
            term3.move_to(UP * 0.5)
            self.play(Write(term3))
            
            explanation3 = Text("Kinetic Energy\n(curvature of ψ)", font_size=22, color=BLUE)
            explanation3.move_to(DOWN * 0.8)
            self.play(Write(explanation3))
        
        with self.voiceover(text="Finally, the potential energy term V of x times psi represents the influence of external forces on the particle. This could be the electric potential from a nucleus in an atom, or the walls of a quantum box. The potential shapes the allowed energy states and determines where the particle is likely to be found.") as tracker:
            self.play(FadeOut(term3), FadeOut(explanation3))
            
            term4 = MathTex(r"V(x)\psi", font_size=36, color=ORANGE)
            term4.move_to(UP * 0.5)
            self.play(Write(term4))
            
            explanation4 = Text("Potential Energy\n(external forces)", font_size=22, color=ORANGE)
            explanation4.move_to(DOWN * 0.8)
            self.play(Write(explanation4))
        
        self.play(FadeOut(*self.mobjects))

    def explain_probability_density(self):
        with self.voiceover(text="The wave function itself is not directly observable. What we can measure is the probability of finding a particle at a particular location. This is given by the square of the absolute value of the wave function, which we call the probability density.") as tracker:
            title = Text("Probability Density", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            prob_equation = MathTex(r"P(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)", font_size=32)
            prob_equation.move_to(UP * 0.5)
            self.play(Write(prob_equation))
        
        with self.voiceover(text="Here's the beautiful part. Even though the wave function is complex and can be negative or imaginary, the probability density is always real and non-negative. This makes physical sense because probabilities must be positive numbers. The star denotes complex conjugation.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 1.2, 0.2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
            prob_curve = axes.plot(
                lambda x: np.exp(-x**2/2),
                color=PURPLE,
                x_range=[-4, 4]
            )
            self.play(Create(prob_curve))
        
        with self.voiceover(text="The probability density must integrate to one over all space. This is called normalization. It means that the particle must be somewhere with one hundred percent certainty. The shape of this curve tells us where we're most likely to find the particle if we make a measurement.") as tracker:
            norm_equation = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1",
                font_size=28
            )
            norm_equation.to_edge(RIGHT, buff=1.0).shift(UP * 1.5)
            self.play(Write(norm_equation))
            
            area = axes.get_area(prob_curve, x_range=[-4, 4], color=PURPLE, opacity=0.3)
            self.play(FadeIn(area))
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box_example(self):
        with self.voiceover(text="Let's examine the simplest quantum system: a particle confined in a one-dimensional box. The walls are infinitely high, so the particle is trapped between x equals zero and x equals L. This model, despite its simplicity, reveals profound quantum behavior.") as tracker:
            title = Text("Example: Particle in a Box", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create box
            box = Rectangle(height=3, width=5, color=WHITE)
            box.move_to(DOWN * 0.5)
            
            wall_left = Line(box.get_corner(DL), box.get_corner(UL), color=RED, stroke_width=8)
            wall_right = Line(box.get_corner(DR), box.get_corner(UR), color=RED, stroke_width=8)
            
            box_label_left = MathTex("x=0", font_size=20).next_to(wall_left, LEFT, buff=0.8)
            box_label_right = MathTex("x=L", font_size=20).next_to(wall_right, RIGHT, buff=0.8)
            
            self.play(Create(box))
            self.play(Create(wall_left), Create(wall_right))
            self.play(Write(box_label_left), Write(box_label_right))
        
        with self.voiceover(text="Inside the box, the potential energy is zero, so the Schrödinger equation simplifies. The solutions are standing waves, similar to vibrations on a guitar string. The wave function must be zero at the walls because the particle cannot exist there.") as tracker:
            potential_eq = MathTex(
                r"V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & \text{otherwise} \end{cases}",
                font_size=24
            )
            potential_eq.to_edge(RIGHT, buff=0.8).shift(UP * 1.0)
            self.play(Write(potential_eq))
            
            # Show wave functions
            wave1 = FunctionGraph(
                lambda x: 0.8 * np.sin(PI * (x + 2.5) / 5),
                x_range=[-2.5, 2.5],
                color=BLUE
            )
            wave1.move_to(box.get_center())
            
            n_label = MathTex("n=1", font_size=20, color=BLUE)
            n_label.next_to(box, DOWN, buff=0.8)
            
            self.play(Create(wave1), Write(n_label))
        
        with self.voiceover(text="The allowed wave functions are sine waves with wavelengths that fit exactly into the box. The quantum number n determines how many half-wavelengths fit inside. For n equals one, we have the ground state. For n equals two, we have the first excited state with one node in the middle.") as tracker:
            wave2 = FunctionGraph(
                lambda x: 0.8 * np.sin(2 * PI * (x + 2.5) / 5),
                x_range=[-2.5, 2.5],
                color=GREEN
            )
            wave2.move_to(box.get_center())
            
            n_label2 = MathTex("n=2", font_size=20, color=GREEN)
            n_label2.move_to(n_label.get_center())
            
            self.play(Transform(wave1, wave2), Transform(n_label, n_label2))
            
            wave3 = FunctionGraph(
                lambda x: 0.8 * np.sin(3 * PI * (x + 2.5) / 5),
                x_range=[-2.5, 2.5],
                color=YELLOW
            )
            wave3.move_to(box.get_center())
            
            n_label3 = MathTex("n=3", font_size=20, color=YELLOW)
            n_label3.move_to(n_label.get_center())
            
            self.play(Transform(wave1, wave3), Transform(n_label, n_label3))
        
        with self.voiceover(text="The energy levels are quantized, meaning only specific discrete energies are allowed. The energy increases with the square of n. This quantization is a purely quantum mechanical effect with no classical analog. Higher energy states have more nodes and shorter wavelengths.") as tracker:
            energy_eq = MathTex(
                r"E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}",
                font_size=28
            )
            energy_eq.to_edge(RIGHT, buff=0.8).shift(DOWN * 1.5)
            self.play(Write(energy_eq))
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_evolution(self):
        with self.voiceover(text="Now let's see how wave functions evolve in time. According to the Schrödinger equation, each energy eigenstate accumulates a phase factor that oscillates with angular frequency omega equals E over h-bar. This phase factor doesn't change the probability density, but it's crucial for interference effects.") as tracker:
            title = Text("Time Evolution", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            time_evolution = MathTex(
                r"\psi(x,t) = \psi(x,0)e^{-iEt/\hbar}",
                font_size=32
            )
            time_evolution.move_to(UP * 0.5)
            self.play(Write(time_evolution))
        
        with self.voiceover(text="Let's visualize a wave packet, which is a superposition of many energy eigenstates. Unlike a single eigenstate, a wave packet moves through space. This animation shows the real part of a Gaussian wave packet traveling to the right. The packet spreads out as it propagates, a phenomenon called wave packet dispersion.") as tracker:
            axes = Axes(
                x_range=[-6, 6, 2],
                y_range=[-1, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8).shift(DOWN * 0.8)
            t_label = Text("t = 0", font_size=20).to_edge(LEFT, buff=0.8).shift(DOWN * 1.5)
            
            self.play(Create(axes), Write(x_label), Write(t_label))
            
            # Animate moving wave packet
            for t in np.linspace(0, 2, 20):
                wave_packet = axes.plot(
                    lambda x: np.cos(5*(x - 2*t)) * np.exp(-(x - 2*t)**2/4),
                    color=BLUE,
                    x_range=[-6, 6]
                )
                new_t_label = Text(f"t = {t:.1f}", font_size=20).to_edge(LEFT, buff=0.8).shift(DOWN * 1.5)
                
                if t == 0:
                    self.play(Create(wave_packet), run_time=0.1)
                else:
                    self.play(
                        Transform(prev_wave, wave_packet),
                        Transform(t_label, new_t_label),
                        run_time=0.1
                    )
                prev_wave = wave_packet
        
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        with self.voiceover(text="The physical interpretation of quantum mechanics, particularly the wave function, was a subject of intense debate among physicists. The Copenhagen interpretation, developed by Niels Bohr and Werner Heisenberg, states that the wave function represents our knowledge of the system.") as tracker:
            title = Text("Physical Interpretation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            copenhagen = Text("Copenhagen Interpretation", font_size=26, color=YELLOW)
            copenhagen.move_to(UP * 0.5)
            self.play(Write(copenhagen))
            
            interpretation_points = VGroup(
                Text("• ψ describes probability", font_size=20),
                Text("• Measurement collapses ψ", font_size=20),
                Text("• Inherent randomness", font_size=20)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
            interpretation_points.move_to(DOWN * 0.8)
            self.play(Write(interpretation_points))
        
        with self.voiceover(text="When we make a measurement, the wave function collapses to one of the possible outcomes. Before measurement, the particle exists in a superposition of all possible states. This is fundamentally different from classical physics, where a particle always has a definite position and momentum.") as tracker:
            self.play(FadeOut(interpretation_points))
            
            # Show measurement collapse
            before = Text("Before Measurement", font_size=20, color=GREEN)
            before.move_to(LEFT * 3 + UP * 0.2)
            
            after = Text("After Measurement", font_size=20, color=RED)
            after.move_to(RIGHT * 3 + UP * 0.2)
            
            # Wave function before (spread out)
            axes_before = Axes(
                x_range=[-2, 2, 1],
                y_range=[0, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False}
            )
            axes_before.move_to(LEFT * 3 + DOWN * 1.2)
            
            wave_before = axes_before.plot(
                lambda x: np.exp(-x**2/0.5),
                color=GREEN
            )
            
            # Wave function after (localized spike)
            axes_after = Axes(
                x_range=[-2, 2, 1],
                y_range=[0, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False}
            )
            axes_after.move_to(RIGHT * 3 + DOWN * 1.2)
            
            spike_x = 0.5
            wave_after = axes_after.plot(
                lambda x: np.exp(-((x-spike_x)**2)/0.01) if abs(x - spike_x) < 0.3 else 0,
                color=RED,
                x_range=[-2, 2]
            )
            
            self.play(Write(before), Write(after))
            self.play(Create(axes_before), Create(wave_before))
            self.play(Create(axes_after), Create(wave_after))
            
            arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, color=YELLOW)
            arrow.move_to(DOWN * 1.2)
            measure_label = Text("Measure!", font_size=18, color=YELLOW)
            measure_label.next_to(arrow, UP, buff=0.8)
            self.play(GrowArrow(arrow), Write(measure_label))
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've journeyed through the fundamentals of the Schrödinger equation, from its historical origins to its profound physical implications. We've seen how the wave function encodes quantum information and how probability densities give us predictions about measurements.") as tracker:
            title = Text("Summary and Conclusion", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation_summary = MathTex(
                r"i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi",
                font_size=32,
                color=YELLOW
            )
            equation_summary.move_to(UP * 1.5)
            self.play(Write(equation_summary))
        
        with self.voiceover(text="The key insights are these: quantum states are described by complex wave functions. The probability of finding a particle is the square of the wave function's magnitude. Energy levels are quantized for bound systems. And measurement fundamentally changes the quantum state through wave function collapse.") as tracker:
            key_points = VGroup(
                Text("1. Wave functions are complex", font_size=22),
                Text("2. Probabilities from |ψ|²", font_size=22),
                Text("3. Quantized energy levels", font_size=22),
                Text("4. Measurement causes collapse", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
            key_points.move_to(DOWN * 1.5)
            
            for point in key_points:
                self.play(FadeIn(point), run_time=0.8)
        
        with self.voiceover(text="The Schrödinger equation remains the cornerstone of quantum mechanics, applicable to everything from electrons in atoms to quantum computers. Its mathematical elegance and predictive power continue to shape our understanding of reality at the smallest scales. Thank you for joining this exploration of quantum mechanics.") as tracker:
            final_message = Text("Thank you for watching!", font_size=28, color=GREEN)
            final_message.move_to(DOWN * 3.0)
            self.play(Write(final_message))
            
            # Final animation - pulsing equation
            self.play(
                equation_summary.animate.scale(1.2),
                equation_summary.animate.set_color(BLUE),
                run_time=1
            )
            self.play(
                equation_summary.animate.scale(1/1.2),
                equation_summary.animate.set_color(YELLOW),
                run_time=1
            )
        
        self.play(FadeOut(*self.mobjects))

# Run the animation
if __name__ == "__main__":
    scene = SchrodingerEquationExplanation()
    scene.render()