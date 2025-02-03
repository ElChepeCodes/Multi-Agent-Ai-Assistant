from agents.voice_agent.stt import SpeechToText
from agents.voice_agent.tts import TextToSpeech
from agents.nlp_agent.model import DeepSeekAgent

# Initialize agents
stt = SpeechToText()
tts = TextToSpeech()
llm = DeepSeekAgent("models/deepseek-7b-Q4_K_M.gguf")

# Main loop
audio = record_audio()
user_input = stt.transcribe(audio)
response = llm.generate(user_input)
tts.speak(response)