import anthropic
import httpx

# SSL検証を無効にして接続する
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

answer = ask_claude("Pythonとは何か、3行で説明してください")
print(answer)