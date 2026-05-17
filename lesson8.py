import anthropic
import httpx
import csv
import schedule
import time
from datetime import datetime

http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(
    api_key="sk-ant-YOUR-API-KEY-HERE",
    http_client=http_client
)

def ask_claude(question):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

# 毎朝実行したい処理
def morning_task():
    print("朝のタスク開始")

    questions = [
        "今日取り組むべき業務効率化のヒントを1つ教えてください",
        "Pythonで今日練習すべきことを1つ提案してください",
    ]

    with open("morning_log.csv", "a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)

        # 初回のみヘッダーを書く
        if f.tell() == 0:
            writer.writerow(["日時", "質問", "回答"])

        for question in questions:
            answer = ask_claude(question)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([now, question, answer])
            print(f"Q: {question}")
            print(f"A: {answer}")
            print()

    print("morning_log.csv に保存完了")

# 毎朝9時に実行するスケジュールを登録
schedule.every().day.at("09:00").do(morning_task)

print("スケジューラ起動。Ctrl+Cで停止。")

# 動作確認用：今すぐ1回実行したい場合はコメントを外す
morning_task()

while True:
    schedule.run_pending()
    time.sleep(1)