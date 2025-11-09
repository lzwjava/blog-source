---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: AWSの主要な障害の歴史
translated: true
type: note
---

### AWSの主要な障害の歴史

Amazon Web Services（AWS）は2006年以来、インターネットの大部分を支えてきましたが、大規模なインフラと同様に、時折障害に直面しています。その広範な運用に比べれば障害は稀ですが、大規模な障害はソーシャルメディアから金融プラットフォームまで、依存するサービスに連鎖的に影響を及ぼす可能性があります。以下は、複数のサービスや著名な顧客に影響を与えた記録された事例から、広範囲または影響の大きい事象に焦点を当てた、主要な過去の障害をまとめた表です。

| 日付              | 影響を受けたサービス/リージョン | 原因                          | 影響 |
|-------------------|---------------------------|--------------------------------|--------|
| 2008年2月15日 | S3, EC2 (グローバル)         | 特定されていない技術的障害 | 様々なウェブサイトの画像ストレージとホスティングに混乱を引き起こし、AWSの初期の主要な問題の一つとして記録されました。 |
| 2011年4月21日    | 複数サービス (US-East-1) | 長時間にわたるデータセンター障害 | RedditやQuoraなどの著名なサイトを数時間にわたりダウンさせ、初期の信頼性に関する懸念を浮き彫りにしました。 |
| 2017年2月28日 | EC2, S3, RDS, その他 (US-East-1) | 人的ミス: デバッグ中のコマンド入力ミス | 数時間に及ぶ障害がSlack、Docker、Exoraなどに影響。推定損失は数億ドル規模。AWSのクラウドダッシュボードもダウンしました。 |
| 2021年12月7日  | EC2, RDS, Lambdaなどのコントロールプレーンサービス (US-East-1) | フェイルオーバー中のコントロールプレーンのソフトウェアバグによる連鎖的障害 | 近年で最長の障害（8時間以上）。Netflix、Disney+、Capital One、政府サイトなどに混乱を引き起こしました。12月15日には同様のサービスに影響する小規模な障害も発生。 |
| 2023年6月13日     | EC2および関連サービス (複数リージョン) | 特定されていないリージョン別の問題 | ニュースメディア（Associated Press、Boston Globeなど）や交通機関（NY MTAなど）に広範囲なダウンタイムをもたらし、数時間続きました。 |
| 2025年10月20日  | DynamoDBエンドポイント、EC2起動、複数サービス (US-East-1、グローバルに波及) | DynamoDBサービスエンドポイントのDNS解決障害 | 長時間の障害（10月19日PDT遅くに開始、10月20日午後までに解決）。Snapchat、Reddit、Roblox、Fortnite、銀行（Lloydsなど）、HMRCに影響。DynamoDBへの依存により、インターネット依存アプリの約1/3へのアクセスをブロックし、数百万人のユーザーに影響。AWSは復旧のため一部操作を制限しました。 |

これらのインシデントは、人的ミス、ネットワーク問題、または環境要因に起因することが多く、AWSはマルチリージョン設定などの冗長性を通じて回復力を向上させてきました。2025年の障害は、AWSで最も利用されているリージョンであるUS-East-1への過度な依存に伴う継続的なリスクを強調しています。

詳細はこちら：
- [A History of AWS Cloud and Data Center Outages](https://www.datacenterknowledge.com/outages/a-history-of-aws-cloud-and-data-center-outages)
- [The Biggest AWS Outage in History: December 7, 2021](https://aws.plainenglish.io/the-biggest-aws-outage-in-history-the-december-7-2021-us-east-1-meltdown-and-lessons-learned-2efab5a02de5)
- [What caused the AWS outage](https://www.bbc.com/news/articles/cev1en9077ro)
- [AWS Update on October 2025 Outage](https://www.aboutamazon.com/news/aws/aws-service-disruptions-outage-update)