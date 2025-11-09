---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: コスト効率の高いMarkdownからPDFへのAPI
translated: true
type: note
---

### おすすめの低コスト案: Google Cloud Run

MarkdownをPDFに変換するシンプルなJavaベースのAPI（例: Flying SaucerやiTextなどのライブラリを使用）で、個人ブログ用途で週に約100リクエストのみの場合、**Google Cloud Run**が最も費用対効果の高い選択肢です。これはサーバーレスプラットフォームで、コンテナ化されたアプリを実行し、アイドル時にはゼロにスケールダウンし、実際の使用量に対してのみ課金されます。VMの管理や常時稼働のコストを心配する必要がなく、あなたのユースケースのような低トラフィックのシナリオに最適です。

#### 他の選択肢よりもCloud Runが優れている理由
- **Compute Engine (VM) との比較**: VMはアイドル状態でも固定の時間単位のコストがかかり、過剰でより高価になります（小さなインスタンスでも最低〜$5–10/月）。
- **App Engineとの比較**: 同様のサーバーレスの利点がありますが、Cloud RunはJavaコンテナに対してより柔軟で、散発的な使用では往々にしてより安価です。
- あなたのワークロードは無料枠に完全に収まるため、実際には**月額$0**が見込めます。

#### 推定コスト
週100リクエスト（月約400リクエスト）の場合：
- 各リクエストが1 vCPUと0.5 GiBメモリを10秒間使用すると仮定（MarkdownからPDFへの迅速な変換としては控えめな見積もり）。
- 総使用量：月約4,000 vCPU秒および約2,000 GiB秒。
- **無料枠がすべてカバー**: ほとんどのリージョンで、月180,000 vCPU秒、360,000 GiB秒、200万リクエストが無料です。
- 仮に超過しても（可能性は低い）、有料レートは無料枠超過後、〜$0.000024/vCPU秒 + $0.0000025/GiB秒 + リクエスト100万回あたり$0.40 — それでも月$0.10未満です。

あなたのユースケースではエグレス料金はかかりません（同一リージョン内の内部APIコールは無料です）。

#### 推奨リージョン: us-central1 (アイオワ)
- これはCloud Runにおいて最も安価なTier 1リージョンであり、コンピュートのレートが最も低く、北米におけるレイテンシに対する追加料金もありません。
- Tier 1リージョン（米国/欧州）間での価格は類似していますが、us-central1は平均インスタンスコストでわずかに優位です。
- 北米以外（例: 欧州やアジア）にいる場合は、レイテンシを改善するため、最寄りのTier 1リージョン（例: europe-west1 (ベルギー)）に切り替えてください — コスト差は10%未満です。
- Tier 2リージョン（例: asia-southeast1）は20〜50%高価なので避けてください。

#### Javaサーバーのクイックセットアップガイド
1.  **アプリのビルド**: シンプルなREST APIにSpring Bootを使用します。エンドポイント例: Markdown本文を含む POST `/convert`、PDFを返す。
    - 依存関係を追加: `implementation 'org.xhtmlrenderer:flying-saucer-pdf:9.1.22'`（または類似品）。
    - コードスニペット例:
      ```java:disable-run
      @RestController
      public class MarkdownController {
          @PostMapping("/convert")
          public ResponseEntity<byte[]> convert(@RequestBody String markdown) {
              // 変換ロジックをここに記述 (例: markdownをHTMLに、その後PDFに変換)
              byte[] pdfBytes = // あなたの変換結果;
              return ResponseEntity.ok()
                  .header("Content-Type", "application/pdf")
                  .body(pdfBytes);
          }
      }
      ```
2.  **コンテナ化**: `Dockerfile` を作成:
    ```
    FROM openjdk:17-jdk-slim
    COPY target/your-app.jar app.jar
    ENTRYPOINT ["java", "-jar", "/app.jar"]
    ```
    ビルド: `docker build -t gcr.io/your-project/markdown-api .`
3.  **Cloud Runへのデプロイ**:
    - GCPコンソールでCloud Run APIを有効にします。
    - `gcloud run deploy markdown-api --image gcr.io/your-project/markdown-api --platform managed --region us-central1 --allow-unauthenticated --memory 512Mi --cpu 1 --max-instances 1`
    - URLを取得: `https://markdown-api-abc.run.app/convert`
4.  **テスト**: MarkdownのPOSTリクエストを送信；自動スケーリングされます。

GCPが初めての場合は、$300の無料トライアルに登録してください。請求ダッシュボードでコストを監視します。

[Cloud Run 料金](https://cloud.google.com/run/pricing)
[GCP リージョンガイド](https://www.cloudzero.com/blog/gcp-regions/)
[Cloud Run クイックスタート](https://cloud.google.com/run/docs/quickstarts/build-and-deploy)