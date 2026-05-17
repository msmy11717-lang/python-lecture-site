import anthropic

client = anthropic.Anthropic(api_key="sk-ant-YOUR-API-KEY-HERE")

def rag_answer(file_path, question):
    # Step1：Retrieve（ファイルから情報を取得）
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    
    # Step2：Augment（情報をプロンプトに埋め込む）
    prompt = f"""以下の情報を参考にして質問に答えてください。

【参考情報】
{data}

【質問】
{question}
"""
    
    # Step3：Generate（LLMが回答）
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text

# 実行
print(rag_answer("company_data.txt", "2024年から2025年の売上成長率を教えてください"))
print("\n---\n")
print(rag_answer("company_data.txt", "この会社の課題に対してどんな対策が考えられますか？"))