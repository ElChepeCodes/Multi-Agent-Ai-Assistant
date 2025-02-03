from agents.voice_agent.stt import SpeechToText

def test_stt():
    stt = SpeechToText(model_size="tiny")
    test_audio = ...  # Load sample audio
    assert "hello" in stt.transcribe(test_audio).lower()