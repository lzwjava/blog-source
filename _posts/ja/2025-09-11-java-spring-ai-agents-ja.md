---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Java Spring モノレポ AI エージェントガイド
translated: true
type: note
---

素晴らしい質問です。以下は、Java/Spring モノレポ（マルチモジュール、Maven/Jetty/Liberty、JaCoCo など）向けにカスタマイズできる、実用的で効果的な AI エージェントです。具体的なトリガー、生成物、連携方法に焦点を当て、表は使用しません。

# コアエンジニアリングエージェント

**1) PR コードレビュアー (Spring 対応)**

*   **トリガー:** プルリクエスト作成時。
*   **動作内容:** 差分と変更された Spring Bean/設定を読み取り、DI の問題、スコープが誤った Bean、不足している `@Transactional`、JPA に伴う N+1 リスク、誤った `@Scheduled` の使用、非同期処理におけるスレッドリーク、リアクティブチェーン上のブロッキングコールを指摘。
*   **入力:** 差分 + `pom.xml` + `application*.yml` + `@Configuration` クラス。
*   **出力:** 行コメントによる提案、リスク概要、クイックフィックス用パッチ。

**2) 依存関係 & プラグインアップグレーダー**

*   **トリガー:** 日次/週次ジョブ。
*   **動作内容:** Spring Boot/Framework、Spring Data/Cloud、Jetty/Liberty、Maven プラグインの互換性のあるバージョンアップを提案し、CVE をチェックし、スモークビルドを実行。
*   **出力:** リスク（パッチ、マイナー、メジャー）でグループ化された PR、変更履歴とロールバック注意事項付き。

**3) API 契約ガーディアン**

*   **トリガー:** コントローラーまたは `openapi.yaml` を変更する PR 作成時。
*   **動作内容:** OpenAPI 仕様と Spring MVC アノテーションの同期を維持。破壊的変更（HTTP ステータスコード、フィールド名変更、nullable/必須属性）を検出。
*   **出力:** API サーフェスの差分を含むコメント。オプションで Pact スタイルの契約テストスタブ。

**4) テスト作成 & 不安定テストドクター**

*   **トリガー:** PR 作成時（テスト差分が少ない場合）および夜間。
*   **動作内容:** サービス/コントローラー/リポジトリ向けに JUnit 5 テストを生成/拡張。不安定なテストを安定化（時間、一時ディレクトリ、並行処理）、決定論的なパターンを提案、`Clock` を使用したクロックの分離。
*   **出力:** 新規テスト、パラメータ化、sleep を Awaitility で置き換えるヒント。

**5) カバレッジオーケストレーター (単体+結合テスト、マルチモジュール)**

*   **トリガー:** CI 上で結合テスト実行後。
*   **動作内容:** JaCoCo エージェントを Jetty/Liberty にアタッチ、`jacoco.exec`/`jacoco-it.exec` をマージ、モジュール間でクラスをマッピング、テストされていない重要パスを強調表示。
*   **出力:** マージされた HTML/XML レポート。モジュールごとにカバーされていないメソッドトップ10とテストスケルトンの提案をリストしたコメント。

**6) ログ & インシデントトリアージ**

*   **トリガー:** CI ジョブ失敗時、またはステージング/本番環境からのストリーミング時。
*   **動作内容:** スタックトレースをクラスタリング、最終デプロイと関連付け、疑わしいコミットへのリンクを提示。迅速な差分と切り替え用のフィーチャーフラグを提案。
*   **出力:** 根本原因の仮説、「次のステップ」チェックリスト、Grafana/ELK へのリンク。

**7) パフォーマンスプロファイラーコーチ**

*   **トリガー:** 負荷テスト実行時または低速エンドポイントアラート時。
*   **動作内容:** JFR/async-profiler の出力と Spring Actuator メトリクスを読み取り、低速な `@Transactional` 境界、N+1、重いマッパー、不適切なサイズのプールを発見。
*   **出力:** 焦点を絞ったパフォーマンス改善計画（JPA fetch graph のヒント、インデックス、プールサイズ、キャッシュ）。

**8) データベースマイグレーションアシスタント (Db2/MySQL/Postgres 対応)**

*   **トリガー:** Flyway/Liquibase 変更時または低速クエリレポート時。
*   **動作内容:** DDL をロックに関してレビュー、インデックスを追加、マイグレーション順序をシミュレート。ロールバックスクリプトを生成。非効率な JPQL/Criteria を SQL とヒント付きで書き換え。
*   **出力:** レビュー済みマイグレーション PR、実行計画ノート、安全なロールアウト手順。

**9) セキュリティ & シークレットセンチネル**

*   **トリガー:** 全ての PR および夜間スキャン時。
*   **動作内容:** Spring Security の誤設定、CSRF/ヘッダー、デシリアライゼーション、SpEL インジェクションに対する SAST。YAML、プロパティ、テストフィクスチャ内のシークレットをスキャン。
*   **出力:** PR インライン注釈、`SecurityFilterChain` の差分提案。

**10) 設定ドリフト & プロファイル監査官**

*   **トリガー:** `application*.yml` を変更する PR 作成時。
*   **動作内容:** プロファイルのオーバーレイ、環境変数バインディング、デフォルト値の欠落を検証。本番環境のみでの予期せぬ設定（例: 異なる `spring.jpa.open-in-view`）を検出。
*   **出力:** プロファイルと環境別の「実効設定」プレビュー。

**11) ビルド警官 (Maven マルチモジュール)**

*   **トリガー:** 全てのビルド時。
*   **動作内容:** プラグイン順序、再現可能なビルド、エンコーディング警告、テストの fork 設定、Surefire/Failsafe の引き継ぎ、モジュールグラフの退行を診断。
*   **出力:** 具体的な `pom.xml` パッチと高速ビルドレシピ。

**12) リリースノート & 変更履歴作成者**

*   **トリガー:** タグまたはリリースブランチマージ時。
*   **動作内容:** コミットを従来のスコープ/モジュールでグループ化。注目すべき API 変更とマイグレーションを抽出。アップグレード手順を含める。
*   **出力:** `CHANGELOG.md` セクション + GitHub リリース本文ドラフト。

# 横断的「グルー」パターン

**イベントソース:** GitHub PRs/Actions、Jenkins、Maven フェーズ、Gradle タスク（もしあれば）、ログパイプライン、JFR 出力、Actuator メトリクス、Pact/Postman 実行。
**コンテキストパック:** 差分 + 変更されたモジュール、`pom.xml` ツリー、OpenAPI、`application*.yml`、主要設定（`SecurityFilterChain`, `DataSource`, `JpaRepositories`）、テストレポート、JaCoCo XML、プロファイラ/フレームグラフ。
**レスポンスターゲット:** コードフェンス付きパッチを含む PR コメント、ステータスチェック、自動 PR、ビルド成果物として保存される markdown レポート。

# 最小限の連携 (コピー&ペースト可能)

**1) エージェント向けにリポジトリコンテキストを準備する GitHub Action ステップ**

```yaml
- name: Prepare Spring context bundle
  run: |
    mkdir -p .agent_ctx
    git diff -U0 origin/main... > .agent_ctx/diff.patch || true
    find . -name "pom.xml" -o -name "build.gradle*" > .agent_ctx/build_files.txt
    find . -name "application*.yml" -o -name "application*.properties" > .agent_ctx/configs.txt
    find . -name "openapi*.yaml" -o -name "openapi*.yml" > .agent_ctx/openapi.txt
```

**2) マルチモジュール向け JaCoCo マージ (単体 + 結合テスト)**

```bash
mvn -q -DskipITs=false -P it-tests verify
mvn -q org.jacoco:jacoco-maven-plugin:prepare-agent verify
mvn -q org.jacoco:jacoco-maven-plugin:report-aggregate
# 実行中の Jetty/Liberty で外部結合テストを収集する場合:
# java -javaagent:jacocoagent.jar=destfile=jacoco-it.exec,append=true ...
# その後マージ:
mvn -q org.jacoco:jacoco-maven-plugin:merge \
  -DdestFile=target/jacoco-merged.exec \
  -Dfile1=target/jacoco.exec -Dfile2=target/jacoco-it.exec
mvn -q org.jacoco:jacoco-maven-plugin:report \
  -DdataFile=target/jacoco-merged.exec
```

**3) PR コメントヘルパー (ChatOps スタイル)**

```yaml
- name: Post agent findings
  if: always()
  run: |
    echo "### API Contract Changes" > agent-comment.md
    echo "" >> agent-comment.md
    cat target/api-diff.md >> agent-comment.md || true
- uses: marocchino/sticky-pull-request-comment@v2
  with:
    path: agent-comment.md
```

# 最初に構築すべきもの (ROI が高い順)

1.  **PR コードレビュー + 設定監査官**: 一般的な Spring のミスの 70% を早期に捕捉。
2.  **カバレッジオーケストレーター**: 単体テストと外部結合テスト（あなたのケース）をマージし、モジュールごとのテスト TODO を出力。
3.  **API 契約ガーディアン**: クライアントを破壊する変更を防止。小さな労力で大きな痛みを回避。
4.  **依存関係アップグレーダー + セキュリティセンチネル**: ノイズを最小限に抑えた継続的な衛生管理。

# ガードレール & 品質

*   **決定性:** エージェントはルール ID と分析した正確なコード行へのリンクを含めるべき。
*   **変更予算:** 自動編集は小さなパッチに制限。大規模なリファクタリングはドラフト PR とする。
*   **プライバシー/アクセス:** 本番ログ/DB スナップショットを制限。モデル呼び出し前にシークレットを編集削除。
*   **メトリクス:** MTTR（失敗 → 修正）、不安定テスト率、テストカバレッジの差分、パフォーマンス SLI を追跡。週次エージェントスコアカードを使用。

# 必要であれば、以下をお手伝いできます:

*   あなたのモジュールと JaCoCo 設定を使用して、「PR コードレビュー + API 契約ガーディアン + カバレッジオーケストレーター」を実行する、**すぐに導入可能な GitHub Actions ワークフロー**の草案作成。
*   あなたのスタック (Jetty/Liberty, Db2, マルチモジュール Maven) に合わせて調整された **スタータールール** の生成。

あなたのリポジリ構造（モジュール名）と現在の結合テストの実行方法（Jetty vs Liberty）を教えてください。そうすれば、YAML と小さなヘルパースクリプトをお届けします。