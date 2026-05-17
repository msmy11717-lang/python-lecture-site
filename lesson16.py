import anthropic

client = anthropic.Anthropic(api_key="sk-ant-YOUR-API-KEY-HERE")

def ask_with_context(question, context=None):
    if context:
        prompt = f"""以下の情報を参考にして答えてください。
情報以外のことは「情報にありません」と答えてください。

【情報】
{context}

【質問】
{question}"""
    else:
        prompt = question

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

# 架空の会社データ
company_info = """
会社名：株式会社ミライテック
所在地：名古屋市中区錦2-3-4
設立：2021年4月
代表：鈴木一郎
従業員：12名
"""

question = "株式会社ミライテックの代表者名と所在地を教えてください"

print("=== 情報なし（幻覚リスクあり）===")
print(ask_with_context(question))

print("\n=== 情報あり（RAGあり）===")
print(ask_with_context(question, company_info))