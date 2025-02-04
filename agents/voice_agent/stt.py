# agents/voice_agent/voice_agent.py
import whisper
import sounddevice as sd
import numpy as np
from wake_word import WakeWordDetector
# from utils import play_beep  # Add this helper

class VoiceAgent:
    def __init__(self):
        self.stt_model = whisper.load_model("base")
        self.wake_word_detector = WakeWordDetector(
            keyword_path="models/wake_word.ppn"
        )
        self.sample_rate = 16000
        self.command_duration = 5  # Seconds to record after wake word
        
    def _record_post_wakeword(self):
        """Record audio after wake word detection"""
        # play_beep()  # Optional audio feedback
        print("Listening...")
        audio = sd.rec(
            int(self.command_duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16
        )
        sd.wait()
        return audio.flatten().astype(np.float32) / 32768.0

    def process_command(self):
        """Full flow: wake word → STT → transcription"""
        # Step 1: Wait for wake word
        self.wake_word_detector.listen_for_wake_word()
        
        # Step 2: Record and transcribe
        audio = self._record_post_wakeword()
        return self.stt_model.transcribe(audio, language="en")["text"]

    def continuous_listen(self):
        """Run indefinitely"""
        try:
            while True:
                command = self.process_command()
                yield command
        except KeyboardInterrupt:
            self.wake_word_detector.cleanup()

# Helper function (create agents/voice_agent/utils.py)
def play_beep():
    """Audio feedback that STT is active"""
    try:
        import winsound  # Windows
        winsound.Beep(1000, 200)
    except:
        print("\a")  # Fallback to system beep