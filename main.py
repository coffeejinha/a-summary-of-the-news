from load_model import load_kobart_summarizer
from scrape import scrape_korean_article
from summarize import summarize_large_text

# 메인 실행
if __name__ == "__main__":
    print("한국 뉴스 기사 요약기")
    url = input("뉴스 URL을 입력하세요 (예: 네이버 뉴스): ")

    print("\n기사 스크래핑 중...")
    article = scrape_korean_article(url)
    
    if not article:
        print("기사 스크래핑 실패! URL을 확인하세요.")
    else:
        print("\n요약 중...")
        summarizer = load_kobart_summarizer()
        summary = summarize_large_text(summarizer, article)

        if summary:
            print("\n요약된 기사:")
            print(summary)
        else:
            print("요약 실패!")
