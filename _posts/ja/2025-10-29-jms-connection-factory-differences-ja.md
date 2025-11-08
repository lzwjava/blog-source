---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: JMS接続ファクトリの相違点
translated: true
type: note
---

IBM WebSphere Application Server (WAS) では、コネクションファクトリとキューコネクションファクトリはどちらも、メッセージングのために JMS プロバイダーへの接続を確立するために使用される JMS リソースです。しかし、これらはスコープ、API 互換性、および JMS ドメインモデル (ポイントツーポイント vs パブリッシュ/サブスクライブ) に基づく使用方法が異なります。以下に詳細を示します：

### 主な相違点

| 観点                      | コネクションファクトリ                                                                     | キューコネクションファクトリ                                                                 |
|---------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **主な目的**              | ポイントツーポイント (キュー) とパブリッシュ/サブスクライブ (トピック) の**両方**のメッセージングに対して、JMS 接続を宛先に作成します。JMS 1.1 で導入された統一された「クラシック」API をサポートします。 | キューを使用したポイントツーポイントメッセージング**専用**の JMS 接続を作成します。JMS 1.0 のレガシーなドメイン固有 API に基づいています。 |
| **API 階層**              | 基底インターフェース (`javax.jms.ConnectionFactory`)。同じ接続/セッション内で `Queue` または `Topic` の宛先とセッションを動的に作成できます。 | `ConnectionFactory` のサブクラス (`javax.jms.QueueConnectionFactory`)。`QueueConnection` および `QueueSession` オブジェクトのみを作成します。トピックを扱うことはできません。 |
| **柔軟性**                | モダンなアプリケーションに対してより柔軟です。キューとトピックの操作を同じトランザクション/作業単位内で混在させることを可能にします (JMS 1.1+)。メッセージングスタイルを再設定なしで切り替える必要があるコードに理想的です。 | 柔軟性が低く、キューに限定されます。レガシーな JMS 1.0 コード、またはポイントツーポイントのみが必要な厳密な関心の分離に有用です。 |
| **WAS での設定**          | 管理コンソールの **リソース > JMS > コネクションファクトリ** で設定されます。(例： デフォルトメッセージング、WebSphere MQ) などの JMS プロバイダーに関連付けられます。 | **リソース > JMS > キューコネクションファクトリ** で設定されます。ポイントツーポイント専用の IBM MQ やデフォルトメッセージングなどのキュー固有プロバイダーに関連付けられます。 |
| **使用すべき状況**        | 新規開発または JMS 1.1+ を使用するアプリケーションで推奨されます。アプリがキューとトピックの両方と対話する可能性がある場合に使用します。 | JMS 1.0 のドメイン固有コードとの後方互換性のため、または明示的にキューに制限する場合 (例： パフォーマンス/セキュリティ分離のための WebSphere MQ 設定) に使用します。 |
| **パフォーマンス/セキュリティ** | 一般的には同等ですが、クロスドメイン使用には追加の設定が必要な場合があります。 | キュー専用に最適化できる (例： MQ でのバインディングストランスポートによるスループット向上、約30%の改善)。 |

### コードでの使用例
- **コネクションファクトリを使用** (統合、柔軟):
  ```java
  ConnectionFactory factory = (ConnectionFactory) context.lookup("jms/ConnectionFactory");
  Connection conn = factory.createConnection();
  Session session = conn.createSession(false, Session.AUTO_ACKNOWLEDGE);
  // どちらも作成可能:
  Queue queue = session.createQueue("myQueue");
  Topic topic = session.createTopic("myTopic");
  ```

- **キューコネクションファクトリを使用** (キュー専用):
  ```java
  QueueConnectionFactory qFactory = (QueueConnectionFactory) context.lookup("jms/QueueConnectionFactory");
  QueueConnection qConn = qFactory.createQueueConnection();
  QueueSession qSession = qConn.createQueueSession(false, Session.AUTO_ACKNOWLEDGE);
  Queue queue = qSession.createQueue("myQueue");
  // ここではトピックを作成できません。
  ```

要約すると、WAS 上の現代的な JMS アプリケーションでは汎用性のために一般的なコネクションファクトリを選択し、キューコネクションファクトリはキュー中心またはレガシーなシナリオのための特化した名残です。

[コネクションファクトリコレクション - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-connection-factory-collection)  
[キューコネクションファクトリコレクション - IBM](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=settings-queue-connection-factory-collection)  
[JMS QueueConnectionFactory vs ConnectionFactory - Stack Overflow](https://stackoverflow.com/questions/30121654/jms-queueconnectionfactory-vs-connectionfactory)  
[Queue Connection Factory VS Connection Factory - MQSeries.net](https://mqseries.net/phpBB/viewtopic.php?p=102901)