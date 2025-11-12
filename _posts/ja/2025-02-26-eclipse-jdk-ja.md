---
audio: false
generated: true
lang: ja
layout: post
title: Eclipse JDK問題の解決
translated: true
type: note
---

`eclipse.exe` をクリックして Eclipse 4.6.3 を起動し、"Java was started but returned exit code" というエラーが `Oracle\Java\javapath\javaw.exe` を参照して表示される場合、Eclipse が互換性のない、または設定が間違っている Java Virtual Machine (JVM) を使用しようとしていることを意味します。パス `Oracle\Java\javapath\javaw.exe` は、Eclipse がシステムの PATH 環境変数で定義された JVM をデフォルトで使用していることを示しており、この JVM は Eclipse 4.6.3 に適していない可能性があります。これを解決するには、互換性のある JVM を使用するように Eclipse を設定し、正しい Java ホームを指定する必要があります。その方法は以下の通りです。

### ステップバイステップの解決策

1. **要件を理解する**
   Eclipse 4.6.3 (Neon) は正常に動作するために少なくとも Java 8 を必要とします。このエラーは、現在の JVM (`Oracle\Java\javapath` からのもの) がこの要件を満たしていないか、設定に問題があることを示唆しています。Eclipse に互換性のある Java インストール (例えば Java 8 JDK) を指し示す必要があります。

2. **Java のインストール場所を特定する**
   システムにインストールされている互換性のある Java バージョン (例: JDK 1.8.0) の場所を特定します。Windows での一般的な場所は以下の通りです:
   - `C:\Program Files\Java\jdk1.8.0_XXX` (64-bit Java の場合)
   - `C:\Program Files (x86)\Java\jdk1.8.0_XXX` (32-bit Java の場合)
   `XXX` は特定のアップデートバージョン (例: JDK 1.8.0_231 の場合は `231`) に置き換えてください。このディレクトリ内で、`javaw.exe` ファイルは `bin` サブディレクトリにあります (例: `C:\Program Files\Java\jdk1.8.0_XXX\bin\javaw.exe`)。

   **ヒント**: バージョンとアーキテクチャを確認するには、コマンドプロンプトを開き、`bin` ディレクトリに移動して (例: `cd C:\Program Files\Java\jdk1.8.0_XXX\bin`)、以下のコマンドを実行します:
   ```
   java -version
   ```
   出力に "64-Bit" または "32-Bit" が表示されているか確認してアーキテクチャを確認します。これがあなたの Eclipse のバージョン (最近ダウンロードしたものならおそらく 64-bit) と一致していることを確認してください。

3. **`eclipse.ini` ファイルを見つける**
   `eclipse.ini` ファイルは、`eclipse.exe` と同じディレクトリにある設定ファイルです。例えば、Eclipse が `C:\eclipse` にインストールされている場合、ファイルは `C:\eclipse\eclipse.ini` にあります。このファイルを使用して、Eclipse が使用すべき JVM を指定できます。

4. **`eclipse.ini` ファイルを編集する**
   テキストエディタ (例: メモ帳) で管理者権限を使って `eclipse.ini` を開きます。Eclipse に使用する JVM を指示する `-vm` 引数を含むように修正します。以下の手順に従ってください:

   - **既存の内容を確認する**: `-vm` 引数を探します。既に存在する場合、次の行にパスが続きます (例: `-vm` の後に `C:/some/path/bin/javaw.exe`)。問題のある `Oracle\Java\javapath\javaw.exe` を指している場合は、それを置き換えます。`-vm` 引数が存在しない場合は、追加します。
   - **`-vm` 引数を追加または修正する**: `-vmargs` セクション (存在する場合) の前、または初期起動パラメータの後のファイルの先頭近くに、以下の2行を挿入します:
     ```
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     ```
     - パースの問題を避けるために、バックスラッシュ (`\`) の代わりにスラッシュ (`/`) を使用してください。
     - `C:/Program Files/Java/jdk1.8.0_XXX` をあなたの Java インストールへの実際のパスに置き換えてください。
   - **適切な配置を確保する**: `-vm` 引数は、通常 `-vmargs` の後に `-Xms256m` や `-Xmx1024m` のような JVM オプションが続く `-vmargs` セクションの前に現れなければなりません。例えば、編集後の `eclipse.ini` は以下のようになるかもしれません:
     ```
     -startup
     plugins/org.eclipse.equinox.launcher_1.3.201.v20161025-1711.jar
     --launcher.library
     plugins/org.eclipse.equinox.launcher.win32.win32.x86_64_1.1.401.v20161122-1740
     -vm
     C:/Program Files/Java/jdk1.8.0_XXX/bin/javaw.exe
     -vmargs
     -Dosgi.requiredJavaVersion=1.8
     -Xms256m
     -Xmx1024m
     ```
   - **余分なスペースや空行を避ける**: これらがあると Eclipse が設定を誤って解釈する可能性があるため、`-vm` またはパス行の直後に不必要なスペースや空行がないことを確認してください。

5. **保存してテストする**
   `eclipse.ini` ファイルを保存し、`eclipse.exe` をダブルクリックして Eclipse を起動します。正しく設定されていれば、Eclipse は "Java was started but returned exit code" エラーなしで起動するはずです。

### 追加の注意点
- **アーキテクチャの一致**: JVM のアーキテクチャ (32-bit または 64-bit) があなたの Eclipse インストールと一致していることを確認してください。64-bit の Eclipse は 64-bit の JVM (通常は `C:\Program Files\Java` にある) を必要とし、32-bit の Eclipse は `C:\Program Files (x86)\Java` からの 32-bit の JVM を必要とします。
- **パスの確認**: 指定した場所に `javaw.exe` が存在することを再確認してください。パスが間違っている場合、Eclipse は起動に失敗します。
- **代替オプション**: これがうまくいかない場合は、`JAVA_HOME` 環境変数 (例: `C:\Program Files\Java\jdk1.8.0_XXX`) を設定し、システムの PATH に `%JAVA_HOME%\bin` を含めるように更新することを検討してください。ただし、Eclipse では `eclipse.ini` を修正する方法が推奨され、より信頼性が高いです。

`eclipse.ini` ファイルを編集して互換性のある `javaw.exe` へのパスを指定した `-vm` 引数を含めることで、Eclipse が起動に使用する正しい JVM を効果的に指定します。