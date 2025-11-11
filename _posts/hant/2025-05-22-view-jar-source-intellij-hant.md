---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 在 IntelliJ IDEA 中檢視 JAR 原始碼
translated: true
type: note
---

在 IntelliJ IDEA 中，您可以輕鬆檢視 JAR 檔案的原始碼。根據 JAR 是否包含原始檔或僅包含編譯後的 `.class` 檔案，有以下幾種方法：

---

### 1. 在 IDEA 中開啟 JAR

* 前往 **檔案 > 開啟…**
* 選擇 JAR 檔案。
* IDEA 會將其像普通壓縮檔一樣在 **專案檢視** 中開啟。
* 如果 JAR 包含 `.java` 原始檔，您可以直接瀏覽它們。
* 如果僅包含 `.class` 檔案，IDEA 會自動將其反編譯為可讀的 Java 程式碼。

---

### 2. 為程式庫 JAR 附加原始碼

如果 JAR 是程式庫的一部分（例如 Maven 或 Gradle 依賴項）：

* 前往 **檔案 > 專案結構 > 程式庫**（或如果是模組專屬的，則前往 **模組 > 依賴項**）。
* 選擇 JAR。
* 點擊 **附加原始碼…** 並將 IDEA 指向 `-sources.jar`（如果可用）。
* 現在 IDEA 將顯示真實原始碼，而不僅僅是反編譯的位元組碼。

---

### 3. 快速導航

* 按住 **Ctrl（在 macOS 上為 Cmd）** 並點擊來自 JAR 的類別或方法。
* 如果未附加原始碼，IDEA 會顯示反編譯版本。
* 如果已附加原始碼，您將看到原始的 Java 程式碼。

---

### 4. 外部反編譯器外掛（可選）

IDEA 已經內建了反編譯器，但如果您需要替代的反編譯選項，可以安裝 **Fernflower** 或 **CFR** 等外掛。

---

👉 通常，如果是由 Maven/Gradle 管理的依賴項，IDEA 可以自動從儲存庫下載並附加 `-sources.jar`。如果是獨立的 JAR，您需要手動附加原始碼或依賴反編譯器。

您是否還想了解 **如何在 IDEA 外部擷取 JAR 的原始碼**（使用 `jd-gui` 或 `jar xf` 等工具），還是主要希望集中在 IDEA 內操作？