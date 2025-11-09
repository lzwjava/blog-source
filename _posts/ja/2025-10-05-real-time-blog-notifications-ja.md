---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: リアルタイムブログ訪問テレグラム通知
translated: true
type: note
---

はい、Cloudflareのログやトラフィックをほぼリアルタイムで分析し、ブログ訪問ごとにTelegram通知を送信するシステムを構築することは可能ですが、標準的なアナリティクスログだけでは簡単ではありません。Cloudflareのアナリティクスは主に集計データ（日次/週次のサマリーなど）であり、ログをエクスポートするLogpush機能でさえデータを1〜5分ごとにバッチ処理するため、訪問ごとの即時アラートには不向きです。Instant Logsはリアルタイムストリーミングを提供しますが、BusinessまたはEnterpriseプランが必要であり、Telegramメッセージをトリガーするにはカスタム処理（WebSocketとスクリプト経由など）が必要です。これはほとんどのユーザーには過剰です。

最も実用的でリアルタイムなアプローチは、**Cloudflare Workers**を使用してブログへの各受信リクエストをインターセプトする方法です。これにより、各訪問でサーバーレスコードが実行され、イベントをログに記録し、Telegram API経由で即座にメッセージを送信できます。低トラフィックでは無料（1日10万リクエストまで）ですが、高トラフィックのブログでは制限に達したりコストが発生したりする可能性があります。さらに、通知がスパムのように送信されるため、フィルタリング（例：特定のIPまたはページのみ）を検討してください。

### クイックセットアップ手順
1. **Telegram Botを作成**:
   - Telegramで@BotFatherにメッセージを送信し、`/newbot`を使用してボットを作成し、ボットトークン（例: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`）をメモします。
   - ボットとチャットを開始し、@userinfobotにメッセージを送信してチャットID（例: `123456789`）を取得します。
   - curlを使用してメッセージ送信をテスト:  
     ```
     curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" \
     -H "Content-Type: application/json" \
     -d '{"chat_id":"<YOUR_CHAT_ID>","text":"Test visit!"}'
     ```

2. **Cloudflare Workerを作成**:
   - Cloudflareダッシュボードにログイン > Workers & Pages > Create application > Create Worker。
   - 名前を付け（例: `blog-visit-notifier`）、デフォルトテンプレートをデプロイ。

3. **通知コードを追加**:
   - ワーカーのコードを編集してリクエストをインターセプトし、Telegramに送信。基本的な例（プレースホルダーを置き換え）:
     ```javascript
     export default {
       async fetch(request, env) {
         // オプション: 訪問をログ記録またはフィルタリング（例：ブログのホームページのみ）
         const url = new URL(request.url);
         if (url.pathname !== '/') {  // 必要に応じてパスを調整
           return fetch(request);  // ブログ以外のページはスキップ
         }

         // Telegramメッセージを送信（ブロックを防ぐため非同期）
         const message = `New visit to ${url.origin}! IP: ${request.headers.get('cf-connecting-ip')}, User-Agent: ${request.headers.get('user-agent')}`;
         await fetch(`https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`, {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
           body: JSON.stringify({
             chat_id: env.TELEGRAM_CHAT_ID,
             text: message,
             parse_mode: 'HTML'  // フォーマットが必要な場合
           })
         }).catch(err => console.error('Telegram send failed:', err));

         // 元のリクエストをブログにプロキシ
         return fetch(request);
       }
     };
     ```
     - これは一致する各リクエストで実行され、基本的な訪問者情報をログに記録し、ページ読み込みを遅らせることなくTelegram経由で送信します。

4. **環境変数を設定**:
   - ワーカー設定 > Variables > Add:  
     - `TELEGRAM_BOT_TOKEN`: ボットトークン。  
     - `TELEGRAM_CHAT_ID`: チャットID。  
   - 保存して再デプロイ。

5. **ワーカーをブログにルーティング**:
   - Workers設定 > Triggers > Add route。  
   - ブログのドメイン/パスに設定（例: `yourblog.com/*`）。  
   - これにより、オリジンサーバーにヒットする前に各訪問でワーカーが実行されます。

6. **テストと監視**:
   - ブログを訪問すると、Telegramで即時に通知が届くはずです。  
   - ダッシュボードのワーカーログでエラーを確認。レート制限（Telegramは30メッセージ/秒など）に達した場合、KVストレージでデバウンスを追加。

### Workersが適さない場合の代替案
- **バッチ処理されたログ分析の場合**: Logpushを使用してHTTPリクエストログをAWS S3やGoogle Pub/Subなどのサービスにエクスポートし、Zapierやn8nなどのツールにパイプしてTelegramアラートを送信（例：時間ごとの訪問を要約）。ただしリアルタイムではありません。
- **統合**: Albatoやn8nなどのツールは、CloudflareウェブフックをTelegramに接続してより広範なイベントに対応できますが、訪問ごとには対応しません。
- **制限**: 無料Workersはリクエストごとに10msのCPU時間です。これはこの用途には問題ありませんが、必要に応じてスケールアップ。スロットリングなしの高トラフィックサイトでは避けてください。

このセットアップにより、Cloudflareトラフィックを実用的な即時アラートに変換できます。コードの調整やエラーへの対応が必要な場合は、詳細を共有してください！

[Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)  
[Telegram Bot API](https://core.telegram.org/bots/api)  
[Cloudflare Instant Logs](https://developers.cloudflare.com/logs/instant-logs/)