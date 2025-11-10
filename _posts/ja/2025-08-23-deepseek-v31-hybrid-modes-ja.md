---
audio: false
generated: true
image: false
lang: ja
layout: post
title: DeepSeek V3.1 ハイブリッドモードの解説
translated: true
type: note
---

**DeepSeek V3.1 API** が新しいハイブリッド推論アーキテクチャ（「思考」モードと「非思考」モード）をどのように扱うかを以下に示します：

---

### API 変更点の概要

#### 1. **2つの異なるエンドポイント（モード）**

* **`deepseek-chat`** は **非思考モード** に対応 — 素早い応答に最適化されています。
* **`deepseek-reasoner`** は **思考モード** に対応 — より慎重な、多段階の推論タスクのために構築されています。
  両エンドポイントは現在、128K トークンのコンテキストウィンドウを持つ同じ V3.1 モデル上で動作します。（[DeepSeek API ドキュメント][1], [Data Science Dojo][2]）

#### 2. **拡張されたコンテキストサポート**

* 両モードは拡張された 128K トークンコンテキストをサポートしており、非常に長い入力の処理を可能にする主要なアップグレードです。（[DeepSeek API ドキュメント][1], [Hugging Face][3]）

#### 3. **改善されたフォーマットと機能**

* **Anthropic API 互換性** がサポートされるようになり、DeepSeek を Anthropic スタイルのクライアントライブラリと統合しやすくなりました。（[DeepSeek API ドキュメント][1]）
* **厳格な関数呼び出し** が（ベータ版で）サポートされ、API を通じてより堅牢で検証されたツール呼び出しが可能になります。（[DeepSeek API ドキュメント][1]）

#### 4. **UI トグルと API 呼び出し**

* Web UI 上（「DeepThink」ボタン）では、ユーザーは対話的にモードを切り替えることができます。
* **API** では、`model` パラメータを `"deepseek-chat"`（非思考用）または `"deepseek-reasoner"`（思考用）のいずれかに設定することで、明示的にモードを選択する必要があります。（[DeepSeek API ドキュメント][1]）

#### 5. **その他の機能強化**

* **より多くの API リソース** と全体的によりスムーズな開発者体験が導入されました。（[DeepSeek API ドキュメント][1]）
* 基礎となるトークナイザーとチャットテンプレートが更新され、モードベースの動作（例：`` トークンの適切な挿入）をサポートするようになりました。（[Hugging Face][3]）

---

### 要約：変更点 — 表なしで

* **新しい命名**:

  * `deepseek-chat` → 非思考モード
  * `deepseek-reasoner` → 思考モード

* **共有アーキテクチャ**: 両者は、長い 128K トークンコンテキストウィンドウを持つ同じ 671B パラメータモデル上に構築されています。

* **強化された統合オプション**:

  * Anthropic スタイルの API をサポート。
  * 厳格な関数呼び出し（ベータ）を提供し、より安全なスキーマベースのツール連携を可能にします。

* **テンプレートの更新**: API は現在、モードを区別するためにプロンプト内で特別なトークン (``) を使用し、チャットテンプレートのロジックを刷新しました。

* **開発者体験**: プラットフォームには、より多くのリソース、更新されたドキュメント、そして全体的によりスムーズな統合プロセスが含まれています。

---

### 使用例 (Python/HTTP)

**非思考 (高速応答):**

```python
import openai  # または DeepSeek 互換 SDK
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role":"user","content":"ジョークを教えてください。"}],
)
```

**思考 (深い推論):**

```python
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role":"user","content":"空が青い理由を説明してください。"}],
)
```

**関数呼び出し (厳格モード, ベータ):**
JSON スキーマで関数（ツール）を定義し、モデルにそれらを呼び出させ、構造化された呼び出しを受け取り、実行してフィードバックすることができます — 自律エージェントの構築に最適です。（[DeepSeek API ドキュメント][1], [Reddit][4], [apidog][5]）

---

ツール使用のためのプロンプト作成、コストや速度の最適化、または Anthropic 互換インターフェースの詳細な調査について、お手伝いが必要でしたらお知らせください！

[1]: https://api-docs.deepseek.com/news/news250821?utm_source=chatgpt.com "DeepSeek-V3.1 Release"
[2]: https://datasciencedojo.com/blog/deep-seek-v3-1/?utm_source=chatgpt.com "Deep Seek v3.1: The Next Leap in Open-Source Large ..."
[3]: https://huggingface.co/deepseek-ai/DeepSeek-V3.1?utm_source=chatgpt.com "deepseek-ai/DeepSeek-V3.1"
[4]: https://www.reddit.com/r/LocalLLaMA/comments/1munvj6/the_new_design_in_deepseek_v31/?utm_source=chatgpt.com "The new design in DeepSeek V3.1 : r/LocalLLaMA"
[5]: https://apidog.com/blog/deepseek-v3-1-api/?utm_source=chatgpt.com "How to Use DeepSeek-V3.1 API ?"