#!/bin/sh

echo "Checking if Ollama server is already running..."
if pgrep -x "ollama" > /dev/null; then
  echo "Ollama is already running."
else
  echo "Starting Ollama server..."
  ollama serve &
fi

echo "Waiting for Ollama server to be active..."
until curl -s http://localhost:11434/api/tags > /dev/null; do
  sleep 2
done

echo "Pulling the model: $MODEL_NAME"
ollama pull $MODEL_NAME

echo "Ollama server is running with the model $MODEL_NAME!"
tail -f /dev/null
