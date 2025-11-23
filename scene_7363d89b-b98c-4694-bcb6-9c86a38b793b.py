from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class SchrodingerEquationExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Introduction
        self.introduction()
        
        # Historical context
        self.historical_context()
        
        # The main equation
        self.show_main_equation()
        
        # Time-dependent vs time-independent
        self.compare_equations()
        
        # Break down each term
        self.explain_terms()
        
        # Wave function visualization
        self.visualize_wave_function()
        
        # Probability interpretation
        self.probability_interpretation()
        
        # Particle in a box example
        self.particle_in_box()
        
        # Quantum tunneling
        self.quantum_tunneling()
        
        # Applications and implications
        self.applications()
        
        # Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of the Schrödinger equation, one of the most fundamental equations in quantum mechanics. Named after Austrian physicist Erwin Schrödinger, this equation revolutionized our understanding of the microscopic world. Today, we'll dive deep into its meaning, components, and fascinating implications for how reality works at the quantum scale.") as tracker:
            title = Text("The Schrödinger Equation", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("A Journey into Quantum Mechanics", font_size=24, color=GRAY)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title), run_time=2)
            self.play(FadeIn(subtitle), run_time=1.5)
            
        with self.voiceover(text="Unlike classical physics, which describes particles with definite positions and velocities, quantum mechanics uses wave functions to describe the probabilistic nature of particles. The Schrödinger equation governs how these wave functions evolve over time, giving us a complete description of quantum systems.") as tracker:
            quantum_text = Text("Quantum mechanics describes particles\nas probability waves", font_size=26, color=WHITE)
            quantum_text.move_to(ORIGIN)
            
            self.play(Write(quantum_text), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="In nineteen twenty-six, Erwin Schrödinger published his groundbreaking wave equation, building on the work of Louis de Broglie who proposed that particles have wave-like properties. This was a pivotal moment in physics, as scientists struggled to understand the bizarre behavior of atoms and electrons that couldn't be explained by classical mechanics.") as tracker:
            title = Text("Historical Context", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            timeline = VGroup()
            year_1926 = Text("1926", font_size=28, color=YELLOW)
            year_1926.move_to(LEFT * 4 + UP * 0.5)
            
            schrodinger = Text("Schrödinger publishes\nwave equation", font_size=22)
            schrodinger.next_to(year_1926, DOWN, buff=0.3)
            
            timeline.add(year_1926, schrodinger)
            
            self.play(FadeIn(timeline), run_time=2)
            
        with self.voiceover(text="Before Schrödinger, physicists like Niels Bohr had proposed models of the atom, but these were incomplete. The Schrödinger equation provided a mathematical framework that could predict atomic spectra, chemical bonding, and countless other quantum phenomena with remarkable accuracy. It earned him the Nobel Prize in Physics in nineteen thirty-three.") as tracker:
            nobel = Text("Nobel Prize 1933", font_size=24, color=GOLD)
            nobel.move_to(RIGHT * 3.5 + UP * 0.5)
            
            impact = Text("Predicted:\n• Atomic spectra\n• Chemical bonds\n• Quantum behavior", font_size=20)
            impact.next_to(nobel, DOWN, buff=0.3)
            
            self.play(FadeIn(nobel), FadeIn(impact), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def show_main_equation(self):
        with self.voiceover(text="Let's now look at the time-dependent Schrödinger equation in all its glory. This is the most general form of the equation, describing how a quantum state evolves through time. On the left side, we have i times h-bar times the partial derivative of the wave function psi with respect to time.") as tracker:
            title = Text("The Time-Dependent Schrödinger Equation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=36
            )
            equation.move_to(UP * 1.5)
            
            self.play(Write(equation), run_time=3)
            
        with self.voiceover(text="On the right side, we have the Hamiltonian operator, denoted by H-hat, acting on the wave function psi. The Hamiltonian represents the total energy of the system, including both kinetic and potential energy. This elegant equation tells us that the rate of change of a quantum state is determined by its energy.") as tracker:
            hamiltonian_exp = MathTex(
                r"\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(x,t)",
                font_size=32
            )
            hamiltonian_exp.move_to(DOWN * 0.5)
            
            label = Text("Hamiltonian = Kinetic + Potential Energy", font_size=22, color=YELLOW)
            label.next_to(hamiltonian_exp, DOWN, buff=0.5)
            
            self.play(Write(hamiltonian_exp), run_time=2)
            self.play(FadeIn(label), run_time=1.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def compare_equations(self):
        with self.voiceover(text="There are actually two forms of the Schrödinger equation: the time-dependent and time-independent versions. The time-dependent equation describes how quantum states change over time, while the time-independent version applies to stationary states, where the energy is constant.") as tracker:
            title = Text("Two Forms of the Equation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            left_label = Text("Time-Dependent", font_size=24, color=GREEN)
            left_label.move_to(LEFT * 3.5 + UP * 2.0)
            
            right_label = Text("Time-Independent", font_size=24, color=ORANGE)
            right_label.move_to(RIGHT * 3.5 + UP * 2.0)
            
            self.play(Write(left_label), Write(right_label))
            
        with self.voiceover(text="The time-dependent form on the left includes the partial derivative with respect to time. The time-independent form on the right is obtained when we separate variables and assume the potential energy doesn't change with time. This gives us the energy eigenvalue equation, where E is the energy of the stationary state.") as tracker:
            time_dep = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=28
            )
            time_dep.move_to(LEFT * 3.5 + UP * 0.3)
            
            time_indep = MathTex(
                r"\hat{H} \psi = E \psi",
                font_size=28
            )
            time_indep.move_to(RIGHT * 3.5 + UP * 0.3)
            
            self.play(Write(time_dep), Write(time_indep), run_time=2.5)
            
        with self.voiceover(text="For most practical problems in quantum mechanics, we solve the time-independent equation to find the allowed energy levels and corresponding wave functions. These solutions are called eigenstates, and they form the building blocks for understanding more complex quantum systems.") as tracker:
            use_case_left = Text("General evolution", font_size=20)
            use_case_left.next_to(time_dep, DOWN, buff=0.6)
            
            use_case_right = Text("Stationary states\nEnergy levels", font_size=20)
            use_case_right.next_to(time_indep, DOWN, buff=0.6)
            
            self.play(FadeIn(use_case_left), FadeIn(use_case_right), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def explain_terms(self):
        with self.voiceover(text="Let's break down each component of the Schrödinger equation to understand what they represent. First, we have the imaginary unit i. Its presence reflects the wave-like nature of quantum mechanics and ensures that probabilities remain real numbers even though the wave function itself is complex-valued.") as tracker:
            title = Text("Understanding Each Term", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi",
                font_size=36
            )
            equation.move_to(UP * 1.8)
            self.play(Write(equation), run_time=2)
            
            i_term = MathTex(r"i", font_size=32, color=YELLOW)
            i_term.move_to(LEFT * 4.5 + DOWN * 0.3)
            i_label = Text("Imaginary unit\n(wave nature)", font_size=18)
            i_label.next_to(i_term, DOWN, buff=0.3)
            
            self.play(Write(i_term), FadeIn(i_label), run_time=2)
            
        with self.voiceover(text="Next is h-bar, the reduced Planck constant, equal to Planck's constant divided by two pi. This fundamental constant sets the scale of quantum effects. It has units of action, connecting energy and time, or momentum and position. The smaller h-bar is, the more classical the system behaves.") as tracker:
            hbar_term = MathTex(r"\hbar = \frac{h}{2\pi}", font_size=30, color=YELLOW)
            hbar_term.move_to(LEFT * 1.5 + DOWN * 0.3)
            hbar_label = Text("Reduced Planck\nconstant", font_size=18)
            hbar_label.next_to(hbar_term, DOWN, buff=0.3)
            
            self.play(Write(hbar_term), FadeIn(hbar_label), run_time=2)
            
        with self.voiceover(text="The wave function psi is the central object in quantum mechanics. It's a complex-valued function that contains all the information about a quantum system. The square of its absolute value gives us the probability density of finding a particle at a particular location. This probabilistic interpretation was proposed by Max Born.") as tracker:
            psi_term = MathTex(r"\psi(x,t)", font_size=30, color=YELLOW)
            psi_term.move_to(RIGHT * 1.8 + DOWN * 0.3)
            psi_label = Text("Wave function\n(quantum state)", font_size=18)
            psi_label.next_to(psi_term, DOWN, buff=0.3)
            
            self.play(Write(psi_term), FadeIn(psi_label), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's examine the right side of the equation. The first term is the kinetic energy operator. It contains the Laplacian, which is the second spatial derivative. This term describes how the wave function curves in space, relating to the particle's kinetic energy. The mass m in the denominator shows that heavier particles have less quantum behavior.") as tracker:
            title2 = Text("Energy Terms", font_size=32, color=BLUE)
            title2.to_edge(UP, buff=1.0)
            self.play(Write(title2))
            
            kinetic = MathTex(
                r"-\frac{\hbar^2}{2m}\nabla^2\psi",
                font_size=36,
                color=GREEN
            )
            kinetic.move_to(UP * 1.5)
            k_label = Text("Kinetic Energy Term", font_size=24, color=GREEN)
            k_label.next_to(kinetic, DOWN, buff=0.4)
            
            self.play(Write(kinetic), FadeIn(k_label), run_time=2.5)
            
        with self.voiceover(text="The final term is the potential energy, V times psi. The potential V can depend on position and possibly time, representing external forces acting on the particle. In an atom, this would be the electric potential from the nucleus. In a molecule, it includes interactions between multiple particles. The form of V determines the specific problem we're solving.") as tracker:
            potential = MathTex(
                r"V(x,t)\psi",
                font_size=36,
                color=ORANGE
            )
            potential.move_to(DOWN * 0.5)
            p_label = Text("Potential Energy Term", font_size=24, color=ORANGE)
            p_label.next_to(potential, DOWN, buff=0.4)
            
            self.play(Write(potential), FadeIn(p_label), run_time=2.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def visualize_wave_function(self):
        with self.voiceover(text="To truly understand the Schrödinger equation, we need to visualize what a wave function looks like. Unlike classical particles that have definite positions, a quantum particle is described by a wave that spreads out in space. Let's see how a simple wave function behaves.") as tracker:
            title = Text("Visualizing the Wave Function", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True, "font_size": 20}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.3).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)
            
        with self.voiceover(text="Here we see a Gaussian wave packet, a common example in quantum mechanics. The wave function has both a real part, shown in blue, and an imaginary part. The wave oscillates and the envelope shows where the particle is most likely to be found. Notice how the wave extends over a region rather than being at a single point.") as tracker:
            wave = axes.plot(
                lambda x: np.exp(-x**2/2) * np.cos(3*x),
                color=BLUE,
                x_range=[-4, 4]
            )
            
            envelope_pos = axes.plot(lambda x: np.exp(-x**2/2), color=RED, stroke_width=2)
            envelope_neg = axes.plot(lambda x: -np.exp(-x**2/2), color=RED, stroke_width=2)
            
            self.play(Create(wave), run_time=2)
            self.play(Create(envelope_pos), Create(envelope_neg), run_time=2)
            
        with self.voiceover(text="As time evolves, this wave packet doesn't just move—it also spreads out. This is called dispersion, and it's a fundamental feature of quantum mechanics. The uncertainty principle tells us that a particle can't be localized perfectly without having infinite uncertainty in its momentum. The more localized the wave packet, the faster it spreads.") as tracker:
            wave2 = axes.plot(
                lambda x: 0.7 * np.exp(-(x-1)**2/3) * np.cos(3*(x-1)),
                color=BLUE,
                x_range=[-4, 4]
            )
            
            self.play(Transform(wave, wave2), run_time=2.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def probability_interpretation(self):
        with self.voiceover(text="One of the most revolutionary aspects of quantum mechanics is the probabilistic interpretation of the wave function. Max Born proposed that the square of the wave function's magnitude gives us the probability density. This means we can only predict the likelihood of finding a particle in a region, not its exact location.") as tracker:
            title = Text("Probability Interpretation", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            prob_equation = MathTex(
                r"P(x) = |\psi(x)|^2",
                font_size=32
            )
            prob_equation.move_to(UP * 2.0)
            
            self.play(Write(prob_equation), run_time=2)
            
        with self.voiceover(text="Let's visualize this concept. Below we show a wave function psi in blue, and its corresponding probability density in red. Notice that the probability density is always positive, even though the wave function oscillates between positive and negative values. The total probability over all space must equal one, ensuring the particle exists somewhere.") as tracker:
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 1.2, 0.2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True, "font_size": 20}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.3).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.5)
            
            prob_density = axes.plot(
                lambda x: np.exp(-x**2),
                color=RED,
                x_range=[-3, 3]
            )
            
            area = axes.get_riemann_rectangles(
                prob_density,
                x_range=[-1, 1],
                dx=0.2,
                color=YELLOW,
                fill_opacity=0.3
            )
            
            self.play(Create(prob_density), run_time=2)
            self.play(FadeIn(area), run_time=1.5)
            
        with self.voiceover(text="The shaded area shows the probability of finding the particle between negative one and positive one. We calculate this by integrating the probability density over that region. This probabilistic nature initially troubled many physicists, including Einstein, who famously said that God does not play dice. However, countless experiments have confirmed this interpretation.") as tracker:
            integral = MathTex(
                r"\int_{-1}^{1} |\psi(x)|^2 dx",
                font_size=30
            )
            integral.next_to(axes, RIGHT, buff=0.8)
            
            self.play(Write(integral), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def particle_in_box(self):
        with self.voiceover(text="Let's explore a classic example: the particle in a box, also called the infinite square well. This is one of the few quantum systems we can solve exactly. Imagine a particle confined to a one-dimensional box with infinitely high walls. The particle cannot escape, so the wave function must be zero at the walls.") as tracker:
            title = Text("Particle in a Box", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Box representation
            box_left = Line(UP * 2.0, DOWN * 2.0, color=WHITE, stroke_width=8)
            box_left.move_to(LEFT * 3.0)
            box_right = Line(UP * 2.0, DOWN * 2.0, color=WHITE, stroke_width=8)
            box_right.move_to(RIGHT * 3.0)
            box_bottom = Line(LEFT * 3.0, RIGHT * 3.0, color=WHITE, stroke_width=4)
            box_bottom.move_to(DOWN * 2.0)
            
            box = VGroup(box_left, box_right, box_bottom)
            
            self.play(Create(box), run_time=2)
            
        with self.voiceover(text="The boundary conditions force the wave function into specific standing wave patterns, similar to vibrations on a guitar string. The allowed energies are quantized, meaning only discrete energy levels are permitted. The ground state, or lowest energy level, is shown here as n equals one.") as tracker:
            axes = Axes(
                x_range=[-3, 3, 1],
                y_range=[-0.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False, "font_size": 18}
            )
            axes.move_to(DOWN * 1.5)
            
            ground_state = axes.plot(
                lambda x: np.sqrt(2/6) * np.sin(np.pi * (x + 3) / 6) if -3 <= x <= 3 else 0,
                color=GREEN,
                x_range=[-3, 3]
            )
            
            n1_label = MathTex("n=1", font_size=28, color=GREEN)
            n1_label.move_to(RIGHT * 3.8 + UP * 0.5)
            
            self.play(Create(axes), Create(ground_state), Write(n1_label), run_time=2.5)
            
        with self.voiceover(text="Higher energy states have more nodes, or zero-crossing points. Here's the second excited state with n equals three. The energy increases as n squared, so higher states have much more energy. Each state represents a different way the particle can exist within the box, and the particle can transition between these states by absorbing or emitting photons.") as tracker:
            excited_state = axes.plot(
                lambda x: np.sqrt(2/6) * np.sin(3 * np.pi * (x + 3) / 6) if -3 <= x <= 3 else 0,
                color=ORANGE,
                x_range=[-3, 3]
            )
            
            n3_label = MathTex("n=3", font_size=28, color=ORANGE)
            n3_label.move_to(RIGHT * 3.8 + DOWN * 0.5)
            
            energy_formula = MathTex(
                r"E_n = \frac{n^2 h^2}{8mL^2}",
                font_size=30
            )
            energy_formula.move_to(UP * 2.5)
            
            self.play(Create(excited_state), Write(n3_label), Write(energy_formula), run_time=2.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def quantum_tunneling(self):
        with self.voiceover(text="Now let's explore one of the most counterintuitive phenomena in quantum mechanics: quantum tunneling. In classical physics, a particle without enough energy cannot overcome a potential barrier. But in quantum mechanics, there's a non-zero probability that the particle can tunnel through the barrier and appear on the other side.") as tracker:
            title = Text("Quantum Tunneling", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create potential barrier
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 2, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True, "font_size": 20}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.3).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label("V", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.5)
            
        with self.voiceover(text="Here we show a rectangular potential barrier in red. A classical particle with energy E, shown by the green line, would bounce back if E is less than the barrier height. But quantum mechanically, the wave function doesn't abruptly stop at the barrier—it decays exponentially inside the barrier region.") as tracker:
            # Barrier
            barrier = VGroup(
                Line(axes.c2p(-0.5, 0), axes.c2p(-0.5, 1.5), color=RED, stroke_width=4),
                Line(axes.c2p(-0.5, 1.5), axes.c2p(0.5, 1.5), color=RED, stroke_width=4),
                Line(axes.c2p(0.5, 1.5), axes.c2p(0.5, 0), color=RED, stroke_width=4)
            )
            
            energy_line = DashedLine(
                axes.c2p(-4, 1.0),
                axes.c2p(4, 1.0),
                color=GREEN,
                stroke_width=3
            )
            
            e_label = MathTex("E", font_size=24, color=GREEN)
            e_label.next_to(energy_line, LEFT, buff=0.3)
            
            self.play(Create(barrier), Create(energy_line), Write(e_label), run_time=2.5)
            
        with self.voiceover(text="If the barrier is thin enough, some of the wave function emerges on the other side with reduced amplitude. This means there's a finite probability of detecting the particle beyond the barrier, even though it never had enough energy to go over it. This phenomenon is crucial for radioactive decay, nuclear fusion in stars, and even the operation of scanning tunneling microscopes.") as tracker:
            # Incoming wave
            wave_left = axes.plot(
                lambda x: 0.8 * np.sin(4*x + 3) if x < -0.5 else 0,
                color=BLUE,
                x_range=[-4, -0.5]
            )
            
            # Decaying wave inside barrier
            wave_barrier = axes.plot(
                lambda x: 0.8 * np.exp(-3*(x+0.5)) if -0.5 <= x <= 0.5 else 0,
                color=PURPLE,
                x_range=[-0.5, 0.5]
            )
            
            # Transmitted wave
            wave_right = axes.plot(
                lambda x: 0.3 * np.sin(4*x + 3) if x > 0.5 else 0,
                color=YELLOW,
                x_range=[0.5, 4]
            )
            
            self.play(Create(wave_left), run_time=1.5)
            self.play(Create(wave_barrier), run_time=1.5)
            self.play(Create(wave_right), run_time=1.5)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def applications(self):
        with self.voiceover(text="The Schrödinger equation isn't just theoretical—it has profound practical applications that shape our modern world. In chemistry, it explains how atoms bond to form molecules by describing the electron orbitals. The shapes of these orbitals, predicted by solving the Schrödinger equation, determine the properties of every chemical compound.") as tracker:
            title = Text("Applications and Impact", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            app1 = Text("• Chemistry & Molecular Bonding", font_size=24)
            app1.move_to(UP * 1.5)
            
            app2 = Text("• Semiconductor Physics", font_size=24)
            app2.next_to(app1, DOWN, buff=0.5)
            
            app3 = Text("• Quantum Computing", font_size=24)
            app3.next_to(app2, DOWN, buff=0.5)
            
            self.play(Write(app1), run_time=1.5)
            self.play(Write(app2), run_time=1.5)
            
        with self.voiceover(text="In semiconductor physics, the equation helps us understand how electrons behave in materials like silicon, enabling the design of transistors and computer chips. The band structure of semiconductors, crucial for electronics, comes directly from quantum mechanical calculations using the Schrödinger equation.") as tracker:
            self.play(Write(app3), run_time=1.5)
            
            app4 = Text("• Spectroscopy & Lasers", font_size=24)
            app4.next_to(app3, DOWN, buff=0.5)
            
            app5 = Text("• Nanotechnology", font_size=24)
            app5.next_to(app4, DOWN, buff=0.5)
            
            self.play(Write(app4), Write(app5), run_time=2)
            
        with self.voiceover(text="Quantum computing relies fundamentally on the Schrödinger equation to describe quantum bits, or qubits, which can exist in superposition states. Spectroscopy uses the equation to predict atomic and molecular spectra, helping us identify elements in distant stars. Nanotechnology depends on quantum effects described by this equation to design materials with novel properties. The reach of the Schrödinger equation extends to nearly every corner of modern physics and technology.") as tracker:
            impact_box = Rectangle(
                width=6, height=2.5,
                color=YELLOW,
                fill_opacity=0.1
            )
            impact_box.move_to(DOWN * 0.2)
            
            impact_text = Text(
                "Foundation of Modern\nQuantum Technology",
                font_size=26,
                color=YELLOW
            )
            impact_text.move_to(impact_box.get_center())
            
            self.play(Create(impact_box), Write(impact_text), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've journeyed through the Schrödinger equation, from its historical origins to its modern applications. This elegant equation describes the fundamental behavior of matter at the quantum scale, replacing deterministic trajectories with probability waves. Its predictions have been verified in countless experiments and have given us technologies that define the modern era.") as tracker:
            title = Text("Conclusion", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            final_equation = MathTex(
                r"i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi",
                font_size=36,
                color=GOLD
            )
            final_equation.move_to(UP * 1.0)
            
            self.play(Write(final_equation), run_time=2.5)
            
        with self.voiceover(text="While quantum mechanics challenges our intuition and forces us to abandon classical notions of reality, it provides an incredibly accurate description of nature. The Schrödinger equation remains one of the pillars of modern physics, guiding our understanding from atomic orbitals to quantum computers. Thank you for joining this exploration of one of science's most beautiful and powerful equations.") as tracker:
            key_points = VGroup(
                Text("✓ Wave-particle duality", font_size=22),
                Text("✓ Probabilistic nature of reality", font_size=22),
                Text("✓ Quantized energy levels", font_size=22),
                Text("✓ Foundation of quantum technology", font_size=22)
            ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            key_points.move_to(DOWN * 1.2)
            
            self.play(FadeIn(key_points), run_time=3)
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Keep exploring the quantum world, and remember that reality is far stranger and more wonderful than we ever imagined.") as tracker:
            thank_you = Text("Thank You for Watching!", font_size=32, color=BLUE)
            thank_you.move_to(ORIGIN)
            
            self.play(Write(thank_you), run_time=2)
            self.wait(2)
        
        self.play(FadeOut(thank_you))


# Render instruction
if __name__ == "__main__":
    scene = SchrodingerEquationExplanation()
    scene.render()