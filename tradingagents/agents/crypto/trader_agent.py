class TraderAgent:
    def decide(self, risk_report):
        # 根据风险报告做出交易决策
        if risk_report["risk_score"] < 0.3:
            return "BUY"
        elif risk_report["risk_score"] > 0.7:
            return "SELL"
        else:
            return "HOLD" 