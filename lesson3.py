# 自分で関数を作って呼び出す練習

def show_persona(name, score):
    if score >= 70:
        result = "刺さる"
    else:
        result = "刺さらない"
    print(name + "の評価：" + result + "（" + str(score) + "点）")

personas = [
    ("田中誠", 85),
    ("伊藤さゆり", 30),
    ("山田健太", 72),
    ("佐藤美咲", 91),
]

for name, score in personas:
    show_persona(name, score)
    