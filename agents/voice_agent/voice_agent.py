import whisper
import sounddevice as sd
import numpy as np
from .wake_word import WakeWordDetector

class VoiceAgent:
    def __init__(self):
        print("🔊 Loading voice agent...")
        self.stt_model = whisper.load_model("base")
        print("🔊 Loaded STT model.")
        self.wake_word_detector = WakeWordDetector(
            keyword_path="models/wake_word.ppn"  # <-- Explicit path
        )
        print("🔊 Loaded wake word detector.")
        self.sample_rate = 16000
        
    def record_command(self, duration=5):
        """Record audio after wake word detection"""
        print("🎤 Recording command...")
        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16
        )
        sd.wait()
        return audio.flatten().astype(np.float32) / 32768.0
    
    def transcribe(self, audio):
        """Convert speech to text"""
        result = self.stt_model.transcribe(audio, language="en")
        return result["text"]
    
    def run(self):
        """Main loop"""
        print("🚀 Starting voice agent...")
        try:
            while True:
                # Wait for wake word
                print("👂 Listening for wake word...")
                self.wake_word_detector.listen_for_wake_word()
                print("🛌 Wake word detected!")
                # Record and transcribe
                audio = self.record_command()
                text = self.transcribe(audio)
                print(f"👉 Command: {text}")
                
                yield text  # Pass to other agents
                
        except KeyboardInterrupt:
            self.wake_word_detector.cleanup()
            print("Voice agent shutdown.")

# Usage example
if __name__ == "__main__":
    agent = VoiceAgent()
    for command in agent.run():
        print(f"Command: {command}")
        if "exit" in command.lower():
            break