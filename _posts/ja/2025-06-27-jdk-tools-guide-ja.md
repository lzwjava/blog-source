---
audio: false
generated: true
lang: ja
layout: post
title: OpenJDK 21 ツール概要
translated: true
type: note
---

ディレクトリ `/usr/lib/jvm/java-21-openjdk-amd64/bin/` には、OpenJDK 21 Java Development Kit (JDK) によって提供されるツールが含まれています。これらのツールは、Java開発、デバッグ、モニタリング、パッケージングに関連する様々なタスクに使用されます。以下に、各ツールとその一般的な使用法を簡潔に説明します。詳細な使用法については、ターミナルで `tool_name --help` または `man tool_name` を実行してください（これらのツールのほとんどで利用可能です）。

---

### 1. **jar** - Java ARchive (JAR) ファイルの作成と管理
- **目的**: JavaクラスとリソースをJARファイルにパッケージ化、またはJARからコンテンツを抽出します。
- **一般的な使用法**:
  ```bash
  jar cf myapp.jar *.class  # JARファイルを作成
  jar xf myapp.jar          # JARのコンテンツを抽出
  jar tf myapp.jar          # JARのコンテンツを一覧表示
  ```
- **例**: `jar cvfm myapp.jar manifest.txt *.class` (マニフェストファイルを含むJARを作成)。

---

### 2. **java** - Javaアプリケーションの起動
- **目的**: クラスファイルまたはJARを実行してJavaプログラムを実行します。
- **一般的な使用法**:
  ```bash
  java MyClass              # クラスファイルを実行
  java -jar myapp.jar       # JARファイルを実行
  java -cp . MyClass        # 特定のクラスパスで実行
  ```
- **例**: `java -Xmx512m -jar myapp.jar` (最大ヒープ512MBでJARを実行)。

---

### 3. **javadoc** - APIドキュメントの生成
- **目的**: JavaソースコードのコメントからHTMLドキュメントを作成します。
- **一般的な使用法**:
  ```bash
  javadoc -d docs MyClass.java  # 'docs'フォルダにドキュメントを生成
  ```
- **例**: `javadoc -d docs -sourcepath src -subpackages com.example` (パッケージのドキュメントを生成)。

---

### 4. **jcmd** - 実行中のJVMに診断コマンドを送信
- **目的**: 実行中のJavaプロセスと対話して診断を行います（スレッドダンプ、ヒープ情報など）。
- **一般的な使用法**:
  ```bash
  jcmd <pid> help           # JVMプロセスで利用可能なコマンドを一覧表示
  jcmd <pid> Thread.print   # スレッドダンプを出力
  ```
- **例**: `jcmd 1234 GC.run` (プロセスID 1234に対してガベージコレクションをトリガー)。

---

### 5. **jdb** - Javaデバッガ
- **目的**: Javaアプリケーションを対話的にデバッグします。
- **一般的な使用法**:
  ```bash
  jdb MyClass               # クラスのデバッグを開始
  java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyClass  # デバッグエージェントで実行
  jdb -attach localhost:5005  # 実行中のJVMにアタッチ
  ```
- **例**: `jdb -sourcepath src MyClass` (ソースコード付きでデバッグ)。

---

### 6. **jdeps** - クラスとJARの依存関係を分析
- **目的**: Javaアプリケーションまたはライブラリの依存関係を特定します。
- **一般的な使用法**:
  ```bash
  jdeps myapp.jar           # JAR内の依存関係を分析
  jdeps -s MyClass.class    # 依存関係の概要
  ```
- **例**: `jdeps -v myapp.jar` (詳細な依存関係分析)。

---

### 7. **jhsdb** - Java HotSpotデバッガ
- **目的**: JVMプロセスの高度なデバッグと分析を行います（コアダンプなど）。
- **一般的な使用法**:
  ```bash
  jhsdb jmap --heap --pid <pid>  # 実行中のプロセスのヒープを分析
  jhsdb hsdb                     # HotSpotデバッガGUIを起動
  ```
- **例**: `jhsdb jmap --heap --pid 1234` (プロセス1234のヒープ情報をダンプ)。

---

### 8. **jinfo** - JVM設定の表示または変更
- **目的**: 実行中のプロセスのJVMオプションを検査または変更します。
- **一般的な使用法**:
  ```bash
  jinfo <pid>               # JVMフラグとプロパティを表示
  jinfo -flag +PrintGC <pid>  # JVMフラグを有効化
  ```
- **例**: `jinfo -sysprops 1234` (プロセス1234のシステムプロパティを表示)。

---

### 9. **jmap** - JVMメモリまたはヒープ情報のダンプ
- **目的**: ヒープダンプまたはメモリ統計を生成します。
- **一般的な使用法**:
  ```bash
  jmap -heap <pid>          # ヒープ概要を出力
  jmap -dump:file=dump.hprof <pid>  # ヒープダンプを作成
  ```
- **例**: `jmap -dump:live,format=b,file=dump.hprof 1234` (生存中のオブジェクトをダンプ)。

---

### 10. **jpackage** - Javaアプリケーションのパッケージング
- **目的**: Javaアプリケーション用のネイティブインストーラーまたは実行ファイルを作成します（例: .deb, .rpm, .exe）。
- **一般的な使用法**:
  ```bash
  jpackage --input target --name MyApp --main-jar myapp.jar --main-class MyClass
  ```
- **例**: `jpackage --type deb --input target --name MyApp --main-jar myapp.jar` (Debianパッケージを作成)。

---

### 11. **jps** - 実行中のJVMプロセスの一覧表示
- **目的**: プロセスID (PID) 付きでJavaプロセスを表示します。
- **一般的な使用法**:
  ```bash
  jps                       # 全てのJavaプロセスを一覧表示
  jps -l                    # 完全なクラス名を含める
  ```
- **例**: `jps -m` (メインクラスと引数を表示)。

---

### 12. **jrunscript** - Javaでスクリプトを実行
- **目的**: Javaスクリプトエンジンを使用してスクリプト（例: JavaScript）を実行します。
- **一般的な使用法**:
  ```bash
  jrunscript -e "print('Hello')"  # 単一のスクリプトコマンドを実行
  jrunscript script.js            # スクリプトファイルを実行
  ```
- **例**: `jrunscript -l js -e "print(2+2)"` (JavaScriptコードを実行)。

---

### 13. **jshell** - 対話型Java REPL
- **目的**: テストや学習のために、対話的にJavaコードスニペットを実行します。
- **一般的な使用法**:
  ```bash
  jshell                    # 対話型シェルを開始
  jshell script.jsh         # JShellスクリプトを実行
  ```
- **例**: `jshell -q` (QuietモードでJShellを開始)。

---

### 14. **jstack** - スレッドダンプの生成
- **目的**: 実行中のJVM内のスレッドのスタックトレースをキャプチャします。
- **一般的な使用法**:
  ```bash
  jstack <pid>              # スレッドダンプを出力
  jstack -l <pid>           # ロック情報を含める
  ```
- **例**: `jstack 1234 > threads.txt` (スレッドダンプをファイルに保存)。

---

### 15. **jstat** - JVM統計の監視
- **目的**: パフォーマンス統計を表示します（ガベージコレクション、メモリ使用量など）。
- **一般的な使用法**:
  ```bash
  jstat -gc <pid>           # ガベージコレクション統計を表示
  jstat -class <pid> 1000   # 1秒ごとにクラスローディング統計を表示
  ```
- **例**: `jstat -gcutil 1234 1000 5` (GC統計を1秒間隔で5回表示)。

---

### 16. **jstatd** - JVM監視デーモン
- **目的**: `jstat` などのツールがリモート接続できるようにするリモート監視サーバーを実行します。
- **一般的な使用法**:
  ```bash
  jstatd -J-Djava.security.policy=jstatd.policy
  ```
- **例**: `jstatd -p 1099` (ポート1099でデーモンを開始)。

---

### 17. **keytool** - 暗号化キーと証明書の管理
- **目的**: セキュアなJavaアプリケーション用のキーストアを作成および管理します。
- **一般的な使用法**:
  ```bash
  keytool -genkeypair -alias mykey -keystore keystore.jks  # キーペアを生成
  keytool -list -keystore keystore.jks                     # キーストアの内容を一覧表示
  ```
- **例**: `keytool -importcert -file cert.pem -keystore keystore.jks` (証明書をインポート)。

---

### 18. **rmiregistry** - RMIレジストリの開始
- **目的**: Java Remote Method Invocation (RMI) オブジェクト用のレジストリを実行します。
- **一般的な使用法**:
  ```bash
  rmiregistry               # デフォルトポート(1099)でRMIレジストリを開始
  rmiregistry 1234          # 特定のポートで開始
  ```
- **例**: `rmiregistry -J-Djava.rmi.server.codebase=file:./classes/` (コードベースを指定して開始)。

---

### 19. **serialver** - クラスの serialVersionUID を生成
- **目的**: `Serializable` を実装するJavaクラスの `serialVersionUID` を計算します。
- **一般的な使用法**:
  ```bash
  serialver MyClass         # クラスのserialVersionUIDを出力
  ```
- **例**: `serialver -classpath . com.example.MyClass` (特定のクラスに対して計算)。

---

### 20. **javac** - Javaコンパイラ
- **目的**: Javaソースファイルをバイトコードにコンパイルします。
- **一般的な使用法**:
  ```bash
  javac MyClass.java        # 単一ファイルをコンパイル
  javac -d bin *.java       # 特定のディレクトリにコンパイル
  ```
- **例**: `javac -cp lib/* -sourcepath src -d bin src/MyClass.java` (依存関係を含めてコンパイル)。

---

### 21. **javap** - クラスファイルの逆アセンブル
- **目的**: コンパイルされたクラスのバイトコードまたはメソッドシグネチャを表示します。
- **一般的な使用法**:
  ```bash
  javap -c MyClass          # バイトコードを逆アセンブル
  javap -s MyClass          # メソッドシグネチャを表示
  ```
- **例**: `javap -c -private MyClass` (プライベートメソッドとバイトコードを表示)。

---

### 22. **jconsole** - グラフィカルJVM監視ツール
- **目的**: GUI経由でJVMのパフォーマンス（メモリ、スレッド、CPU）を監視します。
- **一般的な使用法**:
  ```bash
  jconsole                  # JConsoleを起動しローカルJVMに接続
  jconsole <pid>            # 特定のプロセスに接続
  ```
- **例**: `jconsole localhost:1234` (リモートJVMに接続)。

---

### 23. **jdeprscan** - 非推奨APIのスキャン
- **目的**: JARまたはクラスファイル内での非推奨APIの使用を特定します。
- **一般的な使用法**:
  ```bash
  jdeprscan myapp.jar       # JARをスキャンして非推奨APIを検出
  ```
- **例**: `jdeprscan --release 11 myapp.jar` (Java 11 APIに対してチェック)。

---

### 24. **jfr** - Java Flight Recorder
- **目的**: Java Flight Recorderのプロファイリングデータを管理および分析します。
- **一般的な使用法**:
  ```bash
  jfr print recording.jfr   # JFRファイルの内容を出力
  jfr summary recording.jfr # JFRファイルの概要を表示
  ```
- **例**: `jfr print --events GC recording.jfr` (GCイベントを表示)。

---

### 25. **jimage** - JIMAGEファイルの検査または抽出
- **目的**: JIMAGEファイル（JDKモジュールで使用）を操作します。
- **一般的な使用法**:
  ```bash
  jimage extract image.jimage  # JIMAGEファイルのコンテンツを抽出
  ```
- **例**: `jimage list image.jimage` (JIMAGEの内容を一覧表示)。

---

### 26. **jlink** - カスタムJavaランタイムイメージの作成
- **目的**: 必要なモジュールのみを含む最小限のJREを構築します。
- **一般的な使用法**:
  ```bash
  jlink --module-path mods --add-modules java.base --output myjre
  ```
- **例**: `jlink --add-modules java.base,java.sql --output custom-jre` (特定のモジュールを含むJREを作成)。

---

### 27. **jmod** - JMODファイルの管理
- **目的**: JMODファイル（JDKモジュール用）を作成または管理します。
- **一般的な使用法**:
  ```bash
  jmod create --class-path classes mymod.jmod  # JMODファイルを作成
  jmod list mymod.jmod                        # 内容を一覧表示
  ```
- **例**: `jmod extract mymod.jmod` (JMODの内容を抽出)。

---

### 28. **jwebserver** - シンプルなHTTPサーバー
- **目的**: 静的ファイルを提供するための基本的なWebサーバーを実行します。
- **一般的な使用法**:
  ```bash
  jwebserver -d /path/to/dir  # ディレクトリ用にサーバーを開始
  jwebserver -p 8080          # 特定のポートで開始
  ```
- **例**: `jwebserver -d ./html -p 8000` (./html のファイルをポート8000で提供)。

---

### さらなる学習のためのヒント
- **ドキュメント**: `tool_name --help` を実行するか、OracleのJDKドキュメント (例: https://docs.oracle.com/en/java/javase/21/docs/specs/man/) を参照してください。
- **マニュアルページ**: マニュアルページがあるツールでは `man tool_name` を使用してください。
- **実践**: テストプロジェクトで実験してツールの動作を理解してください。
- **監視ツール**: `jcmd`, `jmap`, `jstack` などでは、`jps` を使用してJavaプロセスのPIDを検索してください。
- **デバッグ**: 高度なデバッグには `jdb`, `jhsdb`, `jconsole` を組み合わせて使用してください。

（ディレクトリから示唆されるように）トレーディングプロジェクトに取り組んでいる場合、アプリケーションのコンパイル、実行、パッケージングには `javac`, `java`, `jar`, `jpackage` などのツールが最も関連する可能性が高いです。パフォーマンスチューニングには `jstat`, `jmap`, `jfr` を使用してください。特定のツールの詳細やトレーディングプロジェクトに関するヘルプが必要な場合はお知らせください！