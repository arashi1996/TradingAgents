from .base_agent import CryptoBaseAgent

class SentimentAgent(CryptoBaseAgent):
    def analyze(self, data):
        # data: 社交媒体/新闻情绪数据
        return {"sentiment": "bullish"} 