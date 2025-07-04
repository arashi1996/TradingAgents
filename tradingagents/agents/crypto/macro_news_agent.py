from .base_agent import CryptoBaseAgent
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", framework="pt")

def classify_event_type(text):
    # 简单规则/关键词匹配
    if "interest rate" in text or "加息" in text:
        return "rate_hike"
    if "ETF" in text:
        return "etf_approval"
    if "regulation" in text or "监管" in text:
        return "regulation"
    return "other"

def sentiment_analysis(text):
    result = sentiment_pipeline(text)
    return result[0]['label'].lower()  # 'positive'/'negative'

def model_event_impact(event):
    # 规则+情感
    if event['type'] == 'rate_hike':
        return 0.8 if event['sentiment'] == 'negative' else 0.5
    if event['type'] == 'etf_approval':
        return 0.7 if event['sentiment'] == 'positive' else 0.4
    if event['type'] == 'regulation':
        return 0.6 if event['sentiment'] == 'negative' else 0.3
    return 0.3

class MacroNewsAgent(CryptoBaseAgent):
    def analyze(self, news_list):
        events = []
        impact_scores = []
        for news in news_list:
            event_type = classify_event_type(news['text'])
            sentiment = sentiment_analysis(news['text'])
            event = {
                "title": news['title'],
                "type": event_type,
                "sentiment": sentiment,
                "source": news['source'],
                "url": news['url']
            }
            events.append(event)
            impact_scores.append(model_event_impact(event))
        overall_sentiment = (
            "bullish" if impact_scores and sum(impact_scores)/len(impact_scores) > 0.5 else "bearish"
        )
        return {
            "macro_sentiment": overall_sentiment,
            "impact_scores": impact_scores,
            "major_events": events
        } 