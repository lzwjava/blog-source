---
audio: false
generated: true
image: false
lang: ja
layout: post
title: WAS Spring JDBCタイムアウトトリアージガイド
translated: true
type: note
---

以下はメンタルモデルとクイックトリアージプレイブックです。

# 動作の仕組み (WAS + Spring + JDBC)

1. **DataSource は WAS 内に存在**

   * WAS 管理コンソールで JDBC プロバイダーと **DataSource** (通常、グローバルトランザクションの場合は `XA`、非 XA) を定義します。
   * WAS が **JCA コネクションプール** を管理し、JDBC コネクションを提供します。

2. **Spring は JNDI 経由で DataSource を取得**

   * Spring アプリケーションはサーバーの DataSource (例: `java:comp/env/jdbc/MyDS`) をルックアップし、それをラップします:

     * プレーン JDBC: `JdbcTemplate` がその DataSource を使用します。
     * JPA/Hibernate: `EntityManagerFactory` がそれを使用します。
   * トランザクションは通常、**コンテナ JTA** (`WebSphereUowTransactionManager` または標準 JTA) です。Spring の `@Transactional` はコンテナトランザクションに参加します。

3. **呼び出しパス**

   * Web リクエスト → WebContainer スレッド → Spring サービス → トランザクション開始 (JTA) → **WAS プール** からの `DataSource.getConnection()` → ドライバ経由で SQL → DB。
   * タイムアウトは複数のレイヤー (Spring, JPA, WAS プール, JTA トランザクション, JDBC ドライバ/DB, ネットワーク) で発生する可能性があります。

# タイムアウトが発生した場合 — 種類の特定

4つのバケットで考えてください。メッセージ/スタックトレースが通常、どれかを示しています。

1. **コネクション取得タイムアウト**
   症状: プールされたコネクションを待機中。
   プール枯渇や `J2CA0086W / J2CA0030E` に関するメッセージを探してください。
   典型的な設定項目: *最大コネクション数*, *コネクションタイムアウト*, *経過タイムアウト*, *削除ポリシー*。

2. **トランザクションタイムアウト (JTA)**
   症状: `WTRN`/`Transaction` メッセージ; *"Transaction timed out after xxx seconds"* のような例外。
   典型的な設定項目: **合計トランザクション存続時間タイムアウト**。DB がまだ動作していても、長時間実行される DB 操作を強制終了できます。

3. **クエリ/ステートメントタイムアウト**
   症状: `java.sql.SQLTimeoutException`, Hibernate/JPA の "query timeout", または Spring の `QueryTimeoutException`。
   設定項目:

   * Spring: `JdbcTemplate.setQueryTimeout(...)`, Hibernate `javax.persistence.query.timeout` / `hibernate.jdbc.timeout`。
   * WAS DataSource カスタムプロパティ (DB2 例): `queryTimeout`, `queryTimeoutInterruptProcessingMode`。
   * ドライバ/DB 側のステートメントタイムアウト。

4. **ソケット/読み取りタイムアウト / ネットワーク**
   症状: 長時間のフェッチ中に何らかのアイドル時間が経過した後; 低レベルの `SocketTimeoutException` またはベンダー固有のコード。
   設定項目: ドライバの `loginTimeout`/`socketTimeout`, ファイアウォール/NAT のアイドルタイムアウト, DB キープアライブ。

# 確認箇所 (レイヤー別)

**WAS 管理コンソールのパス (従来型 WAS)**

* JDBC プロバイダー / DataSource:
  リソース → JDBC → データソース → *YourDS* →

  * *コネクションプールプロパティ*: **コネクションタイムアウト**, **最大コネクション数**, **回収時間**, **未使用タイムアウト**, **経過タイムアウト**, **削除ポリシー**。
  * *カスタムプロパティ*: ベンダー固有 (例: DB2 `queryTimeout`, `currentSQLID`, `blockingReadConnectionTimeout`, `queryTimeoutInterruptProcessingMode`)。
  * *JAAS – J2C* (認証エイリアスが関係する場合)。
* トランザクション:
  アプリケーションサーバー → *server1* → コンテナー設定 → **コンテナーサービス → トランザクションサービス** → **合計トランザクション存続時間タイムアウト**, **最大トランザクションタイムアウト**。
* WebContainer:
  スレッドプールサイズ (リクエストが積み上がる場合)。

**ログ & トレース**

* 従来型 WAS: `<profile_root>/logs/<server>/SystemOut.log` および `SystemErr.log`。
  キーコンポーネント: `RRA` (リソースアダプター), `JDBC`, `ConnectionPool`, `WTRN` (トランザクション)。
  トレースを有効化 (簡潔な開始例):

  ```
  RRA=all:WTRN=all:Transaction=all:JDBC=all:ConnectionPool=all
  ```

  以下を探してください:

  * `J2CA0086W`, `J2CA0114W` (プール/コネクション問題)
  * `WTRN0037W`, `WTRN0124I` (トランザクションタイムアウト/ロールバック)
  * ベンダー SQL コード付きの `DSRA`/`SQL` 例外。
* Liberty: `wlp/usr/servers/<server>/logs/` 下の `messages.log`。

**PMI / モニタリング**

* JDBC コネクションプールとトランザクションメトリクスの **PMI** を有効化。以下を監視:

  * プールサイズ、使用中カウント、待機数、待機時間、タイムアウト数。
  * トランザクションのタイムアウト/ロールバックカウント。

**Spring/JPA アプリケーションログ**

* アプリ内で SQL + 実行時間を有効化 (`org.hibernate.SQL`, `org.hibernate.type`, Spring JDBC デバッグ) して、持続時間とタイムアウトを関連付けます。

**データベース & ドライバ**

* DB2: `db2diag.log`, `MON_GET_PKG_CACHE_STMT`, アクティビティイベントモニター, ステートメントレベルのタイムアウト。
* WAS DataSource または `DriverManager` 内のドライバープロパティ (WAS 上では非典型的)。

**ネットワーク**

* アイドルタイムアウトを持つミドルボックス。OS キープアライブ / ドライバーキープアライブ設定。

# クイックトリアージフロー

1. **タイムアウトを分類**

   * *コネクション待機?* `J2CA` プール警告を探してください。該当する場合、**最大コネクション数** を増やす、リークを修正する、プールを調整する、有害イベントに対して **削除ポリシー = EntirePool** を設定する。
   * *トランザクションタイムアウト?* `WTRN` メッセージ。**合計トランザクション存続時間タイムアウト** を増やす、またはトランザクションあたりの作業量を減らす; 大規模なバッチジョブを単一トランザクションでラップするのは避ける。
   * *クエリタイムアウト?* `SQLTimeoutException` または Spring/Hibernate `QueryTimeout`。**Spring/Hibernate** タイムアウトを **WAS DS** および **DB** タイムアウトと一致させる; 競合する設定を避ける。
   * *ソケット/読み取りタイムアウト?* ネットワーク/ドライバーメッセージ。ドライバの `socketTimeout`/`loginTimeout`, DB キープアライブ, ファイアウォールを確認。

2. **タイミングを関連付ける**

   * 失敗する持続時間と設定されたしきい値を比較 (例: "約30秒で失敗" → 30秒の設定を探す: Spring クエリタイムアウト 30秒? トランザクション存続時間 30秒? プール待機 30秒?)。

3. **プールの健全性を確認**

   * PMI: **待機数** > 0? **使用中** が **最大** に近い? 長時間実行されているホルダー? **コネクションリーク検出** を有効化することを検討 (RRA トレースは誰がコネクションを取得したかを示します)。

4. **DB の可視性**

   * DB 側で確認: ステートメントはまだ実行中だったか? キャンセルされたか? ロック待機はあるか? ロックがある場合 → ロックタイムアウトとステートメントタイムアウトを考慮。

# 有用な設定項目 & 注意点 (WAS + DB2 の例)

* **合計トランザクション存続時間タイムアウト** (サーバーレベル) は、Spring/Hibernate タイムアウトをより高く設定していても、長時間実行されるクエリを強制終了します。これらを一致させてください。
* **queryTimeoutInterruptProcessingMode** (DB2 用 DataSource カスタムプロパティ): タイムアウトしたクエリを DB2 がどのように中断するかを制御 (協調的/強制的)。タイムアウト後もスレッドが固着するのを回避するのに役立ちます。
* **削除ポリシー**: `EntirePool` は (DB 再起動などの) 致命的な SQL 状態からの回復を速めますが、一時的な影響があります。
* **経過/未使用タイムアウト**: 古いコネクションを廃止して、ファイアウォール/NAT のアイドルタイムアウトを回避。
* **検証**: **SQL による検証** または **検証タイムアウト** を有効化して、使用前に切断されたコネクションが検出されるようにします。
* **スレッドプール**: WebContainer スレッドが飽和している場合、*症状はタイムアウトのように見えます*。WebContainer と Default スレッドプールのサイズが適切に設定されていることを確認してください。

# 最小限の Spring 設定例

**JNDI DataSource (XML)**

```xml
<jee:jndi-lookup id="dataSource" jndi-name="java:comp/env/jdbc/MyDS" expected-type="javax.sql.DataSource"/>
<bean id="txManager" class="org.springframework.transaction.jta.JtaTransactionManager"/>
<tx:annotation-driven transaction-manager="txManager"/>
```

**JdbcTemplate クエリタイムアウト (Java)**

```java
@Bean JdbcTemplate jdbcTemplate(DataSource ds) {
  JdbcTemplate jt = new JdbcTemplate(ds);
  jt.setQueryTimeout(60); // 秒
  return jt;
}
```

**Hibernate/JPA タイムアウト**

```properties
javax.persistence.query.timeout=60000  # ミリ秒
hibernate.jdbc.timeout=60              # 秒
```

# エスカレーション時に収集すべき情報

* 正確な例外テキスト + スタックトレース。
* タイムスタンプ: リクエスト開始、トランザクション開始、クエリ開始、エラー発生時刻。
* WAS DS プール設定 (スクリーンショットまたは値)、トランザクションサービスタイムアウト。
* PMI スナップショット (プール待機数、使用中数、タイムアウト数)。
* 障害発生時のセッション/ステートメントの DB ビュー。
* ネットワークトポロジに関するメモ (ファイアウォール、プロキシ、アイドルタイマー)。

特定の例外スニペット (J2CA/WTRN/SQL 状態) を貼り付けて頂ければ、正確なレイヤーと調整すべき対応する設定を特定できます。