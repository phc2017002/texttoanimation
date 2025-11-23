from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class QuantumMechanics3D(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Josh"))
        
        # Call all sections in order
        self.introduction()
        self.historical_context()
        self.schrodinger_equation_3d()
        self.quantum_numbers()
        self.hydrogen_atom_orbitals()
        self.probability_density()
        self.angular_momentum()
        self.spin_and_magnetic_quantum_numbers()
        self.applications()
        self.conclusion()
    
    def introduction(self):
        with self.voiceover(text="Welcome to our comprehensive exploration of quantum mechanics in three dimensions. In this educational journey, we will delve deep into the fascinating world of quantum systems that exist in real three-dimensional space, uncovering the mathematical beauty and physical significance of wave functions, orbitals, and quantum states.") as tracker:
            title = Text("Quantum Mechanics", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("in Three Dimensions", font_size=36, color=BLUE_C)
            subtitle.next_to(title, DOWN, buff=0.4)
            
            self.play(Write(title))
            self.play(Write(subtitle))
        
        with self.voiceover(text="Moving from one dimension to three dimensions represents a profound leap in complexity and richness. While one-dimensional quantum systems like the particle in a box help us understand basic principles, three-dimensional quantum mechanics reveals the true structure of atoms, molecules, and the fundamental building blocks of matter.") as tracker:
            self.play(FadeOut(title), FadeOut(subtitle))
            
            # Create 3D axes
            axes_3d = ThreeDAxes(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                z_range=[-3, 3, 1],
                x_length=7,
                y_length=4,
                z_length=6
            )
            
            axes_3d.scale(0.6)
            
            labels = VGroup(
                Text("x", font_size=24).next_to(axes_3d.x_axis, RIGHT),
                Text("y", font_size=24).next_to(axes_3d.y_axis, UP),
                Text("z", font_size=24).next_to(axes_3d.z_axis, OUT)
            )
            
            self.play(Create(axes_3d), Write(labels))
            self.play(Rotate(axes_3d, angle=PI/6, axis=UP))
            self.play(Rotate(axes_3d, angle=PI/8, axis=RIGHT))
        
        self.play(FadeOut(axes_3d), FadeOut(labels))
    
    def historical_context(self):
        with self.voiceover(text="The story of three-dimensional quantum mechanics begins in the nineteen twenties, when physicists struggled to understand the structure of atoms. Classical physics had utterly failed to explain why atoms were stable, why they emitted light at specific frequencies, and why electrons didn't simply spiral into the nucleus.") as tracker:
            title = Text("Historical Context", font_size=36, color=GOLD)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            timeline = VGroup(
                Text("1900: Planck's Quantum", font_size=24),
                Text("1913: Bohr Model", font_size=24),
                Text("1926: Schrödinger Equation", font_size=24),
                Text("1927: Heisenberg Uncertainty", font_size=24)
            ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            timeline.move_to(ORIGIN)
            
            self.play(Write(timeline))
        
        with self.voiceover(text="Erwin Schrödinger's breakthrough in nineteen twenty-six provided the mathematical framework we still use today. His wave equation, extended to three dimensions, became the cornerstone of quantum mechanics. It successfully predicted atomic spectra, chemical bonding, and countless other phenomena that were previously mysterious.") as tracker:
            self.play(FadeOut(timeline))
            
            schrodinger_portrait = Text("Erwin Schrödinger", font_size=32, color=BLUE_C)
            schrodinger_portrait.move_to(UP * 0.5)
            year = Text("1926", font_size=28, color=YELLOW)
            year.next_to(schrodinger_portrait, DOWN, buff=0.4)
            
            self.play(Write(schrodinger_portrait), Write(year))
        
        self.play(FadeOut(*self.mobjects))
    
    def schrodinger_equation_3d(self):
        with self.voiceover(text="Let us now examine the time-independent Schrödinger equation in three dimensions. This elegant equation is the foundation of all quantum chemistry and atomic physics. It tells us how wave functions behave in space and how to calculate the allowed energy levels of quantum systems.") as tracker:
            title = Text("Schrödinger Equation in 3D", font_size=34, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Main equation
            equation = MathTex(
                r"-\frac{\hbar^2}{2m}\nabla^2\psi + V\psi = E\psi"
            ).scale(0.9)
            equation.move_to(UP * 1.5)
            
            self.play(Write(equation))
        
        with self.voiceover(text="The Laplacian operator, nabla squared, represents the spatial curvature of the wave function in all three dimensions. It's defined as the sum of second derivatives with respect to x, y, and z coordinates. This operator captures how the wave function varies throughout three-dimensional space.") as tracker:
            # Show Laplacian expansion
            laplacian = MathTex(
                r"\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}"
            ).scale(0.8)
            laplacian.move_to(DOWN * 0.5)
            
            self.play(Write(laplacian))
        
        with self.voiceover(text="The potential energy function V depends on the position in space. For the hydrogen atom, this is the Coulomb potential. The wave function psi is a complex-valued function that contains all information about the quantum state. Its square gives the probability density of finding the particle at each point in space.") as tracker:
            # Hydrogen potential
            potential = MathTex(
                r"V(r) = -\frac{e^2}{4\pi\epsilon_0 r}"
            ).scale(0.8)
            potential.next_to(laplacian, DOWN, buff=0.6)
            
            self.play(Write(potential))
        
        self.play(FadeOut(*self.mobjects))
    
    def quantum_numbers(self):
        with self.voiceover(text="When we solve the Schrödinger equation in three dimensions using spherical coordinates, something remarkable emerges. The solutions are characterized by three quantum numbers: n, l, and m. These quantum numbers are not arbitrary - they arise naturally from the mathematics and the boundary conditions of the problem.") as tracker:
            title = Text("Quantum Numbers", font_size=36, color=PURPLE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Create quantum number descriptions
            qn_n = MathTex(r"n", r"\text{: Principal quantum number}", font_size=32)
            qn_n.move_to(UP * 1.5)
            
            qn_l = MathTex(r"\ell", r"\text{: Angular momentum quantum number}", font_size=32)
            qn_l.move_to(UP * 0.3)
            
            qn_m = MathTex(r"m_\ell", r"\text{: Magnetic quantum number}", font_size=32)
            qn_m.move_to(DOWN * 0.9)
            
            self.play(Write(qn_n))
            self.play(Write(qn_l))
            self.play(Write(qn_m))
        
        with self.voiceover(text="The principal quantum number n determines the energy and overall size of the orbital. It can take positive integer values: one, two, three, and so on. The angular momentum quantum number l determines the shape of the orbital and ranges from zero to n minus one. The magnetic quantum number m describes the orientation in space and ranges from minus l to plus l.") as tracker:
            self.play(FadeOut(qn_n), FadeOut(qn_l), FadeOut(qn_m))
            
            # Show allowed values
            values = VGroup(
                MathTex(r"n = 1, 2, 3, \ldots", font_size=30),
                MathTex(r"\ell = 0, 1, 2, \ldots, n-1", font_size=30),
                MathTex(r"m_\ell = -\ell, -\ell+1, \ldots, 0, \ldots, \ell-1, \ell", font_size=30)
            ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
            values.move_to(ORIGIN)
            
            self.play(Write(values))
        
        with self.voiceover(text="Let's visualize the first few combinations. For n equals one, we have only l equals zero, giving us the one s orbital. For n equals two, we can have l equals zero for the two s orbital, or l equals one for the two p orbitals. Each p orbital can have three different m values: minus one, zero, and plus one, corresponding to three different spatial orientations.") as tracker:
            self.play(FadeOut(values))
            
            examples = VGroup(
                Text("n=1: 1s (l=0, m=0)", font_size=26),
                Text("n=2: 2s (l=0, m=0)", font_size=26),
                Text("n=2: 2p (l=1, m=-1,0,+1)", font_size=26),
                Text("n=3: 3s, 3p, 3d orbitals", font_size=26)
            ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            examples.move_to(ORIGIN)
            
            for example in examples:
                self.play(Write(example))
                self.wait(0.3)
        
        self.play(FadeOut(*self.mobjects))
    
    def hydrogen_atom_orbitals(self):
        with self.voiceover(text="The hydrogen atom is the simplest atomic system, yet it reveals the full beauty of three-dimensional quantum mechanics. Its wave functions, called orbitals, have shapes that determine the chemical properties of atoms. Let's visualize these remarkable structures, starting with the s orbitals which are perfectly spherical.") as tracker:
            title = Text("Hydrogen Atom Orbitals", font_size=34, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # 1s orbital equation
            s_orbital = MathTex(
                r"\psi_{1s} = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}"
            ).scale(0.85)
            s_orbital.move_to(UP * 2.0)
            
            self.play(Write(s_orbital))
        
        with self.voiceover(text="The one s orbital has no angular dependence - it looks the same from every direction. The probability density decreases exponentially with distance from the nucleus. The Bohr radius, a sub zero, sets the length scale and equals approximately zero point five three angstroms. This is the most probable distance to find the electron in the ground state.") as tracker:
            # Visualize 1s orbital as sphere with gradient
            sphere = Sphere(radius=1.5, resolution=(20, 20))
            sphere.set_color(BLUE)
            sphere.set_opacity(0.5)
            sphere.move_to(DOWN * 1.0)
            
            self.play(Create(sphere))
            self.play(Rotate(sphere, angle=PI, axis=UP, run_time=2))
        
        with self.voiceover(text="The p orbitals have a completely different shape - they have two lobes pointing in opposite directions. The p x orbital points along the x axis, p y along the y axis, and p z along the z axis. These three orbitals are degenerate, meaning they have the same energy, but they differ in their spatial orientation.") as tracker:
            self.play(FadeOut(sphere), FadeOut(s_orbital))
            
            # p orbital equation
            p_orbital = MathTex(
                r"\psi_{2p_z} \propto r e^{-r/2a_0} \cos\theta"
            ).scale(0.85)
            p_orbital.move_to(UP * 2.0)
            
            self.play(Write(p_orbital))
            
            # Create p orbital lobes
            upper_lobe = Sphere(radius=0.8, resolution=(15, 15))
            upper_lobe.set_color(RED)
            upper_lobe.set_opacity(0.6)
            upper_lobe.move_to(UP * 1.2 + DOWN * 0.5)
            
            lower_lobe = Sphere(radius=0.8, resolution=(15, 15))
            lower_lobe.set_color(BLUE)
            lower_lobe.set_opacity(0.6)
            lower_lobe.move_to(DOWN * 1.2 + DOWN * 0.5)
            
            self.play(Create(upper_lobe), Create(lower_lobe))
        
        self.play(FadeOut(*self.mobjects))
    
    def probability_density(self):
        with self.voiceover(text="A crucial concept in quantum mechanics is that the wave function itself is not directly observable. What we can measure is the probability density, given by the square of the absolute value of the wave function. This probability interpretation, proposed by Max Born, tells us where we are likely to find a particle when we make a measurement.") as tracker:
            title = Text("Probability Density", font_size=36, color=GREEN)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            prob_eq = MathTex(
                r"P(x,y,z) = |\psi(x,y,z)|^2"
            ).scale(0.9)
            prob_eq.move_to(UP * 1.8)
            
            self.play(Write(prob_eq))
        
        with self.voiceover(text="For spherically symmetric states like s orbitals, we often want to know the probability of finding the electron at a certain distance from the nucleus, regardless of direction. This is called the radial probability distribution. It's found by multiplying the probability density by the surface area of a sphere at radius r, which is four pi r squared.") as tracker:
            radial_prob = MathTex(
                r"P(r) = 4\pi r^2 |\psi(r)|^2"
            ).scale(0.85)
            radial_prob.next_to(prob_eq, DOWN, buff=0.8)
            
            self.play(Write(radial_prob))
        
        with self.voiceover(text="Let me show you what this looks like for the one s orbital of hydrogen. Even though the wave function is maximum at the nucleus, the radial probability distribution is zero there because the volume element r squared goes to zero. The maximum occurs at the Bohr radius, which is why we say this is the most probable distance.") as tracker:
            self.play(FadeOut(prob_eq), FadeOut(radial_prob))
            
            # Create axes for radial probability
            axes = Axes(
                x_range=[0, 6, 1],
                y_range=[0, 1.2, 0.2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("r/a_0").shift(DOWN * 0.6).shift(DOWN * 0.8)
            y_label = axes.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            # Radial probability function for 1s
            graph = axes.plot(
                lambda x: 4 * x**2 * np.exp(-2*x) if x > 0 else 0,
                x_range=[0, 6],
                color=YELLOW
            )
            
            self.play(Create(axes), Write(x_label), Write(y_label))
            self.play(Create(graph))
            
            # Mark maximum
            max_point = Dot(axes.c2p(1, 4 * 1**2 * np.exp(-2)), color=RED)
            max_label = MathTex(r"r = a_0", font_size=26).next_to(max_point, UP + RIGHT, buff=0.3)
            
            self.play(Create(max_point), Write(max_label))
        
        self.play(FadeOut(*self.mobjects))
    
    def angular_momentum(self):
        with self.voiceover(text="Angular momentum in quantum mechanics is fundamentally different from classical angular momentum. In three dimensions, angular momentum is quantized - it can only take certain discrete values determined by the quantum numbers l and m. This quantization is a direct consequence of the wave nature of matter and the boundary conditions on the wave function.") as tracker:
            title = Text("Quantum Angular Momentum", font_size=34, color=ORANGE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Total angular momentum
            L_magnitude = MathTex(
                r"|\vec{L}| = \hbar\sqrt{\ell(\ell+1)}"
            ).scale(0.9)
            L_magnitude.move_to(UP * 1.6)
            
            self.play(Write(L_magnitude))
        
        with self.voiceover(text="The magnitude of the angular momentum vector is given by h-bar times the square root of l times l plus one. Meanwhile, the z-component of angular momentum is quantized separately and equals h-bar times m. This is called space quantization - we can know one component precisely, but not all three simultaneously.") as tracker:
            L_z = MathTex(
                r"L_z = \hbar m_\ell"
            ).scale(0.9)
            L_z.next_to(L_magnitude, DOWN, buff=0.7)
            
            self.play(Write(L_z))
        
        with self.voiceover(text="Here's a fascinating consequence: if l equals one, the magnitude of angular momentum is h-bar times the square root of two, which is approximately one point four one h-bar. But the z-component can only be minus h-bar, zero, or plus h-bar. The angular momentum vector can never point exactly along the z-axis because the magnitude is always greater than any single component. This is a purely quantum mechanical feature with no classical analog.") as tracker:
            self.play(FadeOut(L_magnitude), FadeOut(L_z))
            
            # Example with l=1
            example = VGroup(
                MathTex(r"\text{For } \ell = 1:", font_size=28),
                MathTex(r"|\vec{L}| = \hbar\sqrt{2} \approx 1.41\hbar", font_size=28),
                MathTex(r"L_z = -\hbar, 0, +\hbar", font_size=28)
            ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            example.move_to(UP * 0.8)
            
            self.play(Write(example))
        
        with self.voiceover(text="We can visualize this using a vector model. The angular momentum vector precesses around the z-axis, forming a cone. The apex angle depends on the ratio of L z to the total magnitude. This precession is not deterministic motion - rather, it represents our uncertainty about the x and y components when L z is precisely known.") as tracker:
            self.play(FadeOut(example))
            
            # Create vector cone visualization
            z_axis = Arrow(start=DOWN * 2.5, end=UP * 2.5, color=WHITE, buff=0)
            z_label = MathTex("z", font_size=28).next_to(z_axis, UP, buff=0.2)
            
            # Angular momentum vector
            L_vector = Arrow(start=ORIGIN, end=UP * 1.4 + RIGHT * 1.0, color=YELLOW, buff=0)
            L_label = MathTex(r"\vec{L}", font_size=28, color=YELLOW).next_to(L_vector, RIGHT, buff=0.2)
            
            # Projection
            projection = DashedLine(start=UP * 1.4 + RIGHT * 1.0, end=UP * 1.4, color=BLUE)
            Lz_label = MathTex(r"L_z", font_size=26, color=BLUE).next_to(projection, LEFT, buff=0.3)
            
            self.play(Create(z_axis), Write(z_label))
            self.play(Create(L_vector), Write(L_label))
            self.play(Create(projection), Write(Lz_label))
        
        self.play(FadeOut(*self.mobjects))
    
    def spin_and_magnetic_quantum_numbers(self):
        with self.voiceover(text="Beyond the spatial quantum numbers, electrons possess an intrinsic angular momentum called spin. This is not a literal spinning motion, but rather a fundamental quantum property that has no classical counterpart. Spin is always present and contributes to the total angular momentum of an atom.") as tracker:
            title = Text("Spin Quantum Number", font_size=36, color=PURPLE_A)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            spin_eq = MathTex(
                r"s = \frac{1}{2}, \quad m_s = \pm\frac{1}{2}"
            ).scale(0.9)
            spin_eq.move_to(UP * 1.5)
            
            self.play(Write(spin_eq))
        
        with self.voiceover(text="Electrons are spin one-half particles. The spin quantum number s is always one-half, and the spin projection m s can be either plus one-half, called spin up, or minus one-half, called spin down. This gives rise to the Pauli exclusion principle: no two electrons in an atom can have the same set of all four quantum numbers n, l, m, and m s.") as tracker:
            pauli = Text("Pauli Exclusion Principle", font_size=30, color=GOLD)
            pauli.move_to(ORIGIN)
            
            self.play(Write(pauli))
        
        with self.voiceover(text="When we place an atom in a magnetic field, the magnetic quantum number becomes physically significant. Different m values correspond to different orientations of the orbital angular momentum relative to the field, and these states have slightly different energies. This splitting is called the Zeeman effect and provides direct experimental evidence for space quantization.") as tracker:
            self.play(FadeOut(pauli), FadeOut(spin_eq))
            
            zeeman = Text("Zeeman Effect", font_size=32, color=BLUE_C)
            zeeman.move_to(UP * 1.5)
            
            self.play(Write(zeeman))
            
            # Energy level splitting
            energy_levels = VGroup(
                Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE),
                Line(LEFT * 2.5 + UP * 0.8, RIGHT * 2.5 + UP * 0.8, color=YELLOW),
                Line(LEFT * 2.5, RIGHT * 2.5, color=YELLOW),
                Line(LEFT * 2.5 + DOWN * 0.8, RIGHT * 2.5 + DOWN * 0.8, color=YELLOW)
            )
            energy_levels.move_to(DOWN * 0.8)
            
            no_field = Text("No Field", font_size=24).next_to(energy_levels[0], LEFT, buff=0.8)
            with_field = Text("With B Field", font_size=24).next_to(energy_levels[1], RIGHT, buff=0.8)
            
            m_labels = VGroup(
                MathTex("m=+1", font_size=22).next_to(energy_levels[1], LEFT, buff=0.4),
                MathTex("m=0", font_size=22).next_to(energy_levels[2], LEFT, buff=0.4),
                MathTex("m=-1", font_size=22).next_to(energy_levels[3], LEFT, buff=0.4)
            )
            
            self.play(Create(energy_levels[0]), Write(no_field))
            self.play(
                Create(energy_levels[1]),
                Create(energy_levels[2]),
                Create(energy_levels[3]),
                Write(with_field),
                Write(m_labels)
            )
        
        self.play(FadeOut(*self.mobjects))
    
    def applications(self):
        with self.voiceover(text="The principles of three-dimensional quantum mechanics we've explored have profound practical applications. Understanding atomic orbitals is essential for chemistry - chemical bonds form when orbitals from different atoms overlap and share electrons. The shapes and energies of these orbitals determine all of chemistry.") as tracker:
            title = Text("Applications", font_size=32, color=GREEN_C)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            apps = VGroup(
                Text("• Atomic and Molecular Structure", font_size=28),
                Text("• Spectroscopy and Light Emission", font_size=28),
                Text("• Semiconductor Physics", font_size=28),
                Text("• Magnetic Resonance Imaging", font_size=28),
                Text("• Quantum Computing", font_size=28)
            ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
            apps.move_to(DOWN * 0.3)
            
            for app in apps:
                self.play(Write(app))
                self.wait(0.4)
        
        with self.voiceover(text="Spectroscopy relies entirely on quantum transitions between energy levels. When an electron jumps from a higher orbital to a lower one, it emits light with an energy equal to the difference between the levels. This is why hydrogen emits light at specific wavelengths, creating its characteristic spectrum. Every element has a unique spectral fingerprint determined by its quantum structure.") as tracker:
            self.play(FadeOut(apps))
            
            energy_diagram = VGroup(
                Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(DOWN * 2),
                Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(DOWN * 0.5),
                Line(LEFT * 3, RIGHT * 3, color=WHITE).shift(UP * 0.8),
            )
            
            level_labels = VGroup(
                MathTex("n=1", font_size=26).next_to(energy_diagram[0], LEFT, buff=0.4),
                MathTex("n=2", font_size=26).next_to(energy_diagram[1], LEFT, buff=0.4),
                MathTex("n=3", font_size=26).next_to(energy_diagram[2], LEFT, buff=0.4)
            )
            
            self.play(Create(energy_diagram), Write(level_labels))
            
            # Show transition
            arrow = Arrow(
                start=energy_diagram[2].get_center() + RIGHT * 0.5,
                end=energy_diagram[0].get_center() + RIGHT * 0.5,
                color=RED,
                buff=0.1
            )
            photon = MathTex(r"h\nu", font_size=28, color=YELLOW).next_to(arrow, RIGHT, buff=0.3)
            
            self.play(Create(arrow), Write(photon))
        
        with self.voiceover(text="Modern technology increasingly relies on quantum mechanics. Semiconductor devices, lasers, and even the transistors in your computer depend on quantum energy levels and electron behavior in three-dimensional potential wells. Quantum computing, perhaps the most exciting frontier, uses quantum superposition and entanglement to perform calculations impossible for classical computers.") as tracker:
            self.play(FadeOut(energy_diagram), FadeOut(level_labels), FadeOut(arrow), FadeOut(photon))
            
            qc = Text("Quantum Computing", font_size=32, color=BLUE_B)
            qc.move_to(UP * 1.0)
            
            qubit = MathTex(
                r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle"
            ).scale(0.85)
            qubit.next_to(qc, DOWN, buff=0.7)
            
            self.play(Write(qc), Write(qubit))
        
        self.play(FadeOut(*self.mobjects))
    
    def conclusion(self):
        with self.voiceover(text="We have journeyed through the remarkable landscape of three-dimensional quantum mechanics, from the fundamental Schrödinger equation to the intricate structure of atomic orbitals. We've seen how quantum numbers emerge naturally from the mathematics, how probability replaces certainty, and how angular momentum becomes quantized in ways completely foreign to classical physics.") as tracker:
            title = Text("Conclusion", font_size=32, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            summary_points = VGroup(
                Text("✓ Wave functions in 3D space", font_size=26),
                Text("✓ Quantum numbers: n, l, m, s", font_size=26),
                Text("✓ Atomic orbitals and shapes", font_size=26),
                Text("✓ Probability interpretation", font_size=26),
                Text("✓ Quantized angular momentum", font_size=26)
            ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
            summary_points.move_to(DOWN * 0.2)
            
            for point in summary_points:
                self.play(Write(point))
                self.wait(0.3)
        
        with self.voiceover(text="The beauty of quantum mechanics lies not just in its mathematical elegance, but in its extraordinary predictive power. It explains the periodic table, chemical bonding, the stability of matter, and the behavior of light. From the smallest atoms to the largest molecules, from the glow of neon signs to the functioning of our DNA, quantum mechanics governs the microscopic world. Thank you for joining this exploration of one of physics' most profound and beautiful theories.") as tracker:
            self.play(FadeOut(summary_points))
            
            final_eq = MathTex(
                r"\hat{H}\psi = E\psi"
            ).scale(1.2)
            final_eq.move_to(ORIGIN)
            
            self.play(Write(final_eq))
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Keep exploring, keep questioning, and never stop marveling at the quantum world.") as tracker:
            thank_you = Text("Thank You!", font_size=36, color=GOLD)
            thank_you.move_to(ORIGIN)
            self.play(Write(thank_you))
            self.wait(1)
        
        self.play(FadeOut(thank_you))

# Run the animation
if __name__ == "__main__":
    scene = QuantumMechanics3D()
    scene.render()