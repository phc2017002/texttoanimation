# NOTE: This code has been automatically post-processed to fix common issues:
# - Indexed SurroundingRectangle calls have been disabled
# - Layout spacing has been adjusted to prevent overlaps
# - Axis labels have been positioned to stay within frame
# - Font sizes have been capped to prevent massive text

# ⚠️  SYNTAX ERROR DETECTED:
# Line 305: unmatched ')' - Near: wave1_axes.move_to(DOWN * 1.5))
# This code may fail to render. Please review and fix manually.

from manim import *
from manim_voiceover import VoiceoverScene
from manimator.services import ElevenLabsService
import numpy as np

class HeisenbergUncertaintyPrinciple(VoiceoverScene):
    def construct(self):
        self.set_speech_service(ElevenLabsService(voice_id="Rachel"))
        
        # Section 1: Introduction
        self.introduction()
        
        # Section 2: Historical Context
        self.historical_context()
        
        # Section 3: Classical vs Quantum
        self.classical_vs_quantum()
        
        # Section 4: The Main Equation
        self.main_equation()
        
        # Section 5: Wave-Particle Duality
        self.wave_particle_duality()
        
        # Section 6: Position-Momentum Uncertainty
        self.position_momentum_uncertainty()
        
        # Section 7: Energy-Time Uncertainty
        self.energy_time_uncertainty()
        
        # Section 8: Mathematical Derivation
        self.mathematical_derivation()
        
        # Section 9: Real-World Examples
        self.real_world_examples()
        
        # Section 10: Implications
        self.implications()
        
        # Section 11: Common Misconceptions
        self.common_misconceptions()
        
        # Section 12: Conclusion
        self.conclusion()

    def introduction(self):
        with self.voiceover(text="Welcome to this comprehensive exploration of the Heisenberg Uncertainty Principle, one of the most profound and counterintuitive concepts in quantum mechanics.") as tracker:
            title = Text("Heisenberg Uncertainty Principle", font_size=36, color=BLUE)
            title.to_edge(UP, buff=1.0)
            self.play(Write(title))
            
            subtitle = Text("A Fundamental Limit of Nature", font_size=24, color=YELLOW)
            subtitle.next_to(title, DOWN, buff=0.8)
            self.play(FadeIn(subtitle))
        
        with self.voiceover(text="This principle tells us that there are fundamental limits to what we can know about quantum particles. The more precisely we know one property, the less precisely we can know another complementary property.") as tracker:
            quantum_img = Circle(radius=1.5, color=PURPLE, fill_opacity=0.3)
            quantum_img.move_to(DOWN * 0.5)
            
            question_mark = Text("?", font_size=36, color=WHITE)
            question_mark.move_to(quantum_img.get_center())
            
            self.play(Create(quantum_img), FadeIn(question_mark))
        
        with self.voiceover(text="Named after Werner Heisenberg who formulated it in nineteen twenty-seven, this principle fundamentally changed our understanding of reality at the quantum scale.") as tracker:
            self.play(Indicate(quantum_img, scale_factor=1.2))
        
        self.play(FadeOut(*self.mobjects))

    def historical_context(self):
        with self.voiceover(text="To understand the uncertainty principle, we need to travel back to the early twentieth century, when quantum mechanics was just beginning to emerge.") as tracker:
            section_title = Text("Historical Context", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE)
            timeline.move_to(ORIGIN)
            self.play(Create(timeline))
            
            year_1900 = Text("1900", font_size=20).next_to(timeline.get_left(), DOWN, buff=0.8)
            year_1927 = Text("1927", font_size=20).next_to(timeline.get_center(), DOWN, buff=0.8)
            year_1950 = Text("1950", font_size=20).next_to(timeline.get_right(), DOWN, buff=0.8)
            
            self.play(Write(year_1900), Write(year_1927), Write(year_1950))
        
        with self.voiceover(text="In nineteen hundred, Max Planck introduced the concept of energy quanta, marking the birth of quantum theory. Scientists were discovering that classical physics failed to explain phenomena at atomic scales.") as tracker:
            planck_dot = Dot(timeline.get_left(), color=YELLOW)
            planck_label = Text("Planck's Quantum", font_size=18).next_to(planck_dot, UP, buff=0.8)
            self.play(Create(planck_dot), Write(planck_label))
        
        with self.voiceover(text="By nineteen twenty-seven, Heisenberg was working on matrix mechanics, a mathematical formulation of quantum theory. It was during this work that he discovered the fundamental uncertainty relation.") as tracker:
            heisenberg_dot = Dot(timeline.get_center(), color=RED)
            heisenberg_label = Text("Heisenberg's\nUncertainty", font_size=18, line_spacing=0.8)
            heisenberg_label.next_to(heisenberg_dot, UP, buff=0.8)
            self.play(Create(heisenberg_dot), Write(heisenberg_label))
        
        with self.voiceover(text="This discovery was revolutionary. It wasn't just about the limitations of our measuring instruments, but rather a fundamental property of nature itself. The universe, at its most basic level, is inherently uncertain.") as tracker:
            self.play(Indicate(heisenberg_dot, scale_factor=2.0, color=GOLD))
        
        self.play(FadeOut(*self.mobjects))

    def classical_vs_quantum(self):
        with self.voiceover(text="Let's contrast classical physics with quantum physics to understand why the uncertainty principle is so revolutionary.") as tracker:
            section_title = Text("Classical vs Quantum", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            divider = Line(UP * 2.0, DOWN * 3.5, color=WHITE)
            divider.move_to(ORIGIN + DOWN * 0.75)
            self.play(Create(divider))
            
            classical_label = Text("Classical World", font_size=24, color=GREEN)
            classical_label.move_to(LEFT * 3.5 + UP * 2.8)
            
            quantum_label = Text("Quantum World", font_size=24, color=PURPLE)
            quantum_label.move_to(RIGHT * 3.5 + UP * 2.8)
            
            self.play(Write(classical_label), Write(quantum_label))
        
        with self.voiceover(text="In classical physics, a particle has a definite position and momentum at all times. If you know the initial conditions perfectly, you can predict its future behavior with absolute certainty.") as tracker:
            classical_ball = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
            classical_ball.move_to(LEFT * 3.5 + UP * 1.0)
            
            position_arrow = Arrow(classical_ball.get_bottom(), classical_ball.get_bottom() + DOWN * 0.8, color=YELLOW)
            position_label = Text("x", font_size=20).next_to(position_arrow, DOWN, buff=0.8)
            
            momentum_arrow = Arrow(classical_ball.get_right(), classical_ball.get_right() + RIGHT * 1.0, color=RED)
            momentum_label = Text("p", font_size=20).next_to(momentum_arrow, RIGHT, buff=0.8)
            
            self.play(Create(classical_ball))
            self.play(Create(position_arrow), Write(position_label))
            self.play(Create(momentum_arrow), Write(momentum_label))
            
            deterministic = Text("Deterministic", font_size=18, color=GREEN)
            deterministic.move_to(LEFT * 3.5 + DOWN * 1.2)
            self.play(Write(deterministic))
        
        with self.voiceover(text="In the quantum world, however, particles don't have definite properties until measured. A quantum particle is described by a wave function, which gives us only probabilities of finding the particle at different locations.") as tracker:
            quantum_wave = self.create_wave_packet(center=RIGHT * 3.5 + UP * 1.0, width=1.5)
            self.play(Create(quantum_wave))
            
            probabilistic = Text("Probabilistic", font_size=18, color=PURPLE)
            probabilistic.move_to(RIGHT * 3.5 + DOWN * 1.2)
            self.play(Write(probabilistic))
        
        with self.voiceover(text="The Heisenberg Uncertainty Principle tells us that we cannot simultaneously know both the position and momentum of a quantum particle with perfect precision. This isn't a limitation of our technology, it's nature itself.") as tracker:
            uncertainty_eq = MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", font_size=32)
            uncertainty_eq.move_to(RIGHT * 3.5 + DOWN * 2.5)
            self.play(Write(uncertainty_eq))
        
        self.play(FadeOut(*self.mobjects))

    def create_wave_packet(self, center, width):
        axes = Axes(
            x_range=[-1, 1, 0.5],
            y_range=[-0.5, 0.5, 0.25],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": False, "stroke_width": 1}
        )
        axes.move_to(center)
        
        wave = axes.plot(
            lambda x: 0.3 * np.exp(-x**2 / (2 * width**2)) * np.cos(10 * x),
            x_range=[-1, 1],
            color=PURPLE
        )
        
        return VGroup(axes, wave)

    def main_equation(self):
        with self.voiceover(text="Now let's examine the mathematical heart of the uncertainty principle. This elegant equation encapsulates one of nature's deepest truths.") as tracker:
            section_title = Text("The Uncertainty Relation", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            main_eq = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=36
            )
            main_eq.move_to(UP * 0.5)
            self.play(Write(main_eq))
        
        with self.voiceover(text="Let's break down each component. Delta x represents the uncertainty in position. This is not a measurement error, but rather the intrinsic spread in the particle's position.") as tracker:
            # delta_x_box = SurroundingRectangle(main_eq[0][0:2], color=YELLOW, buff=0.8)  # Auto-disabled: indexed SurroundingRectangle
            # self.play(Create(delta_x_box))  # Auto-disabled: uses disabled SurroundingRectangle
            
            delta_x_explanation = Text("Uncertainty in position", font_size=20, color=YELLOW)
            delta_x_explanation.next_to(main_eq, DOWN, buff=1.0)
            self.play(Write(delta_x_explanation))
            self.wait(1)
            self.play(FadeOut(delta_x_explanation))
        
        with self.voiceover(text="Delta p represents the uncertainty in momentum. Momentum is mass times velocity, so this uncertainty tells us how spread out the velocity distribution of the particle is.") as tracker:
            delta_p_explanation = Text("Uncertainty in momentum", font_size=20, color=RED)
            delta_p_explanation.next_to(main_eq, DOWN, buff=1.0)
            self.play(Write(delta_p_explanation))
            self.wait(1)
            self.play(FadeOut(delta_p_explanation))
        
        with self.voiceover(text="The right side contains h-bar, which is Planck's constant divided by two pi. This is approximately one point zero five times ten to the minus thirty-four joule seconds. This incredibly small number sets the scale of quantum effects.") as tracker:
            hbar_value = MathTex(r"\hbar \approx 1.05 \times 10^{-34} \text{ J·s}", font_size=22)
            hbar_value.next_to(main_eq, DOWN, buff=1.0)
            self.play(Write(hbar_value))
        
        with self.voiceover(text="The greater-than-or-equal-to sign is crucial. It means the product of uncertainties can never be smaller than h-bar over two. The more precisely you know position, the less precisely you know momentum, and vice versa.") as tracker:
            self.play(Indicate(main_eq[0][5], scale_factor=1.5, color=GOLD))
        
        self.play(FadeOut(*self.mobjects))

    def wave_particle_duality(self):
        with self.voiceover(text="To truly understand the uncertainty principle, we need to grasp the concept of wave-particle duality. Every quantum object exhibits both wave-like and particle-like properties.") as tracker:
            section_title = Text("Wave-Particle Duality", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
        
        with self.voiceover(text="Consider a particle with well-defined momentum. According to de Broglie's relation, this corresponds to a wave with a specific wavelength. Such a wave extends throughout space, making the position completely uncertain.") as tracker:
            axes1 = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes1.move_to(DOWN * 1.0)
            
            plane_wave = axes1.plot(lambda x: np.cos(3 * x), x_range=[-4, 4], color=BLUE)
            
            label1 = Text("Well-defined momentum", font_size=20, color=BLUE)
            label1.next_to(axes1, DOWN, buff=0.8)
            label2 = Text("Position uncertain", font_size=20, color=RED)
            label2.next_to(label1, DOWN, buff=0.8)
            
            x_label = axes1.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8)
            y_label = axes1.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes1), Write(x_label), Write(y_label))
            self.play(Create(plane_wave))
            self.play(Write(label1), Write(label2))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Now consider a localized wave packet with well-defined position. This packet is actually a superposition of many different wavelengths, meaning many different momenta. The position is well-defined, but momentum is uncertain.") as tracker:
            section_title2 = Text("Wave-Particle Duality", font_size=32, color=BLUE)
            section_title2.to_edge(UP, buff=1.0)
            self.play(Write(section_title2))
            
            axes2 = Axes(
                x_range=[-4, 4, 1],
                y_range=[-1.5, 1.5, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": True}
            )
            axes2.move_to(DOWN * 1.0)
            
            wave_packet = axes2.plot(
                lambda x: np.exp(-x**2 / 0.5) * np.cos(8 * x),
                x_range=[-4, 4],
                color=GREEN
            )
            
            label3 = Text("Well-defined position", font_size=20, color=GREEN)
            label3.next_to(axes2, DOWN, buff=0.8)
            label4 = Text("Momentum uncertain", font_size=20, color=RED)
            label4.next_to(label3, DOWN, buff=0.8)
            
            x_label2 = axes2.get_x_axis_label("x").shift(DOWN * 0.6).shift(DOWN * 0.8)
            y_label2 = axes2.get_y_axis_label(r"\psi", direction=LEFT).shift(LEFT * 0.8).shift(LEFT * 0.8)
            
            self.play(Create(axes2), Write(x_label2), Write(y_label2))
            self.play(Create(wave_packet))
            self.play(Write(label3), Write(label4))
        
        self.play(FadeOut(*self.mobjects))

    def position_momentum_uncertainty(self):
        with self.voiceover(text="Let's visualize the position-momentum uncertainty relation through an interactive demonstration. We'll see how constraining position increases momentum uncertainty.") as tracker:
            section_title = Text("Position-Momentum Trade-off", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            uncertainty_eq = MathTex(r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}", font_size=32)
            uncertainty_eq.next_to(section_title, DOWN, buff=0.8)
            self.play(Write(uncertainty_eq))
        
        with self.voiceover(text="Imagine we have a particle in a box. Initially, the box is very wide, so the position uncertainty is large. We can represent the wave function inside this box.") as tracker:
            box1 = Rectangle(width=6, height=2, color=WHITE)
            box1.move_to(DOWN * 1.5)
            self.play(Create(box1))
            
            wave1_axes = Axes(
                x_range=[0, 6, 1],
                y_range=[-1, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False, "stroke_width": 0}
            )
            wave1_axes.move_to(DOWN * 1.5)
            
            wave1 = wave1_axes.plot(lambda x: 0.7 * np.sin(PI * x / 3), x_range=[0, 6], color=YELLOW)
            self.play(Create(wave1))
            
            dx_label1 = MathTex(r"\Delta x = \text{large}", font_size=24)
            dx_label1.next_to(box1, LEFT, buff=0.6)
            dp_label1 = MathTex(r"\Delta p = \text{small}", font_size=24)
            dp_label1.next_to(box1, RIGHT, buff=0.6)
            self.play(Write(dx_label1), Write(dp_label1))
        
        with self.voiceover(text="Notice that the wave has a small number of oscillations, indicating a relatively well-defined momentum with small uncertainty. Now let's confine the particle to a smaller region.") as tracker:
            self.wait(1)
        
        self.play(FadeOut(box1), FadeOut(wave1), FadeOut(dx_label1), FadeOut(dp_label1))
        
        with self.voiceover(text="As we squeeze the box, reducing the position uncertainty, something remarkable happens. The wave function must have more oscillations to fit in the smaller space, representing higher momentum uncertainty.") as tracker:
            box2 = Rectangle(width=3, height=2, color=WHITE)
            box2.move_to(DOWN * 1.5)
            self.play(Create(box2))
            
            wave2_axes = Axes(
                x_range=[0, 3, 1],
                y_range=[-1, 1, 0.5],
                x_length=7,
                y_length=4,
                axis_config={"include_tip": False, "stroke_width": 0}
            )
            wave2_axes.move_to(DOWN * 1.5)
            
            wave2 = wave2_axes.plot(lambda x: 0.7 * np.sin(2 * PI * x / 1.5), x_range=[0, 3], color=ORANGE)
            self.play(Create(wave2))
            
            dx_label2 = MathTex(r"\Delta x = \text{small}", font_size=24)
            dx_label2.next_to(box2, LEFT, buff=0.6)
            dp_label2 = MathTex(r"\Delta p = \text{large}", font_size=24)
            dp_label2.next_to(box2, RIGHT, buff=0.6)
            self.play(Write(dx_label2), Write(dp_label2))
        
        with self.voiceover(text="This is the essence of the uncertainty principle. The tighter we confine a particle in space, the more uncertain its momentum becomes. Position and momentum are complementary observables that cannot both be known precisely.") as tracker:
            self.play(Indicate(uncertainty_eq, scale_factor=1.2, color=GOLD))
        
        self.play(FadeOut(*self.mobjects))

    def energy_time_uncertainty(self):
        with self.voiceover(text="There's another form of the uncertainty principle that involves energy and time. This relation has profound implications for the existence of virtual particles and the nature of quantum fluctuations.") as tracker:
            section_title = Text("Energy-Time Uncertainty", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            energy_time_eq = MathTex(r"\Delta E \cdot \Delta t \geq \frac{\hbar}{2}", font_size=36)
            energy_time_eq.move_to(UP * 0.5)
            self.play(Write(energy_time_eq))
        
        with self.voiceover(text="Delta E represents the uncertainty in energy, while delta t represents the uncertainty in time. This tells us that energy conservation can be violated, but only for very short time intervals.") as tracker:
            de_explanation = Text("Energy uncertainty", font_size=22, color=YELLOW)
            de_explanation.move_to(LEFT * 3.5 + DOWN * 1.0)
            
            dt_explanation = Text("Time uncertainty", font_size=22, color=RED)
            dt_explanation.move_to(RIGHT * 3.5 + DOWN * 1.0)
            
            self.play(Write(de_explanation), Write(dt_explanation))
        
        with self.voiceover(text="For example, a particle-antiparticle pair can spontaneously appear from the vacuum, borrowing energy delta E from nowhere. But they must annihilate within a time delta t such that their product satisfies the uncertainty relation.") as tracker:
            vacuum = Rectangle(width=6, height=2, color=BLUE, fill_opacity=0.2)
            vacuum.move_to(DOWN * 2.2)
            self.play(Create(vacuum))
            
            particle = Circle(radius=0.2, color=GREEN, fill_opacity=0.8)
            antiparticle = Circle(radius=0.2, color=RED, fill_opacity=0.8)
            
            particle.move_to(vacuum.get_center() + LEFT * 0.5)
            antiparticle.move_to(vacuum.get_center() + RIGHT * 0.5)
            
            self.play(FadeIn(particle), FadeIn(antiparticle))
            
            plus = MathTex("+", font_size=24).move_to(vacuum.get_center() + LEFT * 0.8)
            minus = MathTex("-", font_size=24).move_to(vacuum.get_center() + RIGHT * 0.8)
            self.play(Write(plus), Write(minus))
        
        with self.voiceover(text="These virtual particles are constantly appearing and disappearing throughout space. They're real enough to have measurable effects, such as the Casimir effect and contributions to the anomalous magnetic moment of the electron.") as tracker:
            self.play(FadeOut(particle), FadeOut(antiparticle), FadeOut(plus), FadeOut(minus))
        
        self.play(FadeOut(*self.mobjects))

    def mathematical_derivation(self):
        with self.voiceover(text="Now let's explore the mathematical foundation of the uncertainty principle. This derivation uses the properties of Fourier transforms, which connect position and momentum representations.") as tracker:
            section_title = Text("Mathematical Foundation", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
        
        with self.voiceover(text="The uncertainty in a quantity is defined as the standard deviation of measurements. For position, this is the square root of the expectation value of x squared, minus the expectation value of x, squared.") as tracker:
            sigma_x = MathTex(
                r"\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}",
                font_size=32
            )
            sigma_x.move_to(UP * 1.5)
            self.play(Write(sigma_x))
            
            sigma_p = MathTex(
                r"\Delta p = \sqrt{\langle p^2 \rangle - \langle p \rangle^2}",
                font_size=32
            )
            sigma_p.next_to(sigma_x, DOWN, buff=0.8)
            self.play(Write(sigma_p))
        
        with self.voiceover(text="In quantum mechanics, position and momentum are represented by operators that don't commute. Their commutator is i times h-bar, which is the fundamental source of uncertainty.") as tracker:
            commutator = MathTex(
                r"[\hat{x}, \hat{p}] = i\hbar",
                font_size=32
            )
            commutator.next_to(sigma_p, DOWN, buff=0.7)
            self.play(Write(commutator))
        
        with self.voiceover(text="Using the Cauchy-Schwarz inequality from linear algebra, combined with this commutation relation, we can rigorously prove that the product of uncertainties must satisfy the Heisenberg bound.") as tracker:
            inequality = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{1}{2}|[\hat{x}, \hat{p}]| = \frac{\hbar}{2}",
                font_size=30
            )
            inequality.next_to(commutator, DOWN, buff=0.7)
            self.play(Write(inequality))
        
        with self.voiceover(text="This mathematical derivation shows that uncertainty is not about measurement disturbance, but rather about the fundamental nature of quantum operators and the wave function itself.") as tracker:
            highlight_box = SurroundingRectangle(inequality, color=GOLD, buff=0.2)
            self.play(Create(highlight_box))
        
        self.play(FadeOut(*self.mobjects))

    def real_world_examples(self):
        with self.voiceover(text="Let's examine some real-world examples where the Heisenberg Uncertainty Principle plays a crucial role in observable phenomena.") as tracker:
            section_title = Text("Real-World Applications", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
        
        with self.voiceover(text="First, consider the stability of atoms. According to classical physics, an electron orbiting a nucleus should radiate energy and spiral into the nucleus. But the uncertainty principle prevents this.") as tracker:
            atom_model = Circle(radius=0.3, color=RED, fill_opacity=0.5)
            atom_model.move_to(UP * 0.5)
            nucleus_label = Text("nucleus", font_size=16).next_to(atom_model, DOWN, buff=0.8)
            self.play(Create(atom_model), Write(nucleus_label))
            
            orbit = Circle(radius=1.5, color=BLUE)
            orbit.move_to(atom_model.get_center())
            electron = Dot(color=YELLOW)
            electron.move_to(orbit.point_at_angle(0))
            self.play(Create(orbit), Create(electron))
        
        with self.voiceover(text="If the electron were localized at the nucleus, its position uncertainty would be tiny, about ten to the minus fifteen meters. This would require an enormous momentum uncertainty, giving it huge kinetic energy that prevents collapse.") as tracker:
            energy_explanation = MathTex(
                r"\Delta x \approx 10^{-15} \text{ m} \Rightarrow \Delta p \text{ very large}",
                font_size=24
            )
            energy_explanation.move_to(DOWN * 1.8)
            self.play(Write(energy_explanation))
        
        self.play(FadeOut(*self.mobjects))
        
        with self.voiceover(text="Another example is electron tunneling through barriers. Even if an electron doesn't have enough energy to classically overcome a barrier, the uncertainty principle allows it to briefly violate energy conservation and tunnel through.") as tracker:
            section_title2 = Text("Real-World Applications", font_size=32, color=BLUE)
            section_title2.to_edge(UP, buff=1.0)
            self.play(Write(section_title2))
            
            barrier = Rectangle(width=1, height=3, color=GRAY, fill_opacity=0.7)
            barrier.move_to(ORIGIN)
            self.play(Create(barrier))
            
            electron_left = Dot(color=YELLOW, radius=0.15)
            electron_left.move_to(LEFT * 2.5)
            
            electron_right = Dot(color=YELLOW, radius=0.15)
            electron_right.move_to(RIGHT * 2.5)
            
            arrow1 = Arrow(electron_left.get_center(), barrier.get_left(), color=BLUE)
            arrow2 = Arrow(barrier.get_right(), electron_right.get_center(), color=BLUE, stroke_opacity=0.5)
            
            self.play(Create(electron_left))
            self.play(Create(arrow1))
            self.play(Create(arrow2))
            self.play(Create(electron_right))
            
            tunnel_label = Text("Quantum Tunneling", font_size=22, color=YELLOW)
            tunnel_label.move_to(DOWN * 2.5)
            self.play(Write(tunnel_label))
        
        with self.voiceover(text="This tunneling effect is essential for nuclear fusion in stars, including our Sun. It also forms the basis of scanning tunneling microscopes, which can image individual atoms.") as tracker:
            self.wait(1)
        
        self.play(FadeOut(*self.mobjects))

    def implications(self):
        with self.voiceover(text="The philosophical and scientific implications of the Heisenberg Uncertainty Principle extend far beyond simple measurements. This principle fundamentally changed our view of reality.") as tracker:
            section_title = Text("Profound Implications", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
        
        with self.voiceover(text="First, it establishes that determinism fails at the quantum level. Unlike classical mechanics where the future is determined by present conditions, quantum mechanics is inherently probabilistic.") as tracker:
            determinism = Text("Classical Determinism", font_size=24, color=GREEN)
            determinism.move_to(LEFT * 3.5 + UP * 1.0)
            
            probability = Text("Quantum Probability", font_size=24, color=PURPLE)
            probability.move_to(RIGHT * 3.5 + UP * 1.0)
            
            self.play(Write(determinism))
            self.play(Write(probability))
            
            arrow_cross = Line(determinism.get_right(), probability.get_left(), color=RED)
            cross = Text("X", font_size=36, color=RED).move_to(arrow_cross.get_center())
            self.play(Create(arrow_cross), Write(cross))
        
        with self.voiceover(text="Second, it means that the act of observation fundamentally affects the system. You cannot measure position without disturbing momentum, and vice versa. The observer is inseparable from the observed.") as tracker:
            observer_system = VGroup(
                Text("Observer", font_size=22, color=YELLOW),
                Text("System", font_size=22, color=BLUE),
            ).arrange(RIGHT, buff=2)
            observer_system.move_to(DOWN * 0.5)
            
            interaction = DoubleArrow(
                observer_system[0].get_right(),
                observer_system[1].get_left(),
                color=ORANGE
            )
            
            self.play(Write(observer_system))
            self.play(Create(interaction))
        
        with self.voiceover(text="Third, it reveals that empty space isn't truly empty. Due to energy-time uncertainty, quantum fields are constantly fluctuating, creating virtual particles that pop in and out of existence.") as tracker:
            vacuum_label = Text("Quantum Vacuum", font_size=24, color=PURPLE)
            vacuum_label.move_to(DOWN * 1.5)
            
            fluctuation = MathTex(r"\Delta E \cdot \Delta t \geq \frac{\hbar}{2}", font_size=28)
            fluctuation.next_to(vacuum_label, DOWN, buff=0.8)
            
            self.play(Write(vacuum_label))
            self.play(Write(fluctuation))
        
        self.play(FadeOut(*self.mobjects))

    def common_misconceptions(self):
        with self.voiceover(text="Let's address some common misconceptions about the uncertainty principle. These misunderstandings often arise from oversimplified explanations.") as tracker:
            section_title = Text("Common Misconceptions", font_size=32, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
        
        with self.voiceover(text="Misconception number one: The uncertainty principle is about measurement disturbance. Many people think that measuring position disturbs momentum. While this can happen, the uncertainty principle is deeper than that.") as tracker:
            misconception1 = Text("Misconception 1:", font_size=26, color=RED)
            misconception1.move_to(UP * 1.5)
            self.play(Write(misconception1))
            
            wrong1 = Text("Measurement disturbs the system", font_size=22, color=ORANGE)
            wrong1.next_to(misconception1, DOWN, buff=0.8)
            self.play(Write(wrong1))
            
            cross1 = Text("✗", font_size=36, color=RED)
            cross1.next_to(wrong1, LEFT, buff=0.8)
            self.play(Write(cross1))
        
        with self.voiceover(text="The truth is that uncertainty exists even before any measurement. A particle doesn't have a definite position and momentum simultaneously. It's not that we don't know them, they simply don't exist as definite values.") as tracker:
            truth1 = Text("Truth: Intrinsic quantum property", font_size=22, color=GREEN)
            truth1.next_to(wrong1, DOWN, buff=0.6)
            
            check1 = Text("✓", font_size=36, color=GREEN)
            check1.next_to(truth1, LEFT, buff=0.8)
            self.play(Write(truth1), Write(check1))
        
        self.play(FadeOut(misconception1), FadeOut(wrong1), FadeOut(cross1), FadeOut(truth1), FadeOut(check1))
        
        with self.voiceover(text="Misconception number two: We can beat the uncertainty principle with better technology. Some think that with perfect instruments, we could measure both position and momentum precisely.") as tracker:
            misconception2 = Text("Misconception 2:", font_size=26, color=RED)
            misconception2.move_to(UP * 1.5)
            self.play(Write(misconception2))
            
            wrong2 = Text("Better tech can beat uncertainty", font_size=22, color=ORANGE)
            wrong2.next_to(misconception2, DOWN, buff=0.8)
            self.play(Write(wrong2))
            
            cross2 = Text("✗", font_size=36, color=RED)
            cross2.next_to(wrong2, LEFT, buff=0.8)
            self.play(Write(cross2))
        
        with self.voiceover(text="This is fundamentally impossible. The uncertainty principle is a law of nature, not a technological limitation. It's built into the mathematical structure of quantum mechanics through the commutation relations.") as tracker:
            truth2 = Text("Truth: Fundamental law of nature", font_size=22, color=GREEN)
            truth2.next_to(wrong2, DOWN, buff=0.6)
            
            check2 = Text("✓", font_size=36, color=GREEN)
            check2.next_to(truth2, LEFT, buff=0.8)
            self.play(Write(truth2), Write(check2))
        
        self.play(FadeOut(*self.mobjects))

    def conclusion(self):
        with self.voiceover(text="We've journeyed through one of quantum mechanics' most profound principles. Let's summarize what we've learned about the Heisenberg Uncertainty Principle.") as tracker:
            section_title = Text("Conclusion", font_size=36, color=BLUE)
            section_title.to_edge(UP, buff=1.0)
            self.play(Write(section_title))
            
            final_equation = MathTex(
                r"\Delta x \cdot \Delta p \geq \frac{\hbar}{2}",
                font_size=36,
                color=GOLD
            )
            final_equation.move_to(UP * 0.8)
            self.play(Write(final_equation))
        
        with self.voiceover(text="The uncertainty principle tells us that nature has fundamental limits on what can be known simultaneously. Position and momentum are complementary observables that cannot both be precisely determined.") as tracker:
            point1 = Text("• Fundamental limit of nature", font_size=22)
            point1.move_to(LEFT * 2 + DOWN * 0.5)
            self.play(FadeIn(point1, shift=RIGHT))
        
        with self.voiceover(text="This isn't about measurement limitations, but about the wave-like nature of matter itself. Quantum particles are described by wave functions that inherently possess both position and momentum spreads.") as tracker:
            point2 = Text("• Wave-particle duality", font_size=22)
            point2.next_to(point1, DOWN, buff=0.8, aligned_edge=LEFT)
            self.play(FadeIn(point2, shift=RIGHT))
        
        with self.voiceover(text="The principle has profound implications: atomic stability, quantum tunneling, virtual particles, and the probabilistic nature of reality. It fundamentally changed our understanding of the universe.") as tracker:
            point3 = Text("• Shapes quantum reality", font_size=22)
            point3.next_to(point2, DOWN, buff=0.8, aligned_edge=LEFT)
            self.play(FadeIn(point3, shift=RIGHT))
        
        with self.voiceover(text="Thank you for joining me on this exploration of the Heisenberg Uncertainty Principle. Remember, at the quantum scale, nature is far stranger and more beautiful than our everyday intuition suggests.") as tracker:
            self.play(
                FadeOut(section_title),
                FadeOut(final_equation),
                FadeOut(point1),
                FadeOut(point2),
                FadeOut(point3)
            )
            thank_you = Text("Thank You for Watching!", font_size=32, color=YELLOW)
            thank_you.move_to(ORIGIN)
            self.play(Write(thank_you))
            self.wait(2)
        
        self.play(FadeOut(*self.mobjects))


# Run the animation
if __name__ == "__main__":
    scene = HeisenbergUncertaintyPrinciple()
    scene.render()