---
audio: false
generated: true
lang: zh
layout: post
title: 监控目录变化与FSEvents API
translated: true
---

我使用的是一个 Jekyll 博客，当我运行 `bundle exec jekyll serve --incremental` 时，终端显示了 `fsevent_watch`。因此，我向 AI 询问了这个问题。

---

看起来你可能指的是 `fsevent_watch`，这在大多数编程上下文中并不是一个标准的独立工具或函数。根据你的问题和常见的约定，我假设你在询问如何在 macOS 上使用 **FSEvents API** 来监控文件系统事件——也许你指的是类似 `fsevents` 或相关工具。如果我理解错了，请澄清！

FSEvents API 是一个专门用于 macOS 的框架，允许应用程序接收有关目录树中的更改的通知。它通常用于 C、Objective-C 或 Swift 编程中，用于监控文件系统事件，如文件的创建、删除或修改。由于 `fsevent_watch` 不是一个被识别的命令或函数（可能是拼写错误或第三方工具），我将解释如何直接使用 FSEvents API，这可能是你需要的。

以下是使用 FSEvents 监控目录的实用指南：

### 在 C/Objective-C 中使用 FSEvents
FSEvents API 是 macOS 上 CoreServices 框架的一部分。以下是一个基本的 C 示例，用于监控目录的更改：

1. **包含必要的头文件**：
   你需要从 CoreServices 框架中包含 FSEvents 头文件。

2. **设置事件流**：
   创建一个事件流来监视特定目录，定义一个回调函数来处理事件，并将其与运行循环调度。

3. **处理事件**：
   回调处理事件（例如，文件更改、删除）并提供路径和标志。

以下是一个最小示例：

```c
#include <CoreServices/CoreServices.h>
#include <stdio.h>

// 回调函数处理文件系统事件
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
    // 要监视的路径（例如，你的主目录）
    CFStringRef myPath = CFStringCreateWithCString(NULL, "/Users/yourusername", kCFStringEncodingUTF8);
    CFArrayRef pathsToWatch = CFArrayCreate(NULL, (const void **)&myPath, 1, NULL);

    // 创建事件流
    FSEventStreamRef stream = FSEventStreamCreate(
        NULL,           // 分配器
        &callback,      // 回调函数
        NULL,           // 回调信息（上下文）
        pathsToWatch,   // 要监视的路径
        kFSEventStreamEventIdSinceNow, // 从现在开始的事件
        1.0,            // 延迟（秒）（批处理延迟）
        kFSEventStreamCreateFlagNone // 标志（可以使用 kFSEventStreamCreateFlagFileEvents 进行文件级事件）
    );

    // 将流调度到当前运行循环
    FSEventStreamScheduleWithRunLoop(stream, CFRunLoopGetCurrent(), kCFRunLoopDefaultMode);

    // 启动流
    FSEventStreamStart(stream);

    // 运行循环以监听事件
    printf("Monitoring /Users/yourusername... Press Ctrl+C to stop.\n");
    CFRunLoopRun();

    // 清理（在此示例中不可达，除非停止）
    FSEventStreamStop(stream);
    FSEventStreamInvalidate(stream);
    FSEventStreamRelease(stream);
    CFRelease(pathsToWatch);
    CFRelease(myPath);

    return 0;
}
```

#### 步骤说明：
- **要监视的路径**：你在 `CFArray` 中指定一个或多个目录（例如，`/Users/yourusername`）。
- **回调**：当发生更改时触发 `callback` 函数。它接收受影响的路径数组和标志（例如，`kFSEventStreamEventFlagItemCreated`）。
- **流创建**：`FSEventStreamCreate` 设置监视器。延迟（例如，`1.0` 秒）批处理事件以避免淹没回调。
- **运行循环**：流与运行循环（例如，`CFRunLoopRun`）集成，以保持程序活跃和响应。
- **清理**：完成后停止并释放流（此无限循环示例中未显示）。

#### 编译：
使用 CoreServices 框架编译：
```bash
gcc -o fsevents_example fsevents_example.c -framework CoreServices
```

运行它：
```bash
./fsevents_example
```

### 关键点：
- **粒度**：默认情况下，FSEvents 监控目录级别的更改。对于文件级事件（例如，特定文件的修改），添加 `kFSEventStreamCreateFlagFileEvents` 标志。
- **延迟**：延迟参数（例如，`1.0`）控制回调的触发频率。较低的值提供更快的更新但更多的调用。
- **范围**：FSEvents 递归监控整个目录树——无需指定子目录。

### 替代方案：使用工具
如果你寻找的是命令行工具而不是自己编写代码，标准 macOS 工具包中没有 `fsevent_watch`。然而，第三方工具如 `fswatch` 利用 FSEvents。使用 `fswatch`：

1. **安装 fswatch**（例如，通过 Homebrew）：
   ```bash
   brew install fswatch
   ```

2. **运行它**：
   ```bash
   fswatch /path/to/watch
   ```
   当发生更改时，输出路径。例如：
   ```bash
   fswatch ~/Documents
   ```
   你将看到类似 `/Users/yourusername/Documents/file.txt` 的行，当文件发生更改时。

3. **与脚本一起使用**：
   将其传输到脚本以执行自定义操作：
   ```bash
   fswatch ~/Documents | while read -r file; do echo "Changed: $file"; done
   ```

### 如果你指的是其他内容
如果 `fsevent_watch` 指的是特定的库、工具或拼写错误（例如，`fsevents-watch`），请提供更多上下文——例如你正在使用的编程语言或环境，我将进一步定制回答。

告诉我如何为你改进这个！