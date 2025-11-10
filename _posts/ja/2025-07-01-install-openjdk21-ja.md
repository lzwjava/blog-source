---
audio: false
generated: true
lang: ja
layout: post
title: macOSへのOpenJDK 21アップグレード
translated: true
type: note
---

現在、macOSシステムにHomebrew経由でOpenJDK 17がインストールされている状況ですが、ここでは最新の長期サポート（LTS）リリースであるOpenJDK 21（現在の日付である2025年7月1日時点）をインストールする簡潔なガイドを提供します。OpenJDK 21はOpenJDK 17と並行してインストールし、必要に応じて切り替えることができます。最も簡単な方法はHomebrewを使用することですが、手動インストールのオプションも提供します。

### 方法1: Homebrewを使用したOpenJDK 21のインストール（推奨）
現在のJavaバージョンから、Homebrewは既にシステムにインストールされています。これが最も簡単で保守性の高いアプローチです。

1. **Homebrewの更新**:
   最新のパッケージを取得するためにHomebrewを最新の状態にします：
   ```bash
   brew update
   ```

2. **OpenJDK 21のインストール**:
   HomebrewはOpenJDK 21用の特定のフォーミュラを提供しています。次のコマンドを実行します：
   ```bash
   brew install openjdk@21
   ```
   これはOpenJDK 21をkeg-onlyモードでインストールします。つまり、他のJavaバージョンとの競合を避けるために`/usr/local/bin`にシンボリックリンクは作成されません。

3. **OpenJDK 21をPATHに追加**:
   OpenJDK 21を使用するには、システムのPATHに追加する必要があります。Homebrewはインストール後に指示を提供しますが、通常は一時的または永続的にリンクできます：
   - **一時的（現在のセッションのみ）**:
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
   - **永続的（シェル設定に追加）**:
     シェル設定ファイル（macOSはデフォルトでZshを使用するため、おそらく`~/.zshrc`）を開きます：
     ```bash
     nano ~/.zshrc
     ```
     次の行を追加します：
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
     ファイルを保存して閉じ、変更を適用します：
     ```bash
     source ~/.zshrc
     ```

4. **JAVA_HOMEの設定**:
   JavaアプリケーションがOpenJDK 21を見つけられるようにするために、`JAVA_HOME`環境変数を設定します：
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```
   これを永続的にするには`~/.zshrc`に追加します：
   ```bash
   echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
   source ~/.zshrc
   ```

5. **インストールの確認**:
   OpenJDK 21がインストールされ、アクティブであることを確認します：
   ```bash
   java -version
   ```
   次のような出力が表示されるはずです：
   ```
   openjdk 21.0.1 2023-10-17
   OpenJDK Runtime Environment (build 21.0.1+12)
   OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
   ```

6. **Javaバージョンの切り替え**:
   OpenJDK 17がインストールされているため、`/usr/libexec/java_home`を使用してバージョンを切り替えることができます。例：
   - OpenJDK 17を使用する場合：
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 17)
     ```
   - OpenJDK 21を使用する場合：
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 21)
     ```
   あるいは、より簡単な切り替えのために`jenv`のようなバージョンマネージャーの使用を検討してください（`brew install jenv`でインストール）：
   ```bash
   jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
   jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
   jenv enable-plugin export
   jenv global 21
   ```

### 方法2: 手動インストール
Homebrewを使用したくない場合は、手動でOpenJDK 21をインストールできます。

1. **OpenJDK 21のダウンロード**:
   - 公式OpenJDKウェブサイト（jdk.java.net/21）またはOracle、Azul、Adoptiumなどの信頼できるプロバイダーを訪問します。
   - Apple Silicon（M1/M2）の場合は、`macOS/AArch64` tar.gzファイルをダウンロードします。IntelベースのMacの場合は、`macOS/x64`を選択します。
   - 例：OracleのJDK 21ダウンロードページから、ARM64またはx64 tar.gzファイルを選択します。

2. **ダウンロードの検証**:
   ダウンロードしたファイルの整合性をSHA256チェックサムを使用して確認します：
   ```bash
   shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
   ```
   出力をダウンロードページで提供されているチェックサムと比較します。

3. **ファイルの展開**:
   tar.gzファイルをホームディレクトリなどの目的のディレクトリに展開します：
   ```bash
   tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
   ```
   JDKは`~/OpenJDK/jdk-21.0.1.jdk/Contents/Home`に展開されます。

4. **システムディレクトリへの移動**（オプション）:
   一貫性のために、JDKを標準のmacOS Javaディレクトリに移動できます：
   ```bash
   sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
   ```

5. **JAVA_HOMEとPATHの設定**:
   `~/.zshrc`を更新して以下を含めます：
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```
   変更を適用します：
   ```bash
   source ~/.zshrc
   ```

6. **インストールの確認**:
   インストールを確認します：
   ```bash
   java -version
   ```
   OpenJDK 21が表示されることを確認します。

### 注意点
- **Apple Silicon互換性**: パフォーマンスの問題を避けるために、M1/M2 MacではAArch64ビルドをダウンロードしてください。Homebrewは自動的に正しいアーキテクチャを選択します。
- **複数JDK**: macOSは`/Library/Java/JavaVirtualMachines/`内の複数JDKをサポートしています。`/usr/libexec/java_home -v <version>`を使用して切り替えます。
- **Homebrewの利点**: Homebrewは更新（`brew upgrade openjdk@21`）を簡素化し、システムとの互換性を保証します。
- **代替プロバイダー**: OpenJDK 21のAzul ZuluまたはEclipse Temurinビルドも、それぞれのウェブサイト（例：azul.comやadoptium.net）から利用できます。

問題が発生した場合は、お知らせください。トラブルシューティングをお手伝いします![](https://www.geeksforgeeks.org/how-to-install-openjdk-in-macos/)[](https://formulae.brew.sh/formula/openjdk%4021)[](https://codetrips.com/2023/10/15/installing-java-jdk-21-macos/)