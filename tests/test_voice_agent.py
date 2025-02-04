import sys
import os
import pytest

# Add project root to Python path
print('Adding project root to Python path')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print('Project root added to Python path')
print('importing agents')
# Import agents
from agents.voice_agent.wake_word import WakeWordDetector
print('imported wake word')
from agents.voice_agent.voice_agent import VoiceAgent
print('imported voice agent')

# Test Wake Word Detection
def test_wake_word_detection():
    detector = WakeWordDetector(keyword_path="models/wake_word.ppn")
    assert detector is not None, "Failed to initialize wake word detector"

# Test Voice Agent
def test_voice_agent_initialization():
    agent = VoiceAgent()
    assert agent is not None, "Failed to initialize voice agent"

print('starting voice agent')
voice_agent = VoiceAgent()
print('running voice agent')
# Iterate over the generator to process commands
for command in voice_agent.run():
    print(f"Processing command: {command}")
    if "exit" in command.lower():
        break
print('bye')