from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class VerifyGTTS(VoiceoverScene):
    def construct(self):
        # Initialize gTTS service
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        with self.voiceover(text="This is a test of the Google Text to Speech service integration.") as tracker:
            text = Text("gTTS Verification", font_size=48)
            self.play(Write(text))
            self.wait(1)
            
        with self.voiceover(text="If you can hear this, the migration was successful.") as tracker:
            self.play(FadeOut(text))
            success = Text("Success!", color=GREEN)
            self.play(ScaleInPlace(success, 1.5))
            self.wait(1)
