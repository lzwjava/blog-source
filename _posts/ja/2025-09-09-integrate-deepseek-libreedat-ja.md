---
audio: false
date: 2025-09-09
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: LibreChatとDeepSeekの連携ガイド
translated: true
type: note
---

**DeepSeekをLibreChatで動作させる最も速い方法**をご紹介します。**公式のDeepSeek API**を使用する方法（推奨）と、**OpenRouter**を経由する方法の2つのオプションがあります。

---

## オプション A — DeepSeekの公式APIを使用する（推奨）

1.  **DeepSeek APIキーを取得する**
    DeepSeekアカウントで作成し、以下のベースURLをメモしてください:
    `https://api.deepseek.com` (またはOpenAI互換の `https://api.deepseek.com/v1`)。 ([DeepSeek API Docs][1], [deepseek.apidog.io][2])

2.  **`librechat.yaml`にDeepSeekエンドポイントを追加する**
    これを `endpoints:` → `custom:` の下に配置します:

```yaml
- name: deepseek
  apiKey: ${DEEPSEEK_API_KEY}
  baseURL: https://api.deepseek.com/v1
  models:
    default: deepseek-chat
    fetch: true
    list:
      - deepseek-chat        # V3 (汎用)
      - deepseek-coder       # コード中心
      - deepseek-reasoner    # R1 推論
  titleConvo: true
  dropParams: null
```

LibreChatには **DeepSeek** 設定ガイドが同梱されており、モデル名 (`deepseek-chat`, `deepseek-coder`, `deepseek-reasoner`) と、R1がその「思考プロセス」をストリーミングすることについての注意が確認されています。 ([LibreChat][3])

3.  **`.env`ファイルを介してAPIキーを設定する**
    LibreChatの `.env` ファイル内で:

```
DEEPSEEK_API_KEY=sk-...
```

LibreChatは、`librechat.yaml` + `.env` を介したカスタムOpenAI互換プロバイダーをサポートしています。 ([LibreChat][4])

4.  **スタックを再起動する**
    LibreChatフォルダから:

```bash
docker compose down
docker compose up -d --build
```

(APIコンテナが `librechat.yaml` と `.env` を再読み込みするために必要です。) カスタムエンドポイントが表示されない場合は、`api` コンテナのログをチェックして設定エラーがないか確認してください。 ([GitHub][5])

---

## オプション B — OpenRouter経由でDeepSeekを使用する

すでにOpenRouterを使用している場合は、DeepSeekモデルをOpenRouterエンドポイントブロックに登録するだけです。

`librechat.yaml`:

```yaml
- name: openrouter
  apiKey: ${OPENROUTER_KEY}
  baseURL: https://openrouter.ai/api/v1
  models:
    default: deepseek/deepseek-chat
    list:
      - deepseek/deepseek-chat
      - deepseek/deepseek-coder
      - deepseek/deepseek-reasoner
```

LibreChatドキュメントからの2つの重要な注意点:
* `OPENROUTER_API_KEY` という環境変数名は設定しないでください (代わりに `OPENROUTER_KEY` のような異なる名前を使用してください)。そうしないと、誤ってOpenAIエンドポイントを上書きしてしまいます。
* OpenRouterはLibreChatのカスタムエンドポイントリストでファーストクラスとして扱われます。 ([LibreChat][6])

OpenRouterは、DeepSeekモデルをOpenAI互換のインターフェースで公開しています。 ([OpenRouter][7])

---

## ヒントと注意点

*   **R1 / `deepseek-reasoner`**: 連鎖思考（「思考プロセス」）をストリーミングすることができます。一部のOpenAIパラメータは適用されない可能性があります。出力がおかしい場合は、まず `deepseek-chat` でテストしてください。 ([LibreChat][3])
*   **モデル取得**: `fetch: true` を設定すると、サポートされている場合にLibreChatが最新のモデルリストを取得できるようになります。それ以外の場合は、指定した `list:` が使用されます。 ([LibreChat][8])
*   **これらの設定が保存される場所**: `librechat.yaml` はカスタムエンドポイントファイルです。 `.env` はキーとプロキシ設定を保持します。 ([LibreChat][8])

必要であれば、現在の `librechat.yaml` を貼り付けてください。DeepSeekをきれいに追加するように修正します（表は使いません、約束します）。

[1]: https://api-docs.deepseek.com/?utm_source=chatgpt.com "DeepSeek API Docs: Your First API Call"
[2]: https://deepseek.apidog.io/your-first-api-call-835227m0?utm_source=chatgpt.com "DeepSeek API: Your First API Call"
[3]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek?utm_source=chatgpt.com "Deepseek"
[4]: https://www.librechat.ai/docs/quick_start/custom_endpoints?utm_source=chatgpt.com "Custom Endpoints"
[5]: https://github.com/danny-avila/LibreChat/discussions/2487?utm_source=chatgpt.com "Fix the librechat.yaml file in the main repository. #2487"
[6]: https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/openrouter?utm_source=chatgpt.com "Openrouter"
[7]: https://openrouter.ai/deepseek/deepseek-v3-base%3Afree/api?utm_source=chatgpt.com "DeepSeek V3 Base – Run with an API"
[8]: https://www.librechat.ai/docs/configuration/librechat_yaml?utm_source=chatgpt.com "librechat.yaml config file"