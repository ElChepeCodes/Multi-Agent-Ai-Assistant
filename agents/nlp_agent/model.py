from llama_cpp import Llama

class DeepSeekAgent:
    def __init__(self, model_path):
        self.llm = Llama(model_path=model_path, n_ctx=2048)
    
    def generate(self, prompt):
        return self.llm(prompt)["choices"][0]["text"]