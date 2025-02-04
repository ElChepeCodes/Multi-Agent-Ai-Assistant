import requests

class DeepSeekClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.model = "deepseek-r1:1.5b"
        
    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"]