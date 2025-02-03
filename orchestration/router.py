class Router:
    def __init__(self):
        self.agents = {
            "math": MathAgent(),
            "general": DeepSeekAgent(),
            "retrieval": RagAgent()
        }

    def route(self, user_input):
        if "calculate" in user_input:
            return self.agents["math"].execute(user_input)
        elif "search" in user_input:
            return self.agents["retrieval"].retrieve(user_input)
        else:
            return self.agents["general"].generate(user_input)