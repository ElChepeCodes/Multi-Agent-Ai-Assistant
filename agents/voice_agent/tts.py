from gtts import gTTS
import os

class TextToSpeech:
    def speak(self, text, lang="en"):
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")
        os.system("start response.mp3")  # Windows