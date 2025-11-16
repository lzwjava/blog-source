---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: 大規模言語モデル学習用テキストデータの調達
translated: true
type: note
---

### 大規模言語モデル学習のためのテキストデータ取得方法

大規模言語モデル（LLM）の学習には、書籍、ウェブサイト、コードなどから得られる多様で高品質なテキストデータが大量に必要です（多くの場合、数兆トークン規模）。主な課題は、スケール（テラバイトからペタバイト）、品質（ノイズ、重複、低価値コンテンツのフィルタリング）、合法性（著作権尊重、パブリックドメインまたはライセンスデータの使用）です。データソースを確保するためのステップバイステップガイドを以下に示します。

1.  **パブリックウェブクロールから始める**: これらはほとんどのLLM学習の基盤です。インターネットのスナップショットを取得します。
    - CC-NetやDedup（Hugging Face経由のPythonライブラリ）などのツールを使用してクリーンなテキストをフィルタリングします。
    - サイズに対処するためにチャンクで処理します。ダウンロードにはクラウドストレージ（例：AWS S3）を使用します。

2.  **キュレーションデータセットを利用する**: 研究グループによる事前フィルタリング済みコレクション。APIまたは直接リンク経由でダウンロードします。
    - 多言語、ドメイン固有（コード、科学など）のサブセットに焦点を当て、ニーズに合わせます。
    - Hugging Face Datasetsライブラリのようなツールを使用すると読み込みが容易になります: `from datasets import load_dataset`

3.  **ドメイン固有のソースで補足する**:
    - 書籍: Project Gutenberg（パブリックドメイン）。
    - Wikipedia: 言語別ダンプ。
    - コード: GitHubアーカイブ（BigCode経由）。
    - 合成データを生成: 既存のモデル（例: OpenAI API経由）を使用して推論チェーンを作成しますが、汚染を避けるためにクリーニングします。

4.  **法的・倫理的ヒント**:
    - オープンライセンス（例: CC-BY, MIT）に固執します。
    - 重複排除（MinHashなどのツール）と個人識別情報（PII）の除去を行います。
    - カスタム学習では、スケーリングする前に小規模（例: 1-10GBでのファインチューニング）から始めます。
    - 計算コスト: 控えめな学習でも数百GPU時間を見込んでください。テストにはColabやRunPodを使用します。

5.  **処理パイプライン**:
    - ダウンロード → クリーニング（HTML、非テキストの除去） → トークン化（例: TikTokenを使用） → 学習。
    - ライブラリ: サンプリング用のPandas、前処理用のspaCy/NLTK。

パブリックデータセットは無料で大規模であり、愛好家や研究者に理想的です。プロダクション環境では、企業は独自データをライセンスすることが多いです。

### 特定モデルの学習データソース

OpenAI、Anthropic、DeepSeekなどのプロプライエタリモデルは、競合上の理由から正確なレシピを秘密にしていますが、論文、ブログ、リーク情報を通じて高レベルの詳細を共有しています。オープンソースモデル（例: Llama, Mistral）はより透明性が高く、データセットの設計図を公開することがよくあります。

-   **OpenAIのGPTモデル（例: GPT-4o）**:
    公開されているインターネットデータ（フィルタリングされたウェブクロール）、書籍、記事、コードを混在させて学習します。初期のGPTはCommon Crawlを多用しました。後期のモデルは高品質なSTEM/コーディングソースを重視しています。総計: 数兆トークン、重複排除を徹底。ライセンスデータとユーザーインタラクション（オプトアウト可能）も組み込まれています。完全な公開リリースはありませんが、本質的には「インターネット全体」—スクレイピング、フィルタリング、拡張されたものです。

-   **Anthropicのモデル（例: Claude 3.5）**:
    安全で役立つデータに焦点: パブリックウェブテキスト、書籍、アラインメントのために生成された合成例（例: Constitutional AI）。Claudeからのユーザーチャット（オプトアウト利用可能）やHH-RLHFのようなRLHFデータセットを使用します。多様で非有害なソースを重視。スクレイピングされたYouTubeトランスクリプトをめぐる論争あり。総規模: 同様に数兆トークンですが、倫理面でより厳選されています。

-   **DeepSeekモデル（例: DeepSeek-V3, R1）**:
    中国のオープン寄りモデルで、プレーンなウェブページ、電子書籍、コードリポジトリを使用。V3は意図的な合成データなしで14.8Tトークンを事前学習しましたが、R1はリジェクションサンプリングにより（以前のモデルによって生成された）60万の合成推論サンプルを追加しています。ソース: ウェブクロール + 技術文書。プロプライエタリな混合ですが、論文では透明性があります。

-   **オープンソースモデル（例: Llama 3, BLOOM, GPT-J）**:
    これらは明示的に、The Pile（800GB 多言語混合）、C4（Colossal Clean Crawled Corpus, 750GB 英語ウェブ）、OSCAR（多言語Common Crawl）などのパブリックデータセットを使用します。BLOOMはROOTS（1.6TB, 46言語）を使用しました。プロプライエタリデータを避け、再現性に焦点を当てています。正確な内訳はHugging Faceのモデルカードを確認してください。

要するに: すべてがウェブスケールのデータに依存していますが、プロプライエタリモデルは品質のためにフィルタリング/ライセンス/合成データを追加しています。オープンソースはコミュニティでキュレーションされたパブリックデータに依存します。

### 大規模パブリックテキストデータセットのダウンロードリンク

以下に、無料でダウンロード可能な主要なソースを記載します（サイズは概算。更新を確認してください）。ストレージが限られている場合はサブセットから始めてください。

-   **Common Crawl**: 月次ウェブスナップショット（合計ペタバイト規模）。CC-MAINインデックスでフィルタリング。[Common Crawl Archives](https://commoncrawl.org/get-started)
-   **The Pile**: 800GBの多様な英語テキスト（書籍、コード、arXivなど）。[EleutherAI The Pile on Hugging Face](https://huggingface.co/datasets/EleutherAI/pile)
-   **C4 (Colossal Clean Crawled Corpus)**: 750GBのクリーニング済み英語ウェブ（T5/GPTに使用）。[TensorFlow Datasets C4](https://www.tensorflow.org/datasets/catalog/c4)
-   **OSCAR (Open Super-large Crawled Aggregated coRpus)**: 多言語ウェブ（22言語、～10TB）。[OSCAR on Hugging Face](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201)
-   **Wikipedia Dumps**: 全文抽出（英語: ～20GB）。[Wikimedia Downloads](https://dumps.wikimedia.org/enwiki/latest/)
-   **BooksCorpus/OpenWebText**: 11GB書籍 + 40GB Reddit/ウェブ（GPT-2時代）。[OpenWebText on GitHub](https://github.com/jcpeterson/openwebtext)
-   **RedPajama**: 1T+ トークン、Llama論文から複製。[TogetherAI RedPajama on HF](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
-   **LLMDataHub**: 100以上のデータセット（チャット、コードなど）のキュレーションリスト。[GitHub LLMDataHub](https://github.com/Zjh-819/LLMDataHub)

詳細は、Hugging Face Datasetsハブを参照してください: [Hugging Face Datasets](https://huggingface.co/datasets)。常にライセンスを確認してください！

**参考文献**  
[How ChatGPT and our foundation models are developed](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-language-models-are-developed)  
[What GPT-oss Leaks About OpenAI's Training Data](https://www.lesswrong.com/posts/iY9584TRhqrzawhZg/what-gpt-oss-leaks-about-openai-s-training-data)  
[Anthropic Will Use Claude Chats for Training Data](https://www.wired.com/story/anthropic-using-claude-chats-for-training-how-to-opt-out/)  
[Anthropic's HH-RLHF Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf)  
[What went into training DeepSeek-R1?](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)  
[The Complete Guide to DeepSeek Models](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)  
[LLMDataHub: Awesome Datasets for LLM Training](https://github.com/Zjh-819/LLMDataHub)  
[Open-Sourced Training Datasets for LLMs](https://kili-technology.com/large-language-models-llms/9-open-sourced-datasets-for-training-large-language-models)  
[LLM Training Data: The 8 Main Public Data Sources](https://oxylabs.io/blog/llm-training-data)