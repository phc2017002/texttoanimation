# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame

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
        
        # Section 3: The Wave Function Concept
        self.wave_function_concept()
        
        # Section 4: The Time-Independent Schrödinger Equation
        self.time_independent_equation()
        
        # Section 5: Understanding Each Term
        self.explain_equation_terms()
        
        # Section 6: Wave Function Visualization
        self.visualize_wave_functions()
        
        # Section 7: Probability Density
        self.probability_density_explanation()
        
        # Section 8: Quantum Harmonic Oscillator Example
        self.harmonic_oscillator_example()
        
        # Section 9: Physical Interpretation
        self.physical_interpretation()
        
        # Section 10: Normalization Condition
        self.normalization_condition()
        
        # Section 11: Applications in Modern Physics
        self.applications()
        
        # Section 12: Summary and Conclusion
        self.conclusion()

    def introduction(self):
        """Introduction to the Schrödinger equation"""
        with self.voiceover(text="Welcome to this comprehensive exploration of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. This equation revolutionized our understanding of the microscopic world and continues to be essential in modern physics and chemistry.") as tracker:
            title = Text("The Schrödinger Equation", font_size=42, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            subtitle = Text("Wave Functions and Probability Density", font_size=28, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            subtitle.next_to(title, DOWN, buff=0.6)
            self.play(FadeIn(subtitle))
            
        with self.voiceover(text="In this animation, we will explore the mathematical formulation, physical meaning, and profound implications of this equation. We'll see how it describes the behavior of particles at the quantum scale and why it's so different from classical physics.") as tracker:
            # Create atom-like visualization
            nucleus = Dot(ORIGIN, color=RED, radius=0.15)
            orbits = VGroup(*[
                Circle(radius=r, color=BLUE, stroke_width=2)
                for r in [1.0, 1.5, 2.0]
            ])
            orbits.move_to(ORIGIN)
            
            electrons = VGroup(*[
                Dot(color=YELLOW, radius=0.1).move_to(circle.point_at_angle(angle))
                for circle, angle in zip(orbits, [0, PI/3, 2*PI/3])
            ])
            
            atom_group = VGroup(nucleus, orbits, electrons)
            atom_group.move_to(DOWN * 1.5)
            
            self.play(Create(nucleus))
            self.play(Create(orbits))
            self.play(Create(electrons))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        """Historical background of the equation"""
        with self.voiceover(text="In nineteen twenty-six, Austrian physicist Erwin Schrödinger developed this equation, building on the work of Louis de Broglie who proposed that particles could exhibit wave-like behavior. This was a revolutionary idea that challenged classical Newtonian mechanics.") as tracker:
            heading = Text("Historical Context", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            timeline = NumberLine(
                x_range=[1920, 1930, 2],
                length=10,
                include_numbers=True,
                font_size=24
            )
            timeline.move_to(DOWN * 0.5)
            self.play(Create(timeline))
            
            year_1924 = Text("1924: de Broglie\nWave-Particle Duality", font_size=20, color=GREEN)
            # Auto-fix: Increased spacing to 0.6

            year_1924.next_to(timeline.n2p(1924), UP, buff=0.6)
            
            year_1926 = Text("1926: Schrödinger\nWave Equation", font_size=20, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            year_1926.next_to(timeline.n2p(1926), UP, buff=0.6)
            
            self.play(Write(year_1924))
            
        with self.voiceover(text="The equation emerged from Schrödinger's attempt to describe electrons not as particles, but as waves. This wave description turned out to be extraordinarily successful, explaining phenomena that classical physics could not, such as the discrete energy levels of atoms and the stability of matter itself.") as tracker:
            self.play(Write(year_1926))
            
            wave_demo = self.get_wave_packet()
            wave_demo.move_to(DOWN * 2.5)
            wave_demo.scale(0.6)
            self.play(Create(wave_demo))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def wave_function_concept(self):
        """Explain the wave function concept"""
        with self.voiceover(text="At the heart of quantum mechanics is the wave function, denoted by the Greek letter psi. The wave function is a mathematical function that contains all the information about a quantum system. Unlike classical physics where we can know exact positions and velocities, the wave function gives us probabilities.") as tracker:
            heading = Text("The Wave Function ψ", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            psi_def = MathTex(r"\psi(x, t)").scale(1.2)
            psi_def.move_to(UP * 1.5)
            self.play(Write(psi_def))
            
            description = Text("Position and time dependent", font_size=24, color=YELLOW)
            description.next_to(psi_def, DOWN, buff=0.6)
            self.play(Write(description))
            
        with self.voiceover(text="The wave function can be complex-valued, meaning it has both a real and imaginary component. While the wave function itself is not directly observable, its square gives us the probability density - the likelihood of finding a particle at a particular location. This is one of the most profound aspects of quantum mechanics.") as tracker:
            complex_form = MathTex(r"\psi(x,t) = A e^{i(kx - \omega t)}").scale(0.9)
            complex_form.move_to(ORIGIN)
            self.play(Write(complex_form))
            
            real_part = MathTex(r"\text{Real: } A\cos(kx - \omega t)", color=GREEN).scale(0.8)
            imag_part = MathTex(r"\text{Imaginary: } A\sin(kx - \omega t)", color=RED).scale(0.8)
            
            parts = VGroup(real_part, imag_part).arrange(DOWN, buff=0.4)
            parts.move_to(DOWN * 1.5)
            
            self.play(Write(real_part))
            self.play(Write(imag_part))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def time_independent_equation(self):
        """Present the time-independent Schrödinger equation"""
        with self.voiceover(text="Let's focus on the time-independent Schrödinger equation, which applies to systems with constant energy. This is the most commonly used form and is essential for understanding atomic structure, molecular bonding, and solid-state physics. The equation relates the energy of a system to its wave function.") as tracker:
            heading = Text("Time-Independent Schrödinger Equation", font_size=32, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            main_equation = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi"
            ).scale(0.9)
            main_equation.move_to(UP * 1.2)
            self.play(Write(main_equation))
            
        with self.voiceover(text="This equation is an eigenvalue problem. The left side contains the Hamiltonian operator acting on the wave function, while the right side is simply the energy times the wave function. The solutions to this equation give us the allowed energy levels and corresponding wave functions for the system.") as tracker:
            operator_form = MathTex(r"\hat{H}\psi = E\psi").scale(0.9)
            operator_form.move_to(ORIGIN)
            self.play(Write(operator_form))
            
            hamiltonian = MathTex(
                r"\hat{H} = \hat{T} + \hat{V} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)"
            ).scale(0.8)
            hamiltonian.move_to(DOWN * 1.2)
            self.play(Write(hamiltonian))
            
            labels = VGroup(
                # Auto-fix: Increased spacing to 0.6

                Text("Kinetic Energy", font_size=20, color=GREEN).next_to(hamiltonian, DOWN, buff=0.6).shift(LEFT * 2),
                # Auto-fix: Increased spacing to 0.6

                Text("Potential Energy", font_size=20, color=RED).next_to(hamiltonian, DOWN, buff=0.6).shift(RIGHT * 2)
            )
            self.play(Write(labels))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def explain_equation_terms(self):
        """Explain each term in detail"""
        with self.voiceover(text="Let's break down each component of the equation to understand its physical meaning. The first term contains h-bar, which is Planck's constant divided by two pi. This fundamental constant sets the scale of quantum effects and has units of action. It appears throughout quantum mechanics.") as tracker:
            heading = Text("Understanding Each Term", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            hbar_term = MathTex(r"\hbar = \frac{h}{2\pi} = 1.055 \times 10^{-34} \text{ J·s}").scale(0.8)
            hbar_term.move_to(UP * 1.5)
            self.play(Write(hbar_term))
            
            hbar_meaning = Text("Reduced Planck's constant", font_size=24, color=YELLOW)
            hbar_meaning.next_to(hbar_term, DOWN, buff=0.6)
            self.play(Write(hbar_meaning))
            
        with self.voiceover(text="The kinetic energy term involves the second derivative of the wave function with respect to position. This derivative measures how rapidly the wave function is changing in space - a highly curved wave function corresponds to higher kinetic energy. The factor of m in the denominator is the particle's mass.") as tracker:
            kinetic_term = MathTex(r"\hat{T} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}").scale(0.9)
            kinetic_term.move_to(ORIGIN)
            self.play(Write(kinetic_term))
            
            ke_description = Text("Kinetic energy operator", font_size=24, color=GREEN)
            # Auto-fix: Increased spacing to 0.6

            ke_description.next_to(kinetic_term, DOWN, buff=0.6)
            self.play(Write(ke_description))
            
        with self.voiceover(text="The potential energy term, V of x, represents the forces acting on the particle. For an electron in an atom, this would be the attractive Coulomb potential from the nucleus. For a particle in a box, the potential is zero inside and infinite at the walls. The form of V determines the specific system we're studying.") as tracker:
            self.play(FadeOut(kinetic_term), FadeOut(ke_description))
            
            potential_term = MathTex(r"V(x)\psi(x)").scale(0.9)
            potential_term.move_to(ORIGIN)
            self.play(Write(potential_term))
            
            examples = VGroup(
                MathTex(r"V(x) = \frac{1}{2}m\omega^2 x^2", color=YELLOW).scale(0.7),
                # Auto-fix: Increased spacing to 0.6

                Text("(Harmonic Oscillator)", font_size=18).next_to(ORIGIN, DOWN, buff=0.6)
            )
            examples.arrange(DOWN, buff=0.2)
            examples.move_to(DOWN * 1.5)
            self.play(Write(examples))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def visualize_wave_functions(self):
        """Visualize different wave functions"""
        with self.voiceover(text="Let's visualize some wave functions for different quantum states. For a particle in a one-dimensional box, the wave functions are standing waves. The ground state, or lowest energy state, has no nodes inside the box. Higher energy states have more nodes - points where the wave function crosses zero.") as tracker:
            heading = Text("Wave Function Visualization", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            # Create axes for wave function
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=9,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.0)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.4)
            y_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.6)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            
            # Ground state (n=1)
            n1_wave = axes.plot(
                lambda x: np.sqrt(2/8) * np.sin(np.pi * (x + 4) / 8),
                x_range=[-4, 4],
                color=GREEN
            )
            n1_label = MathTex(r"n=1: \psi_1(x)", color=GREEN).scale(0.8)
            n1_label.next_to(axes, RIGHT, buff=0.6).shift(UP * 1.5)
            
            self.play(Create(n1_wave), Write(n1_label))
            
        with self.voiceover(text="Here we see the second and third excited states. Notice how the number of nodes increases with the quantum number n. Each node represents a point where the probability of finding the particle is exactly zero. The energy also increases with n squared, showing that higher states require more energy.") as tracker:
            # Second excited state (n=2)
            n2_wave = axes.plot(
                lambda x: np.sqrt(2/8) * np.sin(2 * np.pi * (x + 4) / 8),
                x_range=[-4, 4],
                color=YELLOW
            )
            n2_label = MathTex(r"n=2: \psi_2(x)", color=YELLOW).scale(0.8)
            # Auto-fix: Increased spacing to 0.6

            n2_label.next_to(n1_label, DOWN, buff=0.6)
            
            self.play(Transform(n1_wave, n2_wave), Transform(n1_label, n2_label))
            
            # Third excited state (n=3)
            n3_wave = axes.plot(
                lambda x: np.sqrt(2/8) * np.sin(3 * np.pi * (x + 4) / 8),
                x_range=[-4, 4],
                color=RED
            )
            n3_label = MathTex(r"n=3: \psi_3(x)", color=RED).scale(0.8)
            # Auto-fix: Increased spacing to 0.6

            n3_label.next_to(n2_label, DOWN, buff=0.6)
            
            self.play(Transform(n1_wave, n3_wave), Transform(n1_label, n3_label))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def probability_density_explanation(self):
        """Explain probability density in detail"""
        with self.voiceover(text="The Born interpretation, proposed by Max Born in nineteen twenty-six, tells us that the square of the wave function's magnitude gives the probability density. This means psi squared tells us the probability per unit length of finding the particle at a given position. This is fundamentally different from classical physics.") as tracker:
            heading = Text("Probability Density", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            born_rule = MathTex(r"P(x) = |\psi(x)|^2").scale(0.9)
            born_rule.move_to(UP * 1.5)
            self.play(Write(born_rule))
            
            meaning = Text("Probability per unit length", font_size=24, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            meaning.next_to(born_rule, DOWN, buff=0.6)
            self.play(Write(meaning))
            
        with self.voiceover(text="Let's compare a wave function with its corresponding probability density. While the wave function oscillates and can be negative, the probability density is always positive and shows where we're most likely to find the particle. The peaks in probability density correspond to the most probable locations.") as tracker:
            # Create two sets of axes
            axes_wave = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.2, 1.2, 0.5],
                x_length=8,
                y_length=3,
                axis_config={"include_tip": True}
            )
            axes_wave.move_to(UP * 0.3)
            
            axes_prob = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 1.5, 0.5],
                x_length=8,
                y_length=3,
                axis_config={"include_tip": True}
            )
            axes_prob.move_to(DOWN * 2.2)
            
            wave_label = axes_wave.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.6)
            prob_label = axes_prob.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.6)
            
            self.play(Create(axes_wave), Write(wave_label))
            self.play(Create(axes_prob), Write(prob_label))
            
            # Plot wave function
            wave = axes_wave.plot(
                lambda x: np.cos(2*x) * np.exp(-x**2/4),
                x_range=[-3, 3],
                color=GREEN
            )
            
            # Plot probability density
            prob = axes_prob.plot(
                lambda x: (np.cos(2*x) * np.exp(-x**2/4))**2,
                x_range=[-3, 3],
                color=RED
            )
            
            self.play(Create(wave))
            self.play(Create(prob))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def harmonic_oscillator_example(self):
        """Detailed example with quantum harmonic oscillator"""
        with self.voiceover(text="One of the most important exactly solvable systems is the quantum harmonic oscillator. This describes particles in a parabolic potential, like atoms in a crystal lattice or vibrating molecules. The potential energy is proportional to x squared, creating a restoring force toward the center.") as tracker:
            heading = Text("Quantum Harmonic Oscillator", font_size=32, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            potential_eq = MathTex(r"V(x) = \frac{1}{2}m\omega^2 x^2").scale(0.9)
            potential_eq.move_to(UP * 1.5)
            self.play(Write(potential_eq))
            
            # Create axes for potential
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 3, 1],
                x_length=8,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.0)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.4)
            v_label = axes.get_y_axis_label("V", direction=LEFT).shift(LEFT * 0.6)
            
            self.play(Create(axes), Write(x_label), Write(v_label))
            
            # Plot parabolic potential
            parabola = axes.plot(
                lambda x: 0.3 * x**2,
                x_range=[-3, 3],
                color=YELLOW
            )
            self.play(Create(parabola))
            
        with self.voiceover(text="The energy levels of the quantum harmonic oscillator are equally spaced, separated by h-bar omega. This is remarkable - unlike classical systems, the quantum oscillator can only have discrete energies. The ground state has energy one-half h-bar omega, not zero. This is called zero-point energy.") as tracker:
            energy_formula = MathTex(r"E_n = \hbar\omega\left(n + \frac{1}{2}\right)").scale(0.85)
            energy_formula.move_to(UP * 1.5)
            self.play(Transform(potential_eq, energy_formula))
            
            # Draw energy levels
            energy_levels = VGroup(*[
                Line(
                    axes.c2p(-2, 0.5 + n*0.5),
                    axes.c2p(2, 0.5 + n*0.5),
                    color=GREEN,
                    stroke_width=2
                )
                for n in range(5)
            ])
            
            level_labels = VGroup(*[
                MathTex(f"n={n}", font_size=20).next_to(
                    axes.c2p(2.2, 0.5 + n*0.5), RIGHT, buff=0.1
                )
                for n in range(5)
            ])
            
            self.play(Create(energy_levels))
            self.play(Write(level_labels))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        """Physical interpretation and measurement"""
        with self.voiceover(text="The measurement problem in quantum mechanics is profound. Before measurement, a particle exists in a superposition of states - it doesn't have a definite position. The wave function describes all possible positions simultaneously. Only when we measure do we get a specific result, and the wave function collapses to that state.") as tracker:
            heading = Text("Measurement and Interpretation", font_size=32, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            superposition = MathTex(r"\psi = c_1\psi_1 + c_2\psi_2 + c_3\psi_3 + ...").scale(0.85)
            superposition.move_to(UP * 1.5)
            self.play(Write(superposition))
            
            description = Text("Superposition of states", font_size=24, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            description.next_to(superposition, DOWN, buff=0.6)
            self.play(Write(description))
            
        with self.voiceover(text="The coefficients c-n are complex numbers whose squared magnitudes give the probability of measuring that particular state. After measurement, the system is in one definite state. This is the famous wave function collapse. The Copenhagen interpretation says the wave function represents our knowledge, not physical reality itself.") as tracker:
            probability = MathTex(r"P_n = |c_n|^2").scale(0.9)
            probability.move_to(ORIGIN)
            self.play(Write(probability))
            
            normalization = MathTex(r"\sum_n |c_n|^2 = 1").scale(0.85)
            normalization.next_to(probability, DOWN, buff=0.6)
            self.play(Write(normalization))
            
            norm_meaning = Text("Total probability = 1", font_size=22, color=GREEN)
            # Auto-fix: Increased spacing to 0.6

            norm_meaning.next_to(normalization, DOWN, buff=0.6)
            self.play(Write(norm_meaning))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def normalization_condition(self):
        """Explain normalization in detail"""
        with self.voiceover(text="For the probability interpretation to be consistent, the wave function must be normalized. This means that if we integrate the probability density over all space, we must get exactly one - the particle must be somewhere. This normalization condition is a fundamental requirement for any valid wave function.") as tracker:
            heading = Text("Normalization Condition", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            norm_integral = MathTex(r"\int_{-\infty}^{\infty} |\psi(x)|^2 dx = 1").scale(0.9)
            norm_integral.move_to(UP * 1.5)
            self.play(Write(norm_integral))
            
            meaning = Text("Particle must exist somewhere", font_size=24, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            meaning.next_to(norm_integral, DOWN, buff=0.6)
            self.play(Write(meaning))
            
        with self.voiceover(text="Let's visualize this with a Gaussian wave packet. The area under the probability density curve equals one. If we make the wave packet narrower, it gets taller to maintain this area. This demonstrates the uncertainty principle - a more localized wave function requires higher momentum components.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 0.8, 0.2],
                x_length=9,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.0)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.4)
            p_label = axes.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.6)
            
            self.play(Create(axes), Write(x_label), Write(p_label))
            
            # Gaussian wave packet
            gaussian = axes.plot(
                lambda x: (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2),
                x_range=[-4, 4],
                color=GREEN
            )
            
            # Fill area under curve
            area = axes.get_area(gaussian, x_range=[-4, 4], color=GREEN, opacity=0.3)
            
            self.play(Create(gaussian))
            self.play(FadeIn(area))
            
            area_label = MathTex(r"\text{Area} = 1", color=WHITE).scale(0.8)
            area_label.next_to(axes, RIGHT, buff=0.6)
            self.play(Write(area_label))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        """Real-world applications"""
        with self.voiceover(text="The Schrödinger equation is not just theoretical - it has countless practical applications. In chemistry, it explains chemical bonding and molecular structure. Computational chemistry uses approximate solutions to predict reaction rates and design new molecules. Without quantum mechanics, we couldn't understand why atoms form molecules at all.") as tracker:
            heading = Text("Applications in Science and Technology", font_size=32, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            app1 = Text("• Atomic and Molecular Structure", font_size=26, color=GREEN)
            app1.move_to(UP * 1.2)
            self.play(Write(app1))
            
            app2 = Text("• Semiconductor Physics", font_size=26, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            app2.next_to(app1, DOWN, buff=0.6)
            self.play(Write(app2))
            
            app3 = Text("• Quantum Computing", font_size=26, color=RED)
            # Auto-fix: Increased spacing to 0.6

            app3.next_to(app2, DOWN, buff=0.6)
            self.play(Write(app3))
            
        with self.voiceover(text="In materials science and engineering, the Schrödinger equation explains semiconductor behavior, which is the foundation of all modern electronics. Transistors, computer chips, solar cells, and LEDs all rely on quantum mechanics. More recently, quantum computing harnesses superposition and entanglement to perform calculations impossible for classical computers.") as tracker:
            app4 = Text("• Nanotechnology", font_size=26, color=PURPLE)
            # Auto-fix: Increased spacing to 0.6

            app4.next_to(app3, DOWN, buff=0.6)
            self.play(Write(app4))
            
            app5 = Text("• Spectroscopy and Imaging", font_size=26, color=ORANGE)
            # Auto-fix: Increased spacing to 0.6

            app5.next_to(app4, DOWN, buff=0.6)
            self.play(Write(app5))
            
            app6 = Text("• Quantum Cryptography", font_size=26, color=TEAL)
            # Auto-fix: Increased spacing to 0.6

            app6.next_to(app5, DOWN, buff=0.6)
            self.play(Write(app6))
            
        # Cleanup
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        """Summary and conclusion"""
        with self.voiceover(text="We've journeyed through the Schrödinger equation, from its historical origins to its mathematical structure and physical meaning. We've seen how wave functions describe quantum states, how probability density tells us where particles are likely to be found, and how the equation applies to real systems like the harmonic oscillator.") as tracker:
            heading = Text("Summary and Conclusion", font_size=36, color=BLUE)
            heading.to_edge(UP, buff=0.8)
            self.play(Write(heading))
            
            equation_final = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi"
            ).scale(0.9)
            equation_final.move_to(UP * 1.0)
            self.play(Write(equation_final))
            
            key1 = Text("• Wave functions encode quantum information", font_size=22, color=GREEN)
            key1.move_to(ORIGIN)
            self.play(Write(key1))
            
            key2 = Text("• Probability density = |ψ|²", font_size=22, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            key2.next_to(key1, DOWN, buff=0.6)
            self.play(Write(key2))
            
            key3 = Text("• Quantized energy levels", font_size=22, color=RED)
            # Auto-fix: Increased spacing to 0.6

            key3.next_to(key2, DOWN, buff=0.6)
            self.play(Write(key3))
            
        with self.voiceover(text="The Schrödinger equation represents one of humanity's greatest intellectual achievements - a mathematical framework that accurately describes the microscopic world. It challenges our classical intuitions but has been verified by countless experiments. As we continue to develop quantum technologies, this equation remains as relevant today as when Schrödinger first wrote it nearly a century ago. Thank you for watching.") as tracker:
            key4 = Text("• Foundation of modern physics and chemistry", font_size=22, color=PURPLE)
            # Auto-fix: Increased spacing to 0.6

            key4.next_to(key3, DOWN, buff=0.6)
            self.play(Write(key4))
            
            thanks = Text("Thank you for watching!", font_size=32, color=GOLD)
            thanks.move_to(DOWN * 2.5)
            self.play(Write(thanks))
            
            self.wait(2)
            
        # Final cleanup
        self.play(FadeOut(*self.mobjects))

    # Helper method for wave packet
    def get_wave_packet(self):
        """Create a wave packet visualization"""
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 1, 0.5],
            x_length=6,
            y_length=2,
            axis_config={"include_tip": False}
        )
        
        wave = axes.plot(
            lambda x: np.exp(-x**2/2) * np.cos(5*x),
            x_range=[-3, 3],
            color=BLUE
        )
        
        return VGroup(axes, wave)

# Instructions to run:
# manim -pql schrodinger_animation.py SchrodingerEquationExplanation