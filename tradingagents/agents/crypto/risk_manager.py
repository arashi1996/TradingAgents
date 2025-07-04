class RiskManager:
    def assess(self, macro, liquidity, sentiment, crypto_news):
        # 综合各Agent输出，给出风险建议
        risk_score = 0.5  # 0~1
        return {"risk_score": risk_score, "advice": "谨慎观望"} 