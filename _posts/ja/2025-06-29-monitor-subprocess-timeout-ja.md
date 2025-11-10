---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: タイムアウト付きサブプロセス出力監視
translated: true
type: note
---

```python
import subprocess
import threading
import queue
import time
import sys

def read_output(proc, output_queue):
    """スレッド関数：stdoutとstderrを読み取り、キューに投入する"""
    try:
        for line in iter(proc.stdout.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
        # 必要に応じてstderrもチェック
        for line in iter(proc.stderr.readline, b''):
            if not line:
                break
            output_queue.put(line.decode('utf-8', errors='ignore').rstrip())
    except Exception as e:
        output_queue.put(f"出力読み取りエラー: {e}")

def main():
    # 実行するコマンド（例：Windowsでの'mvn clean compile'）
    cmd = ['mvn', 'clean', 'compile']  # 必要に応じて調整（例：['cmd', '/c', 'mvn build']）
    timeout_seconds = 10

    # サブプロセスを開始
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,  # 行バッファリング
        universal_newlines=False,  # バイト列を処理
        cwd=None  # 必要に応じて作業ディレクトリを設定
    )

    # 出力用キュー
    output_queue = queue.Queue()

    # 出力読み取りスレッドを開始
    output_thread = threading.Thread(target=read_output, args=(proc, output_queue))
    output_thread.daemon = True
    output_thread.start()

    print("コマンドを開始しました。10秒ごとに出力を監視中...")

    while proc.poll() is None:
        try:
            # タイムアウト付きで出力を待機
            output = output_queue.get(timeout=timeout_seconds)
            print(f"出力: {output}")  # オプション：出力を表示または処理
        except queue.Empty:
            print(f"{timeout_seconds}秒間出力がありません。コマンドを終了して終了します。")
            proc.terminate()  # 強制終了の場合はproc.kill()
            try:
                proc.wait(timeout=5)  # 正常なシャットダウンのために少し待機
            except subprocess.TimeoutExpired:
                proc.kill()
            sys.exit(1)

    # プロセスが正常に終了
    print("コマンドが完了しました。")
    output_thread.join()  # 出力スレッドの終了を待機

if __name__ == "__main__":
    main()
```

### 説明
- **サブプロセス**: `subprocess.Popen`を使用して`mvn clean compile`を実行（コマンドは必要に応じて調整。単純な`mvn build`の場合は`['mvn', 'build']`、または必要に応じて`cmd /c`でラップ）。stdoutとstderr用のパイプで非同期に実行されます。
- **キューとスレッド**: 別スレッドがstdoutとstderrから行ごとに読み取り（一度にすべての出力を読み取らないように）、デコードして行を`queue.Queue`に投入します。これにより非ブロッキング読み取りが可能になります。
- **タイムアウト監視**: メインスレッドで`get(timeout=10)`を使用してキュー内の新しい出力をチェックします。10秒間出力が到着しない場合、サブプロセスを終了して終了します。
- **Windows互換性**: `subprocess`はWindowsで動作します。コマンドがシェルを必要とする場合（例：PATHに`mvn`がない場合）、`shell=True`を設定し、コマンドを文字列として渡すことができます：`proc = subprocess.Popen("mvn clean compile", shell=True, ...)`
- **エッジケース**: 待機中にプロセスが正常終了した場合、ループが停止し、スレッドを結合します。スレッドは終了時のハングを避けるためにデーモン化されています。
- **カスタマイズ**: 出力を異なる方法で処理するように変更可能（例：印刷の代わりにファイルにログ記録）。stderrの場合、同じキューに結合されています。必要に応じて分離できます。出力がバイナリの場合はデコードを調整してください。