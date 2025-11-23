# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text

from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService

class IdenticalParticlesQuantumMechanics(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Call all sections in sequence
        self.introduction()
        self.classical_vs_quantum_distinguishability()
        self.indistinguishability_principle()
        self.symmetric_and_antisymmetric_wavefunctions()
        self.bosons_and_fermions()
        self.pauli_exclusion_principle()
        self.exchange_interaction()
        self.physical_consequences()
        self.applications()
        self.conclusion()
    
    def introduction(self):
        """Introduction to identical particles - 30 seconds"""
        with self.voiceover(
            text="Welcome to this comprehensive exploration of identical particles in quantum mechanics. This fundamental concept revolutionizes our understanding of matter and explains phenomena that classical physics cannot."
        ) as tracker:
            # Title
            title = Text("Identical Particles", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            subtitle = Text("in Quantum Mechanics", font_size=32, color=TEAL_B)
            subtitle.next_to(title, DOWN, buff=0.3)
            
            self.play(Write(title))
            self.play(FadeIn(subtitle))
        
        with self.voiceover(
            text="Unlike classical particles which can always be distinguished by tracking their trajectories, quantum particles of the same type are fundamentally indistinguishable. This is not just a practical limitation, but a deep property of nature that leads to remarkable consequences."
        ) as tracker:
            # Show two particles
            particle1 = Circle(radius=0.4, color=YELLOW, fill_opacity=0.7)
            particle1.move_to(LEFT * 2.5 + DOWN * 0.5)
            particle2 = Circle(radius=0.4, color=YELLOW, fill_opacity=0.7)
            particle2.move_to(RIGHT * 2.5 + DOWN * 0.5)
            
            label1 = Text("Electron 1?", font_size=24).next_to(particle1, DOWN, buff=0.4)
            label2 = Text("Electron 2?", font_size=24).next_to(particle2, DOWN, buff=0.4)
            
            question = Text("Can we tell them apart?", font_size=28, color=RED)
            question.move_to(DOWN * 2.5)
            
            self.play(FadeIn(particle1), FadeIn(particle2))
            self.play(Write(label1), Write(label2))
            self.play(Write(question))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def classical_vs_quantum_distinguishability(self):
        """Classical vs quantum distinguishability - 40 seconds"""
        with self.voiceover(
            text="In classical mechanics, we can always distinguish between particles by continuously tracking their paths. Even if two billiard balls look identical, we know which is which by watching their trajectories."
        ) as tracker:
            # Title
            title = Text("Classical vs Quantum", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Classical section - left side
            classical_label = Text("Classical Physics", font_size=28, color=GREEN)
            classical_label.move_to(LEFT * 3.5 + UP * 2.2)
            
            # Two classical particles with paths
            ball1_start = LEFT * 5 + UP * 0.5
            ball2_start = LEFT * 2 + UP * 0.5
            ball1_end = LEFT * 2 + DOWN * 1.5
            ball2_end = LEFT * 5 + DOWN * 1.5
            
            ball1 = Circle(radius=0.25, color=RED, fill_opacity=0.8)
            ball1.move_to(ball1_start)
            ball2 = Circle(radius=0.25, color=BLUE, fill_opacity=0.8)
            ball2.move_to(ball2_start)
            
            path1 = Arrow(ball1_start, ball1_end, color=RED, buff=0.25)
            path2 = Arrow(ball2_start, ball2_end, color=BLUE, buff=0.25)
            
            check = Text("✓ Distinguishable", font_size=20, color=GREEN)
            check.move_to(LEFT * 3.5 + DOWN * 2.5)
            
            self.play(Write(classical_label))
            self.play(FadeIn(ball1), FadeIn(ball2))
            self.play(Create(path1), Create(path2))
            self.play(
                ball1.animate.move_to(ball1_end),
                ball2.animate.move_to(ball2_end),
                run_time=2
            )
            self.play(Write(check))
        
        with self.voiceover(
            text="However, in quantum mechanics, particles don't have definite trajectories. They exist in superposition states, and when two identical particles interact and separate, there is fundamentally no way to determine which particle is which. This is the principle of quantum indistinguishability."
        ) as tracker:
            # Quantum section - right side
            quantum_label = Text("Quantum Mechanics", font_size=28, color=PURPLE)
            quantum_label.move_to(RIGHT * 3.5 + UP * 2.2)
            
            # Two quantum particles with wave packets
            wave1 = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5, stroke_width=2)
            wave1.move_to(RIGHT * 5 + UP * 0.5)
            wave2 = Circle(radius=0.3, color=YELLOW, fill_opacity=0.5, stroke_width=2)
            wave2.move_to(RIGHT * 2 + UP * 0.5)
            
            # Fuzzy paths
            fuzzy1 = DashedLine(RIGHT * 5 + UP * 0.5, RIGHT * 2 + DOWN * 1.5, color=YELLOW, dash_length=0.1)
            fuzzy2 = DashedLine(RIGHT * 2 + UP * 0.5, RIGHT * 5 + DOWN * 1.5, color=YELLOW, dash_length=0.1)
            
            cross = Text("✗ Indistinguishable", font_size=20, color=RED)
            cross.move_to(RIGHT * 3.5 + DOWN * 2.5)
            
            self.play(Write(quantum_label))
            self.play(FadeIn(wave1), FadeIn(wave2))
            self.play(Create(fuzzy1), Create(fuzzy2))
            
            # Show overlap/uncertainty
            wave1_end = wave1.copy().move_to(RIGHT * 2 + DOWN * 1.5)
            wave2_end = wave2.copy().move_to(RIGHT * 5 + DOWN * 1.5)
            
            self.play(
                Transform(wave1, wave1_end),
                Transform(wave2, wave2_end),
                run_time=2
            )
            self.play(Write(cross))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def indistinguishability_principle(self):
        """The indistinguishability principle - 35 seconds"""
        with self.voiceover(
            text="The principle of indistinguishability states that swapping two identical particles cannot produce a physically observable change. Mathematically, this means the probability density must remain unchanged under particle exchange."
        ) as tracker:
            # Title
            title = Text("Indistinguishability Principle", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show the mathematical statement
            equation1 = MathTex(
                r"|\psi(x_1, x_2)|^2 = |\psi(x_2, x_1)|^2",
                font_size=36
            )
            equation1.move_to(UP * 1.2)
            
            explanation = Text("Probability unchanged under exchange", font_size=24, color=YELLOW)
            explanation.next_to(equation1, DOWN, buff=0.5)
            
            self.play(Write(equation1))
            self.play(FadeIn(explanation))
        
        with self.voiceover(
            text="This constraint means that the wavefunction itself can only change by a phase factor when we exchange particles. Since exchanging twice returns to the original configuration, this phase factor must square to one, giving us only two possibilities: plus one or minus one."
        ) as tracker:
            # Derive the constraint
            equation2 = MathTex(
                r"\psi(x_2, x_1) = e^{i\phi} \psi(x_1, x_2)",
                font_size=36
            )
            equation2.move_to(DOWN * 0.3)
            
            self.play(Write(equation2))
            
            # Exchange twice
            equation3 = MathTex(
                r"\psi(x_1, x_2) = e^{2i\phi} \psi(x_1, x_2)",
                font_size=36
            )
            equation3.next_to(equation2, DOWN, buff=0.5)
            
            self.play(Write(equation3))
            
            # Therefore
            arrow = MathTex(r"\Downarrow", font_size=36, color=YELLOW)
            arrow.next_to(equation3, DOWN, buff=0.3)
            
            equation4 = MathTex(
                r"e^{i\phi} = \pm 1",
                font_size=36,
                color=GREEN
            )
            equation4.next_to(arrow, DOWN, buff=0.3)
            
            self.play(Write(arrow))
            self.play(Write(equation4))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def symmetric_and_antisymmetric_wavefunctions(self):
        """Symmetric and antisymmetric wavefunctions - 40 seconds"""
        with self.voiceover(
            text="This leads us to two types of wavefunctions. Symmetric wavefunctions remain unchanged under particle exchange, while antisymmetric wavefunctions change sign. These two possibilities correspond to fundamentally different types of particles."
        ) as tracker:
            # Title
            title = Text("Two Types of Wavefunctions", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Symmetric
            sym_label = Text("Symmetric (+1)", font_size=28, color=GREEN)
            sym_label.move_to(LEFT * 3.5 + UP * 2.0)
            
            sym_eq = MathTex(
                r"\psi_S(x_1, x_2) = \psi_S(x_2, x_1)",
                font_size=32
            )
            sym_eq.move_to(LEFT * 3.5 + UP * 0.8)
            
            sym_form = MathTex(
                r"= \frac{1}{\sqrt{2}}[\phi_a(x_1)\phi_b(x_2)",
                r"+ \phi_a(x_2)\phi_b(x_1)]",
                font_size=28
            )
            sym_form.move_to(LEFT * 3.5 + DOWN * 0.2)
            
            self.play(Write(sym_label))
            self.play(Write(sym_eq))
            self.play(Write(sym_form))
        
        with self.voiceover(
            text="Antisymmetric wavefunctions change sign under exchange. Notice the crucial minus sign in the construction. This seemingly small difference has profound physical consequences, including the Pauli exclusion principle."
        ) as tracker:
            # Antisymmetric
            anti_label = Text("Antisymmetric (-1)", font_size=28, color=RED)
            anti_label.move_to(RIGHT * 3.5 + UP * 2.0)
            
            anti_eq = MathTex(
                r"\psi_A(x_1, x_2) = -\psi_A(x_2, x_1)",
                font_size=32
            )
            anti_eq.move_to(RIGHT * 3.5 + UP * 0.8)
            
            anti_form = MathTex(
                r"= \frac{1}{\sqrt{2}}[\phi_a(x_1)\phi_b(x_2)",
                r"- \phi_a(x_2)\phi_b(x_1)]",
                font_size=28
            )
            anti_form.move_to(RIGHT * 3.5 + DOWN * 0.2)
            
            self.play(Write(anti_label))
            self.play(Write(anti_eq))
            self.play(Write(anti_form))
            
            # Highlight the minus sign
            # minus_box = SurroundingRectangle(anti_form[1][0], color=YELLOW, buff=0.1)  # Auto-disabled: indexed SurroundingRectangle
            # self.play(Create(minus_box))  # Auto-disabled: uses disabled SurroundingRectangle
            self.wait(1)
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def bosons_and_fermions(self):
        """Bosons and Fermions - 45 seconds"""
        with self.voiceover(
            text="Particles with symmetric wavefunctions are called bosons, named after the Indian physicist Satyendra Nath Bose. These particles have integer spin: zero, one, two, and so on. Examples include photons, the particles of light, and the recently discovered Higgs boson."
        ) as tracker:
            # Title
            title = Text("Bosons and Fermions", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Bosons - left side
            boson_title = Text("BOSONS", font_size=32, color=GREEN)
            boson_title.move_to(LEFT * 3.5 + UP * 2.2)
            
            boson_sym = MathTex(r"\psi_S(1,2) = +\psi_S(2,1)", font_size=28)
            boson_sym.move_to(LEFT * 3.5 + UP * 1.2)
            
            boson_spin = Text("Integer Spin", font_size=24, color=YELLOW)
            boson_spin.move_to(LEFT * 3.5 + UP * 0.5)
            
            boson_spin_vals = MathTex(r"s = 0, 1, 2, \ldots", font_size=28)
            boson_spin_vals.move_to(LEFT * 3.5 + DOWN * 0.1)
            
            self.play(Write(boson_title))
            self.play(Write(boson_sym))
            self.play(Write(boson_spin))
            self.play(Write(boson_spin_vals))
            
            # Examples
            examples_b = VGroup(
                Text("• Photons (γ)", font_size=22),
                Text("• Gluons (g)", font_size=22),
                Text("• W±, Z bosons", font_size=22),
                Text("• Higgs boson", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            examples_b.move_to(LEFT * 3.5 + DOWN * 1.5)
            
            self.play(Write(examples_b))
        
        with self.voiceover(
            text="Particles with antisymmetric wavefunctions are called fermions, named after Enrico Fermi. Fermions have half-integer spin: one-half, three-halves, and so on. This category includes all matter particles: electrons, protons, neutrons, and quarks. The spin-statistics theorem proves that this connection between spin and statistics is not accidental but fundamental."
        ) as tracker:
            # Fermions - right side
            fermion_title = Text("FERMIONS", font_size=32, color=RED)
            fermion_title.move_to(RIGHT * 3.5 + UP * 2.2)
            
            fermion_sym = MathTex(r"\psi_A(1,2) = -\psi_A(2,1)", font_size=28)
            fermion_sym.move_to(RIGHT * 3.5 + UP * 1.2)
            
            fermion_spin = Text("Half-Integer Spin", font_size=24, color=YELLOW)
            fermion_spin.move_to(RIGHT * 3.5 + UP * 0.5)
            
            fermion_spin_vals = MathTex(r"s = \frac{1}{2}, \frac{3}{2}, \ldots", font_size=28)
            fermion_spin_vals.move_to(RIGHT * 3.5 + DOWN * 0.1)
            
            self.play(Write(fermion_title))
            self.play(Write(fermion_sym))
            self.play(Write(fermion_spin))
            self.play(Write(fermion_spin_vals))
            
            # Examples
            examples_f = VGroup(
                Text("• Electrons (e⁻)", font_size=22),
                Text("• Protons (p⁺)", font_size=22),
                Text("• Neutrons (n)", font_size=22),
                Text("• Quarks (u, d, ...)", font_size=22)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            examples_f.move_to(RIGHT * 3.5 + DOWN * 1.5)
            
            self.play(Write(examples_f))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def pauli_exclusion_principle(self):
        """Pauli Exclusion Principle - 40 seconds"""
        with self.voiceover(
            text="The Pauli exclusion principle is a direct consequence of antisymmetric wavefunctions. If we try to put two identical fermions in the same quantum state, meaning both x one and x two equal to x, the wavefunction must vanish."
        ) as tracker:
            # Title
            title = Text("Pauli Exclusion Principle", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Show the derivation
            step1 = MathTex(
                r"\psi_A(x, x) = -\psi_A(x, x)",
                font_size=36
            )
            step1.move_to(UP * 1.5)
            
            self.play(Write(step1))
            
            arrow1 = MathTex(r"\Downarrow", font_size=36, color=YELLOW)
            arrow1.next_to(step1, DOWN, buff=0.4)
            
            step2 = MathTex(
                r"2\psi_A(x, x) = 0",
                font_size=36
            )
            step2.next_to(arrow1, DOWN, buff=0.4)
            
            self.play(Write(arrow1), Write(step2))
            
            arrow2 = MathTex(r"\Downarrow", font_size=36, color=YELLOW)
            arrow2.next_to(step2, DOWN, buff=0.4)
            
            conclusion = MathTex(
                r"\psi_A(x, x) = 0",
                font_size=36,
                color=RED
            )
            conclusion.next_to(arrow2, DOWN, buff=0.4)
            
            self.play(Write(arrow2), Write(conclusion))
        
        with self.voiceover(
            text="This means two identical fermions cannot occupy the same quantum state simultaneously. This principle is responsible for the structure of atoms, the periodic table, and the stability of matter itself. Without it, all electrons would collapse into the lowest energy state, and chemistry as we know it would not exist."
        ) as tracker:
            # Visual representation
            box = Rectangle(height=0.8, width=6, color=WHITE)
            box.move_to(DOWN * 2.2)
            
            state_label = Text("Same Quantum State", font_size=24)
            state_label.next_to(box, UP, buff=0.3)
            
            # Try to add two fermions
            fermion1 = Circle(radius=0.25, color=RED, fill_opacity=0.8)
            fermion1.move_to(box.get_center() + LEFT * 0.5)
            
            fermion2 = Circle(radius=0.25, color=RED, fill_opacity=0.8)
            fermion2.move_to(UP * 1.5)
            
            cross = Text("✗ FORBIDDEN", font_size=32, color=RED)
            cross.next_to(box, DOWN, buff=0.4)
            
            self.play(Create(box), Write(state_label))
            self.play(FadeIn(fermion1))
            self.play(fermion2.animate.move_to(box.get_center() + RIGHT * 0.5), run_time=1.5)
            self.play(Write(cross))
            self.play(
                fermion2.animate.set_opacity(0),
                cross.animate.set_color(YELLOW),
                run_time=1
            )
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def exchange_interaction(self):
        """Exchange interaction and energy - 35 seconds"""
        with self.voiceover(
            text="The symmetry requirements lead to an additional contribution to the energy called the exchange interaction. This is a purely quantum mechanical effect with no classical analog. It arises from the interference between the direct and exchange terms in the wavefunction."
        ) as tracker:
            # Title
            title = Text("Exchange Interaction", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Energy expression
            energy_label = Text("Total Energy:", font_size=28, color=YELLOW)
            energy_label.move_to(UP * 1.8)
            
            energy_eq = MathTex(
                r"E = E_{\text{direct}} \pm E_{\text{exchange}}",
                font_size=36
            )
            energy_eq.next_to(energy_label, DOWN, buff=0.4)
            
            self.play(Write(energy_label))
            self.play(Write(energy_eq))
            
            # Plus for symmetric, minus for antisymmetric
            sign_note = Text("+ for bosons, − for fermions", font_size=24, color=TEAL_B)
            sign_note.next_to(energy_eq, DOWN, buff=0.5)
            
            self.play(Write(sign_note))
        
        with self.voiceover(
            text="The exchange energy depends on the overlap of the wavefunctions. For fermions with parallel spins, the antisymmetric spatial wavefunction reduces the probability of the particles being close together, effectively creating a repulsion. This exchange force is responsible for magnetism in materials and the stability of white dwarf stars."
        ) as tracker:
            # Exchange integral
            exchange_label = Text("Exchange Energy:", font_size=28, color=YELLOW)
            exchange_label.move_to(DOWN * 0.5)
            
            exchange_integral = MathTex(
                r"E_{\text{ex}} = \int \phi_a^*(x_1) \phi_b^*(x_2) V(x_1, x_2) \phi_b(x_1) \phi_a(x_2) dx_1 dx_2",
                font_size=24
            )
            exchange_integral.next_to(exchange_label, DOWN, buff=0.4)
            
            self.play(Write(exchange_label))
            self.play(Write(exchange_integral))
            
            # Note about overlap
            overlap_note = Text("Depends on wavefunction overlap", font_size=22, color=GREEN)
            overlap_note.move_to(DOWN * 2.5)
            
            self.play(Write(overlap_note))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def physical_consequences(self):
        """Physical consequences - 40 seconds"""
        with self.voiceover(
            text="The consequences of quantum statistics are profound and far-reaching. For bosons, multiple particles can occupy the same state, leading to phenomena like Bose-Einstein condensation, where thousands of atoms behave as a single quantum entity at temperatures near absolute zero."
        ) as tracker:
            # Title
            title = Text("Physical Consequences", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Bosons consequences
            boson_label = Text("Bosons: Multiple Occupancy", font_size=28, color=GREEN)
            boson_label.move_to(UP * 1.8)
            
            self.play(Write(boson_label))
            
            # Show multiple bosons in same state
            states = VGroup()
            for i in range(3):
                state_box = Rectangle(height=0.6, width=2.5, color=WHITE)
                state_box.move_to(UP * (0.6 - i * 0.9))
                
                # Add multiple particles to lowest state
                if i == 2:
                    particles = VGroup(*[
                        Circle(radius=0.15, color=GREEN, fill_opacity=0.7)
                        for _ in range(5)
                    ]).arrange(RIGHT, buff=0.1)
                    particles.move_to(state_box.get_center())
                    states.add(VGroup(state_box, particles))
                else:
                    states.add(state_box)
            
            states.move_to(LEFT * 3.5 + DOWN * 0.3)
            
            bec_label = Text("Bose-Einstein\nCondensate", font_size=20, color=YELLOW)
            bec_label.next_to(states, DOWN, buff=0.4)
            
            self.play(Create(states))
            self.play(Write(bec_label))
        
        with self.voiceover(
            text="For fermions, the exclusion principle forces electrons into higher energy states, creating the shell structure of atoms. This explains the periodic table, chemical bonding, and why matter has volume. The degeneracy pressure from packed fermions even prevents stellar collapse in neutron stars."
        ) as tracker:
            # Fermions consequences
            fermion_label = Text("Fermions: Forced Separation", font_size=28, color=RED)
            fermion_label.move_to(RIGHT * 3.5 + UP * 1.8)
            
            self.play(Write(fermion_label))
            
            # Show electrons filling shells
            shells = VGroup()
            shell_data = [(1, 2), (2, 4), (3, 6)]  # (shell, max electrons)
            
            for i, (shell_n, max_e) in enumerate(shell_data):
                shell_circle = Circle(radius=0.3 + i*0.35, color=BLUE, stroke_width=2)
                shell_circle.move_to(RIGHT * 3.5 + DOWN * 0.5)
                
                electrons = VGroup(*[
                    Dot(radius=0.08, color=RED)
                    for _ in range(min(max_e, 2))
                ]).arrange_in_grid(rows=1, buff=0.2)
                
                angle = 2 * PI * i / 3
                electrons.move_to(shell_circle.get_center() + 
                                (0.3 + i*0.35) * np.array([np.cos(angle), np.sin(angle), 0]))
                
                shells.add(VGroup(shell_circle, electrons))
            
            atom_label = Text("Atomic\nStructure", font_size=20, color=YELLOW)
            atom_label.next_to(shells, DOWN, buff=0.5)
            
            self.play(Create(shells))
            self.play(Write(atom_label))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def applications(self):
        """Real-world applications - 35 seconds"""
        with self.voiceover(
            text="Understanding identical particles is crucial for modern technology. Lasers rely on stimulated emission, where photons as bosons preferentially occupy the same quantum state, creating coherent light. Superconductivity arises when electrons pair up to form bosonic Cooper pairs."
        ) as tracker:
            # Title
            title = Text("Real-World Applications", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Application 1: Lasers
            laser_title = Text("1. Lasers", font_size=28, color=GREEN)
            laser_title.move_to(LEFT * 4.5 + UP * 1.8)
            
            laser_desc = Text("Coherent photons\n(bosons) in same state", font_size=20)
            laser_desc.next_to(laser_title, DOWN, buff=0.3)
            
            # Simple laser visualization
            laser_beam = Arrow(LEFT * 5 + UP * 0.3, LEFT * 2 + UP * 0.3, color=RED, buff=0)
            photons = VGroup(*[
                Circle(radius=0.1, color=YELLOW, fill_opacity=0.8).move_to(LEFT * (5 - i*0.5) + UP * 0.3)
                for i in range(6)
            ])
            
            self.play(Write(laser_title))
            self.play(Write(laser_desc))
            self.play(Create(laser_beam), FadeIn(photons))
        
        with self.voiceover(
            text="Quantum computing exploits fermionic and bosonic properties. Semiconductors depend on electron band structure from the Pauli principle. Even the stability of neutron stars relies on neutron degeneracy pressure. These quantum statistical effects shape our universe from the smallest scales to the largest."
        ) as tracker:
            # Application 2: Semiconductors
            semi_title = Text("2. Semiconductors", font_size=28, color=BLUE)
            semi_title.move_to(RIGHT * 0.5 + UP * 1.8)
            
            semi_desc = Text("Band structure from\nPauli exclusion", font_size=20)
            semi_desc.next_to(semi_title, DOWN, buff=0.3)
            
            # Band gap visualization
            valence = Rectangle(height=0.5, width=2, color=BLUE, fill_opacity=0.5)
            valence.move_to(RIGHT * 0.5 + UP * 0.1)
            
            conduction = Rectangle(height=0.5, width=2, color=RED, fill_opacity=0.5)
            conduction.move_to(RIGHT * 0.5 + UP * 1.0)
            
            gap_label = Text("Band Gap", font_size=18, color=YELLOW)
            gap_label.move_to(RIGHT * 0.5 + UP * 0.55)
            
            self.play(Write(semi_title))
            self.play(Write(semi_desc))
            self.play(FadeIn(valence), FadeIn(conduction))
            self.play(Write(gap_label))
            
            # Application 3: White dwarfs
            star_title = Text("3. Stellar Physics", font_size=28, color=PURPLE)
            star_title.move_to(RIGHT * 5 + UP * 1.8)
            
            star_desc = Text("Degeneracy\npressure", font_size=20)
            star_desc.next_to(star_title, DOWN, buff=0.3)
            
            # Simple star
            star = Circle(radius=0.5, color=WHITE, fill_opacity=0.6)
            star.move_to(RIGHT * 5 + UP * 0.3)
            
            self.play(Write(star_title))
            self.play(Write(star_desc))
            self.play(FadeIn(star))
        
        # Cleanup
        self.play(FadeOut(*self.mobjects))
    
    def conclusion(self):
        """Conclusion and summary - 30 seconds"""
        with self.voiceover(
            text="In summary, the quantum mechanical treatment of identical particles reveals a profound truth about nature. Particles are not just identical in their properties, but fundamentally indistinguishable in a way that has no classical counterpart."
        ) as tracker:
            # Title
            title = Text("Summary", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            # Key points
            key_points = VGroup(
                Text("✓ Quantum indistinguishability is fundamental", font_size=24),
                Text("✓ Two types: Bosons (+) and Fermions (−)", font_size=24),
                Text("✓ Pauli principle from antisymmetry", font_size=24),
                Text("✓ Exchange interaction is purely quantum", font_size=24),
                Text("✓ Explains matter, chemistry, and cosmos", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
            
            key_points.move_to(DOWN * 0.3)
            
            for point in key_points:
                self.play(FadeIn(point), run_time=0.6)
        
        with self.voiceover(
            text="This simple principle of exchange symmetry underlies the structure of matter, the periodic table, the behavior of materials, and even the life cycle of stars. Thank you for exploring this fascinating aspect of quantum mechanics!"
        ) as tracker:
            # Final equation
            final_eq = MathTex(
                r"\psi(\ldots, x_i, \ldots, x_j, \ldots) = \pm \psi(\ldots, x_j, \ldots, x_i, \ldots)",
                font_size=32,
                color=YELLOW
            )
            final_eq.move_to(DOWN * 2.8)
            
            self.play(Write(final_eq))
            self.wait(1)
        
        # Final cleanup and thank you
        self.play(FadeOut(*self.mobjects))
        
        thanks = Text("Thank You!", font_size=36, color=BLUE)
        self.play(Write(thanks))
        self.wait(2)
        self.play(FadeOut(thanks))

# Run the animation
if __name__ == "__main__":
    scene = IdenticalParticlesQuantumMechanics()
    scene.render()