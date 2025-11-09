---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: コパイロット エンタープライズ モデル オプション概要
translated: true
type: note
---

**Copilot Enterprise** でどのモデルが使用されているか、具体的には GPT-4.1、GPT-4o、その他のものなのかについてご質問ですね。**2025年9月** 現在の最新かつ関連性の高い情報は以下の通りです。

---

### Copilot Enterprise で利用可能なモデルは？

#### GitHub Copilot Enterprise & Copilot Chat

* **デフォルトでは**、GitHub Copilot Enterprise (および Copilot Chat) は **GPT-4o** 上で動作し、より高速な応答と品質の向上を提供します。([Reddit][1])
* より最近では **GPT-4.1** が利用可能になりましたが、管理者が Copilot 設定のポリシーで明示的に **有効にする必要があります**。有効にされると、ユーザーは VS Code および github.com 上のモデルセレクターから GPT-4.1 を選択できるようになります。([The GitHub Blog][2])

#### Visual Studio Copilot

* **2025年6月** 現在、Visual Studio の Copilot は、デフォルトのモデルとして GPT-4o ではなく **GPT-4.1 を使用するようになりました**。Microsoft のテストでは、GPT-4.1 が **より高速な応答、高品質な提案、そして高い効率性** をもたらすことが示されました。([Visual Studio Magazine][3], [Microsoft Learn][4])

#### Microsoft 365 Copilot (Office 生産性ツール)

* Microsoft は、より広範な Copilot エコシステム（Microsoft 365 Copilot、GitHub Copilot、Copilot Studio などを含む）に **GPT-5** の統合を開始しており、新しい「**Smart Mode**」を通じて、タスクを必要性に基づいて最も適したモデルに自動的に振り分けることで、推論力、コンテキスト保持、対話品質を向上させています。([The Verge][5])
* さらに Microsoft は、プレゼンテーションのデザインやスプレッドシートの自動化などの高度なタスク向けに Anthropic の **Claude Sonnet 4** を統合し、他の機能については引き続き **GPT-5**（および残りの GPT ベースのルート）を使用することを発表しました。([New York Post][6])

---

### まとめ — **Copilot Enterprise** にはどのモデルが適しているか？

* **GitHub Copilot Enterprise / Copilot Chat**:

  * デフォルト: **GPT-4o**
  * オプション: **GPT-4.1** (管理者が有効にした場合)
* **Visual Studio Copilot**: デフォルトは **GPT-4.1**
* **Microsoft 365 Copilot**: **GPT-5 Smart Mode** を活用し、高性能なルーティングと機能を提供 — また、特定のエンタープライズタスク向けに **Claude Sonnet 4** も統合されています。

---

### 簡単な概要 (ご希望に沿って、広いテーブルはなし):

* **GPT-4o**: GitHub Copilot Enterprise のデフォルト。エンタープライズ向けチャットでの速度と品質で知られる。
* **GPT-4.1**: より強力な後継モデル — コード、指示への追従、長いコンテキストにおいて優れる。GitHub Copilot では有効化すれば利用可能、Visual Studio Copilot では現在デフォルト。([OpenAI][7])
* **GPT-5**: 最新モデル。全ての Copilot プラットフォームで Smart Mode を通じて M365 Copilot に統合され、よりスマートなモデル選択を実現。([The Verge][5])
* **Claude Sonnet 4**: PowerPoint や Excel の自動化などの Office タスク向けに主に追加され、GPT-5 と併用。([New York Post][6])

---

### 次に取るべき行動は？

* **GitHub Copilot Enterprise** を管理する**管理者**の場合は、ユーザーがそのパフォーマンス向上を活用できるように、設定を確認して **GPT-4.1 を有効に**してください。
* **Visual Studio Copilot** をご利用の場合は、デフォルトで **GPT-4.1** が使用されています。
* **Microsoft 365 Copilot** をご利用の場合は、**GPT-5 Smart Mode** のロールアウトと **Claude Sonnet 4** の統合の恩恵を受けられます。必要なアクションはありません — これらは既にサービスのレイヤーに組み込まれています。

これらの設定の構成や、お客様の組織固有の環境でのモデルオプションの確認についてサポートが必要でしたら、お知らせください！

[1]: https://www.reddit.com/r/GithubCopilot/comments/1dx2iq1/github_copilot_enterprise_on_gpt4o/?utm_source=chatgpt.com "GitHub Copilot Enterprise on GPT-4o : r/GithubCopilot"
[2]: https://github.blog/changelog/2025-04-14-openai-gpt-4-1-now-available-in-public-preview-for-github-copilot-and-github-models/?utm_source=chatgpt.com "OpenAI GPT-4.1 now available in public preview for GitHub ..."
[3]: https://visualstudiomagazine.com/articles/2025/06/26/new-default-model-for-visual-studio-copilot-so-how-do-you-choose.aspx?utm_source=chatgpt.com "New Default Model for Visual Studio Copilot, So How Do ..."
[4]: https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=vs-2022&utm_source=chatgpt.com "Using AI models in Copilot Chat - Visual Studio (Windows)"
[5]: https://www.theverge.com/news/753984/microsoft-copilot-gpt-5-model-update?utm_source=chatgpt.com "Microsoft brings GPT-5 to Copilot with new smart mode"
[6]: https://nypost.com/2025/09/10/business/microsoft-to-add-anthropic-ai-models-as-rift-with-openai-grows-report/?utm_source=chatgpt.com "Microsoft to add Anthropic AI models - as rift with OpenAI grows: report"
[7]: https://openai.com/index/gpt-4-1/?utm_source=chatgpt.com "Introducing GPT-4.1 in the API"