import feedparser
import csv
from datetime import datetime

def get_news():
    print("ニュース取得開始")

    # NHKニュースの公式RSS
    url = "https://www3.nhk.or.jp/rss/news/cat0.xml"

    feed = feedparser.parse(url)

    if not feed.entries:
        print("取得失敗またはニュースが見つかりませんでした")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("news_log.csv", "a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)

        for entry in feed.entries[:10]:
            title = entry.title
            link = entry.link
            writer.writerow([now, title, link])
            print(title)

    print("news_log.csv に保存完了")

get_news()