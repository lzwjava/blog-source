---
audio: false
generated: true
lang: hant
layout: post
title: Eclipse IDE 建立的專案檔案
translated: true
---

### 為什麼會有 .project 文件，以及 `filteredResources`、`filter` 和 `matcher` 是用來做什麼的？

`.project` 文件存在的目的是儲存開發環境的專案特定設置和配置。具體來說，在您的問題的情境下，它們用來管理資源（文件和文件夾）在專案中的顯示或處理方式。像 `filteredResources`、`filter` 和 `matcher` 這樣的元素是這些配置的一部分，它們在資源過濾中扮演角色——這是一個功能，允許開發者隱藏某些文件或文件夾，例如構建輸出、臨時文件或其他無關資源。這樣可以保持工作區整潔，專注於當前任務所需的文件。

- **`filteredResources`**：這部分在 `.project` 文件中定義了哪些資源（文件或目錄）被從專案視圖中過濾出去。
- **`filter`**：這指定了過濾的規則或條件，例如文件名、模式或類型。
- **`matcher`**：這與 `filter` 一起工作，定義過濾標準如何應用，例如匹配模式或排除。

例如，如果一個專案生成臨時文件（例如 `.class` 文件或日誌），開發者可能會使用這些設置來排除它們，使得在專案資源管理器中更容易導航代碼庫。

### 哪個 IDE 創建這些文件？

**Eclipse IDE** 是主要創建和使用 `.project` 文件的工具，包括 `filteredResources`、`filter` 和 `matcher` 元素。Eclipse 依賴於 `.project` 文件來儲存有關專案的元數據，例如其性質（例如 Java 專案）、構建命令和資源過濾器。當您在 Eclipse 中配置資源過濾器（例如通過專案資源管理器視圖），這些設置會儲存在 `.project` 文件中，以便在會話之間持久化並在每次打開專案時應用。

儘管 Eclipse 是與這種文件格式相關聯的主要 IDE，但像 **Maven** 或 **Gradle** 這樣的工具也可以生成 `.project` 文件。這些構建工具通常創建它們以確保與 Eclipse 兼容，從而允許專案無縫導入。然而，`filteredResources`、`filter` 和 `matcher` 的具體使用與 Eclipse 的資源管理系統有關。

### 摘要

- **目的**：`.project` 文件存在的目的是管理專案設置，而 `filteredResources`、`filter` 和 `matcher` 由 Eclipse 用來從專案視圖中過濾掉不需要的資源。
- **IDE**：Eclipse 本地創建這些文件，儘管像 Maven 或 Gradle 這樣的工具也可能為 Eclipse 兼容性生成它們。

這種設置對於在複雜專案中工作的開發者特別有用，因為這樣可以避免無關文件的混亂，從而減少工作流程的速度。