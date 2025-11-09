---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: LibreChatにおけるOPENAI_REVERSE_PROXYの設定
translated: true
type: note
---

了解しました 👍 LibreChatの `.env` ファイルを編集しているのですね。
このファイルがまさに `OPENAI_REVERSE_PROXY` を設定する場所です。

---

### 1. 変数の役割

`OPENAI_REVERSE_PROXY` は、LibreChatがOpenAI APIリクエストをプロキシサーバー経由でルーティングしたい場合に使用します（例えば、ロギング、キャッシング、地域ルーティングを追加するため、または制限を回避するためのセルフホステッドリバースプロキシを実行している場合など）。

---

### 2. 設定方法

`.env` ファイルで、リバースプロキシのベースURLを割り当てるだけです。例：

```ini
OPENAI_REVERSE_PROXY=https://your-proxy.example.com/v1
```

注意点：

* URLは、OpenAIの `/v1` APIを模倣するプロキシエンドポイントを指す必要があります。
* プロキシが要求しない限り、末尾の `/` は含めないでください。
* プロキシを使用しない場合は、空のままにしてください (`OPENAI_REVERSE_PROXY=`)。

---

### 3. 変更の適用

`.env` を編集した後、新しい値を読み込むためにLibreChatコンテナを再起動してください：

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### 4. 検証

実行中のコンテナ内で確認できます：

```bash
docker compose exec librechat env | grep OPENAI_REVERSE_PROXY
```

設定した値が表示されるはずです。

---

すでにリバースプロキシのURL（`https://openrouter.ai/api/v1` や独自のNginxインスタンスなど）をお持ちですか？それとも、LibreChat用に**リバースプロキシをセットアップする方法**をご紹介しましょうか？