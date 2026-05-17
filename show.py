with open("data.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, age, job = line.split(",")
        print(f"名前: {name}　年齢: {age}歳　職業: {job}")
