---
audio: false
generated: true
lang: ja
layout: post
title: Windows上のWebSphere LibertyへのYourKitプロファイラ統合
translated: true
type: note
---

WindowsでYourKit Java ProfilerをWebSphere Liberty Serverと使用するには、YourKitエージェントをWebSphere Liberty JVMに統合し、プロファイリング用に設定する必要があります。以下は、利用可能な情報とYourKitとWebSphere Libertyの統合に関するベストプラクティスに基づいて、これを設定する手順です：

### 前提条件
- **YourKit Java Profiler**: Windowsマシンにインストール済み。[YourKit公式サイト](https://www.yourkit.com/)からダウンロードし、有効なライセンスまたはトライアルキーを用意してください。
- **WebSphere Liberty**: Windowsシステムにインストールされ、実行中。サーバー設定ファイルへの管理アクセス権があることを確認してください。
- **Java JDK**: WebSphere LibertyはJavaランタイム（IBM JDKまたはOpenJDK）を使用します。JDKバージョンがYourKitと互換性があることを確認してください（YourKitはJava 5以降をサポートしますが、特定のバージョンとの互換性を確認してください）。
- **管理者権限**: WebSphere Liberty設定ファイルを変更するために必要です。

### ステップバイステップガイド

1. **YourKit Java Profilerのインストール**
   - [YourKitのWebサイト](https://www.yourkit.com/download)からWindows用YourKit Java Profilerをダウンロードしてインストールします。
   - YourKitエージェントライブラリ（`yjpagent.dll`）へのパスが必要になるため、インストールディレクトリをメモしておきます。

2. **YourKitエージェントの場所を特定**
   - Windows用YourKitエージェントは通常、以下の場所にあります：
     ```
     C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll
     ```
     （32ビットJVMを実行している場合は、`win64`の代わりに`win32`を使用してください。）
   - エージェントがWebSphere Libertyで使用されているJVMアーキテクチャ（32ビットまたは64ビット）と一致することを確認してください。

3. **YourKitエージェントを使用するようにWebSphere Libertyを設定**
   - **`jvm.options`ファイルの場所を特定**:
     - WebSphere Libertyサーバーの設定ディレクトリに移動します。通常は：
       ```
       <LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\jvm.options
       ```
       `<LIBERTY_INSTALL_DIR>`をWebSphere Libertyのインストールパス（例：`C:\wlp`）に、`<server_name>`をサーバー名（例：`defaultServer`）に置き換えてください。
     - `jvm.options`ファイルが存在しない場合は、サーバーディレクトリに作成します。
   - **YourKitエージェントパスの追加**:
     - 管理者権限でテキストエディタを使用して`jvm.options`を開きます。
     - YourKitエージェントを含めるために以下の行を追加します：
       ```
       -agentpath:C:\Program Files\YourKit-Java-Profiler-<version>\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
       ```
       - `<version>`をYourKitのバージョン（例：`2023.9`）に置き換えてください。
       - オプション（`disablestacktelemetry`、`disableexceptiontelemetry`、`probe_disable=*`）は、不要なテレメトリを無効にしてオーバーヘッドを削減します。`delay=10000`はサーバー初期化後にエージェントが起動することを保証し、`sessionname=WebSphereLiberty`はプロファイリングセッションを識別します。
       - 例：
         ```
         -agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
         ```
   - **ファイルの保存**: `jvm.options`ファイルへの書き込み権限があることを確認してください。

4. **JVM互換性の確認**
   - WebSphere Libertyは多くの場合、IBM JDKまたはOpenJDKを使用します。YourKitは両方と互換性がありますが、問題が発生した場合（例：一部のIBM JDKケースで記録されている`NoSuchMethodError`）、IBM JDKとの競合を引き起こす可能性のあるプローブを無効にするために、エージェントパスに`probe_disable=*`を追加してください。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - Libertyで使用されているJavaバージョンを確認します：
     ```
     <LIBERTY_INSTALL_DIR>\java\bin\java -version
     ```
     YourKitでサポートされていること（古いバージョンではJava 5以降、最新バージョンではJava 8+）を確認してください。

5. **WebSphere Libertyの起動**
   - 通常通りWebSphere Libertyサーバーを起動します：
     ```
     <LIBERTY_INSTALL_DIR>\bin\server start <server_name>
     ```
     例：
     ```
     C:\wlp\bin\server start defaultServer
     ```
   - YourKitエージェントに関連するエラーがないかサーバーログ（`<LIBERTY_INSTALL_DIR>\usr\servers\<server_name>\logs\console.log`または`messages.log`）を確認してください。
   - YourKitエージェントログを以下で確認します：
     ```
     %USERPROFILE%\.yjp\log\<session_name>-<pid>.log
     ```
     例：
     ```
     C:\Users\<YourUsername>\.yjp\log\WebSphereLiberty-<pid>.log
     ```
     ログには、エージェントがロードされ、ポート（デフォルト：10001）でリッスンしていることが示されるはずです：
     ```
     Profiler agent is listening on port 10001
     ```

6. **YourKit Profiler UIの接続**
   - WindowsマシンでYourKit Java Profiler UIを起動します。
   - YourKit UIで、**Profile | Profile Local Java Server or Application**または**Profile | Profile Remote Java Server or Application**を選択します。
     - ローカルプロファイリングの場合（YourKitとLibertyが同じマシン上にあるため）、**Profile Local Java Server or Application**を選択します。
     - UIはWebSphere Libertyプロセス（`sessionname=WebSphereLiberty`で識別）を自動検出するはずです。
   - 自動検出されない場合は、**Profile Remote Java Server or Application**を使用し、**Direct Connect**を選択して以下を入力します：
     - **ホスト**: `localhost`
     - **ポート**: `10001`（またはエージェントログで指定されたポート）。
   - サーバーに接続します。UIにはCPU、メモリ、スレッドのテレメトリが表示されます。

7. **アプリケーションのプロファイリング**
   - YourKit UIを使用して以下を実行します：
     - **CPUプロファイリング**: パフォーマンスのボトルネックを特定するためにCPUサンプリングまたはトレースを有効にします。高負荷システムではオーバーヘッドを最小限に抑えるために「Profile J2EE」を有効にしないでください。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
     - **メモリプロファイリング**: ヒープ使用量を分析し、オブジェクトをWebアプリケーションごとにグループ化して（Libertyでホストされるアプリに有用）メモリリークを検出します。[](https://www.yourkit.com/docs/java-profiler/latest/help/webapps.jsp)
     - **スレッド分析**: スレッドタブでデッドロックまたはフリーズしたスレッドを確認します。[](https://www.yourkit.com/changes/)
   - 必要に応じてオフライン分析用にスナップショットを取得します（File | Save Snapshot）。
   - プロファイリングはメモリ消費を増加させる可能性があるため、メモリ使用量を監視します。監視なしでの長時間のプロファイリングセッションは避けてください。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

8. **トラブルシューティング**
   - **サーバーの起動失敗または到達不能**:
     - ログ（`console.log`、`messages.log`、YourKitエージェントログ）で`OutOfMemoryError`や`NoSuchMethodError`などのエラーを確認します。[](https://www.yourkit.com/forum/viewtopic.php?t=328)[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - `-agentpath`が正しい`jvm.options`ファイルに追加され、Libertyの起動に使用されるスクリプトと一致していることを確認します。[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
     - IBM JDKを使用している場合、競合を避けるためにエージェントパスに`probe_disable=*`を追加してみてください。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=8042)
   - **ClassNotFoundException**:
     - `java.lang.ClassNotFoundException`（例：`java.util.ServiceLoader`の場合）などのエラーが表示される場合、YourKitエージェントのバージョンがJDKと互換性があることを確認してください。古いIBM JDK（例：Java 5）の場合、YourKit 8.0またはそれ以前を使用してください。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)
   - **プロファイリングデータがない**:
     - YourKitエージェントとUIのバージョンが一致していることを確認してください。バージョンの不一致は接続問題を引き起こす可能性があります。[](https://www.yourkit.com/forum/viewtopic.php?t=328)
     - サーバーがブラウザでアクセス可能か（例：SSLを使用している場合は`https://localhost:9443`）確認してください。アクセスできない場合は、ファイアウォール設定またはSSL設定を確認してください。[](https://www.yourkit.com/forum/viewtopic.php?t=16205)
   - **ログファイルの問題**:
     - `~/.yjp/log/`にYourKitログが作成されない場合、プロセスがユーザーのホームディレクトリへの書き込み権限を持っていることを確認してください。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=3219)
   - **パフォーマンスへの影響**:
     - プロファイリングはパフォーマンスに影響を与える可能性があります。本番環境に近い環境では、最小限の設定（例：スタックテレメトリの無効化）を使用してください。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

9. **オプション：YourKit統合ウィザードの使用**
   - YourKitは設定を簡素化するためのJava Server Integration Wizardを提供します：
     - YourKit UIを起動し、**Profile | Profile Local Java Server or Application**を選択します。
     - サポートされているサーバーのリストから**WebSphere Liberty**を選択します（Libertyがリストにない場合は「Other Java application」）。
     - ウィザードに従って必要な`-agentpath`設定を生成し、`jvm.options`を更新します。設定ファイルへの書き込み権限があることを確認してください。[](https://www.yourkit.com/docs/java-profiler/latest/help/java-server-integration-wizard.jsp)
   - これは正しいパスと設定を保証するために特に有用です。

10. **プロファイリングの停止**
    - プロファイリングを無効にするには、`jvm.options`から`-agentpath`行を削除またはコメントアウトし、サーバーを再起動します。
    - または、サーバーを停止します：
      ```
      <LIBERTY_INSTALL_DIR>\bin\server stop <server_name>
      ```

### 追加の注意点
- **ライセンス**: サーバー上のYourKitエージェントにはライセンスキーは必要ありません。ライセンスはYourKit UIで適用されます。別のWindowsマシンからのリモートプロファイリングの場合、UIに有効なライセンスがあることを確認してください。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=11385)[](https://www.yourkit.com/forum/viewtopic.php?t=11385)
- **リモートプロファイリング**: 別のマシンからプロファイリングする場合、エージェントポート（デフォルト：10001）へのネットワーク接続性を確保し、サーバーのホスト名/IPを使用して**Profile Remote Java Server or Application**オプションを使用してください。
- **パフォーマンスに関する考慮事項**: プロファイリングはメモリとCPU使用量を増加させる可能性があります。本番システムでは、最小限のプロファイリングオプション（例：CPUサンプリング）から始め、サーバーの健全性を監視してください。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)
- **互換性**: IBM JDK 1.4.2または1.5を使用する古いWebSphere Libertyバージョンを使用している場合、古いYourKitバージョン（例：Java 5用に8.0）が必要になる場合があります。[](https://www.yourkit.com/forum/viewtopic.php?f=3&t=7149)[](https://stackoverflow.com/questions/61795/java-profiler-for-ibm-jvm-1-4-2-websphere-6-0-2)
- **ドキュメント**: 詳細なプロファイリングオプションについては、YourKitの公式ドキュメントを参照してください：[YourKit Java Profiler Help](https://www.yourkit.com/docs/java/help/)。[](https://www.jahia.com/blog/analyzing-system-performance-with-yourkit-java-profiler)

### 設定例
以下はサンプルの`jvm.options`ファイルです：
```
-Xmx4G
-Xms4G
-agentpath:C:\Program Files\YourKit-Java-Profiler-2023.9\bin\win64\yjpagent.dll=disablestacktelemetry,disableexceptiontelemetry,delay=10000,probe_disable=*,sessionname=WebSphereLiberty
```

### 設定のテスト
- サーバー起動後、アプリケーション（例：`https://localhost:9443`）にアクセスして実行されていることを確認します。
- YourKit UIで、テレメトリデータ（CPU、メモリ、スレッド）が表示されていることを確認します。
- 問題が発生した場合は、YourKitエージェントログとLibertyログでエラーを確認してください。

特定のエラーが発生した場合や特定の手順でヘルプが必要な場合は、お知らせください。さらに支援を提供します！