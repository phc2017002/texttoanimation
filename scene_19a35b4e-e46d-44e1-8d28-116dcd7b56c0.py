from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Call all sections in sequence
        self.introduction()
        self.historical_context()
        self.wave_function_concept()
        self.the_equation_itself()
        self.time_independent_form()
        self.probability_interpretation()
        self.quantum_harmonic_oscillator()
        self.applications_and_significance()
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. This equation describes how quantum states evolve over time and forms the foundation of our understanding of the microscopic world.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE)
            subtitle = Text("A Journey into Quantum Mechanics", font_size=28, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            self.wait(1)
        
        with self.voiceover(text="Today, we will explore what wave functions are, understand the mathematical structure of the equation, examine probability densities, and see how this framework allows us to predict the behavior of particles at the quantum scale.") as tracker:
            topics = VGroup(
                Text("• Wave Functions", font_size=26),
                Text("• The Equation", font_size=26),
                Text("• Probability Density", font_size=26),
                Text("• Physical Applications", font_size=26)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            topics.shift(DOWN * 0.5)
            
            self.play(FadeOut(title), FadeOut(subtitle))
            self.play(Write(topics), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(topics))

    def historical_context(self):
        with self.voiceover(text="In nineteen twenty-six, Erwin Schrödinger developed his famous equation while attempting to describe matter as waves, building on the ideas of Louis de Broglie. This was a revolutionary moment in physics, as scientists realized that particles don't behave like classical objects.") as tracker:
            year = Text("1926", font_size=56, color=GOLD)
            self.play(Write(year))
            self.wait(1)
            self.play(year.animate.shift(UP * 2.5))
            
            context = Text("The Birth of Wave Mechanics", font_size=32, color=BLUE)
            context.next_to(year, DOWN, buff=0.6)
            self.play(Write(context))
        
        with self.voiceover(text="Schrödinger's work showed that electrons and other particles have wave-like properties. These aren't waves in a physical medium, but rather mathematical functions that describe probability amplitudes. This insight fundamentally changed our understanding of reality at the atomic scale.") as tracker:
            wave_equation = MathTex(
                r"i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi",
                font_size=40,
                color=WHITE
            )
            wave_equation.shift(DOWN * 0.8)
            
            self.play(Write(wave_equation), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_concept(self):
        with self.voiceover(text="Let's begin by understanding what a wave function is. The wave function, denoted by the Greek letter psi, is a mathematical function that contains all the information about a quantum system. It's a complex-valued function that depends on position and time.") as tracker:
            title = Text("The Wave Function ψ", font_size=40, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            psi_def = MathTex(
                r"\psi(x, t)",
                font_size=44,
                color=YELLOW
            )
            psi_def.shift(UP * 1.2)
            
            self.play(Write(psi_def))
            
            properties = VGroup(
                Text("• Complex-valued function", font_size=24),
                Text("• Contains all quantum information", font_size=24),
                Text("• Evolves according to Schrödinger equation", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            properties.shift(DOWN * 0.8)
            
            self.play(Write(properties), run_time=2)
        
        with self.voiceover(text="The wave function itself is not directly observable. However, its square magnitude gives us the probability density of finding a particle at a particular location. Let me show you a simple example of a wave function in one dimension.") as tracker:
            self.play(FadeOut(properties), FadeOut(psi_def))
            
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=8,
                y_length=4,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes.shift(DOWN * 0.8)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT, buff=0.4)
            x_label.scale(0.8)
            y_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.5)
            y_label.scale(0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
            wave_real = axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                color=GREEN,
                x_range=[-4, 4]
            )
            
            wave_label = Text("Real part of ψ(x)", font_size=22, color=GREEN)
            wave_label.next_to(axes, DOWN, buff=0.4)
            
            self.play(Create(wave_real), Write(wave_label), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def the_equation_itself(self):
        with self.voiceover(text="Now let's examine the time-dependent Schrödinger equation in its full glory. This equation tells us how the wave function changes over time. On the left side, we have the time derivative of psi, multiplied by i and h-bar. On the right side, we have the Hamiltonian operator acting on psi.") as tracker:
            title = Text("The Time-Dependent Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            equation = MathTex(
                r"i\hbar", r"\frac{\partial\psi}{\partial t}", r"=", r"\hat{H}", r"\psi",
                font_size=48
            )
            equation.shift(UP * 0.8)
            
            self.play(Write(equation), run_time=2.5)
            self.wait(1)
        
        with self.voiceover(text="Let's break down each component. The imaginary unit i indicates that quantum mechanics is fundamentally complex-valued. H-bar is the reduced Planck constant, a fundamental constant of nature that sets the scale of quantum effects. The partial derivative with respect to time tells us about the dynamics of the system.") as tracker:
            # Highlight each term
            # i_hbar_box = SurroundingRectangle(equation[0], color=YELLOW, buff=0.15)  # Auto-disabled: indexed SurroundingRectangle
            i_hbar_desc = Text("Imaginary unit × reduced Planck constant", font_size=20, color=YELLOW)
            i_hbar_desc.next_to(equation, DOWN, buff=1.2)
            
            # self.play(Create(i_hbar_box), Write(i_hbar_desc))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(2)
            
            # self.play(FadeOut(i_hbar_box), FadeOut(i_hbar_desc))  # Auto-disabled: uses disabled SurroundingRectangle
            
            # deriv_box = SurroundingRectangle(equation[1], color=GREEN, buff=0.15)  # Auto-disabled: indexed SurroundingRectangle
            deriv_desc = Text("Time derivative of wave function", font_size=20, color=GREEN)
            deriv_desc.next_to(equation, DOWN, buff=1.2)
            
            # self.play(Create(deriv_box), Write(deriv_desc))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(2)
            
            # self.play(FadeOut(deriv_box), FadeOut(deriv_desc))  # Auto-disabled: uses disabled SurroundingRectangle
        
        with self.voiceover(text="The Hamiltonian operator represents the total energy of the system. It includes both kinetic energy and potential energy terms. In one dimension, the Hamiltonian can be written explicitly as a sum of the kinetic energy operator and the potential energy function.") as tracker:
            # ham_box = SurroundingRectangle(equation[3], color=RED, buff=0.15)  # Auto-disabled: indexed SurroundingRectangle
            ham_desc = Text("Hamiltonian (Energy operator)", font_size=20, color=RED)
            ham_desc.next_to(equation, DOWN, buff=1.2)
            
            # self.play(Create(ham_box), Write(ham_desc))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1.5)
            
            # self.play(FadeOut(ham_box), FadeOut(ham_desc))  # Auto-disabled: uses disabled SurroundingRectangle
            
            hamiltonian_expanded = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=36
            )
            hamiltonian_expanded.shift(DOWN * 1.0)
            
            self.play(Write(hamiltonian_expanded), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def time_independent_form(self):
        with self.voiceover(text="For systems where the potential energy doesn't change with time, we can separate the time and space dependence of the wave function. This leads to the time-independent Schrödinger equation, which is an eigenvalue problem where energy is the eigenvalue.") as tracker:
            title = Text("Time-Independent Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            separation = MathTex(
                r"\psi(x,t) = \psi(x)e^{-iEt/\hbar}",
                font_size=38
            )
            separation.shift(UP * 1.5)
            
            self.play(Write(separation))
            self.wait(1)
        
        with self.voiceover(text="When we substitute this separated form into the time-dependent equation and simplify, we obtain the time-independent equation. This equation states that the Hamiltonian operator acting on the spatial wave function equals the energy times the wave function. This is the equation we solve to find the allowed energy levels of a quantum system.") as tracker:
            time_indep = MathTex(
                r"\hat{H}\psi(x) = E\psi(x)",
                font_size=44,
                color=YELLOW
            )
            time_indep.shift(UP * 0.2)
            
            self.play(Write(time_indep), run_time=2)
            self.wait(1)
            
            expanded_form = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x)",
                font_size=34
            )
            expanded_form.shift(DOWN * 1.2)
            
            self.play(Write(expanded_form), run_time=2)
            self.wait(1.5)
        
        with self.voiceover(text="This eigenvalue equation is extremely powerful. For each allowed energy E, there is a corresponding wave function psi. These energy levels are often quantized, meaning only certain discrete values are allowed. This is the origin of the term quantum mechanics.") as tracker:
            eigenvalue_note = Text("Energy Eigenvalue Problem", font_size=28, color=GREEN)
            eigenvalue_note.shift(DOWN * 2.6)
            
            self.play(Write(eigenvalue_note))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def probability_interpretation(self):
        with self.voiceover(text="One of the most profound aspects of quantum mechanics is the probabilistic interpretation of the wave function. Max Born proposed that the square of the wave function's magnitude gives the probability density for finding a particle at a given position.") as tracker:
            title = Text("Probability Density and Born's Rule", font_size=36, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            born_rule = MathTex(
                r"P(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)",
                font_size=40,
                color=YELLOW
            )
            born_rule.shift(UP * 1.2)
            
            self.play(Write(born_rule), run_time=2)
            self.wait(1)
        
        with self.voiceover(text="Let me show you a visual example. Here's a wave function for a particle in a box. Notice how it oscillates. Now, when we take the square of its magnitude, we get the probability density. The probability density is always real and non-negative, and it tells us where we're most likely to find the particle.") as tracker:
            axes_wave = Axes(
                x_range=[0, 5, 1],
                y_range=[-1.2, 1.2, 0.5],
                x_length=6,
                y_length=3,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes_wave.shift(UP * 0.2 + LEFT * 3)
            
            x_label_w = axes_wave.get_x_axis_label("x", direction=RIGHT, buff=0.4).scale(0.7)
            y_label_w = axes_wave.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.4).scale(0.7)
            
            wave_func = axes_wave.plot(
                lambda x: np.sqrt(2/5) * np.sin(2*np.pi*x/5),
                color=GREEN,
                x_range=[0, 5]
            )
            
            wave_title = Text("Wave Function", font_size=22, color=GREEN)
            wave_title.next_to(axes_wave, DOWN, buff=0.4)
            
            self.play(Create(axes_wave), Write(x_label_w), Write(y_label_w))
            self.play(Create(wave_func), Write(wave_title), run_time=2)
            
            axes_prob = Axes(
                x_range=[0, 5, 1],
                y_range=[0, 1, 0.5],
                x_length=6,
                y_length=3,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes_prob.shift(UP * 0.2 + RIGHT * 3)
            
            x_label_p = axes_prob.get_x_axis_label("x", direction=RIGHT, buff=0.4).scale(0.7)
            y_label_p = axes_prob.get_y_axis_label(r"|\psi|^2", direction=LEFT).shift(LEFT * 0.5).scale(0.7)
            
            prob_density = axes_prob.plot(
                lambda x: (2/5) * (np.sin(2*np.pi*x/5))**2,
                color=RED,
                x_range=[0, 5]
            )
            
            prob_title = Text("Probability Density", font_size=22, color=RED)
            prob_title.next_to(axes_prob, DOWN, buff=0.4)
            
            self.play(Create(axes_prob), Write(x_label_p), Write(y_label_p))
            self.play(Create(prob_density), Write(prob_title), run_time=2)
            self.wait(1.5)
        
        with self.voiceover(text="An important requirement is that the total probability of finding the particle somewhere must equal one. This is called the normalization condition. We integrate the probability density over all space, and this integral must equal one for the wave function to be physically meaningful.") as tracker:
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1",
                font_size=36,
                color=ORANGE
            )
            normalization.shift(DOWN * 2.5)
            
            self.play(Write(normalization), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def quantum_harmonic_oscillator(self):
        with self.voiceover(text="Let's explore a specific example: the quantum harmonic oscillator. This system models a particle in a parabolic potential, similar to a mass on a spring but at the quantum level. It's one of the most important exactly solvable problems in quantum mechanics.") as tracker:
            title = Text("Quantum Harmonic Oscillator", font_size=36, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            potential = MathTex(
                r"V(x) = \frac{1}{2}m\omega^2 x^2",
                font_size=38
            )
            potential.shift(UP * 1.8)
            
            self.play(Write(potential))
            self.wait(1)
        
        with self.voiceover(text="The potential energy is quadratic in position, characterized by the mass m and angular frequency omega. When we solve the Schrödinger equation for this potential, we find that the energy levels are quantized and equally spaced. The energy of the nth level is given by this beautiful formula.") as tracker:
            energy_levels = MathTex(
                r"E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, \ldots",
                font_size=36,
                color=YELLOW
            )
            energy_levels.shift(UP * 0.6)
            
            self.play(Write(energy_levels), run_time=2)
            self.wait(1.5)
        
        with self.voiceover(text="Notice that even in the ground state, when n equals zero, the energy is not zero but rather one-half h-bar omega. This is called the zero-point energy, a purely quantum mechanical effect with no classical analog. It arises from the uncertainty principle.") as tracker:
            zero_point = Text("Zero-Point Energy: E₀ = ½ℏω", font_size=28, color=GREEN)
            zero_point.shift(DOWN * 0.4)
            
            self.play(Write(zero_point))
            self.wait(2)
            
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 5, 1],
                x_length=7,
                y_length=3.5,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes.shift(DOWN * 2.2)
            
            parabola = axes.plot(
                lambda x: 0.3 * x**2,
                color=WHITE,
                x_range=[-3, 3]
            )
            
            # Energy levels
            e0 = DashedLine(
                axes.c2p(-2, 0.3), axes.c2p(2, 0.3),
                color=GREEN, stroke_width=2
            )
            e1 = DashedLine(
                axes.c2p(-2.5, 0.9), axes.c2p(2.5, 0.9),
                color=YELLOW, stroke_width=2
            )
            e2 = DashedLine(
                axes.c2p(-3, 1.5), axes.c2p(3, 1.5),
                color=RED, stroke_width=2
            )
            
            self.play(FadeOut(zero_point))
            self.play(Create(axes), Create(parabola))
            self.play(Create(e0), Create(e1), Create(e2), run_time=2)
            self.wait(1.5)
        
        self.play(FadeOut(*self.mobjects))

    def applications_and_significance(self):
        with self.voiceover(text="The Schrödinger equation has countless applications across physics and chemistry. It allows us to calculate atomic and molecular structure, understand chemical bonding, predict the behavior of semiconductors, and even describe exotic states of matter like superconductors and superfluids.") as tracker:
            title = Text("Applications and Significance", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            applications = VGroup(
                Text("• Atomic and Molecular Structure", font_size=26),
                Text("• Chemical Bonding and Reactions", font_size=26),
                Text("• Semiconductor Physics", font_size=26),
                Text("• Quantum Computing", font_size=26),
                Text("• Superconductivity", font_size=26)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            applications.shift(DOWN * 0.3)
            
            self.play(Write(applications), run_time=3)
            self.wait(2)
        
        with self.voiceover(text="In quantum computing, the Schrödinger equation governs how qubits evolve. Engineers use it to design quantum gates and algorithms. In materials science, it helps predict the electronic properties of new materials before they're even synthesized in the laboratory.") as tracker:
            self.play(FadeOut(applications))
            
            quantum_computing = Text("Quantum Computing Example", font_size=30, color=YELLOW)
            quantum_computing.shift(UP * 1.5)
            
            qubit_state = MathTex(
                r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle",
                font_size=38
            )
            qubit_state.shift(UP * 0.3)
            
            time_evolution = MathTex(
                r"|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle",
                font_size=38
            )
            time_evolution.shift(DOWN * 0.8)
            
            self.play(Write(quantum_computing))
            self.play(Write(qubit_state), run_time=1.5)
            self.play(Write(time_evolution), run_time=1.5)
            self.wait(2)
        
        with self.voiceover(text="The equation also has profound philosophical implications. It challenges our classical intuitions about reality, determinism, and measurement. The probabilistic nature of quantum mechanics and the measurement problem continue to inspire debates about the fundamental nature of reality.") as tracker:
            philosophical = Text("Philosophical Implications", font_size=28, color=PURPLE)
            philosophical.shift(DOWN * 2.3)
            
            self.play(Write(philosophical))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've covered a lot of ground today. We've explored the Schrödinger equation from multiple angles: its mathematical structure, the concept of wave functions, probability interpretation, and its wide-ranging applications. This equation represents one of humanity's greatest intellectual achievements.") as tracker:
            title = Text("Summary and Conclusion", font_size=40, color=BLUE)
            title.to_edge(UP, buff=0.5)
            self.play(Write(title))
            
            summary_points = VGroup(
                Text("✓ Wave functions describe quantum states", font_size=24),
                Text("✓ Schrödinger equation governs time evolution", font_size=24),
                Text("✓ Probability density: |ψ|²", font_size=24),
                Text("✓ Quantized energy levels", font_size=24),
                Text("✓ Foundation of modern physics", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
            summary_points.shift(DOWN * 0.3)
            
            self.play(Write(summary_points), run_time=3)
            self.wait(2)
        
        with self.voiceover(text="The time-dependent Schrödinger equation encapsulates the dynamics of quantum systems, while the time-independent form gives us energy eigenvalues and eigenstates. The probabilistic interpretation connects abstract mathematics to measurable physical quantities.") as tracker:
            self.play(FadeOut(summary_points))
            
            key_equations = VGroup(
                MathTex(r"i\hbar\frac{\partial\psi}{\partial t} = \hat{H}\psi", font_size=32),
                MathTex(r"\hat{H}\psi = E\psi", font_size=32),
                MathTex(r"P(x) = |\psi(x)|^2", font_size=32)
            ).arrange(DOWN, buff=0.6)
            key_equations.shift(DOWN * 0.2)
            
            self.play(Write(key_equations), run_time=2.5)
            self.wait(2)
        
        with self.voiceover(text="As you continue your journey in quantum mechanics, remember that the Schrödinger equation is your primary tool for understanding the quantum world. From atoms to materials to quantum technologies, this elegant equation continues to reveal the secrets of nature. Thank you for watching, and keep exploring the fascinating world of quantum physics!") as tracker:
            self.play(FadeOut(key_equations))
            
            final_message = Text(
                "Keep Exploring Quantum Mechanics!",
                font_size=36,
                color=GOLD,
                gradient=(BLUE, PURPLE)
            )
            final_message.shift(UP * 0.3)
            
            schrodinger_signature = MathTex(
                r"\psi",
                font_size=80,
                color=YELLOW
            )
            schrodinger_signature.shift(DOWN * 1.2)
            
            self.play(Write(final_message), run_time=2)
            self.play(Write(schrodinger_signature), run_time=2)
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

# Instructions to run:
# Save this file as schrodinger_equation.py
# Run in terminal: manim -pql schrodinger_equation.py SchrodingerEquationExplanation
# For high quality: manim -pqh schrodinger_equation.py SchrodingerEquationExplanation
