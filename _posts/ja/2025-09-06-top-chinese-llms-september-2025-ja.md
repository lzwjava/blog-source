---
audio: false
date: 2025-09-06
generated: true
image: false
lang: ja
layout: post
title: 2025年9月 中国トップLLM
translated: true
type: note
---

以下は、最新のレポートとベンチマークに基づく**2025年9月時点での中国トップLLM**の更新された見方です。表形式の比較はなく、読みやすくするために簡潔な叙述形式でまとめています：

---

## 2025年9月時点での主要な中国製LLM

### 1. **DeepSeek-V3 / R1**

* **DeepSeek-V3** (Mixture-of-Experts設計、約250Bパラメータ) は、計算効率に優れ、最高水準のパフォーマンスを提供します。([Second Talent][1], [Index.dev][2])
* **DeepSeek-R1** は、そのコスト効率に優れたオープンソース版であり、わずかな予算にもかかわらず、推論および推論集中タスクで欧米の対抗モデルを凌駕し、世界的に注目を集めています。([The Guardian][3], [TIME][4], [The Sun][5])

### 2. **Qwenファミリー (Alibaba Cloud)**

* **Qwen 3** (235Bパラメータまでの密および疎バリアント、128Kトークンのコンテキスト長) は2025年半ばにリリースされ、Apache-2.0ライセンス下にあります。([Wikipedia][6])
* 世界的に非常に高い評価を受けており、ベンチマークで多くの欧米モデルを上回りました。([Wikipedia][6], [TechWire Asia][7])

### 3. **Kimi K2 (Moonshot AI)**

* **Kimi K2** は2025年7月にローンチされ、1兆パラメータ規模のMoEモデル (アクティブは32B) で、修正MITライセンス下でオープンウェイトを提供しています。([Wikipedia][8])
* 世界トップクラスのモデルに数えられ、技術オブザーバーによって言及され、広く使用されているオープンウェイトの一つです。([Simon Willison’s Weblog][9], [Wikipedia][8])

### 4. **GLM-4.5 / GLM-4.5V (Zhipu AI / Z.ai)**

* **GLM-4.5** (共通ベンチマークでSOTA) は2025年半ばにリリース。**GLM-4.5V** (106Bのビジョン言語モデル) は2025年8月にローンチしました。([Wikipedia][10])
* GLM-4.5は現在、特に中国国内において、Claudeに対する信頼性の高いコスト効率の良い代替品として位置づけられています。([Reuters][11])

### 5. **Ernie X1 & Ernie 4.5 (Baidu)**

* 推論に焦点を当てた **Ernie X1** と、コストを大幅に抑えながらGPT-4.5を上回るマルチモーダルモデル **Ernie 4.5** は、ともに2025年初頭に発表され、6月までにオープンソース化される予定でした。([Business Insider][12], [Wikipedia][13])

### 6. **Yi (01.AI)**

* **Yi-34B** は、初期から世界的にトップクラスの事前学習済みベースLLMの一つとして認識されていました。([Wikipedia][14])
* **Yi-Coder** (最大128Kトークンのコンテキスト長) と **Yi-Lightning** は、コーディングと効率性のために最適化されています。([Wikipedia][14])

### 7. **Wu Dao 3.0, GLM-4 Plus (ChatGLM), Doubao 1.5 Pro, Kimi k1.5**

* 前世代ではありますが、特定のユースケースでは依然として関連性があります：

  * **Wu Dao 3.0**
  * **ChatGLM (GLM-4 Plus)**
  * **Doubao 1.5 Pro**
  * **Kimi k1.5**
    これらはすべて、優れた多言語対応能力と推論能力を備えた強力なオープンソースの先駆者として認識されています。([Index.dev][15])

### 8. **dots.llm1 (Rednote / Xiaohongshu)**

* 2025年に登場した新参者で、オープンソースとしてリリースされ、コーディングにおいてAlibabaのQwen 2.5と同等のパフォーマンスを示していますが、DeepSeek-V3には及びません。([Reuters][16])

---

## 簡潔なまとめ (叙述形式)

* **DeepSeek-V3 / R1**: パフォーマンスと価格の両面でトップクラス。
* **Qwen 3**: Alibabaの旗艦オープンアクセスモデルファミリーで、ベンチマークを席巻。
* **Kimi K2**: Moonshot AIのMoE、1兆パラメータ、オープンライセンスの主力モデル。
* **GLM-4.5 / 4.5V (Zhipu/Z.ai)**: ベンチマークでSOTAを達成し、Claudeからの移行に魅力的。
* **BaiduのErnie X1 & 4.5**: パフォーマンスと効率に優れた競合モデル、間もなくオープンソース化。
* **Yiシリーズ (01.AI)**: 効率的で長いコンテキスト長を備え、強力なコーディング能力を持つ。
* **旧世代モデル (Wu Dao, ChatGLMなど)**: 特定の分野で依然として重要な役割を担う。
* **dots.llm1**: ソーシャルメディア企業から登場した、注目すべき新興オープンモデル。

---

## これが重要な理由

2025年の中国AIシーンは、**パフォーマンス、オープン性、コスト効率**によって特徴づけられています。DeepSeekやKimiのようなモデルは、高い精度を維持しながら欧米の巨大企業を価格で下回り、AlibabaのQwenファミリーはベンチマークで基準を設定し続け、ZhipuやBaiduは自らの革新をますますオープンにしています。オープンモデルへの移行は加速しており、中国の開発者と政府戦略は、国内での広範な採用と国際競争力の強化に焦点を当てています。([wsj.com][17], [Reuters][16], [Business Insider][12])

---

* [Reuters](https://www.reuters.com/technology/chinas-ai-startup-zhipu-offers-plan-claude-ai-users-migrate-its-own-model-2025-09-05/?utm_source=chatgpt.com)
* [Business Insider](https://www.businessinsider.com/baidu-ernie-x1-ai-reasoning-model-china-competition-openai-2025-3?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/media-telecom/rednote-joins-wave-chinese-firms-releasing-open-source-ai-models-2025-06-09/?utm_source=chatgpt.com)

[1]: https://www.secondtalent.com/resources/chinese-open-source-llms-ai-leaders/?utm_source=chatgpt.com "Top 5 Chinese Open-Source LLMs Dominating 2025"
[2]: https://www.index.dev/blog/chinese-open-source-llms?utm_source=chatgpt.com "Top 5 Chinese Open-Source LLM Models"
[3]: https://www.theguardian.com/commentisfree/2025/jan/28/deepseek-r1-ai-world-chinese-chatbot-tech-world-western?utm_source=chatgpt.com "The DeepSeek panic reveals an AI world ready to blow"
[4]: https://time.com/7210296/chinese-ai-company-deepseek-stuns-american-ai-industry/?utm_source=chatgpt.com "What to Know About DeepSeek, the Chinese AI Company Causing Stock Market Chaos"
[5]: https://www.thesun.co.uk/tech/33023972/china-cheap-ai-chatbot-deepseek-success/?utm_source=chatgpt.com "China's new cheap AI DeepSeek sparks ALARM as it outperforms West's models like ChatGPT amid race to superintelligence"
[6]: https://en.wikipedia.org/wiki/Qwen?utm_source=chatgpt.com "Qwen"
[7]: https://techwireasia.com/2025/07/china-open-source-ai-models-global-rankings/?utm_source=chatgpt.com "China open-source AI models dominate global rankings"
[8]: https://en.wikipedia.org/wiki/Moonshot_AI?utm_source=chatgpt.com "Moonshot AI"
[9]: https://simonwillison.net/2025/Jul/30/chinese-models/?utm_source=chatgpt.com "The best available open weight LLMs now come from China"
[10]: https://en.wikipedia.org/wiki/Z.ai?utm_source=chatgpt.com "Z.ai"
[11]: https://www.reuters.com/technology/chinas-ai-startup-zhipu-offers-plan-claude-ai-users-migrate-its-own-model-2025-09-05/?utm_source=chatgpt.com "China's AI startup Zhipu offers plan for Claude AI users to migrate to its own model"
[12]: https://www.businessinsider.com/baidu-ernie-x1-ai-reasoning-model-china-competition-openai-2025-3?utm_source=chatgpt.com "China puts America's AI industry on notice again with Ernie X1, Baidu's new model"
[13]: https://en.wikipedia.org/wiki/Ernie_Bot?utm_source=chatgpt.com "Ernie Bot"
[14]: https://en.wikipedia.org/wiki/01.AI?utm_source=chatgpt.com "01.AI"
[15]: https://www.index.dev/blog/chinese-ai-models-deepseek?utm_source=chatgpt.com "Top 6 Chinese AI Models Like DeepSeek (LLMs)"
[16]: https://www.reuters.com/business/media-telecom/rednote-joins-wave-chinese-firms-releasing-open-source-ai-models-2025-06-09/?utm_source=chatgpt.com "Rednote joins wave of Chinese firms releasing open-source AI models"
[17]: https://www.wsj.com/tech/ai/how-china-is-girding-for-an-ai-battle-with-the-u-s-5b23af51?utm_source=chatgpt.com "How China Is Girding for an AI Battle With the U.S."