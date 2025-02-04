FROM ollama/ollama

# Install curl (required for API calls)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy the run script into the container
COPY ./run_ollama.sh /tmp/run_ollama.sh

# Set working directory
WORKDIR /tmp

# Make the script executable
RUN chmod +x /tmp/run_ollama.sh && ls -l /tmp/run_ollama.sh

# Expose the port used by Ollama
EXPOSE 11434

# Override entry point to run the script via shell
ENTRYPOINT ["/bin/sh", "/tmp/run_ollama.sh"]
