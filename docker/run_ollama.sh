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

echo "Pulling the model if not already available..."
ollama pull deepseek-r1:1.5b

echo "Ollama server is running with the model deepseek-r1:1.5b!"
tail -f /dev/null  # Keep the container running
