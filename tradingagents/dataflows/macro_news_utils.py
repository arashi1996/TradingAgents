import requests

def fetch_macro_news():
    # 用CryptoPanic免费API聚合新闻
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=45c21bfe2fc55f732f0c3531bb46db1ff88799c6&public=true"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        news_list = []
        for item in resp.json().get('results', []):
            news_list.append({
                "title": item.get('title', ''),
                "text": item.get('title', '') + ' ' + (item.get('body') or ''),
                "source": item.get('source', {}).get('title', ''),
                "url": item.get('url', '')
            })
        return news_list
    except Exception as e:
        print(f"[fetch_macro_news] Error: {e}")
        return [] 