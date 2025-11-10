---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 配置 JaCoCo 代理輸出目錄
translated: true
type: note
---

是的 — 完全正確 👍。

預設情況下，如果您寫入

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

那麼 `jacoco.exec` 會建立在 JVM 程序的**當前工作目錄**中（通常是伺服器根目錄或啟動 Liberty 的位置）。

如果您想控制檔案生成位置，可以指定**絕對路徑或相對路徑**，例如：

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

或

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

（其中 `target/` 是相對於啟動目錄的路徑）。

所以沒錯，如果您想確保 `.exec` 檔案的生成位置，請使用完整路徑。

👉 提示：在 Maven/Gradle 專案中，通常會將其指向 `target/`（Maven）或 `build/`（Gradle）目錄，這樣後續報表外掛就能自動讀取這些檔案。

需要我示範一個配置了完整路徑的 Liberty `jvm.options` 範例嗎？