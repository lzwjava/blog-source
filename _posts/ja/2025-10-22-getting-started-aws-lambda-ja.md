---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AWS Lambda の始め方
translated: true
type: note
---

### AWS Lambda の始め方

AWS Lambda は、サーバーを管理せずにイベントに応じてコードを実行するサーバーレスコンピュートサービスです。以下は、初めてのLambda関数を作成、デプロイ、使用するための初心者向けステップバイステップガイドです。これは公式AWSドキュメントに基づいています。

#### 前提条件
- アクティブなAWSアカウント。お持ちでない場合は [aws.amazon.com](https://aws.amazon.com/) でサインアップしてください。
- Node.jsやPythonなどのプログラミング言語の基本的な知識（Lambdaは多くのランタイムをサポートしています）。

#### ステップ 1: Lambda関数の作成
1. AWS Management Console にログインし、Lambdaサービス（サービスメニューで「Lambda」を検索）に移動します。
2. 関数ページで、**関数の作成** をクリックします。
3. **一から作成** を選択します。
4. **関数名** を入力します（例: `my-first-function`）。
5. **ランタイム** を選択します（例: Node.js 22.x または Python 3.13）。
6. デフォルトのアーキテクチャ（x86_64）のまま、**関数の作成** をクリックします。

これにより、Amazon CloudWatchへのログ書き込みなどの基本的な権限を持つ実行ロール（IAMロール）が自動的に作成されます。

#### ステップ 2: コードの記述
Lambdaコンソールのコードエディタ（**コード** タブ内）で、デフォルトの「Hello World」コードをシンプルなものに置き換えます。以下は、`length` と `width` キーを持つ入力JSONに基づいて長方形の面積を計算する例です。

- **Node.js の例**:
  ```javascript
  exports.handler = async (event) => {
    const length = event.length;
    const width = event.width;
    const area = length * width;
    console.log(`面積は ${area} です`);
    console.log('ロググループ: /aws/lambda/' + process.env.AWS_LAMBDA_FUNCTION_NAME);
    return { area: area };
  };
  ```

- **Python の例**:
  ```python
  import json

  def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = length * width
    print(f"面積は {area} です")
    print(f"ロググループ: /aws/lambda/{context.function_name}")
    return {
        'statusCode': 200,
        'body': json.dumps({'area': area})
    }
  ```

変更を保存します。インタプリタ型言語ではデプロイは自動的に行われます。

コンパイル型言語（例: Java）の場合、ローカルでデプロイパッケージを作成し、コンソールまたはAWS CLI経由でアップロードします。

#### ステップ 3: 関数のテスト
1. **テスト** タブで、**新しいテストイベントの作成** をクリックします。
2. 名前を付けます（例: `test-area-calc`）。
3. サンプルのJSON入力を貼り付けます:
   ```json
   {
     "length": 6,
     "width": 7
   }
   ```
4. 保存して **テスト** をクリックします。

結果は **実行結果** セクションで確認できます（例: `{"area": 42}`）。詳細なログ（実行時間やメモリ使用量など）はCloudWatchで確認してください。

#### ステップ 4: 呼び出しとモニタリング
- **手動呼び出し**: コンソールのテストボタン、またはAWS CLI `aws lambda invoke --function-name my-first-function output.json` を使用します。
- **イベント駆動呼び出し**: API Gateway、S3バケット、DynamoDBストリームなどのトリガーを接続します。**設定** > **トリガー** タブに移動して追加します。
- **ログ**: 自動的にCloudWatch Logsに送信されます。[console.aws.amazon.com/cloudwatch/home#logsV2:log-groups](https://console.aws.amazon.com/cloudwatch/home#logsV2:log-groups) の `/aws/lambda/your-function-name` で確認できます。

主な概念:
- **イベントソース/トリガー**: 関数をイベントデータ（JSONペイロード）とともに呼び出すサービス（例: S3アップロード）。
- **ハンドラー**: イベントを処理するエントリーポイント（例: Node.jsの `index.handler`）。

#### ステップ 5: クリーンアップ（オプション）
コンソールから関数を削除します: アクション > 削除。課金を避けるため、関連するログとIAMロールも削除してください。

#### ヒント
- 無料利用枠（月間100万リクエスト）から始めましょう。
- 高度なデプロイにはAWS SAMまたはServerless Frameworkを使用します。
- 本番環境では、**設定** タブで環境変数、レイヤー、VPC設定を構成します。

[初めてのLambda関数を作成する](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)