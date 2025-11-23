from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))

        # Introduction
        self.introduce_topic()
        
        # Part 1: What is the Schrödinger Equation?
        self.what_is_schrodinger_equation()
        
        # Part 2: Wave Functions
        self.explain_wave_functions()
        
        # Part 3: Probability Density
        self.explain_probability_density()
        
        # Part 4: Time-Dependent Schrödinger Equation
        self.time_dependent_schrodinger()
        
        # Part 5: Time-Independent Schrödinger Equation
        self.time_independent_schrodinger()
        
        # Part 6: Particle in a Box Example
        self.particle_in_box()
        
        # Part 7: Quantum Tunneling
        self.quantum_tunneling()
        
        # Part 8: Harmonic Oscillator
        self.harmonic_oscillator()
        
        # Conclusion
        self.conclusion()

    def introduce_topic(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of the Schrödinger equation, one of the most fundamental equations in quantum mechanics.") as tracker:
            title = Text("The Schrödinger Equation", font_size=48, color=BLUE, gradient=(BLUE, PURPLE))
            title.move_to(ORIGIN)
            self.play(Write(title))
            self.wait(1)
        
        with self.voiceover(text="Named after Austrian physicist Erwin Schrödinger, this equation describes how quantum systems evolve over time.") as tracker:
            subtitle = Text("Wave Functions & Probability Density", font_size=32, color=WHITE)
            subtitle.next_to(title, DOWN, buff=0.5)
            self.play(FadeIn(subtitle))
        
        self.play(FadeOut(title), FadeOut(subtitle))

    def what_is_schrodinger_equation(self):
        with self.voiceover(text="Let's begin by understanding what the Schrödinger equation actually is. At its core, it's a differential equation that governs the behavior of quantum particles.") as tracker:
            section_title = Text("What is the Schrödinger Equation?", font_size=36, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The time-dependent Schrödinger equation is written as follows. Here, i is the imaginary unit, h-bar is the reduced Planck's constant, psi is the wave function, and H is the Hamiltonian operator.") as tracker:
            equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi",
                font_size=50
            )
            equation.move_to(ORIGIN)
            self.play(Write(equation))
            self.wait(2)
        
        with self.voiceover(text="Let's break down each component. The left side contains the time derivative of the wave function, multiplied by i times h-bar.") as tracker:
            # left_box = SurroundingRectangle(equation[0][0:7], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            left_label = Text("Time Evolution", font_size=24, color=GREEN)
            left_label.next_to(left_box, LEFT, buff=0.3)
            self.play(Create(left_box), Write(left_label))
            self.wait(1)
        
        with self.voiceover(text="The right side contains the Hamiltonian operator acting on the wave function. The Hamiltonian represents the total energy of the system.") as tracker:
            self.play(FadeOut(left_box), FadeOut(left_label))
            # right_box = SurroundingRectangle(equation[0][8:], color=RED, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            right_label = Text("Energy Operator", font_size=24, color=RED)
            right_label.next_to(right_box, RIGHT, buff=0.3)
            self.play(Create(right_box), Write(right_label))
            self.wait(1)
        
        with self.voiceover(text="The Hamiltonian operator is typically the sum of kinetic and potential energy operators.") as tracker:
            self.play(FadeOut(right_box), FadeOut(right_label))
            hamiltonian = MathTex(
                r"\hat{H} = \hat{T} + \hat{V} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2} + V(x)",
                font_size=40
            )
            hamiltonian.next_to(equation, DOWN, buff=0.8)
            self.play(Write(hamiltonian))
            self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(equation), FadeOut(hamiltonian))

    def explain_wave_functions(self):
        with self.voiceover(text="Now let's dive deep into wave functions, the central concept of quantum mechanics. The wave function, denoted by psi, contains all the information about a quantum system.") as tracker:
            section_title = Text("Wave Functions", font_size=36, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The wave function psi of x and t is generally a complex-valued function. It depends on position x and time t.") as tracker:
            psi_def = MathTex(r"\psi(x,t) \in \mathbb{C}", font_size=45)
            psi_def.move_to(UP * 1.5)
            self.play(Write(psi_def))
        
        with self.voiceover(text="We can visualize a simple wave function as a sinusoidal wave. Let me show you the real part of a plane wave.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=10,
                y_length=4,
                axis_config={"color": BLUE, "include_tip": True}
            )
            axes.move_to(DOWN * 1)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label(r"Re(\psi)", direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="Here's a plane wave solution. Notice how it oscillates smoothly. This represents a particle with definite momentum.") as tracker:
            wave = axes.plot(lambda x: np.cos(2 * x), color=GREEN, stroke_width=3)
            self.play(Create(wave))
            self.wait(2)
        
        with self.voiceover(text="The wave function can be written as psi equals A times e to the i times k x minus omega t, where k is the wave number and omega is the angular frequency.") as tracker:
            wave_eq = MathTex(r"\psi(x,t) = Ae^{i(kx - \omega t)}", font_size=40)
            wave_eq.next_to(psi_def, DOWN, buff=0.3)
            self.play(Write(wave_eq))
            self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(psi_def), FadeOut(wave_eq), 
                  FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(wave))

    def explain_probability_density(self):
        with self.voiceover(text="One of the most important interpretations in quantum mechanics is the Born interpretation. It tells us that the wave function itself is not directly observable.") as tracker:
            section_title = Text("Probability Density", font_size=36, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Instead, the probability density is given by the absolute square of the wave function. This is what we can actually measure.") as tracker:
            prob_density = MathTex(
                r"\rho(x,t) = |\psi(x,t)|^2 = \psi^*(x,t)\psi(x,t)",
                font_size=45
            )
            prob_density.move_to(UP * 1.5)
            self.play(Write(prob_density))
        
        with self.voiceover(text="Let me demonstrate this with a Gaussian wave packet, which represents a localized particle.") as tracker:
            axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[-1, 1, 0.5],
                x_length=10,
                y_length=3,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label(r"Re(\psi)", direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="This is the real part of a Gaussian wave packet. It's a wave that's localized in space, oscillating within an envelope.") as tracker:
            def gaussian_wave(x, sigma=0.5, k=5):
                return np.exp(-x**2 / (2 * sigma**2)) * np.cos(k * x)
            
            wave_packet = axes.plot(lambda x: gaussian_wave(x), color=GREEN, stroke_width=3)
            self.play(Create(wave_packet))
            self.wait(2)
        
        with self.voiceover(text="Now, let's look at the probability density. This is always real and positive, showing us where we're likely to find the particle.") as tracker:
            prob_axes = Axes(
                x_range=[-5, 5, 1],
                y_range=[0, 1.2, 0.2],
                x_length=10,
                y_length=3,
                axis_config={"color": BLUE}
            )
            prob_axes.move_to(DOWN * 0.5)
            
            prob_x_label = prob_axes.get_x_axis_label("x", direction=RIGHT)
            prob_y_label = prob_axes.get_y_axis_label(r"|\psi|^2", direction=UP)
            
            self.play(
                Transform(axes, prob_axes),
                Transform(x_label, prob_x_label),
                Transform(y_label, prob_y_label),
                FadeOut(wave_packet)
            )
        
        with self.voiceover(text="The probability density is the Gaussian envelope squared. The particle is most likely to be found at the center, with decreasing probability as we move away.") as tracker:
            def prob_density_func(x, sigma=0.5):
                return np.exp(-x**2 / sigma**2)
            
            prob_graph = prob_axes.plot(lambda x: prob_density_func(x), color=RED, stroke_width=3)
            area = prob_axes.get_area(prob_graph, x_range=[-2, 2], color=RED, opacity=0.3)
            
            self.play(Create(prob_graph), FadeIn(area))
            self.wait(2)
        
        with self.voiceover(text="An important constraint is normalization. The total probability of finding the particle anywhere must equal one.") as tracker:
            normalization = MathTex(
                r"\int_{-\infty}^{\infty} |\psi(x,t)|^2 dx = 1",
                font_size=40
            )
            normalization.next_to(prob_density, DOWN, buff=0.3)
            self.play(Write(normalization))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def time_dependent_schrodinger(self):
        with self.voiceover(text="Let's explore the time-dependent Schrödinger equation in more detail. This equation governs how wave functions evolve dynamically.") as tracker:
            section_title = Text("Time-Dependent Schrödinger Equation", font_size=32, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Here's the full form of the equation in one dimension. The Hamiltonian contains both kinetic and potential energy terms.") as tracker:
            tdse = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2} + V(x)\psi",
                font_size=40
            )
            tdse.move_to(UP * 1.5)
            self.play(Write(tdse))
            self.wait(2)
        
        with self.voiceover(text="Let's identify the kinetic energy term. This second derivative represents the particle's kinetic energy, which depends on the curvature of the wave function.") as tracker:
            # kinetic_box = SurroundingRectangle(tdse[0][8:18], color=GREEN, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            kinetic_label = Text("Kinetic Energy", font_size=24, color=GREEN)
            kinetic_label.next_to(kinetic_box, DOWN, buff=0.5)
            self.play(Create(kinetic_box), Write(kinetic_label))
            self.wait(2)
        
        with self.voiceover(text="And here's the potential energy term. The potential V of x represents external forces acting on the particle.") as tracker:
            self.play(FadeOut(kinetic_box), FadeOut(kinetic_label))
            # potential_box = SurroundingRectangle(tdse[0][19:], color=ORANGE, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            potential_label = Text("Potential Energy", font_size=24, color=ORANGE)
            potential_label.next_to(potential_box, DOWN, buff=0.5)
            self.play(Create(potential_box), Write(potential_label))
            self.wait(2)
        
        with self.voiceover(text="For a free particle, where the potential is zero, the equation simplifies significantly. We only have the kinetic energy term.") as tracker:
            self.play(FadeOut(potential_box), FadeOut(potential_label))
            free_particle = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \psi}{\partial x^2}",
                font_size=40
            )
            free_particle.next_to(tdse, DOWN, buff=0.8)
            free_label = Text("Free Particle (V = 0)", font_size=28, color=BLUE)
            free_label.next_to(free_particle, DOWN, buff=0.3)
            self.play(Write(free_particle), Write(free_label))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def time_independent_schrodinger(self):
        with self.voiceover(text="In many cases, we can separate the time and space dependence of the wave function. This leads to the time-independent Schrödinger equation.") as tracker:
            section_title = Text("Time-Independent Schrödinger Equation", font_size=32, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="We use a technique called separation of variables. We write psi of x and t as the product of a spatial function phi of x and a time function e to the minus i E t over h-bar.") as tracker:
            separation = MathTex(
                r"\psi(x,t) = \phi(x)e^{-iEt/\hbar}",
                font_size=45
            )
            separation.move_to(UP * 2)
            self.play(Write(separation))
            self.wait(2)
        
        with self.voiceover(text="Substituting this into the time-dependent equation and simplifying, we arrive at the time-independent Schrödinger equation.") as tracker:
            tise = MathTex(
                r"\hat{H}\phi = E\phi",
                font_size=50
            )
            tise.move_to(UP * 0.5)
            self.play(Write(tise))
            self.wait(1)
        
        with self.voiceover(text="In expanded form, this becomes a second-order differential equation. Here, E is the energy eigenvalue we're solving for.") as tracker:
            tise_expanded = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2} + V(x)\phi = E\phi",
                font_size=40
            )
            tise_expanded.next_to(tise, DOWN, buff=0.8)
            self.play(Write(tise_expanded))
            self.wait(2)
        
        with self.voiceover(text="This is an eigenvalue problem. The solutions phi are called eigenfunctions or stationary states, and E represents the allowed energy levels.") as tracker:
            eigenvalue_text = Text("Eigenvalue Problem: Find φ and E", font_size=28, color=GREEN)
            eigenvalue_text.next_to(tise_expanded, DOWN, buff=0.8)
            self.play(Write(eigenvalue_text))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box(self):
        with self.voiceover(text="Let's apply what we've learned to a classic problem: the particle in a one-dimensional box. This is also called the infinite square well.") as tracker:
            section_title = Text("Particle in a Box", font_size=36, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Imagine a particle confined between two walls at x equals zero and x equals L. Outside this region, the potential is infinite, so the particle cannot escape.") as tracker:
            # Draw the box
            axes = Axes(
                x_range=[-1, 4, 1],
                y_range=[0, 3, 1],
                x_length=8,
                y_length=4,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 0.5)
            
            # Potential walls
            left_wall = Line(axes.c2p(0, 0), axes.c2p(0, 2.5), color=RED, stroke_width=8)
            right_wall = Line(axes.c2p(3, 0), axes.c2p(3, 2.5), color=RED, stroke_width=8)
            floor = Line(axes.c2p(0, 0), axes.c2p(3, 0), color=WHITE, stroke_width=3)
            
            # Labels
            x_label = MathTex("x=0", font_size=28).next_to(left_wall, DOWN)
            l_label = MathTex("x=L", font_size=28).next_to(right_wall, DOWN)
            v_label = Text("V = ∞", font_size=24, color=RED).next_to(left_wall, LEFT)
            v_label2 = Text("V = ∞", font_size=24, color=RED).next_to(right_wall, RIGHT)
            
            self.play(
                Create(axes),
                Create(left_wall), Create(right_wall), Create(floor),
                Write(x_label), Write(l_label), Write(v_label), Write(v_label2)
            )
            self.wait(2)
        
        with self.voiceover(text="Inside the box, the potential is zero, so we solve the free particle Schrödinger equation with boundary conditions.") as tracker:
            equation = MathTex(
                r"-\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2} = E\phi, \quad 0 < x < L",
                font_size=35
            )
            equation.to_edge(UP).shift(DOWN * 0.7)
            self.play(Write(equation))
            self.wait(2)
        
        with self.voiceover(text="The boundary conditions require that the wave function is zero at the walls. This is because the particle cannot exist outside the box.") as tracker:
            bc = MathTex(r"\phi(0) = 0, \quad \phi(L) = 0", font_size=35)
            bc.next_to(equation, DOWN, buff=0.3)
            self.play(Write(bc))
            self.wait(2)
        
        with self.voiceover(text="Solving this differential equation with these boundary conditions, we find that the wave functions are sine functions.") as tracker:
            solution = MathTex(
                r"\phi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)",
                font_size=35
            )
            solution.next_to(bc, DOWN, buff=0.3)
            self.play(Write(solution))
            self.wait(2)
        
        with self.voiceover(text="Let me show you the first three energy levels. The quantum number n can be one, two, three, and so on. Notice how each level has one more node than the previous.") as tracker:
            # Clear previous elements except walls and axes
            self.play(FadeOut(equation), FadeOut(bc), FadeOut(solution))
            
            # Plot wave functions
            n1 = axes.plot(lambda x: 1.2 * np.sin(np.pi * x / 3) if 0 <= x <= 3 else 0, 
                          color=GREEN, stroke_width=3, x_range=[0, 3])
            n1_label = MathTex("n=1", font_size=28, color=GREEN).next_to(axes, LEFT).shift(UP * 0.5)
            
            self.play(Create(n1), Write(n1_label))
            self.wait(2)
        
        with self.voiceover(text="Here's the second energy level, n equals two. It has one node in the middle.") as tracker:
            n2 = axes.plot(lambda x: 1.2 * np.sin(2 * np.pi * x / 3) if 0 <= x <= 3 else 0, 
                          color=BLUE, stroke_width=3, x_range=[0, 3])
            n2_label = MathTex("n=2", font_size=28, color=BLUE).next_to(n1_label, DOWN, buff=0.3)
            
            self.play(Transform(n1, n2), Transform(n1_label, n2_label))
            self.wait(2)
        
        with self.voiceover(text="And the third level, n equals three, has two nodes.") as tracker:
            n3 = axes.plot(lambda x: 1.2 * np.sin(3 * np.pi * x / 3) if 0 <= x <= 3 else 0, 
                          color=PURPLE, stroke_width=3, x_range=[0, 3])
            n3_label = MathTex("n=3", font_size=28, color=PURPLE).next_to(n2_label, DOWN, buff=0.3)
            
            self.play(Transform(n1, n3), Transform(n1_label, n3_label))
            self.wait(2)
        
        with self.voiceover(text="The allowed energy levels are quantized. They're proportional to n squared. This is a fundamental result: energy is not continuous but comes in discrete packets.") as tracker:
            energy = MathTex(
                r"E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, ...",
                font_size=38
            )
            energy.to_edge(UP).shift(DOWN * 0.7)
            self.play(Write(energy))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def quantum_tunneling(self):
        with self.voiceover(text="Now let's explore one of the most fascinating quantum phenomena: quantum tunneling. This is impossible in classical physics.") as tracker:
            section_title = Text("Quantum Tunneling", font_size=36, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="Consider a particle approaching a potential barrier. In classical mechanics, if the particle's energy is less than the barrier height, it cannot pass through.") as tracker:
            # Create axes
            axes = Axes(
                x_range=[-3, 5, 1],
                y_range=[0, 2, 0.5],
                x_length=10,
                y_length=3.5,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 0.8)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label("V(x)", direction=UP)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
        
        with self.voiceover(text="Here's the potential barrier. It has height V-zero and width a. A classical particle with energy E less than V-zero would simply bounce back.") as tracker:
            # Draw barrier
            barrier = VGroup(
                Line(axes.c2p(0, 0), axes.c2p(0, 1.5), color=RED, stroke_width=5),
                Line(axes.c2p(0, 1.5), axes.c2p(2, 1.5), color=RED, stroke_width=5),
                Line(axes.c2p(2, 1.5), axes.c2p(2, 0), color=RED, stroke_width=5)
            )
            
            v0_label = MathTex("V_0", font_size=32, color=RED).next_to(axes.c2p(1, 1.5), UP)
            a_label = MathTex("a", font_size=32).next_to(axes.c2p(1, 0), DOWN)
            
            self.play(Create(barrier), Write(v0_label), Write(a_label))
        
        with self.voiceover(text="Let's draw the energy level of our particle. It's below the barrier height.") as tracker:
            energy_line = DashedLine(axes.c2p(-3, 0.8), axes.c2p(5, 0.8), color=GREEN, stroke_width=3)
            e_label = MathTex("E", font_size=32, color=GREEN).next_to(energy_line, LEFT)
            self.play(Create(energy_line), Write(e_label))
            self.wait(1)
        
        with self.voiceover(text="But in quantum mechanics, something remarkable happens. The wave function doesn't immediately drop to zero at the barrier. Instead, it decays exponentially inside.") as tracker:
            # Incident wave
            incident = axes.plot(lambda x: 0.5 * np.cos(4*x) * np.exp(-0.3*(x+3)**2) if x < 0 else 0,
                               color=YELLOW, stroke_width=3, x_range=[-3, 0])
            
            # Inside barrier (exponential decay)
            inside = axes.plot(lambda x: 0.5 * np.exp(-1.5*x) if 0 <= x <= 2 else 0,
                             color=ORANGE, stroke_width=3, x_range=[0, 2])
            
            # Transmitted wave
            transmitted = axes.plot(lambda x: 0.15 * np.cos(4*x) if x > 2 else 0,
                                  color=GREEN, stroke_width=3, x_range=[2, 5])
            
            self.play(Create(incident))
            self.wait(1)
            self.play(Create(inside))
            self.wait(1)
            self.play(Create(transmitted))
            self.wait(2)
        
        with self.voiceover(text="There's a non-zero probability that the particle will appear on the other side of the barrier! This is quantum tunneling.") as tracker:
            tunneling_text = Text("Particle 'tunnels' through!", font_size=28, color=GREEN)
            tunneling_text.next_to(section_title, DOWN, buff=0.3)
            self.play(Write(tunneling_text))
            self.wait(2)
        
        with self.voiceover(text="The transmission probability depends on the barrier width and height. It decreases exponentially with both parameters.") as tracker:
            transmission = MathTex(
                r"T \approx e^{-2\kappa a}, \quad \kappa = \sqrt{\frac{2m(V_0-E)}{\hbar^2}}",
                font_size=35
            )
            transmission.next_to(tunneling_text, DOWN, buff=0.4)
            self.play(Write(transmission))
            self.wait(3)
        
        with self.voiceover(text="Quantum tunneling is not just theoretical. It's responsible for radioactive decay, allows scanning tunneling microscopes to work, and is crucial in modern electronics.") as tracker:
            applications = VGroup(
                Text("• Radioactive Decay", font_size=24),
                Text("• Scanning Tunneling Microscope", font_size=24),
                Text("• Tunnel Diodes", font_size=24),
                Text("• Nuclear Fusion in Stars", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            applications.next_to(transmission, DOWN, buff=0.5)
            self.play(Write(applications))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def harmonic_oscillator(self):
        with self.voiceover(text="Let's examine another fundamental quantum system: the quantum harmonic oscillator. This models many physical systems, from molecular vibrations to electromagnetic fields.") as tracker:
            section_title = Text("Quantum Harmonic Oscillator", font_size=34, color=YELLOW)
            section_title.to_edge(UP)
            self.play(Write(section_title))
        
        with self.voiceover(text="The harmonic oscillator potential is parabolic. It's given by one-half times m omega squared x squared, where omega is the classical oscillation frequency.") as tracker:
            potential = MathTex(
                r"V(x) = \frac{1}{2}m\omega^2 x^2",
                font_size=45
            )
            potential.move_to(UP * 2.2)
            self.play(Write(potential))
        
        with self.voiceover(text="Let me show you the potential well. Unlike the particle in a box, this potential is smooth and continuous.") as tracker:
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 3, 1],
                x_length=9,
                y_length=4,
                axis_config={"color": BLUE}
            )
            axes.move_to(DOWN * 0.5)
            
            x_label = axes.get_x_axis_label("x", direction=RIGHT)
            y_label = axes.get_y_axis_label("V(x)", direction=UP)
            
            parabola = axes.plot(lambda x: 0.3 * x**2, color=RED, stroke_width=4)
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(parabola))
            self.wait(2)
        
        with self.voiceover(text="The Schrödinger equation for this system can be solved exactly. The energy levels are equally spaced, which is a remarkable result.") as tracker:
            energy_formula = MathTex(
                r"E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0, 1, 2, ...",
                font_size=40
            )
            energy_formula.next_to(potential, DOWN, buff=0.3)
            self.play(Write(energy_formula))
            self.wait(2)
        
        with self.voiceover(text="Notice something interesting: even in the ground state, where n equals zero, the energy is not zero. It's one-half h-bar omega. This is called zero-point energy.") as tracker:
            zero_point = MathTex(
                r"E_0 = \frac{1}{2}\hbar\omega \neq 0",
                font_size=38,
                color=GREEN
            )
            zero_point.next_to(energy_formula, DOWN, buff=0.3)
            self.play(Write(zero_point))
            self.wait(2)
        
        with self.voiceover(text="Let me show you the first few energy levels and their corresponding wave functions. First, the ground state, n equals zero.") as tracker:
            # Energy levels
            e0_line = DashedLine(axes.c2p(-2.5, 0.15), axes.c2p(2.5, 0.15), color=GREEN, stroke_width=2)
            e0_label = MathTex("n=0", font_size=24, color=GREEN).next_to(e0_line, RIGHT)
            
            self.play(Create(e0_line), Write(e0_label))
            
            # Ground state wave function (Gaussian)
            psi0 = axes.plot(lambda x: 0.8 * np.exp(-x**2) + 0.15, 
                           color=GREEN, stroke_width=3)
            self.play(Create(psi0))
            self.wait(2)
        
        with self.voiceover(text="The ground state is a Gaussian function centered at zero. It has no nodes, as expected for the lowest energy state.") as tracker:
            self.wait(2)
        
        with self.voiceover(text="Now the first excited state, n equals one. Notice it has one node at the center.") as tracker:
            e1_line = DashedLine(axes.c2p(-2.5, 0.45), axes.c2p(2.5, 0.45), color=BLUE, stroke_width=2)
            e1_label = MathTex("n=1", font_size=24, color=BLUE).next_to(e1_line, RIGHT)
            
            self.play(Create(e1_line), Write(e1_label))
            
            psi1 = axes.plot(lambda x: (1.1 * x * np.exp(-x**2/2) + 0.45) if abs(x) < 2.5 else 0.45,
                           color=BLUE, stroke_width=3)
            self.play(Transform(psi0, psi1))
            self.wait(2)
        
        with self.voiceover(text="The second excited state, n equals two, has two nodes. Each higher state adds one more node.") as tracker:
            e2_line = DashedLine(axes.c2p(-2.5, 0.75), axes.c2p(2.5, 0.75), color=PURPLE, stroke_width=2)
            e2_label = MathTex("n=2", font_size=24, color=PURPLE).next_to(e2_line, RIGHT)
            
            self.play(Create(e2_line), Write(e2_label))
            
            psi2 = axes.plot(lambda x: (0.7 * (2*x**2 - 1) * np.exp(-x**2/2) + 0.75) if abs(x) < 2.5 else 0.75,
                           color=PURPLE, stroke_width=3)
            self.play(Transform(psi0, psi2))
            self.wait(2)
        
        with self.voiceover(text="The wave functions are called Hermite polynomials times a Gaussian. They form a complete orthonormal basis for quantum mechanics.") as tracker:
            hermite = MathTex(
                r"\phi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2^n n!}} H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right) e^{-\frac{m\omega x^2}{2\hbar}}",
                font_size=28
            )
            hermite.to_edge(DOWN)
            self.play(Write(hermite))
            self.wait(3)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="Let's summarize everything we've learned about the Schrödinger equation today.") as tracker:
            title = Text("Summary", font_size=48, color=BLUE)
            title.to_edge(UP)
            self.play(Write(title))
        
        with self.voiceover(text="We started with the fundamental time-dependent Schrödinger equation, which governs all quantum mechanical systems.") as tracker:
            point1 = Text("• Time-Dependent Schrödinger Equation", font_size=28)
            point1.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=1)
            eq1 = MathTex(r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi", font_size=32)
            eq1.next_to(point1, RIGHT, buff=0.5)
            self.play(Write(point1), Write(eq1))
            self.wait(1)
        
        with self.voiceover(text="We learned that wave functions contain all information about a quantum system, but are not directly observable.") as tracker:
            point2 = Text("• Wave Functions (Complex-Valued)", font_size=28)
            point2.next_to(point1, DOWN, buff=0.5).align_to(point1, LEFT)
            eq2 = MathTex(r"\psi(x,t) \in \mathbb{C}", font_size=32)
            eq2.next_to(point2, RIGHT, buff=0.5)
            self.play(Write(point2), Write(eq2))
            self.wait(1)
        
        with self.voiceover(text="The probability density, given by the absolute square of the wave function, tells us where we can find the particle.") as tracker:
            point3 = Text("• Probability Density", font_size=28)
            point3.next_to(point2, DOWN, buff=0.5).align_to(point1, LEFT)
            eq3 = MathTex(r"|\psi|^2", font_size=32)
            eq3.next_to(point3, RIGHT, buff=0.5)
            self.play(Write(point3), Write(eq3))
            self.wait(1)
        
        with self.voiceover(text="For stationary states, we solved the time-independent Schrödinger equation to find energy eigenvalues.") as tracker:
            point4 = Text("• Energy Quantization", font_size=28)
            point4.next_to(point3, DOWN, buff=0.5).align_to(point1, LEFT)
            eq4 = MathTex(r"\hat{H}\phi = E\phi", font_size=32)
            eq4.next_to(point4, RIGHT, buff=0.5)
            self.play(Write(point4), Write(eq4))
            self.wait(1)
        
        with self.voiceover(text="We explored three important examples: the particle in a box, quantum tunneling, and the harmonic oscillator.") as tracker:
            point5 = Text("• Applications: Particle in Box, Tunneling, Oscillator", font_size=28)
            point5.next_to(point4, DOWN, buff=0.5).align_to(point1, LEFT)
            self.play(Write(point5))
            self.wait(2)
        
        with self.voiceover(text="These concepts form the foundation of quantum mechanics and are essential for understanding atomic physics, chemistry, and modern technology.") as tracker:
            closing = Text(
                "The Schrödinger equation is the cornerstone\nof our quantum understanding of nature.",
                font_size=28,
                color=YELLOW
            )
            closing.next_to(point5, DOWN, buff=0.8)
            self.play(Write(closing))
            self.wait(2)
        
        with self.voiceover(text="Thank you for joining me on this journey through the Schrödinger equation, wave functions, and probability density. Keep exploring the quantum world!") as tracker:
            final_message = Text("Thank You!", font_size=48, color=GREEN)
            final_message.move_to(ORIGIN)
            self.play(FadeOut(title), FadeOut(point1), FadeOut(eq1), FadeOut(point2), FadeOut(eq2),
                     FadeOut(point3), FadeOut(eq3), FadeOut(point4), FadeOut(eq4), FadeOut(point5), FadeOut(closing))
            self.play(Write(final_message))
            self.wait(3)
        
        self.play(FadeOut(final_message))
