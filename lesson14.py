import anthropic

client = anthropic.Anthropic(api_key="sk-ant-YOUR-API-KEY-HERE")

def run_agent(steps):
    messages = []
    
    for i, step in enumerate(steps):
        print(f"\n=== ステップ{i+1} ===")
        print(f"指示：{step}")
        
        messages.append({"role": "user", "content": step})
        
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system="あなたは日本歴史の博士です。全ての回答を歴史的背景を交えて答えてください。",
            messages=messages
        )
        
        answer = response.content[0].text
        print(f"回答：{answer}")
        
        messages.append({"role": "assistant", "content": answer})

steps = [
    "日本の都市を3つ挙げてください。",
    "その中で一番人口が多い都市はどこですか？",
    "その都市の特徴を2つ教えてください。"
]

run_agent(steps)