---
audio: false
generated: true
lang: ja
layout: post
title: VSCodeでGradleのプロキシを設定する
translated: true
type: note
---

Gradle がプロキシ経由で依存関係をダウンロードできるようにするため、Visual Studio Code (VSCode) で Gradle のプロキシを設定するには、Gradle の設定でプロキシ設定を行う必要があります。Gradle はプロパティファイルを使用してこのような設定を管理し、VSCode は Gradle プロジェクトにおいて Gradle のビルドシステムに依存しています。設定方法は以下の通りです。

### VSCode で Gradle のプロキシを設定する手順

1. **Gradle プロパティファイルの場所を確認または作成する**
   - Gradle は `gradle.properties` というファイルを使用してグローバルな設定を保存します。
   - このファイルは通常、Gradle ユーザーホームディレクトリにあります：
     - Windows: `C:\Users\<ユーザー名>\.gradle\gradle.properties`
     - macOS/Linux: `~/.gradle/gradle.properties`
   - ファイルが存在しない場合は、上記の場所に作成してください。

2. **`gradle.properties` にプロキシ設定を追加する**
   - テキストエディタで `gradle.properties` ファイルを開きます。
   - 以下の行を追加し、プレースホルダー (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) を実際のプロキシの詳細に置き換えてください：
     ```
     systemProp.http.proxyHost=<proxyHost>
     systemProp.http.proxyPort=<proxyPort>
     systemProp.http.proxyUser=<username>
     systemProp.http.proxyPassword=<password>
     systemProp.https.proxyHost=<proxyHost>
     systemProp.https.proxyPort=<proxyPort>
     systemProp.https.proxyUser=<username>
     systemProp.https.proxyPassword=<password>
     ```
   - 実際の値を使用した例：
     ```
     systemProp.http.proxyHost=proxy.example.com
     systemProp.http.proxyPort=8080
     systemProp.http.proxyUser=myuser
     systemProp.http.proxyPassword=mypassword
     systemProp.https.proxyHost=proxy.example.com
     systemProp.https.proxyPort=8080
     systemProp.https.proxyUser=myuser
     systemProp.https.proxyPassword=mypassword
     ```
   - 認証（ユーザー名/パスワード）を必要としないプロキシの場合は、`proxyUser` と `proxyPassword` の行を省略できます。

3. **オプション: プロジェクトごとにプロキシを設定する**
   - プロキシ設定をグローバルではなく特定のプロジェクトにのみ適用したい場合は、プロジェクトのルートディレクトリ (例: `<project-root>/gradle.properties`) に `gradle.properties` ファイルを追加し、上記と同じ内容を記述できます。

4. **Gradle がプロキシを使用していることを確認する**
   - VSCode で Gradle プロジェクトを開きます。
   - VSCode のターミナルまたは Gradle 拡張機能を使用してビルドタスク (例: `gradle build`) を実行します。
   - Gradle は公式サイトからの依存関係のダウンロードなどで、指定されたプロキシを経由するようになります。

5. **VSCode 固有の注意点**
   - VSCode で **Java Extension Pack** と **Gradle for Java** 拡張機能がインストールされていることを確認してください。これらは Gradle プロジェクトのサポートを強化します。
   - それでも VSCode に問題がある場合は、使用している Java ランタイム (Gradle によって使用される) もプロキシを尊重するか確認してください。JVM のプロキシ引数を設定する必要があるかもしれません：
     - VSCode で `ファイル > 基本設定 > 設定` に移動します。
     - `java.gradle.build.jvmArguments` を検索します。
     - 以下のようなものを追加します：
       ```
       -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
       ```

6. **設定をテストする**
   - VSCode でプロジェクトをリロードします (例: 閉じて再度開く、または Gradle サイドバーの「Refresh」ボタンを使用する)。
   - Gradle タスク (例: `gradle build` または `gradle dependencies`) を実行し、プロキシ経由でファイルがダウンロードされることを確認します。

### トラブルシューティング
- **プロキシの詳細を確認する**: プロキシホスト、ポート、認証情報が正しいことを確認してください。
- **ファイアウォールまたはネットワーク**: それでも失敗する場合、プロキシまたはネットワークが特定の Gradle URL (例: `https://services.gradle.org`) をブロックしている可能性があります。`curl` などのコマンドでテストするか、ネットワーク管理者に相談してください。
- **詳細な出力**: VSCode のターミナルで `--debug` または `--info` を付けて Gradle を実行します (例: `gradle build --debug`)。ネットワークリクエストに関する詳細なログを確認できます。

この設定により、VSCode 内の Gradle がプロキシ経由で依存関係のダウンロードに成功するはずです。問題が発生した場合はお知らせください！