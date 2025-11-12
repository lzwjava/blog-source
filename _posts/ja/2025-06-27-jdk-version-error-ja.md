---
audio: false
generated: true
lang: ja
layout: post
title: VisualVMにおける「Unsupported OpenJDK」エラーの修正
translated: true
type: note
---

VisualVMの実行時に表示されるエラー「Version of OpenJDK is not supported. Please use the default-jdk」は、使用されているJava Development Kit（JDK）のバージョンがVisualVMと互換性がないことを示しています。この問題は、VisualVMがサポート対象のJDKを見つけられない場合や、インストールされているJDKが適切に設定されていない場合に頻繁に発生します。以下に、あなたの環境（YourKit Java Profiler 2025.3とLinuxシステム上でのVisualVM）に基づいた解決手順を説明します。

### 問題解決の手順

1. **現在のJavaバージョンを確認**
   インストールされているJavaのバージョンを確認するために、次のコマンドを実行します：
   ```bash
   java -version
   ```
   これにより、以下のようなOpenJDKのバージョンが表示されます：
   ```
   openjdk version "17.0.9" 2023-10-17
   OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)
   OpenJDK 64-Bit Server VM (build 17.0.9+9-Ubuntu-122.04, mixed mode, sharing)
   ```
   VisualVMは通常、JREだけでなくJDKを必要とし、Oracle JDK 8以降または互換性のあるOpenJDKバージョンをサポートします。サポート対象のJDKがインストールされていることを確認してください。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://visualvm.github.io/troubleshooting.html)

2. **デフォルトJDKをインストール**
   エラーメッセージは`default-jdk`の使用を推奨しています。Ubuntu/Debianでは、以下のコマンドでインストールできます：
   ```bash
   sudo apt update
   sudo apt install default-jdk
   ```
   これにより、通常は安定したサポート対象のOpenJDKバージョン（例：OpenJDK 11または17）がインストールされます。インストール後、`java -version`で再度バージョンを確認してください。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

3. **JAVA_HOME環境変数を設定**
   VisualVMはJDKの場所を特定するために`JAVA_HOME`環境変数に依存しています。設定されているか確認します：
   ```bash
   echo $JAVA_HOME
   ```
   設定されていない場合や、サポート対象外のJDKを指している場合は、正しいJDKのパスに設定します。例えば、`default-jdk`でOpenJDK 17がインストールされた場合、パスは`/usr/lib/jvm/java-17-openjdk-amd64`のようになります。以下のコマンドで設定します：
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   ```
   これを恒久的にするには、`~/.bashrc`または`~/.zshrc`に次の行を追加します：
   ```bash
   echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
   source ~/.bashrc
   ```
   パスはシステム上の実際のJDKパスに置き換えてください（`update-alternatives --list java`で確認できます）。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://github.com/oracle/visualvm/issues/558)

4. **VisualVMにJDKパスを指定**
   `JAVA_HOME`の設定で問題が解決しない場合、VisualVM起動時に明示的にJDKパスを指定できます：
   ```bash
   ~/bin/YourKit-JavaProfiler-2025.3/bin/visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
   ```
   `/usr/lib/jvm/java-17-openjdk-amd64`をあなたのJDKのパスに置き換えてください。これにより、VisualVMは指定されたJDKを使用します。[](https://visualvm.github.io/download.html)[](https://notepad.onghu.com/2021/solve-visualvm-does-not-start-on-windows-openjdk/)

5. **互換性のあるJDKをインストール**
   `default-jdk`がまだ互換性がない場合、VisualVMで動作することが知られている特定のJDKバージョン（例：OpenJDK 11またはOracle JDK 8以降）をインストールします：
   ```bash
   sudo apt install openjdk-11-jdk
   ```
   その後、上記で説明したように`JAVA_HOME`を更新するか、`--jdkhome`オプションを使用してください。[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)

6. **VisualVMのインストールを確認**
   VisualVMが正しくインストールされていることを確認してください。エラーは、YourKit Java Profilerディレクトリ（`~/bin/YourKit-JavaProfiler-2025.3/bin`）からVisualVMを実行していることを示唆しています。これは一般的ではなく、VisualVMは通常スタンドアロンツールまたはJDKにバンドルされています。VisualVMが破損していないか確認します：
   - `visualvm.github.io/download.html`から最新のVisualVMリリースをダウンロードします（例：VisualVM 2.2、2025年4月22日リリース、JDK 24をサポート）。[](https://visualvm.github.io/relnotes.html)[](https://visualvm.github.io/)
   - 新しいディレクトリに解凍して実行します：
     ```bash
     unzip visualvm_22.zip
     cd visualvm_22/bin
     ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
     ```
   既存のVisualVMインストールの上書き解凍は問題を引き起こす可能性があるため避けてください。[](https://visualvm.github.io/troubleshooting.html)

7. **複数のJavaインストールを確認**
   複数のJavaバージョンが競合を引き起こす可能性があります。インストールされているすべてのJavaバージョンをリスト表示します：
   ```bash
   update-alternatives --list java
   ```
   複数のバージョンがリストされている場合、互換性のあるものをデフォルトとして設定します：
   ```bash
   sudo update-alternatives --config java
   ```
   互換性のあるJDK（例：OpenJDK 11または17）に対応する番号を選択します。[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

8. **VisualVMの依存関係を確認**
   VisualVMは`libnb-platform18-java`と`libvisualvm-jni`を必要とします。これらがインストールされていることを確認します：
   ```bash
   sudo apt install libnb-platform18-java libvisualvm-jni
   ```
   これは特に、`apt`経由でVisualVMをインストールした場合に関連します。[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

9. **OpenJDKの制限を回避（オプション）**
   サポート対象外のOpenJDKビルド（例：IcedTeaやAdoptOpenJDK）を使用している場合、プロファイリング機能が制限される可能性があります。コマンドライン引数を追加することで一部の制限を回避できます：
   ```bash
   ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64 -J-Dorg.graalvm.visualvm.profiler.SupportAllVMs=true
   ```
   これにより、サポート対象外のJVMに対するプロファイリングが有効になりますが、完全な動作は保証されません。[](https://github.com/oracle/visualvm/issues/143)

10. **YourKitとVisualVMの互換性を確認**
    YourKit Java ProfilerディレクトリからVisualVMを実行しているため、YourKitの環境が干渉していないか確認します。YourKit Java Profiler 2025.3は特定のVisualVMバージョンや設定をバンドルしている可能性があります。YourKitのドキュメントを確認するか、`support@yourkit.com`に連絡してあなたのJDKとの互換性を確認してください。別の方法として、問題を切り分けるために、独立して（別途ダウンロードして）VisualVMを実行してみてください。[](https://www.yourkit.com/changes/)

### 追加の注意点
- **YourKitのコンテキスト**: このエラーはYourKit Java Profilerに直接関連するものではありませんが、YourKitのディレクトリからVisualVMを実行していることから、統合が示唆されます。YourKitはJava 7–15およびそれ以降のバージョンをEAPビルドでサポートしているため、両ツールを併用する場合はあなたのJDKが両方と互換性があることを確認してください。[](https://www.yourkit.com/forum/viewtopic.php?t=41723)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **ログファイル**: 詳細を確認するためにVisualVMのログを確認します。ログは通常`~/.visualvm/<version>/var/log`にあります。YourKitについては、プロファイラエージェントのログを`~/.yjp/log/`で確認します。問題が解決しない場合は、ログを`support@yourkit.com`に送信してください。[](https://stackoverflow.com/questions/70211315/java-17-and-yourkit-2021-11)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **代替手段**: VisualVMが引き続き失敗する場合は、YourKitの組み込みプロファイリングツールや、JProfilerやAsync Profilerなど、あなたの環境との互換性がより高い別のプロファイラの使用を検討してください。[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)

### 問題が解決しない場合
上記のいずれも問題を解決しない場合は、以下を提供してください：
- `java -version`と`echo $JAVA_HOME`の出力。
- `update-alternatives --list java`の出力。
- 正確なVisualVMバージョン（`visualvm --help`またはダウンロードページで確認）。
- YourKitにバンドルされているVisualVMを使用しているか、スタンドアロンインストールか。

これにより、問題をさらに特定するのに役立ちます。また、VisualVM GitHubページ（`https://github.com/oracle/visualvm`）に問題を報告するか、YourKitサポートに具体的なガイダンスを求めることもできます。[](https://github.com/oracle/visualvm/issues/558)