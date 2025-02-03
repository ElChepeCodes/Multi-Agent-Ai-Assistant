import whisper

class SpeechToText:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)
    
    def transcribe(self, audio):
        return self.model.transcribe(audio)["text"]