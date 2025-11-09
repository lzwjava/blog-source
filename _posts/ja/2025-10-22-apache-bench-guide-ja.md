---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Apache Bench Webサーバーテストガイド
translated: true
type: note
---

### Apache Bench (ab)とは？

Apache Bench (ab) は、Apache HTTP Serverに付属するシンプルなコマンドラインツールで、Webサーバーのパフォーマンスをベンチマークするために使用されます。指定した数のHTTPリクエストをURLに送信し、1秒あたりのリクエスト数、リクエストあたりの時間、転送レート、エラーレートなどのメトリクスを計測します。簡易的な負荷テストには優れていますが、複雑なシナリオ（例：デフォルトではHTTPSをサポートせず、高度なスクリプトも不可）には制限があります。そのような場合はJMeterなどのツールを検討してください。

### インストール方法

abはApache HTTP Serverにバンドルされています。インストール方法は以下の通りです：

- **Ubuntu/Debian (Linux)の場合**:
  ```
  sudo apt update
  sudo apt install apache2-utils
  ```

- **macOS (Homebrew経由)の場合**:
  ```
  brew install httpd
  ```

- **Windowsの場合**:
  公式サイトからApache HTTP Serverをダウンロードし、その`bin`ディレクトリをPATHに追加します。

- **インストールの確認**:
  `ab -V`を実行してバージョンを確認します。

### 基本的な使い方

基本的なコマンド構文は以下の通りです：
```
ab [オプション] URL
```

- **URLの形式**: 完全なHTTP URLである必要があります（例：`http://example.com/`）。（HTTPSの場合は、`openssl s_client`などのラッパーを使用するか、`wrk`などのツールに切り替えてください。）

主なオプション：
- `-n <リクエスト数>`: 実行するリクエスト数（デフォルト: 1）。テストでは100〜1000から始めます。
- `-c <同時接続数>`: 同時に実行するリクエスト数（デフォルト: 1）。サーバーに過負荷をかけないよう低め（例：10〜50）に保ちます。
- `-t <秒数>`: リクエスト数ではなく、指定した時間実行します。
- `-k`: HTTP Keep-Aliveを有効にします（接続を再利用します）。
- `-H "ヘッダー: 値"`: カスタムヘッダーを追加します（例：認証用）。
- `-p <ファイル>`: ファイルからPOSTデータを読み込みます。
- `-T <コンテンツタイプ>`: POSTリクエストのContent-typeを指定します。
- `-l`: 可変長ドキュメントを受け入れます（動的コンテンツ用）。

### ステップバイステップの例

1. **シンプルなGETリクエストのテスト**:
   ローカルサーバーに対して、10の同時接続で100リクエストをシミュレートします：
   ```
   ab -n 100 -c 10 http://localhost:8080/
   ```
   出力例：
   ```
   Server Software:        Apache/2.4.41
   Server Hostname:        localhost
   Server Port:            8080

   Document Path:          /
   Document Length:        1234 bytes

   Concurrency Level:      10
   Time taken for tests:   1.234 seconds
   Complete requests:      100
   Failed requests:        0
   Requests per second:    81.03 [#/sec] (mean)
   Time per request:       123.456 [ms] (mean)
   ```

2. **POSTデータを使用したテスト**（例：フォーム送信）:
   `postdata.txt`ファイルにペイロード（例：`key=value`）を作成します。
   ```
   ab -n 50 -c 5 -p postdata.txt -T application/x-www-form-urlencoded http://example.com/api/endpoint
   ```

3. **指定時間の実行**:
   ```
   ab -n 10000 -c 20 -t 30 http://example.com/  # 最大10kリクエストまたは30秒間
   ```

### 結果の解釈

- **1秒あたりのリクエスト数 (Requests per second)**: 高いほど良い（スループット）。
- **リクエストあたりの時間 (Time per request)**: 低いほど良い（レイテンシ）。
- **転送レート (Transfer rate)**: 帯域幅の効率性。
- 「Failed requests」や「Non-2xx responses」に注意して問題を発見します。
- キャッシュやネットワークの影響で1回の実行結果が偏る可能性があるため、複数回実行して平均を取ります。

### ヒントと制限事項

- **別のマシンから実行**: 可能であればlocalhostに対してテストせず、実際のトラフィックをシミュレートします。
- **ウォームアップ**: キャッシュを準備するために最初に数回リクエストを送信します。
- **スケーリング**: より高い負荷には、`wrk`、`siege`、Locustなどのツールを使用します。
- **HTTPS**: abはネイティブでHTTPSをサポートしていません。プロキシを使用するか、代替ツールを検討してください。
- **エラー**: 「socket: Too many open files」エラーが表示された場合は、OSのファイル記述子の制限を増やします（例：`ulimit -n 4096`）。

詳細については、manページ（`man ab`）または公式ドキュメントを参照してください。

[Apache Bench ドキュメント](https://httpd.apache.org/docs/2.4/programs/ab.html)