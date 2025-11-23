from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np
import random

class HeisenbergUncertaintyPrinciple(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Call all sections in order
        self.introduction()
        self.historical_context()
        self.classical_vs_quantum()
        self.mathematical_formulation()
        self.position_uncertainty()
        self.momentum_uncertainty()
        self.wave_particle_duality()
        self.physical_implications()
        self.measurement_problem()
        self.real_world_examples()
        self.philosophical_implications()
        self.conclusion()

    def introduction(self):
        """Introduction to the Heisenberg Uncertainty Principle"""
        with self.voiceover(text="Welcome to this comprehensive exploration of one of the most profound principles in quantum mechanics: the Heisenberg Uncertainty Principle. This principle fundamentally changed our understanding of reality and showed us that nature has built-in limitations on what we can know about the physical world.") as tracker:
            title = Text("Heisenberg Uncertainty Principle", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            subtitle = Text("A Journey into Quantum Mechanics", font_size=24, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.8)
            self.play(FadeIn(subtitle), run_time=1.5)
        
        with self.voiceover(text="By the end of this animation, you will understand not just what the uncertainty principle states, but why it exists, how it manifests in the quantum world, and what profound implications it has for our understanding of measurement, observation, and reality itself.") as tracker:
            quantum_cloud = VGroup()
            for i in range(20):
                dot = Dot(color=random.choice([BLUE, GREEN, PURPLE, YELLOW]), radius=0.08)
                dot.move_to([np.random.uniform(-5, 5), np.random.uniform(-2, 1), 0])
                quantum_cloud.add(dot)
            
            self.play(FadeIn(quantum_cloud), run_time=2)
            self.play(quantum_cloud.animate.shift(DOWN * 0.5), run_time=1.5)
        
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        """Historical background of the uncertainty principle"""
        with self.voiceover(text="In nineteen twenty-seven, Werner Heisenberg, a young German physicist, made a discovery that would revolutionize physics. At the time, quantum mechanics was still in its infancy, and scientists were grappling with strange experimental results that classical physics could not explain.") as tracker:
            year = Text("1927", font_size=36, color=GOLD)
            year.move_to(UP * 2)
            self.play(Write(year), run_time=2)
            
            heisenberg_name = Text("Werner Heisenberg", font_size=32, color=WHITE)
            heisenberg_name.move_to(ORIGIN)
            self.play(FadeIn(heisenberg_name), run_time=2)
            
            context = Text("The Birth of Quantum Mechanics", font_size=24, color=BLUE)
            context.move_to(DOWN * 1.5)
            self.play(Write(context), run_time=1.5)
        
        with self.voiceover(text="Heisenberg realized that the act of measuring a particle's position inevitably disturbs its momentum, and vice versa. This wasn't just a limitation of our measurement tools, but a fundamental property of nature. The more precisely you know one property, the less precisely you can know the other. This was a radical departure from classical physics.") as tracker:
            uncertainty_eq = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=36,
                color=YELLOW
            )
            uncertainty_eq.move_to(DOWN * 1.0)
            self.play(Write(uncertainty_eq), run_time=2.5)
        
        self.play(FadeOut(*self.mobjects))

    def classical_vs_quantum(self):
        """Comparison between classical and quantum worldviews"""
        with self.voiceover(text="To truly appreciate the uncertainty principle, we must first understand how it differs from classical physics. In the classical world of Newton, if you know the position and momentum of a particle at any instant, you can predict its entire future trajectory with perfect accuracy. This is determinism at its finest.") as tracker:
            classical_title = Text("Classical Physics", font_size=32, color=GREEN)
            classical_title.to_edge(UP, buff=1.0)
            self.play(Write(classical_title), run_time=2)
            
            # Classical particle trajectory
            axes_classical = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes_classical.move_to(DOWN * 0.5)
            
            x_label = axes_classical.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.4).shift(DOWN * 0.8)
            y_label = axes_classical.get_y_axis_label("p", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes_classical), Write(x_label), Write(y_label), run_time=2)
            
            classical_dot = Dot(axes_classical.c2p(0, 0), color=GREEN, radius=0.12)
            self.play(FadeIn(classical_dot), run_time=1)
        
        with self.voiceover(text="In classical physics, a particle has a definite position and momentum at every instant. We can know both with arbitrary precision. The particle follows a well-defined path, and uncertainty only arises from our imperfect measurements, not from nature itself.") as tracker:
            path = axes_classical.plot(lambda x: 0.5 * np.sin(2 * x), color=GREEN, x_range=[-3, 3])
            self.play(MoveAlongPath(classical_dot, path), run_time=3)
            
            deterministic = Text("Deterministic & Predictable", font_size=20, color=GREEN)
            deterministic.next_to(axes_classical, DOWN, buff=0.8)
            self.play(FadeIn(deterministic), run_time=1.5)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Quantum mechanics tells a very different story. A quantum particle doesn't have a definite position and momentum simultaneously. Instead, it exists in a superposition of states, described by a wave function. The particle is spread out in space, and its properties are inherently uncertain until we make a measurement.") as tracker:
            quantum_title = Text("Quantum Physics", font_size=32, color=PURPLE)
            quantum_title.to_edge(UP, buff=1.0)
            self.play(Write(quantum_title), run_time=2)
            
            # Quantum wave function
            axes_quantum = Axes(
                x_range=[-3, 3, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes_quantum.move_to(DOWN * 0.5)
            
            x_label_q = axes_quantum.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.4).shift(DOWN * 0.8)
            psi_label = axes_quantum.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes_quantum), Write(x_label_q), Write(psi_label), run_time=2)
            
            wave = axes_quantum.plot(lambda x: np.exp(-x**2) * np.cos(4*x), color=PURPLE, x_range=[-3, 3])
            self.play(Create(wave), run_time=2)
            
            probabilistic = Text("Probabilistic & Uncertain", font_size=20, color=PURPLE)
            probabilistic.next_to(axes_quantum, DOWN, buff=0.8)
            self.play(FadeIn(probabilistic), run_time=1.5)
        
        self.play(FadeOut(*self.mobjects))

    def mathematical_formulation(self):
        """Detailed mathematical formulation of the uncertainty principle"""
        with self.voiceover(text="Now let's dive into the mathematics. The Heisenberg Uncertainty Principle is expressed as a fundamental inequality. Delta x represents the uncertainty in position, delta p represents the uncertainty in momentum, and h-bar is the reduced Planck constant, approximately one point zero five times ten to the minus thirty-four joule seconds.") as tracker:
            math_title = Text("Mathematical Formulation", font_size=32, color=BLUE)
            math_title.to_edge(UP, buff=1.0)
            self.play(Write(math_title), run_time=2)
            
            main_equation = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=36,
                color=YELLOW
            )
            main_equation.move_to(UP * 0.5)
            self.play(Write(main_equation), run_time=2.5)
        
        with self.voiceover(text="Let's break down each component. Delta x is not just an error in our measurement, but the standard deviation of the position probability distribution. Similarly, delta p is the standard deviation of the momentum distribution. These represent the fundamental spread or fuzziness in the quantum state itself.") as tracker:
            delta_x = MathTex(
                r"\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}",
                font_size=28,
                color=GREEN
            )
            delta_x.move_to(DOWN * 0.8)
            self.play(Write(delta_x), run_time=2)
            
            delta_p = MathTex(
                r"\Delta p = \sqrt{\langle p^2 \rangle - \langle p \rangle^2}",
                font_size=28,
                color=RED
            )
            delta_p.next_to(delta_x, DOWN, buff=0.8)
            self.play(Write(delta_p), run_time=2)
        
        with self.voiceover(text="The reduced Planck constant, h-bar, sets the scale of quantum effects. It's incredibly small, which is why we don't see quantum uncertainty in everyday objects. The factor of one-half comes from rigorous mathematical analysis and represents the minimum possible uncertainty, achieved only by special quantum states called coherent states.") as tracker:
            hbar_value = MathTex(
                r"\hbar = \frac{h}{2\pi} \approx 1.05 \times 10^{-34} \text{ J·s}",
                font_size=26,
                color=ORANGE
            )
            hbar_value.move_to(DOWN * 2.2)
            self.play(Write(hbar_value), run_time=2.5)
        
        self.play(FadeOut(*self.mobjects))

    def position_uncertainty(self):
        """Visualizing position uncertainty"""
        with self.voiceover(text="Let's visualize what position uncertainty means. Imagine trying to localize a quantum particle. In the classical world, a particle is a point with a definite location. But in quantum mechanics, the particle is described by a wave function, and its position is spread out over space.") as tracker:
            title = Text("Position Uncertainty", font_size=32, color=GREEN)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[0, 1.2, 0.2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.4).shift(DOWN * 0.8)
            prob_label = axes.get_y_axis_label("P", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(prob_label), run_time=2)
        
        with self.voiceover(text="Here we see the probability distribution for finding the particle at different positions. The width of this distribution is delta x. A narrow distribution means we know the position well, but as we'll see, this comes at the cost of momentum uncertainty. A wide distribution means the particle could be found anywhere in a large region.") as tracker:
            # Narrow Gaussian (well-localized position)
            narrow_gaussian = axes.plot(
                lambda x: np.exp(-4*x**2),
                color=GREEN,
                x_range=[-2, 2]
            )
            
            narrow_label = Text("Small Δx", font_size=20, color=GREEN)
            narrow_label.next_to(axes, DOWN, buff=0.8)
            
            self.play(Create(narrow_gaussian), Write(narrow_label), run_time=2.5)
            self.wait(1)
            
            # Wide Gaussian (poorly localized position)
            wide_gaussian = axes.plot(
                lambda x: 0.5 * np.exp(-0.5*x**2),
                color=BLUE,
                x_range=[-4, 4]
            )
            
            wide_label = Text("Large Δx", font_size=20, color=BLUE)
            wide_label.next_to(axes, DOWN, buff=0.8)
            
            self.play(
                Transform(narrow_gaussian, wide_gaussian),
                Transform(narrow_label, wide_label),
                run_time=2.5
            )
        
        self.play(FadeOut(*self.mobjects))

    def momentum_uncertainty(self):
        """Visualizing momentum uncertainty"""
        with self.voiceover(text="Now let's look at momentum uncertainty. In quantum mechanics, momentum is intimately connected to wavelength through the de Broglie relation: momentum equals h-bar times the wave number. A particle with well-defined momentum has a well-defined wavelength, which means it must be spread out over a large region of space.") as tracker:
            title = Text("Momentum Uncertainty", font_size=32, color=RED)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            de_broglie = MathTex(
                r"p = \hbar k = \frac{h}{\lambda}",
                font_size=36,
                color=YELLOW
            )
            de_broglie.next_to(title, DOWN, buff=0.6)
            self.play(Write(de_broglie), run_time=2)
        
        with self.voiceover(text="Here's the beautiful contradiction at the heart of quantum mechanics. A pure sine wave, extending from minus infinity to plus infinity, has a perfectly defined wavelength and therefore perfectly defined momentum. But it's completely delocalized in space. You have no idea where the particle is. The position uncertainty is infinite.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.4).shift(DOWN * 0.8)
            psi_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(psi_label), run_time=2)
            
            # Pure sine wave (definite momentum, undefined position)
            sine_wave = axes.plot(lambda x: 0.8 * np.sin(3*x), color=RED, x_range=[-4, 4])
            
            definite_p = Text("Δp ≈ 0, Δx → ∞", font_size=22, color=RED)
            definite_p.next_to(axes, DOWN, buff=0.8)
            
            self.play(Create(sine_wave), Write(definite_p), run_time=2.5)
        
        self.play(FadeOut(*self.mobjects))

    def wave_particle_duality(self):
        """Connecting uncertainty to wave-particle duality"""
        with self.voiceover(text="The uncertainty principle is deeply connected to wave-particle duality. To have a localized particle, we need to combine many waves of different wavelengths. This is called a wave packet. The more wavelengths we include, the more localized the packet becomes, but this also means greater spread in momentum.") as tracker:
            title = Text("Wave Packets and Uncertainty", font_size=32, color=PURPLE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            superposition = MathTex(
                r"\psi(x) = \sum_k A_k e^{ikx}",
                font_size=32,
                color=YELLOW
            )
            superposition.next_to(title, DOWN, buff=0.8)
            self.play(Write(superposition), run_time=2)
        
        with self.voiceover(text="Let me show you how this works. We'll build a wave packet by adding together sine waves with different wavelengths. Watch as adding more and more waves creates a localized bump, but the range of wavelengths needed means the momentum becomes less certain. This is the uncertainty principle in action.") as tracker:
            axes = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes.move_to(DOWN * 1.5)
            
            x_label = axes.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.4).shift(DOWN * 0.8)
            psi_label = axes.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes), Write(x_label), Write(psi_label), run_time=1.5)
            
            # Start with one wave
            wave1 = axes.plot(lambda x: 0.5 * np.sin(2*x), color=BLUE, x_range=[-4, 4])
            self.play(Create(wave1), run_time=1.5)
            
            # Add more waves to create wave packet
            wave_packet = axes.plot(
                lambda x: np.exp(-x**2) * np.cos(3*x),
                color=PURPLE,
                x_range=[-3, 3]
            )
            self.play(Transform(wave1, wave_packet), run_time=2)
            
            localized = Text("Localized Wave Packet", font_size=20, color=PURPLE)
            localized.next_to(axes, DOWN, buff=0.8)
            self.play(Write(localized), run_time=1.5)
        
        self.play(FadeOut(*self.mobjects))

    def physical_implications(self):
        """Physical implications and complementarity"""
        with self.voiceover(text="The uncertainty principle reveals a profound truth about nature: certain pairs of physical quantities cannot be simultaneously known with arbitrary precision. These are called complementary observables. Position and momentum are complementary. So are energy and time. The more you know about one, the less you can know about the other.") as tracker:
            title = Text("Complementary Observables", font_size=32, color=ORANGE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            # Show multiple uncertainty relations
            relations = VGroup(
                MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", color=GREEN),
                MathTex(r"\Delta E \cdot \Delta t \geq \frac{\hbar}{2}", color=BLUE),
                MathTex(r"\Delta L_x \cdot \Delta L_y \geq \frac{\hbar}{2}|L_z|", color=PURPLE)
            ).arrange(DOWN, buff=0.6).scale(0.9)
            relations.move_to(DOWN * 0.3)
            
            self.play(Write(relations[0]), run_time=2)
            self.play(Write(relations[1]), run_time=2)
            self.play(Write(relations[2]), run_time=2)
        
        with self.voiceover(text="These uncertainty relations aren't limitations of our technology or experimental technique. They're woven into the fabric of quantum reality. They arise from the mathematical structure of quantum mechanics itself, specifically from the fact that complementary observables are represented by non-commuting operators. The universe simply doesn't allow certain pieces of information to coexist.") as tracker:
            commutator = MathTex(
                r"[\hat{x}, \hat{p}] = i\hbar",
                font_size=36,
                color=YELLOW
            )
            commutator.move_to(DOWN * 2.2)
            self.play(Write(commutator), run_time=2.5)
        
        self.play(FadeOut(*self.mobjects))

    def measurement_problem(self):
        """The measurement problem and wave function collapse"""
        with self.voiceover(text="One of the most mysterious aspects of quantum mechanics is the measurement problem. Before measurement, a particle exists in a superposition of states, with uncertainties in position and momentum. But when we measure, say, the position, the wave function collapses to a definite value, and we lose all information about momentum.") as tracker:
            title = Text("The Measurement Problem", font_size=32, color=RED)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            before = Text("Before Measurement", font_size=24, color=BLUE)
            before.move_to(UP * 0.8)
            self.play(Write(before), run_time=1.5)
            
            # Spread out wave function
            axes_before = Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 1, 0.2],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes_before.move_to(DOWN * 0.3)
            
            x_label_b = axes_before.get_x_axis_label("x", direction=DOWN).shift(DOWN * 0.3).shift(DOWN * 0.8)
            self.play(Create(axes_before), Write(x_label_b), run_time=1.5)
            
            wave_before = axes_before.plot(
                lambda x: 0.8 * np.exp(-0.5*x**2),
                color=BLUE,
                x_range=[-3, 3]
            )
            self.play(Create(wave_before), run_time=2)
        
        with self.voiceover(text="During measurement, the smooth wave function suddenly collapses to a spike at the measured position. This is wave function collapse. The position is now known precisely, but we've completely lost information about the momentum. The uncertainty principle ensures that gaining information about one observable necessarily destroys information about its complement.") as tracker:
            self.play(FadeOut(before), FadeOut(wave_before))
            
            after = Text("After Measurement", font_size=24, color=RED)
            after.move_to(UP * 0.8)
            self.play(Write(after), run_time=1.5)
            
            # Collapsed wave function (delta function approximation)
            spike = axes_before.plot(
                lambda x: 0.95 * np.exp(-25*(x-0.5)**2),
                color=RED,
                x_range=[-1, 2]
            )
            self.play(Create(spike), run_time=2)
            
            collapse_label = Text("Wave Function Collapse", font_size=18, color=RED)
            collapse_label.next_to(axes_before, DOWN, buff=0.8)
            self.play(Write(collapse_label), run_time=1.5)
        
        self.play(FadeOut(*self.mobjects))

    def real_world_examples(self):
        """Real-world examples and applications"""
        with self.voiceover(text="You might wonder: if quantum uncertainty is real, why don't we see it in everyday life? The answer lies in the incredibly small value of Planck's constant. For macroscopic objects like baseballs or cars, the uncertainty is so tiny that it's completely negligible. Let me show you with a calculation.") as tracker:
            title = Text("Real-World Scale", font_size=32, color=YELLOW)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            example = Text("Example: Baseball", font_size=28, color=WHITE)
            example.next_to(title, DOWN, buff=0.8)
            self.play(Write(example), run_time=1.5)
        
        with self.voiceover(text="Consider a baseball with mass point one four five kilograms, moving at forty meters per second. If we know its position to within one millimeter, the uncertainty in velocity is absurdly small, about ten to the minus thirty meters per second. You'd never notice this in a million years. But for an electron, with its tiny mass, quantum uncertainty becomes absolutely crucial.") as tracker:
            calc = VGroup(
                MathTex(r"m = 0.145 \text{ kg}", color=GREEN),
                MathTex(r"\Delta x = 0.001 \text{ m}", color=BLUE),
                MathTex(r"\Delta v \geq \frac{\hbar}{2m\Delta x}", color=YELLOW),
                MathTex(r"\Delta v \approx 10^{-30} \text{ m/s}", color=RED)
            ).arrange(DOWN, buff=0.8).scale(0.8)
            calc.move_to(DOWN * 0.5)
            
            for eq in calc:
                self.play(Write(eq), run_time=1.8)
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now let's look at an electron in a hydrogen atom. The electron is confined to a region of about ten to the minus ten meters. This gives a momentum uncertainty that translates to kinetic energy of several electron volts, which is exactly the scale of atomic energies. Quantum mechanics isn't optional for atoms, it's essential for their very existence.") as tracker:
            electron_title = Text("Electron in Atom", font_size=28, color=CYAN)
            electron_title.to_edge(UP, buff=1.0)
            self.play(Write(electron_title), run_time=2)
            
            atom_calc = VGroup(
                MathTex(r"\Delta x \sim 10^{-10} \text{ m}", color=GREEN),
                MathTex(r"\Delta p \sim \frac{\hbar}{\Delta x}", color=BLUE),
                MathTex(r"E_{kinetic} = \frac{(\Delta p)^2}{2m} \sim \text{few eV}", color=YELLOW)
            ).arrange(DOWN, buff=0.6).scale(0.85)
            atom_calc.move_to(ORIGIN)
            
            for eq in atom_calc:
                self.play(Write(eq), run_time=2)
            
            conclusion = Text("Uncertainty is Essential for Atoms!", font_size=22, color=RED)
            conclusion.move_to(DOWN * 2.2)
            self.play(Write(conclusion), run_time=2)
        
        self.play(FadeOut(*self.mobjects))

    def philosophical_implications(self):
        """Philosophical implications of the uncertainty principle"""
        with self.voiceover(text="The Heisenberg Uncertainty Principle has profound philosophical implications. It tells us that the universe has fundamental limits on knowledge. No matter how advanced our technology becomes, we can never simultaneously know certain pairs of properties with perfect precision. This isn't ignorance, it's the nature of reality itself.") as tracker:
            title = Text("Philosophical Implications", font_size=32, color=PURPLE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            implications = VGroup(
                Text("• Limits on Knowledge", font_size=24, color=BLUE),
                Text("• End of Determinism", font_size=24, color=GREEN),
                Text("• Observer Effect", font_size=24, color=YELLOW),
                Text("• Probabilistic Universe", font_size=24, color=RED)
            ).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
            implications.move_to(DOWN * 0.5)
            
            for implication in implications:
                self.play(FadeIn(implication), run_time=1.8)
        
        with self.voiceover(text="Einstein famously struggled with this. He believed God does not play dice with the universe. But quantum mechanics, including the uncertainty principle, has been verified in countless experiments. The universe is fundamentally probabilistic. We can predict probabilities with exquisite precision, but individual outcomes remain uncertain. This is not a bug in our theories, it's a feature of nature.") as tracker:
            quote = Text(
                '"God does not play dice"\n- Einstein',
                font_size=22,
                color=ORANGE,
                slant=ITALIC
            )
            quote.move_to(DOWN * 2.5)
            self.play(Write(quote), run_time=2.5)
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        """Conclusion and summary"""
        with self.voiceover(text="Let's summarize what we've learned. The Heisenberg Uncertainty Principle states that certain pairs of observables cannot be simultaneously measured with arbitrary precision. Position and momentum, energy and time, and other complementary pairs are fundamentally limited by the relationship delta x times delta p is greater than or equal to h-bar over two.") as tracker:
            title = Text("Summary", font_size=36, color=GOLD)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title), run_time=2)
            
            final_equation = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=36,
                color=YELLOW
            )
            final_equation.move_to(UP * 0.5)
            self.play(Write(final_equation), run_time=2.5)
        
        with self.voiceover(text="This principle isn't a limitation of measurement technology, but a fundamental property of quantum mechanics arising from wave-particle duality. It has profound implications for how we understand reality, showing us that nature has built-in indeterminacy. The uncertainty principle is essential for understanding atoms, explaining why matter is stable, and why the quantum world behaves so differently from our everyday experience.") as tracker:
            key_points = VGroup(
                Text("• Fundamental property of nature", font_size=22, color=BLUE),
                Text("• Arises from wave-particle duality", font_size=22, color=GREEN),
                Text("• Essential for atomic stability", font_size=22, color=PURPLE),
                Text("• Limits on simultaneous knowledge", font_size=22, color=RED)
            ).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
            key_points.move_to(DOWN * 1.3)
            
            for point in key_points:
                self.play(FadeIn(point), run_time=1.5)
        
        with self.voiceover(text="Thank you for joining me on this journey through one of physics' most beautiful and mysterious principles. The Heisenberg Uncertainty Principle reminds us that the universe is far stranger and more wonderful than our everyday intuition suggests. Keep exploring, keep questioning, and never stop being amazed by the quantum world.") as tracker:
            thanks = Text(
                "Thank you for watching!",
                font_size=32,
                color=GOLD
            )
            thanks.move_to(DOWN * 3.0)
            self.play(FadeIn(thanks, shift=UP), run_time=2)
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects), run_time=2)

# Run the animation
if __name__ == "__main__":
    scene = HeisenbergUncertaintyPrinciple()
    scene.render()