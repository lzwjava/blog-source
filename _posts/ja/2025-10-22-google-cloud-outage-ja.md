---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Google Cloud Platformの大規模障害
translated: true
type: note
---

### 概要
2025年6月12日、Google Cloud Platform (GCP) は約7.5時間（PDT 10:51からPDT 18:18まで）にわたる大規模なグローバル障害を経験しました。このインシデントは、GoogleのService Controlシステム内で新しく導入された機能のバグ、特にクォータポリシーチェックに関連するものに起因しています。これにより、無効な自動化されたクォータ更新がグローバルに伝播し、広範囲でのAPI拒否やタスク過負荷を引き起こしました。特にus-central1（アイオワ）のような高トラフィック地域で顕著でした。この障害により、多数のGCPサービス、Google Workspace製品、およびGCPインフラに依存するサードパーティアプリケーションへのアクセスが妨げられ、Downdetectorには140万件を超えるユーザーレポートが寄せられました。

### タイムライン
(すべての時刻は US/Pacific, PDT)

- **10:51 AM**: 障害開始。複数のGCPおよびGoogle Workspace製品で外部APIリクエストにおける503エラーが増加し、断続的なアクセス問題が発生。
- **11:46 AM**: エンジニアリングチームが広範なサービス影響を確認。調査を開始。
- **12:09 PM**: 緩和策を開始。us-central1を除くほとんどの地域で回復。
- **12:41 PM**: 根本原因が無効なクォータポリシーデータであると特定。クォータチェックのバイパスを実装。
- **1:16 PM**: us-central1およびUSマルチリージョンを除くすべての地域でインフラ完全回復。
- **2:00 PM**: us-central1で回復の兆候。1時間以内の完全な緩和を予測。
- **3:16 PM**: ほとんどのGCP製品は回復したが、Dataflow、Vertex AI、Personalized Service Healthでは残存する問題が継続。
- **5:06 PM**: DataflowおよびPersonalized Service Healthは解決。Vertex AIの問題は継続中。解決予定時刻(ETA)は午後10:00。
- **6:27 PM**: すべてのリージョンでVertex AIが完全回復。
- **6:18 PM**: サービスが完全に復旧し、インシデントが正式に終了。

主要な緩和策には約3時間を要しましたが、残存するバックログとエラーのため、総合的な影響時間は7.5時間に及びました。

### 根本原因
この障害は、APIクォータとポリシーを管理するService Control機能の欠陥によって引き起こされました。自動化されたシステムが、空白またはnullフィールドを含む無効なクォータポリシーをデータベースに挿入しました。グローバルなレプリケーション（ニアインスタントの一貫性を目的として設計）により、この破損したデータは数秒で世界中に広がりました。APIリクエストがクォータチェックに到達すると、nullポインタ例外とリクエスト拒否（503および5xxエラーの増加）が発生しました。us-central1のような大規模リージョンでは、失敗したリクエストの流入により、深刻なタスク過負荷と依存サービスの連鎖的障害が発生しました。この新機能には、空白フィールドのようなエッジケースに対する十分な検証が欠けており、システムは「フェイルオープン」（チェック中にリクエストを継続して許可する）しませんでした。

### 影響を受けたサービス
この障害は、GCPに依存するGoogle製品および外部サービスの広範な範囲に影響を与えました。主要なGCPおよびGoogle Workspaceサービスは、API障害やUIアクセス問題など、様々な程度で中断が見られました（ストリーミングおよびIaaSリソースは影響を受けませんでした）。

#### 影響を受けた主要なGoogle Cloud プロダクト
- **コンピュート & ストレージ**: Google Compute Engine, Cloud Storage, Persistent Disk.
- **データベース**: Cloud SQL, Cloud Spanner, Cloud Bigtable, Firestore.
- **データ & アナリティクス**: BigQuery, Dataflow, Dataproc, Vertex AI (Online PredictionおよびFeature Storeを含む).
- **ネットワーキング & セキュリティ**: Cloud Load Balancing, Cloud NAT, Identity and Access Management (IAM), Cloud Security Command Center.
- **デベロッパーツール**: Cloud Build, Cloud Functions, Cloud Run, Artifact Registry.
- **AI/ML**: Vertex AI Search, Speech-to-Text, Document AI, Dialogflow.
- **その他**: Apigee, Cloud Monitoring, Cloud Logging, Resource Manager API.

#### 影響を受けた主要な Google Workspace プロダクト
- Gmail, Google Drive, Google Docs, Google Meet, Google Calendar, Google Chat.

#### 影響を受けたサードパーティサービス
GCPでホストされている、または部分的にGCPに依存する多くのコンシューマーおよびエンタープライズアプリがダウンタイムを経験しました：
- **Spotify**: ストリーミングおよびアプリアクセスが約46,000人のユーザーで中断。
- **Discord**: ボイスチャットおよびサーバー接続性问题。
- **Fitbit**: 同期およびアプリ機能が停止。
- **その他**: OpenAI (ChatGPT), Shopify, Snapchat, Twitch, Cloudflare (連鎖的DNS問題), Anthropic, Replit, Microsoft 365 (部分的), Etsy, Nest.

GCPはインターネットのバックエンドインフラの大部分を支えているため、グローバルな規模が影響を増幅させました。

### 解決策
Googleのエンジニアリングチームは迅速に無効なポリシーを特定し、クォータチェックのバイパスを実装しました。これにより、危機的状況中は検証なしでAPIリクエストが処理されるようになり、PDT午後12:48までにほとんどのリージョンが復旧しました。us-central1については、対象を絞った過負荷緩和策が適用され、その後、DataflowやVertex AIなどの影響を受けたサービスで手動によるバックログ解消が行われました。監視により、PDT午後6:18までに完全な回復が確認されました。データ損失は発生しませんでしたが、一部のサービスでは一時的な遅延が発生しました。

### 影響
- **規模**: Downdetectorへの報告が140万件を超え、リアルタイムのグローバルな混乱を浮き彫りに。
- **経済的**: 企業にとって数十億円規模の生産性損失の可能性。Spotifyはピーク時間帯のユーザー不満を報告。
- **評判**: クラウド集中のリスクを強調し、より優れたマルチクラウド戦略の必要性が叫ばれる。

### 教訓と予防措置
Googleは回復力に重点を置いた詳細なポストモーテムを発表しました：
- **アーキテクチャの変更**: Service Controlをモジュール化して障害を分離し、「フェイルオープン」モードを可能に。
- **データ検証**: グローバル変更の段階的伝播と事前検証の実施。無効な入力に対するテストの強化。
- **デプロイメントの安全対策**: 重要な更新に対する必須の機能フラグ。静的解析とエラー処理の改善。
- **監視 & コミュニケーション**: 障害検出ツールが独立して動作することを確保。より迅速な自動化された顧客アラート。
- **その他**: 過負荷の連鎖を防ぐためのリトライロジックにおけるランダム化バックオフ。

これらのステップは、同様のインシデントを防ぐことを目的としており、クォータシステムの監査が継続的に行われています。

[Google Cloud インシデントレポート](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)  
[ThousandEyes 障害分析](https://www.thousandeyes.com/blog/google-cloud-outage-analysis-june-12-2025)  
[Ookla Downdetector レポート](https://www.ookla.com/articles/google-cloud-outage-june-2025)  
[ByteByteGo 解説](https://blog.bytebytego.com/p/how-the-google-cloud-outage-crashed)  
[Medium 根本原因の説明](https://medium.com/@tahirbalarabe2/%EF%B8%8Fhow-a-single-google-cloud-bug-caused-global-internet-outage-on-june-12-2025-652a83ad9e68)