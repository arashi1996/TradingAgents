from tradingagents.agents.crypto.macro_news_agent import MacroNewsAgent
from tradingagents.dataflows.macro_news_utils import fetch_macro_news

if __name__ == "__main__":
    print("=== 宏观新闻自动分析演示 ===")
    news_list = fetch_macro_news()
    print(f"抓取到 {len(news_list)} 条新闻")
    if news_list:
        agent = MacroNewsAgent("MacroNews")
        result = agent.analyze(news_list)
        print("\n分析结果：")
        print(f"整体情绪: {result['macro_sentiment']}")
        print(f"影响分数: {result['impact_scores']}")
        print("主要事件:")
        for event in result['major_events'][:5]:
            print(f"- [{event['type']}] {event['title']} ({event['sentiment']}) 来源: {event['source']} 链接: {event['url']}")
    else:
        print("未获取到新闻数据，请检查API Token或网络连接。") 