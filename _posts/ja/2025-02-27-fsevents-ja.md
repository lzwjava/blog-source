---
audio: false
generated: true
lang: ja
layout: post
title: FSEvents APIを使用したディレクトリ変更の監視
translated: true
type: note
---

Jekyllブログを使用していて、`bundle exec jekyll serve --incremental` を実行した際、ターミナルに `fsevent_watch` が表示されました。そのため、AIに質問してみました。

---

おそらく `fsevent_watch` についてお聞きになりたいのでしょうが、これはほとんどのプログラミングコンテキストにおいて標準的なスタンドアロンツールや関数ではありません。ご質問の内容と一般的な慣例から、macOSの **FSEvents API** を使用してファイルシステムイベントを監視する方法についてお尋ねだと推測します。もし誤解していたら、詳しく教えてください！

FSEvents APIは、ディレクトリツリー内の変更についてアプリケーションが通知を受け取ることを可能にする、macOS固有のフレームワークです。ファイル作成、削除、変更などのファイルシステムイベントを監視するために、C、Objective-C、またはSwiftプログラミングで一般的に使用されます。`fsevent_watch` は認識されているコマンドや関数ではないため（タイポまたはサードパーティ製ツールの可能性があります）、本来の目的であろうFSEvents APIを直接使用する方法を説明します。

以下は、ディレクトリを監視するためにFSEventsを使用する実践的なガイドです：

### C/Objective-CでのFSEventsの使用
FSEvents APIは、macOSのCoreServicesフレームワークの一部です。以下は、変更を監視するための基本的なC言語の例です：

1. **必要なヘッダーをインクルード**：
   CoreServicesフレームワークからFSEventsヘッダーをインクルードする必要があります。

2. **イベントストリームの設定**：
   特定のディレクトリを監視するイベントストリームを作成し、イベントを処理するコールバック関数を定義し、実行ループにスケジュールします。

3. **イベントの処理**：
   コールバックはイベント（例：ファイル変更、削除）を処理し、パスとフラグを提供します。

以下は最小限の例です：

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// ファイルシステムイベントを処理するコールバック関数
void callback(
    ConstFSEventStreamRef streamRef,
    void *clientCallBackInfo,
    size_t numEvents,
    void *eventPaths,
    const FSEventStreamEventFlags eventFlags[],
    const FSEventStreamEventId eventIds[])
{
    char **paths = (char **)eventPaths;
    for (size_t i = 0; i < numEvents; i++) {
        printf("Change detected at: %s (Flags: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // 監視するパス（例：ホームディレクトリ）
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // イベントストリームの作成
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // アロケータ
        &callback,      // コールバック関数
        NULL,           // コールバック情報（コンテキスト）
        pathsToWatch,   // 監視するパス
        kFSEventStreamEventIdSinceNow, // 現在からイベントを開始
        1.0,            // 遅延時間（秒単位）（バッチ処理の遅延）
        kFSEventStreamCreateFlagNone // フラグ（ファイルレベルイベントにはkFSEventStreamCreateFlagFileEventsを使用可能）
    );

    // 現在の実行ループにストリームをスケジュール
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // ストリームの開始
    FSEventStreamStart(stream);

    // イベントをリッスンするためにループを実行
    printf("Monitoring /Users/yourusername... Press Ctrl+C to stop.\n");
    CFRunLoopRun();

    // クリーンアップ（この例では停止しない限り到達不能）
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### 手順の説明：
- **監視するパス**：1つ以上のディレクトリ（例：`/Users/yourusername`）を `CFArray` で指定します。
- **コールバック**：変更が発生すると `callback` 関数がトリガーされます。影響を受けたパスとフラグ（例：`kFSEventStreamEventFlagItemCreated`）の配列を受け取ります。
- **ストリーム作成**：`FSEventStreamCreate` はウォッチャーを設定します。遅延時間（例：`1.0` 秒）は、コールバックが過剰に呼び出されないようにイベントをバッチ処理します。
- **実行ループ**：ストリームは実行ループ（`CFRunLoopRun` など）と統合され、プログラムを生き続けさせ応答性を維持します。
- **クリーンアップ**：完了したらストリームを停止して解放します（この無限ループの例では示されていません）。

#### コンパイル：
CoreServicesフレームワークを使用してコンパイルします：
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

実行：
```bash
./fsevents_example
```

### 主なポイント：
- **粒度**：デフォルトでは、FSEventsはディレクトリレベルの変更を監視します。ファイルレベルのイベント（例：特定のファイル変更）には、`kFSEventStreamCreateFlagFileEvents` フラグを追加します。
- **遅延時間**：遅延パラメータ（例：`1.0`）は、コールバックが発生する頻度を制御します。低い値はより速い更新を提供しますが、より多くの呼び出しが発生します。
- **範囲**：FSEventsはディレクトリツリー全体を再帰的に監視します。サブディレクトリを指定する必要はありません。

### 代替案：ツールの使用
自分でコーディングするのではなく、コマンドラインツールを探している場合、標準のmacOSツールキットには `fsevent_watch` はありません。ただし、`fswatch` のようなサードパーティ製ツールはFSEventsを利用しています。`fswatch` を使用するには：

1. **fswatchのインストール**（例：Homebrew経由）：
   ```bash
   brew install fswatch
   ```

2. **実行**：
   ```bash
   fswatch /監視する/パス
   ```
   変更が発生するとパスを出力します。例：
   ```bash
   fswatch ~/Documents
   ```
   ファイルが変更されると、`/Users/yourusername/Documents/file.txt` のような行が表示されます。

3. **スクリプトとの連携**：
   カスタムアクションのためにパイプでスクリプトに渡します：
   ```bash
   fswatch ~/Documents | while read -r file; do echo "Changed: $file"; done
   ```

### もし別のものを意図していた場合
もし `fsevent_watch` が特定のライブラリ、ツール、またはタイポ（例：`fsevents-watch`）を指している場合は、作業中のプログラミング言語や環境などの詳細なコンテキストを提供してください。それに合わせて回答をさらに調整します。

どのように改良すればよいかお知らせください！