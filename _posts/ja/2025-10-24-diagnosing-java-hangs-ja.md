---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: JstackによるJavaハング診断
translated: true
type: note
---

### jstackを使用したJavaアプリケーションのハングまたは応答停止の診断

jstackはJDKに含まれるコマンドラインツールで、実行中のJava仮想マシン（JVM）のスレッドダンプを生成します。スレッドダンプは特定の時点での全スレッドの状態を捕捉し、デッドロック、無限ループ、ブロックされたI/O、CPU集中型操作など、ハングの原因を特定する上で重要です。Linux/Unixシステムやクロスプラットフォーム環境で特に有用です。

#### jstackの使用手順:
1. **JavaプロセスID（PID）の特定:**
   - `jps`（JDKの一部）を実行して全Javaプロセスをリスト表示:  
     ```
     jps -l
     ```
     出力例: `12345 MyApp.jar`。PID（例: 12345）をメモします。

   - 代替案: Linux/macOSでは`ps aux | grep java`などのOSコマンドを使用。

2. **スレッドダンプの生成:**
   - jstackをPID付きで実行し、ダンプをファイルに出力:  
     ```
     jstack <PID> > thread-dump.txt
     ```
     - `<PID>`は実際のプロセスIDに置き換えてください。
     - より詳細なダンプ（ロック情報を含む）には`jstack -l <PID> > thread-dump.txt`を使用。
     - JVMがシグナルに応答しない場合、`jhsdb jstack --pid <PID>`を使用（JDK 8以降で利用可能）。

3. **分析用に複数ダンプを取得:**
   - ハング解析には経時比較が有効。10-30秒間隔で3-5回ダンプを取得:  
     ```
     jstack <PID> > dump1.txt
     sleep 10
     jstack <PID> > dump2.txt
     sleep 10
     jstack <PID> > dump3.txt
     ```
     - 必要に応じてbashスクリプトなどでループ処理を自動化。

4. **ダンプの分析:**
   - テキストファイルをエディタまたはIDEで開く。
   - 以下の点を確認:
     - **スレッド状態:** `RUNNABLE`（アクティブ）、`BLOCKED`（ロック待ち、デッドロックの可能性）、`WAITING`（アイドル待機）、`TIMED_WAITING`状態のスレッドに注目。
     - **デッドロック:** "deadlock"を検索、または`jstack -l`のデッドロック検出機能を利用。
     - **スタックトレース:** 繰り返しパターンや特定メソッドで停止している箇所（例: ループ内の無限ループ）を特定。
     - **ネイティブフレーム:** スレッドがネイティブコードで停止している場合、JNI問題やOSレベルでのブロックを示唆。
   - 詳細分析ツール: VisualVM、Eclipse MAT、fastThread.ioなどのオンラインパーサー。例: VisualVMでは「Thread」タブでダンプファイルを読み込み、ロックと状態を可視化。

JVMが応答しない場合（Unixで`kill -3 <PID>`から出力なし）、OSレベルでのハングが疑われるため、`gcore <PID>`による完全コアダンプを検討。

### ProcDumpを使用したプロセスのハングまたは応答停止の診断

ProcDumpはWindows用の無料Sysinternalsツールで、プロセスのメモリまたはCPUダンプを作成します。アプリケーション（Java含む）のハング発生時のスナップショット取得に優れ、特にプロセスが応答不能な場合に有効。WinDbgやVisual Studio Debuggerでの分析用に完全メモリダンプを取得する際に使用。

#### ProcDumpの使用手順:
1. **ダウンロードとセットアップ:**
   - Microsoft SysinternalsサイトからProcDump（procdump.exe）を取得。
   - 管理者権限でコマンドプロンプトを起動。
   - procdump.exeを含むフォルダに移動。

2. **プロセスの特定:**
   - タスクマネージャーまたは`tasklist | findstr <プロセス名>`を使用してPIDまたはイメージ名（例: `java.exe`）を取得。

3. **ハングダンプの取得:**
   - 即時完全メモリダンプ（応答停止プロセスに有用）:  
     ```
     procdump -ma <プロセス名またはPID>
     ```
     - `-ma`: 完全メモリダンプ（全スレッドとヒープを含む）。
     - 例: `procdump -ma java.exe` または `procdump -ma 12345`。

   - 自動ハング検出（応答不能時にトリガー）:  
     ```
     procdump -h <プロセス名またはPID> -o
     ```
     - `-h`: ハングを監視（5秒以上ウィンドウメッセージに応答しないプロセス。ウィンドウなしサービスの場合は`-h 80`のようにCPU閾値を併用）。
     - `-o`: 既存ダンプを上書き。
     - サービス向け: 例外検出の`-e`またはCPU監視と併用: `procdump -c 80 -h <サービス実行ファイル>`。

   - 複数ダンプ取得: 間隔を置いて3回ダンプ（例: 10秒遅延の`-t 10`）:  
     ```
     procdump -ma -n 3 -t 10 <PID>
     ```

4. **ダンプの分析:**
   - ダンプはカレントディレクトリに`.dmp`ファイルとして保存。
   - WinDbg（Microsoft提供の無料版）またはVisual Studio Debuggerで開く。
   - WinDbgの主要コマンド:
     - `!threads`: スレッドと状態のリスト表示（ブロック/待機中のスレッドを確認）。
     - `~<スレッドID>s`: スレッドに切り替え、`k`でスタックトレース表示。
     - `!analyze -v`: ハング/デッドロックの自動分析。
   - Java特有の分析: ダンプをEclipse MATに読み込む、またはヒープダンプ（`-mh`フラグ付きで取得）に対して`jhat`を使用。

ProcDumpは非対話型プロセス（サービスなど）に有効。CPU負荷型ハングの場合は`-c`で高CPU使用率時にトリガー。

### 両ツールの一般的なヒント
- **安全性:** ダンプは大容量（完全メモリでGB単位）の可能性あり。十分なディスク空きを確保。
- **ツールの併用:** Windows上のJavaでは、軽量なjstackを最初に使用し、深いOSレベルの洞察にはProcDumpを併用。
- **予防策:** ログ取得のため`-XX:+PrintGCDetails`などのJVMフラグを有効化、またはJFRなどのプロファイリングエージェントを使用。
- ダンプで明確な問題が確認できない場合、`top`やパフォーマンスモニターなどのツールでシステムリソース（CPU、メモリ、I/O）を確認。

[Oracle Javaトラブルシューティングガイド](https://docs.oracle.com/en/java/javase/17/troubleshoot/troubleshoot-process-hangs-and-loops.html)  
[ProcDumpを使用したハングダンプの取得](https://www.poppastring.com/blog/taking-a-hang-dump-or-crash-dump-with-procdump)  
[Javaスレッドダンプ分析](https://www.baeldung.com/java-analyze-thread-dumps)  
[ハング向けProcDump使用方法](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)