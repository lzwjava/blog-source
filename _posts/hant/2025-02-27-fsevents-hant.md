---
audio: false
generated: true
lang: hant
layout: post
title: 使用 FSEvents API 監控目錄變更
translated: true
type: note
---

我當時正在使用 Jekyll 部落格，當執行 `bundle exec jekyll serve --incremental` 時，終端機顯示了 `fsevent_watch`。因此，我向 AI 詢問了相關資訊。

---

您可能指的是 `fsevent_watch`，但這在大多數程式設計情境中並非標準的獨立工具或函式。根據您的提問與常見慣例，我假設您是想了解如何在 macOS 上使用 **FSEvents API** 來監控檔案系統事件——或許您實際想問的是類似 `fsevents` 或相關工具。若我的理解有誤，請進一步說明！

FSEvents API 是 macOS 專用的框架，允許應用程式接收目錄樹變更的通知。它常用於 C、Objective-C 或 Swift 程式設計中，用來監控檔案系統事件，例如檔案的建立、刪除或修改。由於 `fsevent_watch` 並非公認的命令或函式（可能是拼寫錯誤或第三方工具），我將直接解釋如何使用 FSEvents API，這很可能就是您需要的內容。

以下是用 FSEvents 監控目錄的實用指南：

### 在 C/Objective-C 中使用 FSEvents
FSEvents API 屬於 macOS 的 CoreServices 框架。以下是一個用 C 語言監控目錄變更的基本範例：

1. **引入必要標頭檔**：
   您需要從 CoreServices 框架引入 FSEvents 標頭檔。

2. **設定事件串流**：
   建立事件串流來監控特定目錄，定義處理事件的回呼函式，並將其排程到執行循環中。

3. **處理事件**：
   回呼函式會處理事件（例如檔案變更、刪除），並提供路徑和標誌資訊。

以下是一個簡易範例：

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// 處理檔案系統事件的回呼函式
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
        printf("偵測到變更於：%s (標誌：0x%x)\n", paths[i], eventFlags[i]);
    }
}

int main() {
    // 要監控的路徑（例如您的使用者目錄）
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // 建立事件串流
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // 分配器
        &callback,      // 回呼函式
        NULL,           // 回呼資訊（上下文）
        pathsToWatch,   // 要監控的路徑
        kFSEventStreamEventIdSinceNow, // 從現在開始追蹤事件
        1.0,            // 延遲時間（秒）（批次處理延遲）
        kFSEventStreamCreateFlagNone // 標誌（可使用 kFSEventStreamCreateFlagFileEvents 來啟用檔案層級事件）
    );

    // 將串流排程到當前執行循環
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // 啟動串流
    FSEventStreamStart(stream);

    // 執行循環以監聽事件
    printf("正在監控 /Users/yourusername... 按 Ctrl+C 停止。\n");
    CFRunLoopRun();

    // 清理（在此無限循環範例中不會執行到）
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### 步驟說明：
- **監控路徑**：您在 `CFArray` 中指定一個或多個目錄（例如 `/Users/yourusername`）。
- **回呼函式**：當變更發生時，會觸發 `callback` 函式。它會接收受影響的路徑陣列和標誌（例如 `kFSEventStreamEventFlagItemCreated`）。
- **串流建立**：`FSEventStreamCreate` 設定監控器。延遲參數（例如 `1.0` 秒）會將事件批次處理，避免回呼函式被過度觸發。
- **執行循環**：串流與執行循環（如 `CFRunLoopRun`）整合，讓程式保持活動狀態並響應事件。
- **清理**：完成後停止並釋放串流（在此無限循環範例中未示範）。

#### 編譯方法：
使用 CoreServices 框架進行編譯：
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

執行：
```bash
./fsevents_example
```

### 關鍵要點：
- **監控粒度**：預設情況下，FSEvents 監控目錄層級的變更。若要啟用檔案層級事件（例如特定檔案修改），請加入 `kFSEventStreamCreateFlagFileEvents` 標誌。
- **延遲設定**：延遲參數（例如 `1.0`）控制回呼函式的觸發頻率。較低的值會提供更快的更新，但會導致更多呼叫。
- **監控範圍**：FSEvents 會遞迴監控整個目錄樹——無需指定子目錄。

### 替代方案：使用工具
如果您想使用命令列工具而非自行編寫程式，macOS 標準工具集中並沒有 `fsevent_watch`。但第三方工具如 `fswatch` 便是基於 FSEvents 開發的。使用 `fswatch` 的方法如下：

1. **安裝 fswatch**（例如透過 Homebrew）：
   ```bash
   brew install fswatch
   ```

2. **執行**：
   ```bash
   fswatch /path/to/watch
   ```
   這會在變更發生時輸出路徑。例如：
   ```bash
   fswatch ~/Documents
   ```
   當檔案變更時，您會看到類似 `/Users/yourusername/Documents/file.txt` 的輸出。

3. **搭配腳本使用**：
   可將其輸出導向自訂腳本進行處理：
   ```bash
   fswatch ~/Documents | while read -r file; do echo "已變更：$file"; done
   ```

### 若您指的是其他內容
如果 `fsevent_watch` 是指特定的函式庫、工具或拼寫錯誤（例如 `fsevents-watch`），請提供更多上下文資訊——例如您使用的程式語言或環境——我會進一步調整回應內容。

請告訴我如何為您進一步完善說明！