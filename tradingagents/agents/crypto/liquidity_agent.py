from .base_agent import CryptoBaseAgent

class LiquidityAgent(CryptoBaseAgent):
    def analyze(self, data):
        # data: 流动性相关数据
        return {"liquidity_score": 75} 