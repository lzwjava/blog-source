---
audio: false
generated: false
lang: ja
layout: post
title: ディレクトリの変更を監視するFSEvents API
translated: true
---

Jekyllのブログを使用しており、`bundle exec jekyll serve --incremental`を実行すると、ターミナルに`fsevent_watch`が表示されました。そのため、AIに質問しました。

---

おそらく、`fsevent_watch`という名前の標準的な独立したツールや関数はほとんどのプログラミングコンテキストにはありません。質問と一般的な慣習に基づいて、macOSでファイルシステムのイベントを監視するために**FSEvents API**について質問していると仮定します。もし違っていたら、教えてください！

FSEvents APIは、macOS固有のフレームワークで、アプリケーションがディレクトリツリーの変更について通知を受け取ることを可能にします。通常、C、Objective-C、またはSwiftのプログラミングで、ファイルの作成、削除、または変更などのファイルシステムイベントを監視するために使用されます。`fsevent_watch`は認識されるコマンドや関数ではありません（タイポか第三者のツールかもしれません）、FSEvents APIを直接使用する方法を説明します。おそらくこれが求めているものです。

以下は、FSEventsを使用してディレクトリを監視するための実践的なガイドです。

### C/Objective-CでFSEventsを使用する
FSEvents APIは、macOSのCoreServicesフレームワークの一部です。以下は、Cでディレクトリの変更を監視するための基本的な例です。

1. **必要なヘッダーをインクルード**:
   CoreServicesフレームワークからFSEventsヘッダーをインクルードする必要があります。

2. **イベントストリームの設定**:
   特定のディレクトリを監視するためのイベントストリームを作成し、イベントを処理するためのコールバック関数を定義し、ランループでスケジュールします。

3. **イベントの処理**:
   コールバックはイベント（例：ファイルが変更、削除された）を処理し、パスとフラグを提供します。

以下は最小限の例です：

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// ファイルシステムイベントを処理するためのコールバック関数
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
        printf("変更が検出されました: %s (フラグ: 0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // 監視するパス（例：ホームディレクトリ）
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // イベントストリームを作成
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // アロケーター
        &callback,      // コールバック関数
        NULL,           // コールバック情報（コンテキスト）
        pathsToWatch,   // 監視するパス
        kFSEventStreamEventIdSinceNow, // 現在からのイベントで開始
        1.0,            // 遅延（秒単位、バッチング遅延）
        kFSEventStreamCreateFlagNone // フラグ（ファイルレベルのイベントのためにkFSEventStreamCreateFlagFileEventsを使用できます）
    );

    // ストリームを現在のランループでスケジュール
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // ストリームを開始
    FSEventStreamStart(stream);

    // イベントを待ち受けるためにループを実行
    printf("監視中 /Users/yourusername... Ctrl+Cで停止してください。\n");
    CFRunLoopRun();

    // クリーンアップ（この例では停止しない限り到達しない）
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### ステップの説明：
- **監視するパス**: 1つまたは複数のディレクトリ（例：`/Users/yourusername`）を`CFArray`に指定します。
- **コールバック**: `callback`関数は変更が発生したときにトリガーされます。影響を受けたパスとフラグ（例：`kFSEventStreamEventFlagItemCreated`）の配列を受け取ります。
- **ストリームの作成**: `FSEventStreamCreate`はウォッチャーを設定します。遅延（例：`1.0`秒）はイベントをバッチングしてコールバックを圧倒しないようにします。
- **ランループ**: ストリームはランループ（例：`CFRunLoopRun`）と統合され、プログラムが生きていて反応的であるようにします。
- **クリーンアップ**: 終了時にストリームを停止し、解放します（この無限ループの例では表示されません）。

#### コンパイル:
CoreServicesフレームワークでコンパイルします：
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

実行します：
```bash
./fsevents_example
```

### 主要なポイント：
- **粒度**: デフォルトでは、FSEventsはディレクトリレベルの変更を監視します。ファイルレベルのイベント（例：特定のファイルの変更）を監視するには、`kFSEventStreamCreateFlagFileEvents`フラグを追加します。
- **遅延**: 遅延パラメータ（例：`1.0`）はコールバックがトリガーされる頻度を制御します。低い値は更新が速くなりますが、呼び出しが増えます。
- **範囲**: FSEventsはディレクトリツリー全体を再帰的に監視します。サブディレクトリを指定する必要はありません。

### 代替手段: ツールを使用する
標準的なmacOSツールキットには`fsevent_watch`というコマンドラインツールはありませんが、FSEventsを利用する第三者のツールがあります。例えば、`fswatch`を使用するには：

1. **fswatchをインストール**します（例：Homebrewを使用）：
   ```bash
   brew install fswatch
   ```

2. **実行します**：
   ```bash
   fswatch /path/to/watch
   ```
   変更が発生したときにパスを出力します。例えば：
   ```bash
   fswatch ~/Documents
   ```
   ファイルが変更されたときに、以下のような行が表示されます：`/Users/yourusername/Documents/file.txt`。

3. **スクリプトと一緒に使用**：
   カスタムアクションにパイプします：
   ```bash
   fswatch ~/Documents | while read -r file; do echo "変更: $file"; done
   ```

### 別のものを意味していた場合
`fsevent_watch`が特定のライブラリやツール、またはタイポ（例：`fsevents-watch`）を指している場合、さらに詳細なコンテキスト（例：使用しているプログラミング言語や環境）を提供してください。それに基づいて応答を調整します。

さらにどのように改善できますか？