---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Google Imagen 4 プレビューガイド
translated: true
type: note
---

Google Imagen 4 Preview 0606を使用するには、GoogleのVertex AIプラットフォームを通じてアクセスする必要があります。これはテキストから画像を生成するためのGenerative AI Previewサービスです。以下は利用可能な情報に基づくステップバイステップガイドです：

### Google Imagen 4 Preview 0606の使用方法

1. **Vertex AIへのアクセス**：
   - **プラットフォーム**：Imagen 4 Preview 0606はGoogle CloudのVertex AIで利用可能です。開始するにはGoogle Cloudアカウントが必要です。
   - **サインアップ**：アカウントをお持ちでない場合は、[cloud.google.com](https://cloud.google.com)でサインアップし、プロジェクトを設定してください。これはプレビューサービスであり潜在的なコストが発生する可能性があるため、課金が有効になっていることを確認してください（価格詳細はVertex AIのImagenセクションの価格ページで確認できます）。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)
   - **Vertex AIへの移動**：ログイン後、Google Cloud ConsoleのVertex AIセクションに移動し、Generative AIツールを見つけてください。

2. **環境のセットアップ**：
   - **認証**：Google Cloudの認証情報を使用してアカウントを認証します。次のコマンドを使用してアクセストークンを生成できます：
     ```bash
     gcloud auth print-access-token
     ```
   - **プロジェクトとロケーション**：Google CloudプロジェクトIDとロケーション（例：`us-central1`）を設定します。例：
     ```bash
     export GOOGLE_CLOUD_PROJECT=your-project-id
     export GOOGLE_CLOUD_LOCATION=us-central1
     ```

3. **Imagen 4モデルの使用**：
   - **APIアクセス**：Imagen 4 Preview 0606はVertex AI APIを通じてアクセスできます。モデルエンドポイント`imagen-4.0-generate-preview-06-06`を使用します。cURLやGoogle Gen AI SDK for Pythonなどのツールを使用してプログラムで操作できます。
   - **cURLリクエストの例**：
     ```bash
     curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-06-06:predict" \
     -d '{"instances": [{"prompt": "A cat reading a book"}], "parameters": {"sampleCount": 1}}'
     ```
     これはbase64エンコードされた画像を返します。[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)
   - **Python SDKの例**：
     ```python
     from google import genai
     from google.genai.types import GenerateImagesConfig
     client = genai.Client()
     image = client.models.generate_images(
         model="imagen-4.0-generate-preview-06-06",
         prompt="A dog reading a newspaper",
         config=GenerateImagesConfig(image_size="2K")
     )
     image.generated_images[0].image.save("output-image.png")
     print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")
     ```
     これは画像を生成し、PNGファイルとして保存します。[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

4. **効果的なプロンプトの作成**：
   - **プロンプト構造**：最良の結果を得るには、詳細で具体的なプロンプトを使用してください。被写体、環境、芸術的スタイル（例：写実的、抽象的）、ムード、構図要素（例：カメラアングル）を含めます。例：「夕暮れ時の未来的な都市の鮮やかなグラフィックイラスト、サイバーパンクスタイル、ネオンライトと劇的なローアングル視点」
   - **ヒント**：
     - 明確に：曖昧なプロンプトは予測不可能な結果を招く可能性があります。
     - 無意味な入力（例：ランダムな絵文字）は一貫性のない出力を生成する可能性があるため避けてください。
     - 必要に応じてテキストを指定します。Imagen 4はタイポグラフィのレンダリングが改善されています。[](https://deepmind.google/models/imagen/)[](https://replicate.com/blog/google-imagen-4)
   - **ネガティブプロンプト**：不要な要素を除外するためにネガティブプロンプトを使用できます（例：画像にテキストを入れたくない場合は「no text」）。[](https://docs.aimlapi.com/api-references/image-models/google/imagen-4-preview)

5. **バリアントの探索**：
   - Imagen 4 Preview 0606には、**Fast**（最大10倍高速、バルク生成向けに最適化）や**Ultra**（プロフェッショナル用途向けにプロンプトとの高い整合性）などのバリアントがあります。これらがVertex AIインターフェースで利用可能か確認し、ニーズに基づいて選択してください（例：迅速なプロトタイピングにはFast、高品質出力にはUltra）。[](https://fal.ai/models/fal-ai/imagen4/preview)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

6. **出力と安全性機能の確認**：
   - **出力形式**：画像は2K解像度までのPNGやJPEGなどの標準形式で生成されます。[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **SynthIDウォーターマーク**：すべての画像にはAI生成であることを識別するための不可視のデジタルウォーターマークが含まれており、透明性を確保しています。[](https://deepmind.google/models/imagen/)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - **コンテンツ制限**：Imagen 4は有害なコンテンツを最小化するためのフィルタリングを使用しますが、複雑な構図、小さな顔、中央に配置された画像などで苦労する可能性があります。コンテンツ制限についてはGoogleの利用ガイドラインを確認してください。[](https://deepmind.google/models/imagen/)[](https://cloud.google.com/vertex-ai/generative-ai/docs/image/overview)

7. **代替プラットフォーム**：
   - Imagen 4はReplicate、fal.ai、AI/ML APIなどのサードパーティプラットフォームでも利用可能で、よりシンプルなインターフェースやテスト用のサンドボックス環境を提供する場合があります。例：
     - **Replicate**：「夕暮れ時の静かな山岳風景、ハイパーリアリスティックスタイル」のようなプロンプトでImagen 4を実行します。APIキーと使用方法についてはReplicateのドキュメントを確認してください。[](https://replicate.com/blog/google-imagen-4)[](https://replicate.com/google/imagen-4-fast)
     - **fal.ai**：以下のようなリクエストでAPIを使用：
       ```javascript
       const result = await fal.subscribe("fal-ai/imagen4/preview", {
           input: { prompt: "A serene mountain landscape at sunset, hyperrealistic style" }
       });
       console.log(result.images[0].url);
       ```
       価格は様々です（例：Standard $0.04/画像、Fast $0.04/画像、Ultra $0.06/画像）。[](https://fal.ai/models/fal-ai/imagen4/preview)
   - **GeminiアプリまたはGoogle Workspace**：Imagen 4はGeminiアプリ、Google Slides、Docs、Vidsに統合されており、ワークフロー内で直接画像生成が可能です。例えば、Google Docsでは文書を説明する画像を生成できます。[](https://www.stablediffusion.blog/imagen4)

8. **テストと反復**：
   - 本番環境に統合する前に、サンドボックス環境（例：限定無料テスト用のGoogle AI Studio）でプロンプトを実験してください。[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)
   - プレビューサービスはサポートが限定されているか機能が変更される可能性があるため、プラットフォームのダッシュボードでAPI使用量とコストを監視してください。[](https://fal.ai/models/fal-ai/imagen4/preview)

### 追加注記
- **価格**：Imagen 4のコスト（例：Standard $0.04/画像、Ultra $0.06/画像）についてはVertex AIの価格ページを確認してください。[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)[](https://fal.ai/models/fal-ai/imagen4/preview)
- **制限事項**：Imagen 4は曖昧なプロンプト、小さな顔、完全に中央に配置された構図などで苦労する可能性があります。最良の結果を得るには明確で構造化されたプロンプトを使用してください。[](https://deepmind.google/models/imagen/)
- **可用性**：プレビューサービスとして、機能とサポートは変更される可能性があります。更新情報についてはGoogle Cloudのローンチステージの説明を確認してください。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-fast-generate-preview-06-06)

詳細なドキュメントについては、[Vertex AI Imagenページ](https://cloud.google.com/vertex-ai/docs/generative-ai/image/overview)または[Google Developers Blog](https://developers.googleblog.com)を訪問してください。APIアクセスについては、[x.ai/api](https://x.ai/api)で一般的なAI APIガイダンスを参照できますが、Imagen 4の具体的な詳細はGoogle Cloudにあります。[](https://cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-preview-06-06)[](https://developers.googleblog.com/en/imagen-4-now-available-in-the-gemini-api-and-google-ai-studio/)

特定のプラットフォームやユースケースについてヘルプが必要な場合は、お知らせください！