import anthropic
import httpx
import csv
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

# 質問リスト
questions = [
    "変数とは何か、1文で説明してください",
    "リストとは何か、1文で説明してください",
    "繰り返しとは何か、1文で説明してください",
]

# CSVに保存する
with open("qa_log.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)

    # ヘッダー
    writer.writerow(["日時", "質問", "回答"])

    for question in questions:
        answer = ask_claude(question)

        # 画面にも表示
        print(f"Q: {question}")
        print(f"A: {answer}")
        print()

        # CSVに1行保存
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, question, answer])

print("qa_log.csv に保存完了")
