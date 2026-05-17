# Python講義サイト

PythonとAIを活用した自動化ツール構築を、実践的な課題を通じて学ぶ講義サイトです。

## 講義サイトを開く

**→ [`index.html`](./index.html) をダウンロードして、ブラウザで開いてください。**

AIチャット・QAルーム・全22回の講義コンテンツが1ファイルで完結しています。

---

## 講義一覧（全22回）

| 回 | タイトル | キーワード |
|---|---|---|
| 01 | Pythonの全体像 | 全体像・7領域・自動化 |
| 02 | 環境構築 | Python本体・VSCode・PATH |
| 03 | 基本文法 | 変数・リスト・for文・if文 |
| 04 | 関数とライブラリ | def・import・pip install |
| 05 | Claude API呼び出し | APIキー・anthropic・ask_claude |
| 06 | ファイルの読み書き | open()・csv・datetime |
| 07 | フォルダの自動整理 | os・shutil・自動仕分け |
| 08 | 定期実行 | schedule・while True |
| 09 | Webスクレイピング | requests・BeautifulSoup |
| 10 | データ×AI分析 | CSV読み込み・プロンプト設計 |
| 11 | 講義サイトを作る | HTML・JavaScript・AIチャット |
| 12 | LLMは何をしているのか | トークン・確率・temperature |
| 13 | プロンプトは何をしているのか | System・User・Few-shot |
| 14 | AIエージェントの構造 | ループ・ツール・状態管理 |
| 15 | RAGとは何か | Retrieval・外部情報・ファイル読み込み |
| 16 | AIの限界と信頼性 | ハルシネーション・対処法 |
| 17 | Claude Codeとは何か | エージェント統合・全体像 |
| 18 | Gitとは何か | バージョン管理・コミット |
| 19 | Gitの基本操作 | git init・add・commit・log |
| 20 | ブランチとは何か | branch・checkout -b・merge |
| 21 | GitHubとは何か | remote add・push・pull |
| 22 | Claude CodeとGitの連携 | Git自動操作・日本語指示 |

---

## ファイル構成

```
python-lecture-site/
├── README.md          ← このファイル（リポジトリの表紙）
├── index.html         ← 講義サイトのメインページ（ここを開く）
├── Lecture01.html     ─┐
│   ...                 │ 各回の講義詳細ページ（index.html から自動リンク）
└── lecture22.html     ─┘
```

### Pythonスクリプト

| ファイル | 内容 |
|---|---|
| `claude_test.py` | Claude API 呼び出しの基本 |
| `lesson3.py` | 基本文法（変数・リスト・for・if） |
| `lesson6.py` | ファイル読み書き・CSV保存 |
| `lesson7.py` | フォルダ自動整理 |
| `lesson8.py` | 定期実行（schedule） |
| `lesson9.py` | Webスクレイピング |
| `lesson10.py` | データ×AI分析 |
| `lesson14.py` | AIエージェント（多ターン会話） |
| `lesson15.py` | RAG実装 |
| `lesson16.py` | ハルシネーション検証 |
| `make_csv.py` | サンプルCSVデータ生成 |
| `hello_agent.py` | エージェント基礎 |
| `show.py` | データ表示ユーティリティ |
| `orbit.py` | 軌道計算サンプル |

> **注意：** スクリプト内の `api_key="sk-ant-YOUR-API-KEY-HERE"` は自分のAPIキーに置き換えて使用してください。

---

## 使い方

1. このリポジトリをクローンまたはZIPでダウンロード
2. `index.html` をブラウザで開く
3. AIチャット機能を使う場合は、[Anthropic Console](https://console.anthropic.com) でAPIキーを取得して入力
