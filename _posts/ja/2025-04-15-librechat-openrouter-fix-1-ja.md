---
audio: false
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: LibreChat OpenRouter Web検索エラーの修正
translated: true
type: note
---

エラー **「404 No endpoints found that support tool use」** は、LibreChatでOpenRouterを使用する際のウェブ検索機能に関する既知の問題です。原因と解決方法を以下に示します：

---

## **原因**
- **OpenRouterのすべてのモデルが「ツール使用」（ウェブ検索、関数呼び出しなど）をサポートしているわけではありません**—対応しているのは一部のモデルのみです。ツールをサポートしていないモデルを選択すると、この404エラーが発生します。
- OpenRouterでは、ウェブ検索などの機能を利用するために、**ツール/関数呼び出しをサポートするモデルを明示的に選択する必要があります**。
- LibreChatの設定が正しく構成されていない場合、エンドポイントが上書きされ、ルーティングの問題が発生することもあります。

---

## **解決方法**

### 1. **ツールをサポートするモデルを選択**
- [OpenRouterのモデル一覧](https://openrouter.ai/models)にアクセスし、サイドバーで **「tools」でフィルタリング**してください。ツールサポートがあるモデルのみがLibreChatのウェブ検索機能で動作します。
- 推奨モデル：「function calling」または「tools」をサポートするモデル（例：一部のGPT-4バージョン、Claude、その他の高度なモデル）を探してください。

### 2. **LibreChatの設定を更新**
- LibreChatの設定で **`OPENROUTER_API_KEY`を使用しないでください**。OpenAIエンドポイントを上書きし、競合を引き起こす可能性があります。
- `librechat.yaml`で、OpenRouterエンドポイントが正しく構成され、「Ignored Providers」でブロックされていないか、「Allowed Providers」で制限されていないことを確認してください。

### 3. **プロバイダーの制限を解除**
- OpenRouterの設定で、**「Ignored Providers」のブロックをすべて解除**し、**「Allowed Providers」をクリア**して、LibreChatが利用可能なすべてのエンドポイントにアクセスできるようにしてください。

### 4. **LibreChatを再起動**
- これらの変更を加えた後、LibreChatを再起動して新しい設定を適用してください。

---

## **それでも動作しない場合**
- 高度な設定については、[LibreChatドキュメントのカスタムエンドポイント](https://www.librechat.ai/docs/quick_start/custom_endpoints)を確認してください。
- 問題が解決しない場合は、公式OpenRouter API（アクセス権がある場合）またはツール使用をサポートする他のプロバイダーに切り替えてみてください。