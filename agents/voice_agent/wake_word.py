import pvporcupine
import pyaudio
import numpy as np
import os

class WakeWordDetector:
    def __init__(self, access_key=None, keyword_path="models/wake_word.ppn"):  # <-- Changed here
        self.access_key = access_key or os.getenv("PICOVOICE_API_KEY")
        self.keyword_path = keyword_path
        
        if not os.path.exists(self.keyword_path):
            raise FileNotFoundError(f"Wake word model not found at {self.keyword_path}")
            
        self.porcupine = pvporcupine.create(
            access_key=self.access_key,
            keyword_paths=[self.keyword_path]  # <-- Use custom model
        )
        
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    
    def listen_for_wake_word(self):
        """Blocks until wake word is detected"""
        print("🔈 Listening for wake word...")
        while True:
            pcm = self.stream.read(self.porcupine.frame_length)
            pcm = np.frombuffer(pcm, dtype=np.int16)
            result = self.porcupine.process(pcm)
            if result >= 0:
                print("⚠️ Wake word detected!")
                return True
    
    def cleanup(self):
        self.stream.close()
        self.audio.terminate()
        self.porcupine.delete()