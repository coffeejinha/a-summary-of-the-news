import requests
from bs4 import BeautifulSoup

# 한국 뉴스 기사 본문 스크래핑 함수 (네이버 뉴스 예시)
def scrape_korean_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # 네이버 뉴스의 본문 추출
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    except Exception as e:
        print(f"Error while fetching the article: {e}")
        return None
