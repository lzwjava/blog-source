---
audio: false
date: 2025-09-13
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 最新AIモデルとその応用
translated: true
type: note
---

以下は、GPT-5、Gemini 2.5 Pro、GPT-5 mini、およびそれらがCopilot / プレミアムモデルでどのように使用されているかについて、私たちが*知っている*ことのまとめです（2025年9月中旬時点）：

---

## GPT-5 (OpenAI)

* **リリース**: 2025年8月7日。 ([OpenAI][1])
* **概要**: 推論能力の向上、幻覚発生の低減、コーディング、数学、文章作成、健康、視覚認識などにおけるパフォーマンス向上を備えた統一LLM。より要求の厳しいタスク向けに「GPT-5 pro」バージョンを含む。 ([OpenAI][1])
* **推論 / 思考**: GPT-5は内部メカニズム（「高速」対「深い推論」）を持ち、ユーザーは「GPT-5 thinking」を選択するか、「think hard about this」のようなプロンプトを与えて、より詳細な推論を要求できる。 ([OpenAI][1])
* **アクセス階層 / 制限**:

  * すべてのChatGPTユーザー（無料 + 有料）がアクセス可能。 ([OpenAI][1])
  * 無料ユーザーは使用量がより制限されており、一定の使用後はより軽量なバージョン（「GPT-5 mini」）に切り替えられる可能性がある。 ([OpenAI][1])
  * 有料（Plus, Pro, Team, Enterprise, EDU）はより高い使用制限を取得。Proユーザーは「GPT-5 pro」を取得。 ([OpenAI][1])

---

## Gemini 2.5 Pro (Google)

* **リリース / 利用可能性**:

  * Gemini 2.5 Pro (実験版) は2025年3月25日に最初に発表された。 ([blog.google][2])
  * 安定版（「一般提供」）のGemini 2.5 Proは2025年6月17日にリリースされた。 ([Google Cloud][3])
* **能力**: GoogleのGemini 2.5ファミリーで最も先進的なモデル。大規模なコンテキストウィンドウ（100万トークン）、強力な推論、コーディング、多言語サポートなどを備える。 ([blog.google][2])

---

## GPT-5 mini

* **概要 / 時期**: GPT-5 miniは、GPT-5のより軽量/高速なバージョンで、2025年8月中旬にGitHub Copilot（パブリックプレビュー）で利用可能になった。 ([The GitHub Blog][4])
* **場所と方法**: GitHub Copilot Chat (on github.com)、VS Code、GitHub Mobile (iOS/Android) で利用可能。ユーザーのモデルピッカーにも表示される。 ([The GitHub Blog][4])
* **プレミアムリクエスト / コスト**: GitHub Copilotの有料プランにおける「プレミアムリクエスト」を*消費しない*。つまり、GPT-5 miniの使用は「プレミアムリクエスト」のクォータを消費しない。 ([The GitHub Blog][4])

---

## **Copilot / Premium / Microsoft / GitHub** でのこれらの使用法

* **GitHub Copilot**:

  * すべてのCopilotプラン（無料プランを含む）がGPT-5 miniにアクセス可能。 ([The GitHub Blog][4])
  * GPT-5 (フルバージョン) は有料のCopilotプランでのみ利用可能。 ([The GitHub Blog][5])
  * モデルピッカーにより、ユーザーは自身のプランと組織設定に応じて、GPT-5、GPT-5 miniなどを選択できる。 ([The GitHub Blog][4])

* **Microsoft Copilot / Copilot Studio / 365 Copilot**:

  * Microsoftは自社のCopilot製品でのGPT-5の使用をサポート。例えば、Copilot Studioを使用するメーカーはGPT-5を選択でき、異なるGPT-5バリアント（チャット対推論）間の自動ルーティングなどが存在する。 ([Microsoft Developer][6])
  * プレミアム機能は一般に有料サブスクリプションを必要とする。GPT-5の使用、またはより高容量のモデル、より多くの推論を備えたモデルは、多くの場合、有料ユーザーまたはエンタープライズ階層に制限される。 ([OpenAI][1])

---

ご希望であれば、**パフォーマンス比較**（GPT-5対Gemini 2.5 Proなど）や、**将来/噂されている機能**についても掘り下げることができます。それらも必要ですか？

[1]: https://openai.com/index/introducing-gpt-5/?utm_source=chatgpt.com "Introducing GPT-5"
[2]: https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/?utm_source=chatgpt.com "Gemini 2.5: Our most intelligent AI model"
[3]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions?utm_source=chatgpt.com "Model versions and lifecycle | Generative AI on Vertex AI"
[4]: https://github.blog/changelog/2025-08-13-gpt-5-mini-now-available-in-github-copilot-in-public-preview/?utm_source=chatgpt.com "GPT-5 mini now available in GitHub Copilot in public preview"
[5]: https://github.blog/changelog/2025-09-09-openai-gpt-5-and-gpt-5-mini-are-now-generally-available-in-github-copilot/?utm_source=chatgpt.com "OpenAI GPT-5 and GPT-5 mini are now generally available ..."
[6]: https://developer.microsoft.com/blog/gpt-5-for-microsoft-developers?utm_source=chatgpt.com "GPT-5 for Microsoft Developers"