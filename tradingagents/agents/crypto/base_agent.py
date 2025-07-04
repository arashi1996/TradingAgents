class CryptoBaseAgent:
    def __init__(self, name):
        self.name = name

    def analyze(self, data):
        raise NotImplementedError("analyze() must be implemented by subclasses") 