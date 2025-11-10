---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: LibreChat OpenRouterモデルエラーの修正
translated: true
type: note
---

このエラーは、**LibreChat** で **OpenRouter** をバックエンドとして使用し、選択したモデル（`gpt-5-chat` など）が利用できない、または適切にルーティングされていない場合に発生します。以下に、問題の詳細と解決方法を説明します。

---

## **エラーが発生する理由**
- **OpenRouter** は様々な AI モデルへのプロキシとして機能しますが、すべてのモデルがデフォルトで利用可能または有効になっているわけではありません。
- エラー `404 No endpoints found that support tool use` は、選択したモデル（`gpt-5-chat`）が以下のいずれかであることを意味します：
  - OpenRouter でサポートされていない。
  - LibreChat の設定で構成されていない。
  - 別のプロバイダまたは API キーを必要とする。

---

## **解決方法**

### 1. **OpenRouter で利用可能なモデルを確認する**
- [OpenRouter のモデル一覧](https://openrouter.ai/models) にアクセスして、利用可能なモデルを確認してください。
- 現時点では、`gpt-5-chat` は公式の OpenAI モデルではありません（最新は GPT-4o です）。GPT-4 を意図している場合は、`openai/gpt-4` などを使用してください。

### 2. **LibreChat の設定を更新する**
- LibreChat で、**設定** > **モデル選択** に移動します。
- **OpenRouter でサポートされている** モデル（例: `openai/gpt-4`, `mistralai/mistral-7b` など）を選択してください。
- OpenAI を直接使用したい場合は、**API プロバイダ** を **OpenRouter** から **OpenAI** に切り替えてください。

### 3. **API キーを確認する**
- （OpenRouter を使用する場合）有効な **OpenRouter API キー** があること、または（OpenAI を使用する場合）**OpenAI API キー** があることを確認してください。
- キーは LibreChat の **設定** > **API キー** で追加してください。

### 4. **LibreChat を再起動する**
- 設定を変更した後、変更を適用するために LibreChat を再起動してください。

### 5. **LibreChat のドキュメントを確認する**
- 詳細な手順については、[LibreChat の OpenRouter セットアップガイド](https://github.com/danny-avila/LibreChat#openrouter) を参照してください。

---

## **代替ソリューション**
- OpenAI のモデルを使用したい場合は、プロバイダを **OpenAI** に設定し、`gpt-4`, `gpt-4o`, `gpt-3.5-turbo` を選択してください。
- OpenRouter を使用したい場合は、[サポートされているモデル一覧](https://openrouter.ai/models) からモデルを選択してください。

---