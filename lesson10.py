import anthropic
import httpx
import csv

http_client = httpx.Client(verify=False)
client = anthropic.Anthropic(
    api_key="sk-ant-YOUR-API-KEY-HERE",
    http_client=http_client
)

def ask_claude(prompt):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

# CSVを読み込んで文字列に変換する
def load_csv_as_text(filename):
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(",".join(row))
    return "\n".join(rows)

# データを読み込む
csv_text = load_csv_as_text("data.csv")

# プロンプトにデータを埋め込む
prompt = f"""
以下は私の1週間の作業記録です。

{csv_text}

このデータを分析して以下を教えてください：
1. 最も時間がかかっている作業は何か
2. 未完了タスクのパターン
3. 業務効率化のための具体的な提案を3つ
"""

print("Claudeが分析中...")
result = ask_claude(prompt)
print(result)
