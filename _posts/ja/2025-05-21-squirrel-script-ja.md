---
audio: false
generated: true
lang: ja
layout: post
title: SQuirreL起動スクリプト
translated: true
type: note
---

このバッチスクリプトは、Javaベースのデータベース管理ツールであるSQuirreL SQL Clientを起動するために使用されます。以下に、スクリプトの目的、構造、機能を段階的に詳しく説明します。

---

### **概要**
このスクリプトは以下のように設計されています：
1. SQuirreL SQL Clientを実行するためのJava環境を設定する
2. Javaバージョンの互換性（Java 1.6または1.7が必要）を確認する
3. ソフトウェアアップデートを確認し、利用可能な場合は適用する
4. SQuirreLとそのライブラリのクラスパスを構築する
5. 適切なパラメータでSQuirreL SQL Clientアプリケーションを起動する

このスクリプトはWindows用（`.bat`拡張子を使用）に書かれており、Windowsコマンドプロンプトのバッチスクリプト言語を使用しています。

---

### **行単位の説明**

#### **1. `@echo off`**
- **目的**: コンソールへのコマンドのエコーを無効にし、意図された出力（エラーメッセージや特定の`echo`文など）のみを表示することで、スクリプトの出力をクリーンにする
- **効果**: `echo`を使用して明示的に印刷されない限り、スクリプトで実行されたコマンドは表示されない

---

#### **2. `@rem IZPACK_JAVA is filtered in by the IzPack installer when this script is installed`**
- **目的**: `IZPACK_JAVA`変数がインストール中にIzPackインストーラによって設定されることを示すコメント（`@rem`）
- **コンテキスト**: IzPackはJavaアプリケーション用のインストーラを作成するために使用されるツールです。セットアップ中に使用されたJavaインストールを指すように、スクリプト内の`JAVA_HOME`環境変数を動的に設定します

#### **3. `set IZPACK_JAVA=%JAVA_HOME`**
- **目的**: `JAVA_HOME`環境変数（IzPackによって設定）の値を`IZPACK_JAVA`変数に割り当てる
- **説明**: これにより、スクリプトはJavaインストールの場所を認識します。`JAVA_HOME`は通常、Java Development Kit（JDK）またはJava Runtime Environment（JRE）のルートディレクトリを指します

---

#### **4. Java検出ロジック**
```bat
@rem We detect the java executable to use according to the following algorithm:
@rem 1. If the one used by the IzPack installer is available then use that; otherwise
@rem 2. Use the java that is in the command path.
if exist "%IZPACK_JAVA%\bin\javaw.exe" (
  set LOCAL_JAVA=%IZPACK_JAVA%\bin\javaw.exe
) else (
  set LOCAL_JAVA=javaw.exe
)
```
- **目的**: SQuirreL SQLを実行するために使用するJava実行ファイルを決定する
- **ロジック**:
  1. **IzPack Javaの確認**: スクリプトは、`IZPACK_JAVA`で指定されたJavaインストールの`bin`ディレクトリに`javaw.exe`が存在するかどうかを確認します
     - `javaw.exe`は、コンソールウィンドウを開かずにJavaアプリケーションを実行するWindows固有のJava実行ファイルです（`java.exe`とは異なります）
     - 見つかった場合、`LOCAL_JAVA`は`javaw.exe`の完全なパスに設定されます
  2. **PATHへのフォールバック**: `javaw.exe`が`IZPACK_JAVA`ディレクトリに見つからない場合、スクリプトはシステムの`PATH`環境変数から`javaw.exe`を使用することにフォールバックします
- **なぜ`javaw.exe`なのか？**: `javaw.exe`を使用すると、永続的なコマンドウィンドウなしでアプリケーションが実行され、よりクリーンなユーザーエクスペリエンスが提供されます

#### **5. `echo Using java: %LOCAL_JAVA%`**
- **目的**: デバッグまたは情報提供のために、使用されているJava実行ファイルのパスをコンソールに出力する
- **出力例**: `LOCAL_JAVA`が`C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe`の場合、以下を表示します：
  ```
  Using java: C:\Program Files\Java\jre1.6.0_45\bin\javaw.exe
  ```

---

#### **6. SQuirreL SQLホームディレクトリの決定**
```bat
set basedir=%~f0
:strip
set removed=%basedir:~-1%
set basedir=%basedir:~0,-1%
if NOT "%removed%"=="\" goto strip
set SQUIRREL_SQL_HOME=%basedir%
```
- **目的**: SQuirreL SQLがインストールされているディレクトリ（`SQUIRREL_SQL_HOME`）を決定する
- **説明**:
  - `%~f0`: これはバッチスクリプト自体の完全なパスに展開されます（例：`C:\Program Files\SQuirreL\squirrel-sql.bat`）
  - **`:strip`ループ**: スクリプトは、バックスラッシュ（`\`）に遭遇するまで、`basedir`から最後の文字を繰り返し削除し、スクリプトのファイル名を効果的に取り除いてディレクトリパスを取得します
  - **結果**: `SQUIRREL_SQL_HOME`はスクリプトを含むディレクトリに設定されます（例：`C:\Program Files\SQuirreL`）
- **なぜこのアプローチなのか？**: これにより、スクリプトは独自のインストールディレクトリを動的に決定でき、異なるシステム間で移植性が高くなります

---

#### **7. Javaバージョンチェック**
```bat
"%LOCAL_JAVA%" -cp "%SQUIRREL_SQL_HOME%\lib\versioncheck.jar" JavaVersionChecker 1.6 1.7
if ErrorLevel 1 goto ExitForWrongJavaVersion
```
- **目的**: JavaバージョンがSQuirreL SQLと互換性があるか（Java 1.6または1.7が必要）を確認する
- **説明**:
  - スクリプトは、SQuirreL SQLの`lib`ディレクトリにある`versioncheck.jar`から`JavaVersionChecker`クラスを実行します
  - **`-cp`**: クラスパスを指定し、`versioncheck.jar`を指します
  - **引数**: `1.6 1.7`は、Javaバージョンが1.6または1.7でなければならないことを示します
  - **注記**: `versioncheck.jar`はJava 1.2.2互換でコンパイルされており、バージョンチェックを実行するために古いJVMで実行できることが保証されています
  - **エラーハンドリング**: Javaバージョンに互換性がない場合、`ErrorLevel`は1に設定され、スクリプトは`:ExitForWrongJavaVersion`ラベルにジャンプして実行を終了します
- **なぜこのチェックなのか？**: SQuirreL SQLは正常に機能するために特定のJavaバージョンを必要とし、これによりサポートされていないJVMでアプリケーションが実行されるのを防ぎます

---

#### **8. ソフトウェアアップデートチェック**
```bat
if not exist "%SQUIRREL_SQL_HOME%\update\changeList.xml" goto launchsquirrel
SET TMP_CP="%SQUIRREL_SQL_HOME%\update\downloads\core\squirrel-sql.jar"
if not exist %TMP_CP% goto launchsquirrel
dir /b "%SQUIRREL_SQL_HOME%\update\downloads\core\*.*" > %TEMP%\update-lib.tmp
FOR /F %%I IN (%TEMP%\update-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\update\downloads\core\%%I"
SET UPDATE_CP=%TMP_CP%
SET UPDATE_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\update-log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
"%LOCAL_JAVA%" -cp %UPDATE_CP% -Dlog4j.defaultInitOverride=true -Dprompt=true net.sourceforge.squirrel_sql.client.update.gui.installer.PreLaunchUpdateApplication %UPDATE_PARAMS%
```
- **目的**: メインアプリケーションを起動する前にソフトウェアアップデートを確認し、適用する
- **説明**:
  1. **アップデートファイルの確認**:
     - スクリプトは、`update`ディレクトリに`changeList.xml`が存在するかどうかを確認します。このファイルは、アップデートを追跡するためにSQuirreLのソフトウェアアップデート機能によって作成されます
     - `changeList.xml`が存在しない場合、スクリプトはアップデートプロセスをスキップして`:launchsquirrel`にジャンプします
     - また、`update\downloads\core`ディレクトリに更新された`squirrel-sql.jar`があるかどうかも確認します。存在しない場合、スクリプトは`:launchsquirrel`にスキップします
  2. **アップデートクラスパスの構築**:
     - `dir /b`コマンドは、`update\downloads\core`ディレクトリ内のすべてのファイルをリストし、それらを一時ファイル（`%TEMP%\update-lib.tmp`）に書き込みます
     - `FOR /F`ループは`update-lib.tmp`内のファイルを反復処理し、各ファイルを`TMP_CP`に格納されたクラスパスに追加するために`addpath.bat`を呼び出します
     - `UPDATE_CP`は、アップデートディレクトリからの`squirrel-sql.jar`で始まるクラスパスに設定されます
  3. **アップデートパラメータの設定**:
     - `UPDATE_PARMS`には以下が含まれます：
       - `--log-config-file`: アップデートプロセス中のロギング用のLog4j設定ファイルを指定します
       - `--squirrel-home`: SQuirreLインストールディレクトリを渡します
       - `%1 %2 %3 ... %9`: スクリプトに提供されたコマンドライン引数を渡します
  4. **アップデートアプリケーションの実行**:
     - スクリプトは、アップデートを適用するために`PreLaunchUpdateApplication`（`squirrel-sql.jar`内のJavaクラス）を起動します
     - **`-Dlog4j.defaultInitOverride=true`**: デフォルトのLog4j設定をオーバーライドします
     - **`-Dprompt=true`**: アップデートプロセス中に対話型プロンプトを有効にする可能性があります
- **なぜこのステップなのか？**: SQuirreL SQLは自動アップデートをサポートしており、このセクションはメインアプリケーションを起動する前にダウンロードされたアップデートが適用されることを保証します

---

#### **9. SQuirreL SQLの起動**
```bat
:launchsquirrel
@rem build SQuirreL's classpath
set TMP_CP="%SQUIRREL_SQL_HOME%\squirrel-sql.jar"
dir /b "%SQUIRREL_SQL_HOME%\lib\*.*" > %TEMP%\squirrel-lib.tmp
FOR /F %%I IN (%TEMP%\squirrel-lib.tmp) DO CALL "%SQUIRREL_SQL_HOME%\addpath.bat" "%SQUIRREL_SQL_HOME%\lib\%%I"
SET SQUIRREL_CP=%TMP_CP%
echo "SQUIRREL_CP=%SQUIRREL_CP%"
```
- **目的**: メインSQuirreL SQLアプリケーションのクラスパスを構築し、起動の準備をする
- **説明**:
  1. **クラスパスの初期化**:
     - `TMP_CP`は、SQuirreLインストールディレクトリ内の`squirrel-sql.jar`へのパスで初期化されます
  2. **ライブラリJarの追加**:
     - `dir /b`コマンドは、`lib`ディレクトリ内のすべてのファイルをリストし、それらを`squirrel-lib.tmp`に書き込みます
     - `FOR /F`ループはファイルを反復処理し、各ライブラリファイル（例：`.jar`ファイル）を`TMP_CP`クラスパスに追加するために`addpath.bat`を呼び出します
  3. **最終クラスパスの設定**:
     - `SQUIRREL_CP`は完成したクラスパスに設定されます
  4. **デバッグ出力**:
     - スクリプトはデバッグ目的で最終クラスパス（`SQUIRREL_CP`）を出力します

---

#### **10. 起動パラメータの設定**
```bat
SET TMP_PARMS=--log-config-file "%SQUIRREL_SQL_HOME%\log4j.properties" --squirrel-home "%SQUIRREL_SQL_HOME%" %1 %2 %3 %4 %5 %6 %7 %8 %9
```
- **目的**: SQuirreL SQLアプリケーションに渡すパラメータを定義する
- **説明**:
  - `--log-config-file`: メインアプリケーション用のLog4j設定ファイルを指定します
  - `--squirrel-home`: SQuirreLインストールディレクトリを渡します
  - `%1 %2 ... %9`: スクリプトに提供されたコマンドライン引数を渡します

---

#### **11. アプリケーションの起動**
```bat
@rem -Dsun.java2d.noddraw=true prevents performance problems on Win32 systems.
start "SQuirreL SQL Client" /B "%LOCAL_JAVA%" -Xmx256m -Dsun.java2d.noddraw=true -cp %SQUIRREL_CP% -splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg" net.sourceforge.squirrel_sql.client.Main %TMP_PARMS%
```
- **目的**: SQuirreL SQL Clientアプリケーションを起動する
- **説明**:
  - **`start "SQuirreL SQL Client" /B`**: 新しいコンソールウィンドウを開かずに新しいプロセスでコマンドを実行します（`/B`はウィンドウを抑制します）
  - **`%LOCAL_JAVA%`**: 使用するJava実行ファイルを指定します
  - **`-Xmx256m`**: メモリ使用量を制限するために、Javaヒープの最大サイズを256 MBに設定します
  - **`-Dsun.java2d.noddraw=true`**: Windowsシステムでのパフォーマンス問題を回避するために、Java 2DグラフィックスのDirectDrawを無効にします
  - **`-cp %SQUIRREL_CP%`**: アプリケーションのクラスパスを指定します
  - **`-splash:"%SQUIRREL_SQL_HOME%/icons/splash.jpg"`**: アプリケーション起動時にスプラッシュスクリーン（画像）を表示します
  - **`net.sourceforge.squirrel_sql.client.Main`**: 実行するメインJavaクラス
  - **`%TMP_PARMS%`**: 前述のパラメータを渡します

---

#### **12. 間違ったJavaバージョンのための終了**
```bat
:ExitForWrongJavaVersion
```
- **目的**: Javaバージョンチェックが失敗した場合の終了点として使用されるラベル
- **説明**: Javaバージョンが1.6または1.7でない場合、スクリプトはここにジャンプし、アプリケーションを起動せずに終了します

---

### **主要コンポーネントと概念**
1. **クラスパス構築**:
   - スクリプトは、`squirrel-sql.jar`と`lib`または`update\downloads\core`ディレクトリ内のすべての`.jar`ファイルを含めることで、アップデートプロセス（`UPDATE_CP`）とメインアプリケーション（`SQUIRREL_CP`）の両方のクラスパスを動的に構築します
   - `addpath.bat`スクリプト（表示されていない）は、各ファイルをクラスパス変数に追加すると想定されています

2. **Log4j設定**:
   - Log4jはSQuirreL SQLで使用されるロギングフレームワークです。スクリプトは、アップデートプロセス（`update-log4j.properties`）とメインアプリケーション（`log4j.properties`）用に個別のLog4j設定ファイルを指定します

3. **ソフトウェアアップデートメカニズム**:
   - SQuirreL SQLは自動アップデートをサポートし、`PreLaunchUpdateApplication`クラスによって管理されます。スクリプトはアップデートファイルを確認し、必要に応じてアップデートプロセスを実行します

4. **Javaバージョン互換性**:
   - スクリプトはJava 1.6または1.7との厳格な互換性を強制します。これは、これらのバージョンに固有の依存関係または機能による可能性があります

5. **移植性**:
   - スクリプトは、インストールディレクトリとJava実行ファイルの場所を動的に決定することで、移植性が高く設計されています

---

### **潜在的な問題と考慮事項**
1. **Javaバージョン制限**:
   - スクリプトはJava 1.6または1.7のみを許可しますが、これらは時代遅れです（それぞれ2006年と2011年にリリース）。最新のシステムには新しいJavaバージョンがある可能性があり、古いJREがインストールされていない限りスクリプトは失敗します
   - **回避策**: ユーザーは互換性のあるJREをインストールするか、スクリプトを変更して新しいバージョンをサポートする必要があるかもしれません（SQuirreL SQLが互換性がある場合）

2. **ハードコードされたパス**:
   - スクリプトは、特定のファイル（例：`squirrel-sql.jar`、`versioncheck.jar`、`addpath.bat`）が`SQUIRREL_SQL_HOME`に対して特定のディレクトリに存在することを想定しています。これらが欠落しているか移動された場合、スクリプトは失敗します

3. **Windows固有**:
   - スクリプトはWindows固有のコマンド（`dir /b`、`FOR /F`、`start /B`）と`javaw.exe`を使用するため、変更なしでは非Windowsシステムと互換性がありません

4. **エラーハンドリング**:
   - スクリプトはJavaバージョンエラーを処理しますが、他の失敗（例：`squirrel-sql.jar`の欠落や無効なクラスパス）に対する詳細なエラーメッセージを提供しません

5. **メモリ制限**:
   - `-Xmx256m`フラグはJVMを256 MBのメモリに制限しますが、これは大規模なデータベースや複雑なクエリには不十分な可能性があり、`OutOfMemoryError`を引き起こす可能性があります

---

### **まとめ**
このバッチスクリプトはSQuirreL SQL Clientのランチャーであり、以下のタスクを実行します：
- Java実行ファイルを検出および設定する
- Javaバージョンの互換性（1.6または1.7）を確認する
- 利用可能な場合はソフトウェアアップデートを確認および適用する
- アプリケーションのクラスパスを構築する
- スプラッシュスクリーンとメモリ設定を含む適切なパラメータでSQuirreL SQLを起動する

このスクリプトはその目的に対してよく構造化されていますが、特定の環境（Windows、Java 1.6/1.7）に合わせて調整されており、最新のシステムまたは新しいJavaバージョンをサポートするには更新が必要な場合があります。

スクリプトの変更（例：新しいJavaバージョンのサポート）に関するさらなる質問や支援が必要な場合は、お知らせください！