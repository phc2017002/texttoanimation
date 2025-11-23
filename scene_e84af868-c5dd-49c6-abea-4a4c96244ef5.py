from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import random

class IdenticalParticlesExplanation(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Animation structure for 5+ minutes
        self.show_introduction()
        self.classical_vs_quantum()
        self.indistinguishability_concept()
        self.two_particle_wavefunction()
        self.symmetry_requirements()
        self.bosons_and_fermions()
        self.pauli_exclusion_principle()
        self.exchange_symmetry_mathematics()
        self.physical_examples()
        self.implications_and_applications()
        self.summary_and_conclusion()
        
    def show_introduction(self):
        with self.voiceover(text="Welcome to this comprehensive explanation of identical particles in quantum mechanics. This is one of the most fascinating and counterintuitive aspects of the quantum world.") as tracker:
            title = Text("Identical Particles", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("in Quantum Mechanics", font_size=32, color=TEAL_B)
            subtitle.next_to(title, DOWN, buff=0.4)
            self.play(Write(title))
            self.play(FadeIn(subtitle))
            
        with self.voiceover(text="In the quantum realm, identical particles are truly indistinguishable in a profound way that has no classical analogue. This indistinguishability leads to remarkable consequences that shape the structure of matter and the behavior of the universe.") as tracker:
            # Create visual representation of particles
            particle1 = Circle(radius=0.4, color=YELLOW, fill_opacity=0.7)
            particle2 = Circle(radius=0.4, color=YELLOW, fill_opacity=0.7)
            particles = VGroup(particle1, particle2).arrange(RIGHT, buff=2.5)
            particles.move_to(DOWN * 0.5)
            
            question = Text("Are these the same?", font_size=28)
            question.next_to(particles, DOWN, buff=0.6)
            
            self.play(Create(particles))
            self.play(Write(question))
            
        with self.voiceover(text="Today, we will explore what it means for particles to be identical, how this affects their wave functions, and why this concept is absolutely crucial for understanding atoms, molecules, and all of chemistry.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def classical_vs_quantum(self):
        with self.voiceover(text="Let's begin by understanding the fundamental difference between classical and quantum particles. In classical physics, we can always distinguish particles by tracking their trajectories.") as tracker:
            section_title = Text("Classical vs Quantum", font_size=36, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            # Classical side
            classical_label = Text("Classical Particles", font_size=28, color=GREEN)
            classical_label.move_to(LEFT * 3.5 + UP * 1.5)
            
            # Create classical particles with paths
            c_particle1 = Circle(radius=0.25, color=RED, fill_opacity=0.8).move_to(LEFT * 5 + DOWN * 0.5)
            c_particle2 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8).move_to(LEFT * 2 + DOWN * 0.5)
            
            self.play(Write(classical_label))
            self.play(Create(c_particle1), Create(c_particle2))
            
        with self.voiceover(text="Even if two classical particles look identical, we can label them as particle one and particle two by following their continuous paths through space. They maintain their individual identities over time.") as tracker:
            # Show paths
            path1 = Arrow(LEFT * 5 + DOWN * 0.5, LEFT * 2 + DOWN * 0.5, color=RED, buff=0.25)
            path2 = Arrow(LEFT * 2 + DOWN * 0.5, LEFT * 5 + DOWN * 0.5, color=BLUE, buff=0.25)
            
            label1 = Text("Particle 1", font_size=20, color=RED).next_to(c_particle1, DOWN, buff=0.3)
            label2 = Text("Particle 2", font_size=20, color=BLUE).next_to(c_particle2, DOWN, buff=0.3)
            
            self.play(Write(label1), Write(label2))
            self.play(Create(path1), Create(path2))
            self.play(
                c_particle1.animate.move_to(LEFT * 2 + DOWN * 0.5),
                c_particle2.animate.move_to(LEFT * 5 + DOWN * 0.5),
                run_time=2
            )
            
        with self.voiceover(text="In quantum mechanics, the situation is radically different. Quantum particles do not have definite trajectories. They are described by wavefunctions that spread out in space, and when two identical particles interact, we cannot keep track of which is which.") as tracker:
            # Quantum side
            quantum_label = Text("Quantum Particles", font_size=28, color=PURPLE)
            quantum_label.move_to(RIGHT * 3.5 + UP * 1.5)
            
            self.play(Write(quantum_label))
            
            # Create quantum wavefunctions
            axes = Axes(
                x_range=[-1, 4, 1],
                y_range=[-0.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False, "stroke_width": 1}
            ).move_to(RIGHT * 3.5 + DOWN * 0.8)
            
            wavefunction1 = axes.plot(lambda x: np.exp(-2*(x-0.5)**2), color=YELLOW, stroke_width=3)
            wavefunction2 = axes.plot(lambda x: np.exp(-2*(x-2.5)**2), color=YELLOW, stroke_width=3)
            
            self.play(Create(axes))
            self.play(Create(wavefunction1), Create(wavefunction2))
            
        with self.voiceover(text="When quantum wavefunctions overlap, as they inevitably do during interactions, there is absolutely no way to distinguish which particle is which. This indistinguishability is a fundamental feature of nature, not just a limitation of our measurement capabilities.") as tracker:
            # Show overlap
            combined_wavefunction = axes.plot(
                lambda x: np.exp(-2*(x-0.5)**2) + np.exp(-2*(x-2.5)**2),
                color=ORANGE,
                stroke_width=4
            )
            
            self.play(
                Transform(wavefunction1, combined_wavefunction),
                FadeOut(wavefunction2)
            )
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def indistinguishability_concept(self):
        with self.voiceover(text="Let's dive deeper into what indistinguishability really means. Consider two electrons. They have the same mass, the same charge, and the same spin value. But the indistinguishability goes far beyond just having identical properties.") as tracker:
            title = Text("True Indistinguishability", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show two electrons
            electron1 = Circle(radius=0.35, color=BLUE, fill_opacity=0.6)
            electron2 = Circle(radius=0.35, color=BLUE, fill_opacity=0.6)
            electrons = VGroup(electron1, electron2).arrange(RIGHT, buff=2.0)
            electrons.move_to(UP * 0.5)
            
            e_label = MathTex(r"e^-", font_size=32).move_to(electron1.get_center())
            e_label2 = MathTex(r"e^-", font_size=32).move_to(electron2.get_center())
            
            self.play(Create(electrons))
            self.play(Write(e_label), Write(e_label2))
            
        with self.voiceover(text="In quantum mechanics, if we swap two identical particles, the physical state of the system must remain unchanged. Any observable property we could measure must give the same result before and after the exchange.") as tracker:
            # Show properties
            properties = VGroup(
                Text("Same mass", font_size=24),
                Text("Same charge", font_size=24),
                Text("Same spin", font_size=24),
                Text("Same quantum numbers", font_size=24)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            properties.move_to(DOWN * 1.0)
            
            self.play(Write(properties))
            
        with self.voiceover(text="This means the probability density, which is the absolute square of the wavefunction, must be symmetric under particle exchange. However, the wavefunction itself can acquire a phase factor, and this is where the fascinating distinction between bosons and fermions emerges.") as tracker:
            equation = MathTex(
                r"|\psi(1,2)|^2 = |\psi(2,1)|^2",
                font_size=36
            )
            equation.next_to(properties, DOWN, buff=0.6)
            
            self.play(Write(equation))
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def two_particle_wavefunction(self):
        with self.voiceover(text="Now let's write down the mathematical description of a two-particle system. For distinguishable particles, we would simply write the wavefunction as a product of single-particle states, psi-A of particle one, times psi-B of particle two.") as tracker:
            title = Text("Two-Particle Wavefunctions", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Distinguishable case
            dist_label = Text("Distinguishable:", font_size=28, color=GREEN)
            dist_label.move_to(UP * 1.8)
            
            dist_eq = MathTex(
                r"\psi_{\text{dist}}(1,2) = \psi_A(1) \psi_B(2)",
                font_size=36
            )
            dist_eq.next_to(dist_label, DOWN, buff=0.5)
            
            self.play(Write(dist_label))
            self.play(Write(dist_eq))
            
        with self.voiceover(text="But for identical particles, we must account for the fact that we could have particle one in state A and particle two in state B, or particle one in state B and particle two in state A. Since we cannot tell which is which, both possibilities must contribute to the wavefunction.") as tracker:
            # Show both possibilities
            possibility1 = MathTex(
                r"\psi_A(1) \psi_B(2)",
                font_size=32
            ).move_to(LEFT * 2.5 + DOWN * 0.5)
            
            or_text = Text("or", font_size=28).move_to(DOWN * 0.5)
            
            possibility2 = MathTex(
                r"\psi_A(2) \psi_B(1)",
                font_size=32
            ).move_to(RIGHT * 2.5 + DOWN * 0.5)
            
            self.play(Write(possibility1))
            self.play(Write(or_text))
            self.play(Write(possibility2))
            
        with self.voiceover(text="For identical particles, we must form a linear combination of these two terms. We add them together or subtract them, and normalize the result. The plus sign gives us the symmetric wavefunction, while the minus sign gives us the antisymmetric wavefunction.") as tracker:
            # Symmetric wavefunction
            symmetric_eq = MathTex(
                r"\psi_S = \frac{1}{\sqrt{2}}[\psi_A(1)\psi_B(2) + \psi_A(2)\psi_B(1)]",
                font_size=32
            )
            symmetric_eq.move_to(DOWN * 1.8)
            
            symmetric_label = Text("Symmetric (Bosons)", font_size=24, color=YELLOW)
            symmetric_label.next_to(symmetric_eq, DOWN, buff=0.3)
            
            self.play(Write(symmetric_eq))
            self.play(Write(symmetric_label))
            
        with self.voiceover(text="The normalization factor of one over square root of two ensures that the total probability integrates to one. This construction guarantees that the wavefunction properly accounts for the indistinguishability of the particles.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def symmetry_requirements(self):
        with self.voiceover(text="The symmetry of the wavefunction under particle exchange is not arbitrary - it is dictated by the spin of the particles. This connection between spin and statistics is one of the most profound results in quantum mechanics, known as the spin-statistics theorem.") as tracker:
            title = Text("Exchange Symmetry", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Exchange operator
            exchange_text = Text("Exchange Operator:", font_size=28)
            exchange_text.move_to(UP * 1.8)
            
            exchange_op = MathTex(
                r"\hat{P}_{12} \psi(1,2) = \psi(2,1)",
                font_size=36
            )
            exchange_op.next_to(exchange_text, DOWN, buff=0.5)
            
            self.play(Write(exchange_text))
            self.play(Write(exchange_op))
            
        with self.voiceover(text="When we apply the exchange operator twice, we swap the particles and then swap them back, returning to the original configuration. This means the exchange operator squared must equal the identity. Therefore, the eigenvalues of the exchange operator can only be plus one or minus one.") as tracker:
            # Mathematical derivation
            eigenvalue_eq = MathTex(
                r"\hat{P}_{12}^2 = \hat{I}",
                r"\Rightarrow",
                r"\lambda = \pm 1",
                font_size=36
            )
            eigenvalue_eq.move_to(DOWN * 0.2)
            
            self.play(Write(eigenvalue_eq))
            
        with self.voiceover(text="An eigenvalue of plus one corresponds to a symmetric wavefunction, where swapping particles leaves the wavefunction unchanged. An eigenvalue of minus one corresponds to an antisymmetric wavefunction, where swapping particles introduces a minus sign.") as tracker:
            # Show both cases
            symmetric_case = MathTex(
                r"\psi_S(2,1) = +\psi_S(1,2)",
                font_size=32,
                color=YELLOW
            )
            symmetric_case.move_to(LEFT * 3 + DOWN * 1.5)
            
            antisymmetric_case = MathTex(
                r"\psi_A(2,1) = -\psi_A(1,2)",
                font_size=32,
                color=RED
            )
            antisymmetric_case.move_to(RIGHT * 3 + DOWN * 1.5)
            
            self.play(Write(symmetric_case))
            self.play(Write(antisymmetric_case))
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def bosons_and_fermions(self):
        with self.voiceover(text="Based on their exchange symmetry, all particles in nature fall into exactly two categories: bosons and fermions. This classification is fundamental and determines virtually all the properties of matter and the forces between particles.") as tracker:
            title = Text("Bosons and Fermions", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Bosons are particles with integer spin - zero, one, two, and so on. They obey Bose-Einstein statistics and have symmetric wavefunctions. Examples include photons with spin one, the Higgs boson with spin zero, and helium-4 atoms in certain conditions.") as tracker:
            # Bosons column
            boson_title = Text("BOSONS", font_size=32, color=YELLOW, weight=BOLD)
            boson_title.move_to(LEFT * 3.5 + UP * 2.2)
            
            boson_spin = MathTex(r"\text{Spin: } 0, 1, 2, \ldots", font_size=28)
            boson_spin.next_to(boson_title, DOWN, buff=0.4)
            
            boson_sym = MathTex(r"\psi_S(2,1) = +\psi_S(1,2)", font_size=26)
            boson_sym.next_to(boson_spin, DOWN, buff=0.4)
            
            boson_examples = VGroup(
                Text("• Photons (γ)", font_size=22),
                Text("• Gluons (g)", font_size=22),
                Text("• W/Z bosons", font_size=22),
                Text("• Higgs boson", font_size=22),
                Text("• ⁴He atoms", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            boson_examples.next_to(boson_sym, DOWN, buff=0.5)
            
            self.play(Write(boson_title))
            self.play(Write(boson_spin))
            self.play(Write(boson_sym))
            self.play(Write(boson_examples))
            
        with self.voiceover(text="Fermions are particles with half-integer spin - one-half, three-halves, and so on. They obey Fermi-Dirac statistics and have antisymmetric wavefunctions. All matter particles are fermions, including electrons, protons, neutrons, and quarks.") as tracker:
            # Fermions column
            fermion_title = Text("FERMIONS", font_size=32, color=RED, weight=BOLD)
            fermion_title.move_to(RIGHT * 3.5 + UP * 2.2)
            
            fermion_spin = MathTex(r"\text{Spin: } \frac{1}{2}, \frac{3}{2}, \ldots", font_size=28)
            fermion_spin.next_to(fermion_title, DOWN, buff=0.4)
            
            fermion_sym = MathTex(r"\psi_A(2,1) = -\psi_A(1,2)", font_size=26)
            fermion_sym.next_to(fermion_spin, DOWN, buff=0.4)
            
            fermion_examples = VGroup(
                Text("• Electrons (e⁻)", font_size=22),
                Text("• Protons (p⁺)", font_size=22),
                Text("• Neutrons (n)", font_size=22),
                Text("• Quarks", font_size=22),
                Text("• Neutrinos (ν)", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            fermion_examples.next_to(fermion_sym, DOWN, buff=0.5)
            
            self.play(Write(fermion_title))
            self.play(Write(fermion_spin))
            self.play(Write(fermion_sym))
            self.play(Write(fermion_examples))
            
        with self.voiceover(text="This distinction between bosons and fermions is not merely academic. It determines whether particles can occupy the same quantum state, which in turn determines the structure of atoms, the properties of materials, and the behavior of stars.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def pauli_exclusion_principle(self):
        with self.voiceover(text="The antisymmetric nature of fermion wavefunctions leads directly to one of the most important principles in physics: the Pauli Exclusion Principle. Let's see how this emerges mathematically from the antisymmetry requirement.") as tracker:
            title = Text("Pauli Exclusion Principle", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="Consider what happens if we try to put two identical fermions in the same quantum state. Let's say both particles are in state A. We write the antisymmetric wavefunction as one over square root of two, times the difference of the two terms.") as tracker:
            same_state_label = Text("Two fermions in state A:", font_size=28)
            same_state_label.move_to(UP * 1.5)
            
            antisym_wf = MathTex(
                r"\psi = \frac{1}{\sqrt{2}}[\psi_A(1)\psi_A(2) - \psi_A(2)\psi_A(1)]",
                font_size=34
            )
            antisym_wf.next_to(same_state_label, DOWN, buff=0.5)
            
            self.play(Write(same_state_label))
            self.play(Write(antisym_wf))
            
        with self.voiceover(text="But notice that the two terms in the brackets are identical! Psi-A of one times psi-A of two is the same as psi-A of two times psi-A of one. When we subtract them, we get zero. The wavefunction vanishes completely!") as tracker:
            # Show simplification
            simplification = MathTex(
                r"= \frac{1}{\sqrt{2}}[\psi_A(1)\psi_A(2) - \psi_A(1)\psi_A(2)]",
                font_size=34
            )
            simplification.move_to(DOWN * 0.3)
            
            result = MathTex(
                r"= 0",
                font_size=36,
                color=RED
            )
            result.next_to(simplification, DOWN, buff=0.5)
            
            self.play(Write(simplification))
            self.play(Write(result))
            
        with self.voiceover(text="This is the Pauli Exclusion Principle: no two identical fermions can occupy the same quantum state. It's not a separate postulate we add to quantum mechanics - it's an inevitable consequence of the antisymmetry of fermion wavefunctions.") as tracker:
            pauli_statement = Text(
                "No two fermions in the same state!",
                font_size=32,
                color=YELLOW,
                weight=BOLD
            )
            pauli_statement.move_to(DOWN * 2.0)
            
            self.play(Write(pauli_statement))
            self.wait(1)
            
        with self.voiceover(text="This principle is responsible for the entire structure of the periodic table. Electrons fill up atomic orbitals one at a time because they cannot all collapse into the lowest energy state. Without the Pauli principle, all atoms would behave like hydrogen, and chemistry as we know it would not exist.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def exchange_symmetry_mathematics(self):
        with self.voiceover(text="Let's explore the mathematics of exchange symmetry more rigorously. For a system of N identical particles, we need to construct wavefunctions that have the proper symmetry under all possible particle exchanges.") as tracker:
            title = Text("Exchange Symmetry Mathematics", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="For bosons, the wavefunction must be completely symmetric. We can construct this by summing over all possible permutations of the particle labels. For two particles in states A and B, this gives us the symmetric combination we saw earlier.") as tracker:
            # Symmetric construction
            sym_label = Text("Symmetric (Bosons):", font_size=28, color=YELLOW)
            sym_label.move_to(UP * 1.8)
            
            sym_wf = MathTex(
                r"\psi_S = \frac{1}{\sqrt{2}}(\psi_A(1)\psi_B(2) + \psi_A(2)\psi_B(1))",
                font_size=30
            )
            sym_wf.next_to(sym_label, DOWN, buff=0.4)
            
            self.play(Write(sym_label))
            self.play(Write(sym_wf))
            
        with self.voiceover(text="For fermions, we use the Slater determinant. This is a mathematical construction that automatically ensures antisymmetry. For two particles, the Slater determinant is written as a two-by-two matrix with the single-particle wavefunctions as entries.") as tracker:
            # Antisymmetric construction
            antisym_label = Text("Antisymmetric (Fermions):", font_size=28, color=RED)
            antisym_label.move_to(UP * 0.2)
            
            slater_det = MathTex(
                r"\psi_A = \frac{1}{\sqrt{2}}\begin{vmatrix} \psi_A(1) & \psi_B(1) \\ \psi_A(2) & \psi_B(2) \end{vmatrix}",
                font_size=30
            )
            slater_det.next_to(antisym_label, DOWN, buff=0.4)
            
            self.play(Write(antisym_label))
            self.play(Write(slater_det))
            
        with self.voiceover(text="When we expand this determinant, we get psi-A of one times psi-B of two, minus psi-A of two times psi-B of one. This is exactly the antisymmetric combination. The determinant formulation generalizes beautifully to any number of particles.") as tracker:
            # Expansion
            expansion = MathTex(
                r"= \frac{1}{\sqrt{2}}(\psi_A(1)\psi_B(2) - \psi_A(2)\psi_B(1))",
                font_size=30
            )
            expansion.next_to(slater_det, DOWN, buff=0.5)
            
            self.play(Write(expansion))
            
        with self.voiceover(text="The beautiful property of determinants is that if any two rows or columns are identical - meaning two particles are in the same state - the determinant vanishes. This is the mathematical origin of the Pauli exclusion principle, embedded directly in the structure of the wavefunction.") as tracker:
            property_text = Text(
                "Identical rows → Determinant = 0",
                font_size=26,
                color=ORANGE
            )
            property_text.move_to(DOWN * 2.0)
            
            self.play(Write(property_text))
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def physical_examples(self):
        with self.voiceover(text="Now let's look at some concrete physical examples where the distinction between bosons and fermions has dramatic consequences. These examples illustrate why identical particle statistics is not just abstract theory, but has profound real-world implications.") as tracker:
            title = Text("Physical Examples", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="First, consider the helium atom. Helium-4 has two protons, two neutrons, and two electrons. The nucleus behaves as a boson because it has integer total spin. At very low temperatures, helium-4 atoms can all condense into the same quantum state, forming a superfluid.") as tracker:
            # Helium example
            he_title = Text("Superfluid Helium-4", font_size=30, color=YELLOW)
            he_title.move_to(UP * 1.8)
            
            he_diagram = VGroup(
                Circle(radius=0.5, color=BLUE, fill_opacity=0.3),
                Text("⁴He", font_size=24).move_to(ORIGIN)
            )
            he_diagram.move_to(LEFT * 3.5 + UP * 0.2)
            
            he_description = VGroup(
                Text("• Total spin = 0 (boson)", font_size=22),
                Text("• Can occupy same state", font_size=22),
                Text("• Forms superfluid at T < 2.17 K", font_size=22),
                Text("• Flows without friction", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            he_description.next_to(he_diagram, RIGHT, buff=0.8)
            
            self.play(Write(he_title))
            self.play(Create(he_diagram))
            self.play(Write(he_description))
            
        with self.voiceover(text="In contrast, helium-3 has one less neutron, giving it half-integer spin. It's a fermion! Helium-3 atoms cannot all occupy the same state, so it does not become superfluid under the same conditions. It requires much lower temperatures and forms pairs first, similar to electrons in superconductors.") as tracker:
            # Helium-3 comparison
            he3_title = Text("vs Helium-3", font_size=26, color=RED)
            he3_title.move_to(DOWN * 0.8)
            
            he3_description = VGroup(
                Text("• Total spin = 1/2 (fermion)", font_size=22),
                Text("• Cannot occupy same state", font_size=22),
                Text("• Superfluid only at T < 0.003 K", font_size=22),
                Text("• Forms Cooper pairs first", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            he3_description.next_to(he3_title, DOWN, buff=0.3)
            
            self.play(Write(he3_title))
            self.play(Write(he3_description))
            
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Another dramatic example is white dwarf stars. These are stellar remnants supported against gravitational collapse by electron degeneracy pressure. The electrons are fermions, so they resist being compressed into the same quantum state.") as tracker:
            wd_title = Text("White Dwarf Stars", font_size=32, color=BLUE)
            wd_title.to_edge(UP, buff=1.0)
            self.play(Write(wd_title))
            
            # White dwarf visualization
            star = Circle(radius=1.2, color=WHITE, fill_opacity=0.2, stroke_width=3)
            star.move_to(LEFT * 3.5 + DOWN * 0.3)
            
            electrons = VGroup(*[
                Dot(radius=0.06, color=BLUE).move_to(
                    star.get_center() + np.array([
                        np.random.uniform(-0.8, 0.8),
                        np.random.uniform(-0.8, 0.8),
                        0
                    ])
                ) for _ in range(30)
            ])
            
            self.play(Create(star))
            self.play(Create(electrons))
            
        with self.voiceover(text="The Pauli exclusion principle prevents the electrons from all collapsing to the lowest energy state. This creates a quantum mechanical pressure that can support a star with the mass of the sun in an object the size of Earth. Without fermion statistics, white dwarfs could not exist.") as tracker:
            wd_description = VGroup(
                Text("Electron degeneracy pressure:", font_size=26, weight=BOLD),
                Text("• Fermions cannot occupy same state", font_size=22),
                Text("• Creates quantum pressure", font_size=22),
                Text("• Supports star against gravity", font_size=22),
                Text("• Mass ~ Sun, Size ~ Earth", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            wd_description.move_to(RIGHT * 2.8 + DOWN * 0.5)
            
            self.play(Write(wd_description))
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def implications_and_applications(self):
        with self.voiceover(text="The implications of identical particle statistics extend far beyond these examples. This fundamental quantum property shapes virtually every aspect of the physical world, from the microscopic to the cosmic scale.") as tracker:
            title = Text("Implications & Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="In chemistry, the Pauli exclusion principle determines the electron configuration of atoms. Electrons fill orbitals with opposite spins, creating shells and subshells. This explains the periodic table, chemical bonding, and molecular structure - essentially all of chemistry emerges from fermion statistics.") as tracker:
            # Chemistry application
            chem_title = Text("Chemistry & Materials", font_size=28, color=GREEN)
            chem_title.move_to(UP * 1.8)
            
            atom_shells = VGroup(
                Circle(radius=0.4, color=BLUE, stroke_width=2),
                Circle(radius=0.8, color=GREEN, stroke_width=2),
                Circle(radius=1.2, color=RED, stroke_width=2)
            )
            atom_shells.move_to(LEFT * 4 + DOWN * 0.2)
            
            nucleus = Dot(color=YELLOW, radius=0.1).move_to(atom_shells.get_center())
            
            chem_points = VGroup(
                Text("• Electron shells structure", font_size=22),
                Text("• Chemical bonding", font_size=22),
                Text("• Periodic table organization", font_size=22),
                Text("• Molecular orbitals", font_size=22),
                Text("• Band structure in solids", font_size=22)
            ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            chem_points.next_to(atom_shells, RIGHT, buff=1.2)
            
            self.play(Write(chem_title))
            self.play(Create(atom_shells), Create(nucleus))
            self.play(Write(chem_points))
            
        with self.voiceover(text="In condensed matter physics, boson and fermion statistics lead to completely different collective behaviors. Bosons can form Bose-Einstein condensates, where macroscopic numbers of particles occupy the same quantum state. This leads to phenomena like superconductivity and superfluidity.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="In particle physics, the spin-statistics connection is absolute. Every force-carrying particle is a boson - photons mediate electromagnetism, gluons mediate the strong force, and W and Z bosons mediate the weak force. Meanwhile, all matter particles are fermions.") as tracker:
            particle_title = Text("Particle Physics", font_size=32, color=BLUE)
            particle_title.to_edge(UP, buff=1.0)
            self.play(Write(particle_title))
            
            # Standard model organization
            forces = VGroup(
                Text("Force Carriers (Bosons):", font_size=26, weight=BOLD, color=YELLOW),
                Text("• Photon (γ) - Electromagnetic", font_size=22),
                Text("• Gluons (g) - Strong force", font_size=22),
                Text("• W±, Z - Weak force", font_size=22),
                Text("• Graviton (g) - Gravity*", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            forces.move_to(LEFT * 3.5 + DOWN * 0.5)
            
            matter = VGroup(
                Text("Matter Particles (Fermions):", font_size=26, weight=BOLD, color=RED),
                Text("• Quarks (u, d, c, s, t, b)", font_size=22),
                Text("• Leptons (e, μ, τ)", font_size=22),
                Text("• Neutrinos (νₑ, νᵤ, ν_τ)", font_size=22)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            matter.move_to(RIGHT * 3.2 + DOWN * 0.5)
            
            self.play(Write(forces))
            self.play(Write(matter))
            
        with self.voiceover(text="This organization of the standard model - bosons carrying forces, fermions making up matter - is not accidental. It reflects the deep connection between spin, statistics, and the fundamental structure of quantum field theory.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
    def summary_and_conclusion(self):
        with self.voiceover(text="Let's summarize what we've learned about identical particles in quantum mechanics. We've seen that this concept is far more than a technical detail - it's a cornerstone of our understanding of nature.") as tracker:
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
        with self.voiceover(text="First, quantum particles of the same type are truly indistinguishable. Unlike classical particles, we cannot track their individual identities. This indistinguishability is not due to measurement limitations, but is a fundamental feature of quantum mechanics.") as tracker:
            point1 = VGroup(
                Text("1. Fundamental Indistinguishability", font_size=28, weight=BOLD),
                Text("• No individual particle identities", font_size=24),
                Text("• Wavefunctions must account for all permutations", font_size=24)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point1.move_to(UP * 1.5)
            
            self.play(Write(point1))
            
        with self.voiceover(text="Second, particles fall into two categories based on spin. Bosons have integer spin and symmetric wavefunctions. Fermions have half-integer spin and antisymmetric wavefunctions. This is the spin-statistics theorem, one of the deepest results in quantum field theory.") as tracker:
            point2 = VGroup(
                Text("2. Spin-Statistics Connection", font_size=28, weight=BOLD),
                Text("• Integer spin → Bosons → Symmetric", font_size=24),
                Text("• Half-integer spin → Fermions → Antisymmetric", font_size=24)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point2.move_to(UP * 0.0)
            
            self.play(Write(point2))
            
        with self.voiceover(text="Third, the antisymmetry of fermion wavefunctions leads to the Pauli exclusion principle. No two fermions can occupy the same quantum state. This single principle explains the structure of atoms, the periodic table, and the stability of matter.") as tracker:
            point3 = VGroup(
                Text("3. Pauli Exclusion Principle", font_size=28, weight=BOLD),
                Text("• Fermions cannot share quantum states", font_size=24),
                Text("• Foundation of atomic structure", font_size=24)
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            point3.move_to(DOWN * 1.5)
            
            self.play(Write(point3))
            
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="The physics of identical particles demonstrates the profound difference between quantum and classical mechanics. It shows us that nature at its most fundamental level operates according to principles that have no classical analogue.") as tracker:
            conclusion_title = Text("Conclusion", font_size=36, color=BLUE)
            conclusion_title.to_edge(UP, buff=1.0)
            self.play(Write(conclusion_title))
            
            quote = Text(
                '"The same, yet not the same"',
                font_size=32,
                color=YELLOW,
                slant=ITALIC
            )
            quote.move_to(UP * 0.8)
            
            self.play(Write(quote))
            
        with self.voiceover(text="From the structure of atoms to the behavior of stars, from superconductivity to the standard model of particle physics, identical particle statistics shapes our universe at every scale. Understanding this concept is essential for understanding modern physics.") as tracker:
            final_text = VGroup(
                Text("Identical particle statistics:", font_size=26),
                Text("• Explains chemistry and materials", font_size=24),
                Text("• Determines stellar structure", font_size=24),
                Text("• Organizes the Standard Model", font_size=24),
                Text("• Enables quantum technologies", font_size=24)
            ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            final_text.move_to(DOWN * 0.8)
            
            self.play(Write(final_text))
            
        with self.voiceover(text="Thank you for joining me in this exploration of identical particles in quantum mechanics. I hope this has given you a deeper appreciation for one of the most beautiful and consequential principles in physics.") as tracker:
            self.wait(1)
            
        self.play(FadeOut(*self.mobjects))
        
        # Final thank you
        with self.voiceover(text="Keep exploring the quantum world!") as tracker:
            thank_you = Text("Thank You!", font_size=36, color=BLUE)
            self.play(Write(thank_you))
            self.wait(1)
            
        self.play(FadeOut(thank_you))

# Run the animation
if __name__ == "__main__":
    scene = IdenticalParticlesExplanation()
    scene.render()