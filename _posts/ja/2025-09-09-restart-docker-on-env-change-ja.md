---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 環境変数変更後のDockerコンテナ再起動
translated: true
type: note
---

`.env` を変更しても、Docker は自動的にそれらの環境変数をリロードしません。新しい値を読み込むには、コンテナを再起動する必要があります。LibreChat の設定の場合、以下のように行います：

1. `docker-compose.yml` ファイルがあるのと同じディレクトリにいることを確認してください。
2. 以下を実行します：

```bash
docker compose down
docker compose up -d
```

これにより、実行中のコンテナが停止・削除され、新しい `.env` の値で再作成されます。

---

### 代替案: 再起動のみ

すべてを完全に破棄したくない場合は、リビルドを強制することでコンテナに新しい環境変数を読み込ませることができます：

```bash
docker compose up -d --force-recreate
```

または、Dockerfiles や依存関係も変更した場合は、`--build` を追加します：

```bash
docker compose up -d --build
```

---

✅ 要約すると：

* `.env` を編集した後は、常にコンテナを**再作成**してください (`down` + `up` または `up --force-recreate`)。
* 単純な `docker compose restart` では新しい環境変数の値はリロードされず、古い値で再起動するだけです。

あなたの LibreChat コンテナが新しい環境変数の値を使用していることを**確認**する方法 (例: `docker inspect` や `docker exec env` を使用) もお見せしましょうか？