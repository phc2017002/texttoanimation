from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Section 1: Introduction and Historical Context
        self.introduction()
        
        # Section 2: Classical vs Quantum
        self.classical_vs_quantum()
        
        # Section 3: The Wave Function Concept
        self.wave_function_concept()
        
        # Section 4: The Time-Independent Schrödinger Equation
        self.time_independent_equation()
        
        # Section 5: Breaking Down the Equation
        self.equation_breakdown()
        
        # Section 6: Probability Density
        self.probability_density()
        
        # Section 7: Simple Example - Particle in a Box
        self.particle_in_box()
        
        # Section 8: Wave Function Visualization
        self.wave_function_visualization()
        
        # Section 9: Quantum Tunneling
        self.quantum_tunneling()
        
        # Section 10: Physical Interpretation
        self.physical_interpretation()
        
        # Section 11: Applications
        self.applications()
        
        # Section 12: Summary and Conclusion
        self.summary()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. Developed by Austrian physicist Erwin Schrödinger in 1926, this equation revolutionized our understanding of the atomic and subatomic world.") as tracker:
            title = Text("The Schrödinger Equation", font_size=42, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            self.wait(1)
            
            subtitle = Text("A Journey into Quantum Mechanics", font_size=28, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            subtitle.next_to(title, DOWN, buff=0.6)
            self.play(FadeIn(subtitle))
        
        with self.voiceover(text="Before Schrödinger's breakthrough, physicists struggled to explain the wave-particle duality of matter. How could an electron behave both as a particle and a wave? The Schrödinger equation provided the mathematical framework to answer this profound question, forever changing our view of reality at the smallest scales.") as tracker:
            self.wait(2)
            
            # Create Schrödinger portrait placeholder (circle with name)
            portrait = Circle(radius=1.2, color=WHITE)
            portrait.move_to(LEFT * 3 + DOWN * 0.5)
            name = Text("Erwin\nSchrödinger\n1887-1961", font_size=20)
            name.move_to(portrait.get_center())
            
            # Timeline
            timeline = Line(LEFT * 2, RIGHT * 4, color=BLUE)
            timeline.move_to(RIGHT * 1 + DOWN * 0.5)
            
            year_1926 = Text("1926", font_size=24, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            year_1926.next_to(timeline.get_center(), UP, buff=0.6)
            
            achievement = Text("Schrödinger Equation\nPublished", font_size=20)
            # Auto-fix: Increased spacing to 0.6

            achievement.next_to(timeline.get_center(), DOWN, buff=0.6)
            
            self.play(Create(portrait), Write(name))
            self.play(Create(timeline), Write(year_1926), Write(achievement))
        
        self.play(FadeOut(*self.mobjects))

    def classical_vs_quantum(self):
        with self.voiceover(text="To appreciate the revolutionary nature of quantum mechanics, we must first understand how it differs from classical physics. In classical mechanics, a particle has a definite position and momentum at any given time. We can predict its trajectory with absolute certainty using Newton's laws.") as tracker:
            title = Text("Classical vs Quantum Physics", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # Classical side
            classical_label = Text("Classical Mechanics", font_size=28, color=GREEN)
            classical_label.move_to(LEFT * 3.5 + UP * 1.5)
            
            particle = Dot(color=RED, radius=0.15)
            particle.move_to(LEFT * 5 + DOWN * 0.5)
            
            path = Line(LEFT * 5 + DOWN * 0.5, LEFT * 2 + DOWN * 0.5, color=YELLOW)
            
            classical_text = Text("Definite trajectory\nExact position & momentum", font_size=18)
            classical_text.move_to(LEFT * 3.5 + DOWN * 2)
            
            self.play(Write(classical_label))
            self.play(Create(particle))
            self.play(MoveAlongPath(particle, path), Create(path), run_time=2)
            self.play(Write(classical_text))
        
        with self.voiceover(text="Quantum mechanics tells a very different story. At the quantum scale, we cannot know both position and momentum precisely at the same time. This is not due to experimental limitations, but a fundamental property of nature itself, described by Heisenberg's uncertainty principle. Instead of definite trajectories, we have probability waves.") as tracker:
            # Quantum side
            quantum_label = Text("Quantum Mechanics", font_size=28, color=PURPLE)
            quantum_label.move_to(RIGHT * 3.5 + UP * 1.5)
            
            # Create wave function visualization
            axes_small = Axes(
                x_range=[-1, 3, 1],
                y_range=[-1, 1, 0.5],
                x_length=3.5,
                y_length=2,
                axis_config={"include_tip": False, "stroke_width": 1}
            )
            axes_small.move_to(RIGHT * 3.5 + DOWN * 0.5)
            
            wave = axes_small.plot(lambda x: 0.6 * np.sin(3 * x) * np.exp(-0.3 * x), color=BLUE)
            
            quantum_text = Text("Probability wave\nUncertainty principle", font_size=18)
            quantum_text.move_to(RIGHT * 3.5 + DOWN * 2)
            
            self.play(Write(quantum_label))
            self.play(Create(axes_small), Create(wave))
            self.play(Write(quantum_text))
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_concept(self):
        with self.voiceover(text="At the heart of quantum mechanics lies the wave function, typically denoted by the Greek letter psi. The wave function is a mathematical description of a quantum system. It contains all the information we can possibly know about a particle or system of particles.") as tracker:
            title = Text("The Wave Function ψ", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # Large psi symbol
            psi = MathTex(r"\psi(x, t)", font_size=80, color=YELLOW)
            psi.move_to(UP * 0.5)
            self.play(Write(psi))
            
            # Description
            description = Text("Contains all quantum information", font_size=24)
            description.move_to(DOWN * 1.2)
            self.play(FadeIn(description))
        
        with self.voiceover(text="The wave function is generally a complex-valued function that depends on position and time. By itself, the wave function doesn't represent something we can directly measure. It's a mathematical tool, an abstract object that lives in a complex mathematical space. However, from the wave function, we can extract all measurable properties of the system.") as tracker:
            self.play(FadeOut(description))
            
            # Properties we can extract
            properties = VGroup(
                Text("• Energy levels", font_size=22),
                Text("• Momentum distribution", font_size=22),
                Text("• Position probability", font_size=22),
                Text("• Observable quantities", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            properties.move_to(DOWN * 1)
            
            self.play(Write(properties), run_time=3)
        
        with self.voiceover(text="One crucial property of the wave function is that it must be normalized. This means the total probability of finding the particle somewhere in all of space must equal one. The particle must exist somewhere! This mathematical requirement ensures physical consistency.") as tracker:
            self.play(FadeOut(properties))
            
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x, t)|^2 \, dx = 1",
                font_size=36
            )
            normalization.move_to(DOWN * 0.8)
            
            norm_label = Text("Normalization Condition", font_size=24, color=GREEN)
            # Auto-fix: Increased spacing to 0.6

            norm_label.next_to(normalization, DOWN, buff=0.6)
            
            self.play(Write(normalization))
            self.play(FadeIn(norm_label))
        
        self.play(FadeOut(*self.mobjects))

    def time_independent_equation(self):
        with self.voiceover(text="Now we arrive at the famous time-independent Schrödinger equation. This form of the equation is used when we're interested in stationary states, where the energy of the system doesn't change with time. It's an eigenvalue equation that determines the allowed energy levels of a quantum system.") as tracker:
            title = Text("Time-Independent Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # The main equation
            equation = MathTex(
                r"\hat{H}\psi = E\psi",
                font_size=48
            )
            equation.move_to(UP * 1.2)
            self.play(Write(equation))
            
            # Expanded form
            expanded = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi",
                font_size=38
            )
            expanded.move_to(DOWN * 0.3)
            
            self.wait(1)
            self.play(Write(expanded))
        
        with self.voiceover(text="Let me break down what each symbol means. The operator H-hat is the Hamiltonian, which represents the total energy of the system. Psi is our wave function. E is the energy eigenvalue, one of the allowed energy levels. H-bar is the reduced Planck constant, m is the particle's mass, and V of x is the potential energy function.") as tracker:
            # Labels for each term
            labels = VGroup(
                MathTex(r"\hat{H}: \text{ Hamiltonian (total energy)}", font_size=22),
                MathTex(r"\psi: \text{ Wave function}", font_size=22),
                MathTex(r"E: \text{ Energy eigenvalue}", font_size=22),
                MathTex(r"\hbar: \text{ Reduced Planck constant}", font_size=22),
                MathTex(r"m: \text{ Particle mass}", font_size=22),
                MathTex(r"V(x): \text{ Potential energy}", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            labels.move_to(DOWN * 2.2)
            labels.scale(0.9)
            
            self.play(Write(labels), run_time=4)
        
        self.play(FadeOut(*self.mobjects))

    def equation_breakdown(self):
        with self.voiceover(text="Let's examine each term of the Schrödinger equation in detail. The equation consists of two main parts: the kinetic energy term and the potential energy term. Together, they form the Hamiltonian operator, which acts on the wave function to give us the total energy.") as tracker:
            title = Text("Breaking Down the Equation", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            full_eq = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi",
                font_size=36
            )
            full_eq.move_to(UP * 1.8)
            self.play(Write(full_eq))
        
        with self.voiceover(text="The first term, negative h-bar squared over two m times the second derivative of psi, represents the kinetic energy operator. The second derivative tells us how much the wave function is curving. High curvature means high kinetic energy. This makes intuitive sense: a rapidly oscillating wave has higher momentum and thus higher kinetic energy.") as tracker:
            # Highlight kinetic energy term
            # kinetic_box = SurroundingRectangle(full_eq[0][0:12], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            kinetic_label = Text("Kinetic Energy", font_size=26, color=GREEN)
            # kinetic_label.next_to(kinetic_box, DOWN, buff=0.6)  # Auto-disabled: uses disabled SurroundingRectangle
            
            kinetic_formula = MathTex(
                r"\hat{T} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}",
                font_size=32
            )
            # Auto-fix: Increased spacing to 0.6

            kinetic_formula.next_to(kinetic_label, DOWN, buff=0.6)
            
            explanation = Text("Curvature → Kinetic Energy", font_size=22)
            # Auto-fix: Increased spacing to 0.6

            explanation.next_to(kinetic_formula, DOWN, buff=0.6)
            
            # self.play(Create(kinetic_box))  # Auto-disabled: uses disabled SurroundingRectangle
            self.play(Write(kinetic_label))
            self.play(Write(kinetic_formula))
            self.play(FadeIn(explanation))
        
        with self.voiceover(text="The second term, V of x times psi, represents the potential energy. This depends on where the particle is located. Different positions in space may have different potential energies. For example, an electron near a positively charged nucleus has lower potential energy than one far away. The potential energy function shapes the allowed wave functions and energy levels.") as tracker:
            self.play(FadeOut(kinetic_label), FadeOut(kinetic_formula), FadeOut(explanation))
            
            # Highlight potential energy term
            # potential_box = SurroundingRectangle(full_eq[0][13:19], color=YELLOW, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            potential_label = Text("Potential Energy", font_size=26, color=YELLOW)
            # potential_label.next_to(potential_box, DOWN, buff=0.6)  # Auto-disabled: uses disabled SurroundingRectangle
            
            potential_formula = MathTex(
                r"\hat{V} = V(x)",
                font_size=32
            )
            # Auto-fix: Increased spacing to 0.6

            potential_formula.next_to(potential_label, DOWN, buff=0.6)
            
            pot_explanation = Text("Position-dependent energy", font_size=22)
            # Auto-fix: Increased spacing to 0.6

            pot_explanation.next_to(potential_formula, DOWN, buff=0.6)
            
            # self.play(Create(potential_box))  # Auto-disabled: uses disabled SurroundingRectangle
            self.play(Write(potential_label))
            self.play(Write(potential_formula))
            self.play(FadeIn(pot_explanation))
        
        with self.voiceover(text="On the right side of the equation, we have E times psi, where E is the total energy eigenvalue. This equation is telling us that when the Hamiltonian operator acts on psi, we get back psi multiplied by a constant, E. This is what makes psi an eigenfunction and E an eigenvalue. Only certain special functions psi and certain special energies E will satisfy this equation.") as tracker:
            # self.play(FadeOut(potential_box), FadeOut(potential_label),  # Auto-disabled: uses disabled SurroundingRectangle
                     FadeOut(potential_formula), FadeOut(pot_explanation))
            
            # Highlight energy term
            # energy_box = SurroundingRectangle(full_eq[0][21:24], color=RED, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            energy_label = Text("Total Energy", font_size=26, color=RED)
            # energy_label.next_to(energy_box, DOWN, buff=0.6)  # Auto-disabled: uses disabled SurroundingRectangle
            
            eigenvalue_note = Text("Eigenvalue equation:\nOnly discrete energies allowed", 
                                  font_size=22, line_spacing=1.2)
            # Auto-fix: Increased spacing to 0.6

            eigenvalue_note.next_to(energy_label, DOWN, buff=0.6)
            
            # self.play(Create(energy_box))  # Auto-disabled: uses disabled SurroundingRectangle
            self.play(Write(energy_label))
            self.play(FadeIn(eigenvalue_note))
        
        self.play(FadeOut(*self.mobjects))

    def probability_density(self):
        with self.voiceover(text="Now we come to one of the most important concepts in quantum mechanics: the probability density. While the wave function psi itself is complex and not directly measurable, the square of its magnitude gives us the probability density. This tells us where we're likely to find the particle if we make a measurement.") as tracker:
            title = Text("Probability Density", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # Main formula
            prob_formula = MathTex(
                r"P(x) = |\psi(x)|^2 = \psi^*(x)\psi(x)",
                font_size=40
            )
            prob_formula.move_to(UP * 1.5)
            self.play(Write(prob_formula))
            
            interpretation = Text("Probability per unit length", font_size=26)
            # Auto-fix: Increased spacing to 0.6

            interpretation.next_to(prob_formula, DOWN, buff=0.6)
            self.play(FadeIn(interpretation))
        
        with self.voiceover(text="Let's visualize this concept with a graph. The blue curve represents a wave function, which can have both positive and negative values, and is generally complex. The red curve shows the probability density, which is always positive or zero. Notice how the probability density peaks where the wave function has the largest magnitude. These peaks tell us where the particle is most likely to be found.") as tracker:
            self.play(FadeOut(interpretation))
            
            # Create side-by-side plots
            axes_psi = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.2, 1.2, 0.5],
                x_length=6,
                y_length=3.5,
                axis_config={"include_tip": True, "stroke_width": 2}
            )
            axes_psi.move_to(DOWN * 1.5)
            
            # Wave function
            wave_func = axes_psi.plot(
                lambda x: 0.8 * np.sin(2 * x) * np.exp(-0.2 * x**2),
                color=BLUE,
                stroke_width=3
            )
            
            # Probability density
            prob_density = axes_psi.plot(
                lambda x: (0.8 * np.sin(2 * x) * np.exp(-0.2 * x**2))**2,
                color=RED,
                stroke_width=3
            )
            
            # Labels
            x_label = axes_psi.get_x_axis_label("x").shift(DOWN * 0.4)
            
            psi_label = MathTex(r"\psi(x)", color=BLUE, font_size=28)
            # Auto-fix: Increased spacing to 0.6

            psi_label.next_to(axes_psi, LEFT, buff=0.6).shift(UP * 0.5)
            
            prob_label = MathTex(r"|\psi|^2", color=RED, font_size=28)
            # Auto-fix: Increased spacing to 0.6

            prob_label.next_to(psi_label, DOWN, buff=0.6)
            
            self.play(Create(axes_psi), Write(x_label))
            self.play(Create(wave_func), Write(psi_label))
            self.play(Create(prob_density), Write(prob_label))
        
        with self.voiceover(text="The Born interpretation, proposed by Max Born in 1926, states that the probability of finding a particle in a small region between x and x plus delta x is given by psi squared times delta x. If we integrate this over any region, we get the total probability of finding the particle in that region. This probabilistic interpretation was revolutionary and remains one of the most debated aspects of quantum mechanics.") as tracker:
            # Show integration for probability in region
            born_rule = MathTex(
                r"P(a \leq x \leq b) = \int_a^b |\psi(x)|^2 \, dx",
                font_size=32
            )
            born_rule.to_edge(RIGHT, buff=0.6).shift(UP * 0.5)
            
            born_label = Text("Born Rule", font_size=24, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            born_label.next_to(born_rule, UP, buff=0.6)
            
            self.play(Write(born_label))
            self.play(Write(born_rule))
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box(self):
        with self.voiceover(text="To make these abstract concepts concrete, let's examine the simplest quantum mechanical system: a particle confined to a one-dimensional box. Imagine a particle that can move freely between two walls at x equals zero and x equals L, but cannot escape. This is called the infinite square well or particle in a box.") as tracker:
            title = Text("Particle in a Box", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
            
            # Draw the box
            box_bottom = Line(LEFT * 3, RIGHT * 3, color=WHITE, stroke_width=3)
            box_bottom.move_to(DOWN * 0.5)
            
            left_wall = Line(DOWN * 1.5, UP * 1.5, color=WHITE, stroke_width=6)
            left_wall.move_to(LEFT * 3 + DOWN * 0.5)
            
            right_wall = Line(DOWN * 1.5, UP * 1.5, color=WHITE, stroke_width=6)
            right_wall.move_to(RIGHT * 3 + DOWN * 0.5)
            
            # Labels
            x_zero = MathTex("x=0", font_size=24)
            # Auto-fix: Increased spacing to 0.6

            x_zero.next_to(left_wall, DOWN, buff=0.6)
            
            x_L = MathTex("x=L", font_size=24)
            # Auto-fix: Increased spacing to 0.6

            x_L.next_to(right_wall, DOWN, buff=0.6)
            
            particle_dot = Dot(color=YELLOW, radius=0.12)
            particle_dot.move_to(DOWN * 0.5)
            
            self.play(Create(box_bottom), Create(left_wall), Create(right_wall))
            self.play(Write(x_zero), Write(x_L))
            self.play(Create(particle_dot))
        
        with self.voiceover(text="Inside the box, the potential energy is zero, so the particle moves freely. At the walls and outside, the potential is infinite, which means the particle cannot exist there. This gives us our boundary conditions: the wave function must be zero at the walls. Solving the Schrödinger equation with these boundary conditions gives us the allowed wave functions and energy levels.") as tracker:
            # Potential energy diagram
            potential = MathTex(
                r"V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & \text{otherwise} \end{cases}",
                font_size=30
            )
            potential.to_edge(RIGHT, buff=0.6).shift(UP * 1)
            
            boundary = Text("Boundary: ψ(0) = ψ(L) = 0", font_size=22)
            # Auto-fix: Increased spacing to 0.6

            boundary.next_to(potential, DOWN, buff=0.6)
            
            self.play(Write(potential))
            self.play(FadeIn(boundary))
        
        with self.voiceover(text="The solutions are standing waves, similar to waves on a vibrating string. The allowed wave functions are sine waves that fit exactly into the box. The quantum number n tells us how many half-wavelengths fit in the box. n equals one is the ground state, n equals two is the first excited state, and so on. Each state has a specific energy proportional to n squared.") as tracker:
            self.play(FadeOut(particle_dot), FadeOut(potential), FadeOut(boundary))
            
            # Show the first three wave functions
            solutions = MathTex(
                r"\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)",
                font_size=28
            )
            solutions.to_edge(RIGHT, buff=0.6).shift(UP * 1.2)
            
            energy_formula = MathTex(
                r"E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}",
                font_size=28
            )
            # Auto-fix: Increased spacing to 0.6

            energy_formula.next_to(solutions, DOWN, buff=0.6)
            
            self.play(Write(solutions))
            self.play(Write(energy_formula))
            
            # Draw n=1 state
            n1_wave = FunctionGraph(
                lambda x: 0.6 * np.sin(np.pi * (x + 3) / 6),
                x_range=[-3, 3],
                color=BLUE
            )
            n1_wave.move_to(DOWN * 0.5)
            
            n1_label = MathTex("n=1", font_size=24, color=BLUE)
            # Auto-fix: Increased spacing to 0.6

            n1_label.next_to(left_wall, UP, buff=0.6)
            
            self.play(Create(n1_wave), Write(n1_label))
        
        with self.voiceover(text="Notice that the energy is quantized. The particle can only have discrete energy values, not any continuous value. This quantization emerges naturally from the boundary conditions and the wave nature of matter. The energy increases as n squared, so higher excited states are much more energetic. This simple system captures the essence of quantum mechanics: wave-like behavior, discrete energy levels, and probability distributions.") as tracker:
            # Show n=2 state
            n2_wave = FunctionGraph(
                lambda x: 0.6 * np.sin(2 * np.pi * (x + 3) / 6),
                x_range=[-3, 3],
                color=GREEN
            )
            n2_wave.move_to(DOWN * 0.5)
            
            n2_label = MathTex("n=2", font_size=24, color=GREEN)
            n2_label.move_to(n1_label.get_center())
            
            self.play(Transform(n1_wave, n2_wave), Transform(n1_label, n2_label))
            
            # Show n=3 state
            n3_wave = FunctionGraph(
                lambda x: 0.6 * np.sin(3 * np.pi * (x + 3) / 6),
                x_range=[-3, 3],
                color=RED
            )
            n3_wave.move_to(DOWN * 0.5)
            
            n3_label = MathTex("n=3", font_size=24, color=RED)
            n3_label.move_to(n1_label.get_center())
            
            self.play(Transform(n1_wave, n3_wave), Transform(n1_label, n3_label))
        
        self.play(FadeOut(*self.mobjects))

    def wave_function_visualization(self):
        with self.voiceover(text="Let's create a detailed visualization of how wave functions and probability densities look for different quantum states. Understanding these shapes is crucial for developing quantum intuition. Each energy level has a characteristic pattern that tells us about the particle's behavior.") as tracker:
            title = Text("Wave Function Shapes", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
        
        with self.voiceover(text="For the ground state, n equals one, we have a single smooth hump. The probability density is highest at the center of the box. This means if we measure the particle's position, we're most likely to find it near the middle. Notice there are no nodes, or zero-crossing points, inside the box. The number of nodes increases with the quantum number.") as tracker:
            # Ground state visualization
            axes = Axes(
                x_range=[-0.5, 5.5, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=9,
                y_length=4.5,
                axis_config={"include_tip": True, "stroke_width": 2}
            )
            axes.move_to(DOWN * 1.2)
            
            ground_state = axes.plot(
                lambda x: np.sqrt(2/5) * np.sin(np.pi * x / 5) if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=BLUE,
                stroke_width=3
            )
            
            ground_prob = axes.plot(
                lambda x: (np.sqrt(2/5) * np.sin(np.pi * x / 5))**2 if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=RED,
                stroke_width=3
            )
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.4)
            
            state_label = MathTex(r"n=1 \text{ (ground state)}", font_size=28)
            state_label.to_edge(LEFT, buff=0.6).shift(UP * 0.8)
            
            psi_legend = MathTex(r"\psi(x)", color=BLUE, font_size=24)
            # Auto-fix: Increased spacing to 0.6

            psi_legend.next_to(state_label, DOWN, buff=0.6)
            
            prob_legend = MathTex(r"|\psi|^2", color=RED, font_size=24)
            # Auto-fix: Increased spacing to 0.6

            prob_legend.next_to(psi_legend, DOWN, buff=0.6)
            
            self.play(Create(axes), Write(x_label))
            self.play(Write(state_label))
            self.play(Create(ground_state), Write(psi_legend))
            self.play(Create(ground_prob), Write(prob_legend))
        
        with self.voiceover(text="For the first excited state, n equals two, the wave function has one node at the center. The probability density now has two peaks, one on each side of the box. Interestingly, there's zero probability of finding the particle at the exact center! This is a purely quantum phenomenon with no classical analog. The particle can be on the left or right, but never in the middle.") as tracker:
            # First excited state
            first_excited = axes.plot(
                lambda x: np.sqrt(2/5) * np.sin(2 * np.pi * x / 5) if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=BLUE,
                stroke_width=3
            )
            
            first_prob = axes.plot(
                lambda x: (np.sqrt(2/5) * np.sin(2 * np.pi * x / 5))**2 if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=RED,
                stroke_width=3
            )
            
            new_label = MathTex(r"n=2 \text{ (1st excited)}", font_size=28)
            new_label.move_to(state_label.get_center())
            
            # Highlight the node
            node_arrow = Arrow(UP * 0.3, DOWN * 0.8, color=YELLOW, buff=0.1)
            node_arrow.move_to(axes.c2p(2.5, 0))
            node_text = Text("Node", font_size=20, color=YELLOW)
            # Auto-fix: Increased spacing to 0.6

            node_text.next_to(node_arrow, UP, buff=0.6)
            
            self.play(
                Transform(ground_state, first_excited),
                Transform(ground_prob, first_prob),
                Transform(state_label, new_label)
            )
            self.play(Create(node_arrow), Write(node_text))
        
        with self.voiceover(text="As we go to higher energy states, the number of nodes increases. For n equals three, we have two nodes, dividing the box into three regions. The wave function oscillates more rapidly, reflecting the higher kinetic energy. Each additional node represents a higher energy state. This pattern continues for all excited states, creating increasingly complex probability distributions.") as tracker:
            # Second excited state
            second_excited = axes.plot(
                lambda x: np.sqrt(2/5) * np.sin(3 * np.pi * x / 5) if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=BLUE,
                stroke_width=3
            )
            
            second_prob = axes.plot(
                lambda x: (np.sqrt(2/5) * np.sin(3 * np.pi * x / 5))**2 if 0 < x < 5 else 0,
                x_range=[0, 5],
                color=RED,
                stroke_width=3
            )
            
            third_label = MathTex(r"n=3 \text{ (2nd excited)}", font_size=28)
            third_label.move_to(state_label.get_center())
            
            self.play(FadeOut(node_arrow), FadeOut(node_text))
            self.play(
                Transform(ground_state, second_excited),
                Transform(ground_prob, second_prob),
                Transform(state_label, third_label)
            )
        
        self.play(FadeOut(*self.mobjects))

    def quantum_tunneling(self):
        with self.voiceover(text="One of the most remarkable predictions of quantum mechanics is quantum tunneling. This phenomenon allows particles to pass through energy barriers that would be completely impossible to cross according to classical physics. Tunneling is responsible for many important processes, from nuclear fusion in stars to the operation of modern electronics.") as tracker:
            title = Text("Quantum Tunneling", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
        
        with self.voiceover(text="Imagine a particle approaching a potential energy barrier. In classical mechanics, if the particle's energy is less than the barrier height, it will simply bounce back. It doesn't have enough energy to climb over the barrier. However, in quantum mechanics, there's a non-zero probability that the particle can appear on the other side of the barrier, as if it tunneled through!") as tracker:
            # Create potential barrier diagram
            axes = Axes(
                x_range=[-3, 7, 1],
                y_range=[0, 3, 1],
                x_length=9,
                y_length=4,
                axis_config={"include_tip": True, "stroke_width": 2}
            )
            axes.move_to(DOWN * 1.3)
            
            # Potential barrier (rectangular)
            barrier_left = Line(axes.c2p(2, 0), axes.c2p(2, 2.5), color=WHITE, stroke_width=4)
            barrier_top = Line(axes.c2p(2, 2.5), axes.c2p(4, 2.5), color=WHITE, stroke_width=4)
            barrier_right = Line(axes.c2p(4, 2.5), axes.c2p(4, 0), color=WHITE, stroke_width=4)
            
            # Energy level
            energy_line = DashedLine(axes.c2p(-3, 1.5), axes.c2p(7, 1.5), color=YELLOW, stroke_width=2)
            energy_label = MathTex("E", color=YELLOW, font_size=24)
            # Auto-fix: Increased spacing to 0.6

            energy_label.next_to(energy_line, RIGHT, buff=0.6)
            
            # Barrier label
            barrier_label = MathTex("V_0", font_size=24)
            # Auto-fix: Increased spacing to 0.6

            barrier_label.next_to(barrier_top, UP, buff=0.6)
            
            x_label = axes.get_x_axis_label("x").shift(DOWN * 0.4)
            y_label = axes.get_y_axis_label("V", direction=LEFT).shift(LEFT * 0.6)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(barrier_left), Create(barrier_top), Create(barrier_right))
            self.play(Write(barrier_label))
            self.play(Create(energy_line), Write(energy_label))
        
        with self.voiceover(text="The wave function behaves very differently from a classical particle. Before the barrier, the wave is oscillating, representing the incoming particle. Inside the barrier, where the energy is less than the potential, the wave function decays exponentially but doesn't immediately go to zero. After the barrier, if it's not too thick, the wave function can resume oscillating, representing the transmitted particle. The probability of tunneling depends exponentially on the barrier width and height.") as tracker:
            # Draw wave function
            incident_wave = axes.plot(
                lambda x: 0.8 * np.cos(3 * x) if x < 2 else 0,
                x_range=[-3, 2],
                color=BLUE,
                stroke_width=3
            )
            
            barrier_wave = axes.plot(
                lambda x: 0.8 * np.exp(-1.5 * (x - 2)) if 2 <= x <= 4 else 0,
                x_range=[2, 4],
                color=BLUE,
                stroke_width=3
            )
            
            transmitted_wave = axes.plot(
                lambda x: 0.3 * np.cos(3 * x) if x > 4 else 0,
                x_range=[4, 7],
                color=BLUE,
                stroke_width=3
            )
            
            wave_label = MathTex(r"\psi(x)", color=BLUE, font_size=24)
            # Auto-fix: Increased spacing to 0.6

            wave_label.next_to(axes, LEFT, buff=0.6).shift(DOWN * 0.8)
            
            self.play(Create(incident_wave))
            self.play(Create(barrier_wave))
            self.play(Create(transmitted_wave), Write(wave_label))
        
        with self.voiceover(text="The tunneling probability is given by an exponential factor involving the barrier width, the barrier height, and the particle's mass. Wider and taller barriers suppress tunneling, while lighter particles tunnel more easily. This is why tunneling is more significant for electrons than for larger particles. Quantum tunneling enables phenomena like alpha decay in radioactive nuclei and is essential for the functioning of tunnel diodes and scanning tunneling microscopes.") as tracker:
            # Tunneling probability formula
            tunneling_formula = MathTex(
                r"T \approx e^{-2\kappa a}",
                font_size=32
            )
            tunneling_formula.to_edge(RIGHT, buff=0.6).shift(UP * 1.5)
            
            kappa_def = MathTex(
                r"\kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}",
                font_size=26
            )
            # Auto-fix: Increased spacing to 0.6

            kappa_def.next_to(tunneling_formula, DOWN, buff=0.6)
            
            width_label = Text("a = barrier width", font_size=20)
            # Auto-fix: Increased spacing to 0.6

            width_label.next_to(kappa_def, DOWN, buff=0.6)
            
            self.play(Write(tunneling_formula))
            self.play(Write(kappa_def))
            self.play(FadeIn(width_label))
        
        self.play(FadeOut(*self.mobjects))

    def physical_interpretation(self):
        with self.voiceover(text="The physical interpretation of quantum mechanics has been debated since its inception. What does the wave function really represent? Is it a physical wave spreading through space, or merely a mathematical tool for calculating probabilities? These questions touch on the deepest mysteries of quantum theory.") as tracker:
            title = Text("Physical Interpretation", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
        
        with self.voiceover(text="The Copenhagen interpretation, developed primarily by Niels Bohr and Werner Heisenberg, is the most widely taught view. It states that the wave function represents our knowledge about the system. Before measurement, the particle doesn't have a definite position. It exists in a superposition of all possible positions. The act of measurement causes the wave function to collapse to a single outcome. This collapse is instantaneous and fundamentally random.") as tracker:
            copenhagen = Text("Copenhagen Interpretation", font_size=30, color=YELLOW)
            copenhagen.move_to(UP * 1.8)
            self.play(Write(copenhagen))
            
            points = VGroup(
                Text("• Wave function = knowledge/information", font_size=22),
                Text("• Superposition before measurement", font_size=22),
                Text("• Collapse upon observation", font_size=22),
                Text("• Fundamental randomness", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            points.move_to(UP * 0.3)
            
            self.play(Write(points), run_time=3)
        
        with self.voiceover(text="Many physicists find the idea of wave function collapse unsatisfying. Alternative interpretations have been proposed. The Many Worlds interpretation suggests that all possible outcomes actually occur, but in different branches of reality. When we measure a particle's position, the universe splits into multiple versions, one for each possible outcome. There's no collapse, just branching.") as tracker:
            self.play(FadeOut(copenhagen), FadeOut(points))
            
            many_worlds = Text("Many Worlds Interpretation", font_size=30, color=GREEN)
            many_worlds.move_to(UP * 1.8)
            self.play(Write(many_worlds))
            
            mw_points = VGroup(
                Text("• All outcomes occur in parallel", font_size=22),
                Text("• Universe branches at each measurement", font_size=22),
                Text("• No wave function collapse", font_size=22),
                Text("• Deterministic but untestable", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            mw_points.move_to(UP * 0.3)
            
            self.play(Write(mw_points), run_time=3)
        
        with self.voiceover(text="Other interpretations include pilot wave theory, which treats particles as real objects guided by a real wave field, and quantum Bayesianism, which views quantum mechanics as a tool for updating beliefs. Despite these philosophical differences, all interpretations make the same experimental predictions. The mathematics of the Schrödinger equation works perfectly regardless of how we interpret it. Science progresses even when we don't fully understand what our equations mean.") as tracker:
            self.play(FadeOut(many_worlds), FadeOut(mw_points))
            
            other = Text("Other Interpretations", font_size=30, color=PURPLE)
            other.move_to(UP * 1.8)
            self.play(Write(other))
            
            other_points = VGroup(
                Text("• Pilot Wave (de Broglie-Bohm)", font_size=22),
                Text("• Quantum Bayesianism (QBism)", font_size=22),
                Text("• Consistent Histories", font_size=22),
                Text("• Objective Collapse Theories", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            other_points.move_to(UP * 0.3)
            
            self.play(Write(other_points), run_time=2)
            
            key_point = Text("All make identical predictions!", font_size=26, color=YELLOW)
            key_point.move_to(DOWN * 1.8)
            self.play(FadeIn(key_point))
        
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        with self.voiceover(text="The Schrödinger equation is not just an abstract mathematical curiosity. It forms the foundation for understanding and predicting the behavior of atoms, molecules, and materials. Every modern technology involving electronics, chemistry, or materials science relies on quantum mechanics in some way.") as tracker:
            title = Text("Applications of Quantum Mechanics", font_size=38, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
        
        with self.voiceover(text="In chemistry, the Schrödinger equation explains chemical bonding and molecular structure. When atoms come together to form molecules, their electrons occupy molecular orbitals described by solutions to the multi-electron Schrödinger equation. Computational chemistry uses approximate solutions to predict reaction rates, molecular shapes, and material properties. Modern drug design relies heavily on these quantum mechanical calculations.") as tracker:
            chemistry_title = Text("Chemistry & Materials", font_size=28, color=GREEN)
            chemistry_title.move_to(UP * 1.6)
            self.play(Write(chemistry_title))
            
            chem_apps = VGroup(
                Text("• Chemical bonding and reactions", font_size=22),
                Text("• Molecular orbital theory", font_size=22),
                Text("• Spectroscopy and molecular structure", font_size=22),
                Text("• Drug design and materials discovery", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            chem_apps.move_to(LEFT * 2 + UP * 0.2)
            
            # Simple molecular orbital illustration
            orbital = Circle(radius=0.8, color=BLUE, fill_opacity=0.3)
            orbital.move_to(RIGHT * 3.5 + UP * 0.2)
            orbital_label = Text("Molecular\nOrbital", font_size=18)
            # Auto-fix: Increased spacing to 0.6

            orbital_label.next_to(orbital, DOWN, buff=0.6)
            
            self.play(Write(chem_apps))
            self.play(Create(orbital), FadeIn(orbital_label))
        
        with self.voiceover(text="In semiconductor physics, the band structure of materials emerges from solving the Schrödinger equation for electrons in a periodic crystal lattice. This understanding enabled the development of transistors, integrated circuits, and all of modern computing. Quantum mechanics also explains tunneling in flash memory, the photoelectric effect in solar cells, and the behavior of LEDs and lasers.") as tracker:
            self.play(FadeOut(chemistry_title), FadeOut(chem_apps), 
                     FadeOut(orbital), FadeOut(orbital_label))
            
            electronics_title = Text("Electronics & Computing", font_size=28, color=PURPLE)
            electronics_title.move_to(UP * 1.6)
            self.play(Write(electronics_title))
            
            elec_apps = VGroup(
                Text("• Transistors and integrated circuits", font_size=22),
                Text("• Semiconductor devices and LEDs", font_size=22),
                Text("• Lasers and fiber optic communication", font_size=22),
                Text("• Quantum computing and cryptography", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            elec_apps.move_to(LEFT * 2 + UP * 0.2)
            
            # Circuit representation
            chip = Rectangle(width=1.5, height=1.5, color=YELLOW)
            chip.move_to(RIGHT * 3.5 + UP * 0.2)
            chip_label = Text("Quantum\nDevice", font_size=18)
            # Auto-fix: Increased spacing to 0.6

            chip_label.next_to(chip, DOWN, buff=0.6)
            
            self.play(Write(elec_apps))
            self.play(Create(chip), FadeIn(chip_label))
        
        with self.voiceover(text="Looking to the future, quantum technologies promise revolutionary advances. Quantum computers exploit superposition and entanglement to solve certain problems exponentially faster than classical computers. Quantum sensors can measure magnetic fields, gravity, and time with unprecedented precision. Quantum communication offers theoretically unbreakable encryption. All these technologies rely on our ability to control and manipulate systems described by the Schrödinger equation.") as tracker:
            self.play(FadeOut(electronics_title), FadeOut(elec_apps),
                     FadeOut(chip), FadeOut(chip_label))
            
            future_title = Text("Emerging Quantum Technologies", font_size=28, color=RED)
            future_title.move_to(UP * 1.6)
            self.play(Write(future_title))
            
            future_apps = VGroup(
                Text("• Quantum computers (superposition & entanglement)", font_size=22),
                Text("• Quantum sensors (ultra-precise measurements)", font_size=22),
                Text("• Quantum communication (secure encryption)", font_size=22),
                Text("• Quantum simulation (modeling complex systems)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            future_apps.move_to(DOWN * 0.5)
            
            self.play(Write(future_apps), run_time=3)
        
        self.play(FadeOut(*self.mobjects))

    def summary(self):
        with self.voiceover(text="Let's summarize our journey through the Schrödinger equation and quantum mechanics. We've explored one of the most profound equations in all of physics, an equation that reveals the fundamental wave nature of matter and the probabilistic character of reality at the smallest scales.") as tracker:
            title = Text("Summary", font_size=42, color=BLUE)
            title.to_edge(UP, buff=0.8)
            self.play(Write(title))
        
        with self.voiceover(text="We learned that the Schrödinger equation is an eigenvalue equation that determines the allowed quantum states and energy levels of a system. The wave function contains all possible information about a quantum system, though we can only extract probabilities from it. The square of the wave function's magnitude gives us the probability density, telling us where we're likely to find a particle upon measurement.") as tracker:
            # Main equation review
            main_eq = MathTex(
                r"\hat{H}\psi = E\psi",
                font_size=40
            )
            main_eq.move_to(UP * 1.5)
            
            expanded_eq = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi",
                font_size=32
            )
            # Auto-fix: Increased spacing to 0.6

            expanded_eq.next_to(main_eq, DOWN, buff=0.6)
            
            self.play(Write(main_eq))
            self.play(Write(expanded_eq))
        
        with self.voiceover(text="Key concepts include quantization of energy, where only discrete energy levels are allowed in bound systems. Wave-particle duality, where matter exhibits both wave and particle properties. The uncertainty principle, which sets fundamental limits on what we can know. And quantum tunneling, where particles can pass through barriers forbidden by classical physics.") as tracker:
            self.play(FadeOut(main_eq), FadeOut(expanded_eq))
            
            key_concepts = VGroup(
                Text("✓ Quantization of energy", font_size=26, color=YELLOW),
                Text("✓ Wave-particle duality", font_size=26, color=YELLOW),
                Text("✓ Uncertainty principle", font_size=26, color=YELLOW),
                Text("✓ Quantum tunneling", font_size=26, color=YELLOW),
                Text("✓ Probability interpretation", font_size=26, color=YELLOW)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            key_concepts.move_to(UP * 0.5)
            
            self.play(Write(key_concepts), run_time=4)
        
        with self.voiceover(text="The Schrödinger equation has proven to be one of the most successful theories in all of science. It accurately predicts atomic spectra, explains chemical bonding, enables modern electronics, and forms the basis for emerging quantum technologies. Yet deep questions about its interpretation remain. What is the wave function really? Why does measurement seem special? These mysteries continue to fascinate physicists and philosophers alike.") as tracker:
            self.play(FadeOut(key_concepts))
            
            impact = Text("Impact on Science & Technology", font_size=32, color=GREEN)
            impact.move_to(UP * 1.5)
            self.play(Write(impact))
            
            fields = VGroup(
                Text("• Atomic and molecular physics", font_size=22),
                Text("• Chemistry and materials science", font_size=22),
                Text("• Electronics and semiconductor physics", font_size=22),
                Text("• Quantum computing and cryptography", font_size=22),
                Text("• Foundations of physics and philosophy", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
            fields.move_to(DOWN * 0.3)
            
            self.play(Write(fields), run_time=3)
        
        with self.voiceover(text="Thank you for joining me on this exploration of the Schrödinger equation. From wave functions to probability densities, from particles in boxes to quantum tunneling, we've covered the essential ideas that make quantum mechanics both strange and powerful. Keep exploring, keep questioning, and remember that even after a century, quantum mechanics still holds deep mysteries waiting to be understood. The quantum world is endlessly fascinating!") as tracker:
            self.play(FadeOut(impact), FadeOut(fields))
            
            # Final message
            final_message = Text("Thank you for watching!", font_size=36, color=BLUE)
            final_message.move_to(UP * 0.8)
            
            psi_symbol = MathTex(r"\psi", font_size=100, color=YELLOW)
            psi_symbol.move_to(DOWN * 0.8)
            
            self.play(Write(final_message))
            self.play(Write(psi_symbol))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

# Instructions to run:
# 1. Save this file as schrodinger_equation.py
# 2. Make sure you have manim, manim-voiceover, and the ElevenLabs service installed
# 3. Set your ElevenLabs API key as an environment variable: ELEVEN_LABS_API_KEY
# 4. Run: manim -pqh schrodinger_equation.py SchrodingerEquationExplanation
# 5. The animation will render with synchronized voiceover using the Rachel voice
