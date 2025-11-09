---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AWS障害事例分析 2025年10月
translated: true
type: note
---

### 2025年10月20日AWS障害：詳細な事例分析

2025年10月20日に発生したAWS障害は、AWSで最大かつ最も重要なデータセンターである米国東部（バージニア北部）リージョン（us-east-1）を起点とした大規模な障害でした。太平洋夏時間（PDT）で10月19日深夜に始まり、約16時間継続し、140以上のサービスに影響を与え、このリージョンへの依存性により世界的に連鎖しました。このインシデントは、DNS解決、サービス間の依存関係、および復旧プロセスにおける脆弱性を浮き彫りにし、アプリ、ウェブサイト、サービスを利用する何百万人ものユーザーに影響を与えました。以下は、AWSの公式事後分析報告と当時の報告に基づく詳細です。

#### タイムライン
障害は段階的に進行し、検出から始まり、連鎖的な障害へとエスカレートした後、段階的な復旧を遂げました。主な出来事（全てPDT時刻）：

| 時刻 | イベント |
|------|-------|
| 11:49 PM (10月19日) | us-east-1の複数のAWSサービスでエラーレートとレイテンシーの増加を検出。 |
| 12:11 AM (10月20日) | AWSがエラーレートの上昇を公表；DownDetectorなどの監視サイトで初期ユーザーレポートが急増。 |
| 12:26 AM | us-east-1のDynamoDB APIエンドポイントに対するDNS解決障害が問題点として特定される。 |
| 1:26 AM | DynamoDB API（Global Tablesを含む）での高いエラーレートが確認される。 |
| 2:22 AM | 初期の軽減策を適用；復旧の初期兆候が現れる。 |
| 2:24 AM | DynamoDB DNS問題が解決され、サービスの部分的な復旧を引き起こす—しかし、EC2起動障害とNetwork Load Balancer（NLB）ヘルスチェック失敗が表面化。 |
| 3:35 AM | DNSが完全に軽減；ほとんどのDynamoDB操作が成功するが、EC2起動は全アベイラビリティーゾーン（AZ）で障害状態のまま。 |
| 4:08 AM | EC2エラーとSQS Event Source MappingsのためのLambdaポーリング遅延への対応を継続。 |
| 5:48 AM | 一部のAZでEC2起動が部分的に復旧；SQSのバックログ解消が始まる。 |
| 6:42 AM | AZ全体に軽減策を展開；AWSは安定化のため、新規EC2インスタンス起動にレート制限を実施。 |
| 7:14 AM | サービス全体でAPIエラーと接続問題が継続；ユーザー影響を伴う障害がピークに（例：アプリの停止）。 |
| 8:04 AM | 調査がEC2内部ネットワークに焦点を当てる。 |
| 8:43 AM | ネットワーク問題の根本原因を特定：NLBヘルスモニタリングのためのEC2内部サブシステムの障害。 |
| 9:13 AM | NLBヘルスチェックへの追加的な軽減策。 |
| 9:38 AM | NLBヘルスチェックが完全に復旧。 |
| 10:03 AM – 12:15 PM | EC2起動が段階的に改善；Lambda呼び出しと接続性がAZ間で段階的に安定化。 |
| 1:03 PM – 2:48 PM | Redshift、Amazon Connect、CloudTrailなどのサービスのスロットルが緩和され、バックログが処理される。 |
| 3:01 PM | 全サービスで完全な運用正常性が回復；AWS Config、Redshiftなどの軽微なバックログは数時間以内に解消見込み。 |
| 3:53 PM | AWSが障害解決を宣言。 |

DownDetectorなどのプラットフォームでのユーザーレポートは、PDT午前6時頃にピーク（5,000件以上のインシデント）に達した後、減少しました。

#### 根本原因
この障害は、us-east-1のDynamoDBサービスエンドポイントに影響を与えたDNS解決障害に起因していました。NoSQLデータベースサービスであるDynamoDBは、多くのAWS機能にとって重要な「コントロールプレーン」として機能し、メタデータ、セッション、ルーティングを扱っています。DNSがこれらのエンドポイントを解決できなくなると、DynamoDB APIはレイテンシーとエラーの増加を経験しました。

この初期の問題は速やかに解決されましたが、連鎖を引き起こしました：
- EC2インスタンスの起動は、メタデータストレージとしてDynamoDBに依存しているため、失敗しました。
- NLBヘルスを監視するEC2の内部サブシステムの潜在的なバグがネットワーク接続問題を悪化させ、ロードバランシングとAPI呼び出しにおけるより広範な障害につながりました。
- 復旧努力には、過負荷を防ぐためのスロットリング（例：EC2起動とLambda呼び出しの制限）が含まれましたが、依存サービスのリトライが負荷を増幅させました。

AWSは、サイバー攻撃ではなく、インフラストラクチャ関連の不具合（おそらく障害のあるDNSデータベース更新またはバックアップシステムの障害に関連）であったと確認しました。世界的な波及が発生したのは、us-east-1が他のリージョンのリソースに対しても、IAMやLambdaなどの主要なコントロールプレーンをホストしているためです。

#### 影響を受けたサービス
142以上のAWSサービスが影響を受け、主にDynamoDB、EC2、またはus-east-1エンドポイントに依存するサービスでした。主要なカテゴリ：

- **データベース & ストレージ**: DynamoDB（主原因）、RDS、Redshift、SQS（バックログ）。
- **コンピュート & オーケストレーション**: EC2（起動）、Lambda（呼び出し、ポーリング）、ECS、EKS、Glue。
- **ネットワーキング & ロードバランシング**: Network Load Balancer（ヘルスチェック）、API Gateway。
- **モニタリング & マネジメント**: CloudWatch、CloudTrail、EventBridge、IAM（更新）、AWS Config。
- **その他**: Amazon Connect、Athena、DynamoDB Global Tablesなどのグローバル機能。

全てのサービスが完全にダウンしたわけではなく、多くのサービスは部分的なエラーや遅延が見られましたが、相互接続された性質により、軽微な問題さえも伝播しました。

#### 影響範囲
この障害は、インターネットに依存するアプリケーションの約1/3を混乱させ、世界中で推定1億人以上のユーザーに影響を与えました。顕著な例：
- **ソーシャル & メディア**: Snapchat（ログイン障害）、Reddit（停止）、Twitch（配信問題）。
- **ゲーム**: Roblox（サーバークラッシュ）、Fortnite（マッチメイキング障害）。
- **金融 & 決済**: Venmo、Lloydsなどの銀行（取引遅延）、HMRC（英国税務サービス）。
- **小売 & Eコマース**: Amazon自社の小売サイトの一部；航空会社のチェックイン（例：Delta、Unitedの遅延）。
- **その他**: Alexaデバイス（音声障害）、Twilio（通信不具合）。

経済的損失は5億ドル以上と推定され、ユーザーの慌てた行動によりサイバーセキュリティスキャンが300%急増しました。これはインターネットの集中化を強調するものでした：us-east-1はAWSトラフィックの約30%を処理しており、マルチAZ設計にもかかわらず、単一障害点となっています。

#### 解決と教訓
AWSは、対象を絞った軽減策（DNS修正、EC2/NLBのサブシステムパッチ、段階的なスロットル緩和）を通じて問題を解決しました。インシデント後、彼らは以下を推奨しました：
- 失敗したリクエストの再試行。
- DNSキャッシュのフラッシュ。
- リソースの複数のAZ/リージョンへの分散（例：Auto Scaling Groupsを介して）。
- リトライに対する緩衝としてのサービスクォータとキャッシングの使用。

より広範な教訓としては、コントロールプレーンにおける冗長性の向上、より迅速なトリアージのためのAI駆動の異常検出、および多様化されたクラウド戦略の必要性が含まれます。AWSは顧客への完全な根本原因分析（RCA）を約束し、このような事象は稀ではあるものの、ハイパースケールにおけるスケーリングの課題を明らかにすると強調しました。

これは2021年以来、AWSのus-east-1で最も破壊的な障害でしたが、自動化ツールにより、過去の事例よりも復旧は迅速でした。

#### 参考文献
- [AWS Health Dashboard: Service Health - Oct 20, 2025](https://health.aws.amazon.com/health/status?eventID=arn:aws:health:us-east-1::event/MULTIPLE_SERVICES/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE/AWS_MULTIPLE_SERVICES_OPERATIONAL_ISSUE_BA540_514A652BE1A)
- [AWS Outage Analysis: October 20, 2025](https://www.thousandeyes.com/blog/aws-outage-analysis-october-20-2025)
- [Amazon's massive AWS outage points to a key weakness in the modern internet](https://finance.yahoo.com/news/amazons-massive-aws-outage-points-to-a-key-weakness-in-the-modern-internet-145418180.html)
- [What caused Amazon's AWS outage, and why did so many major apps go offline?](https://www.aljazeera.com/news/2025/10/21/what-caused-amazons-aws-outage-and-why-did-so-many-major-apps-go-offline)
- [AWS Outage on October 20: How a DNS Glitch in DynamoDB Disrupted the Internet](https://medium.com/@ansababy/aws-outage-on-october-20-how-a-dns-glitch-in-dynamodb-disrupted-the-internet-40e1f0440a12)
- [Update - AWS services operating normally](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)
- [AWS was down — live updates following massive outage](https://www.tomsguide.com/news/live/amazon-outage-october-2025)