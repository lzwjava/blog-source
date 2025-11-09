---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: JaCoCo 運行時執行檔案行為
translated: true
type: note
---

當你在 **WebSphere Liberty Profile** 中搭配 **JaCoCo 代理** 以 `exec` 模式運行時，JaCoCo 代理在運行期間**不會修改**原始的 `.exec` 檔案。以下是具體情況：

---

### JaCoCo 在 `exec` 模式下的運作方式
- **目的**：JaCoCo 代理在應用程式運行時收集**程式碼覆蓋率資料**。
- **輸出**：它將覆蓋率資料寫入 `.exec` 檔案（例如 `jacoco.exec`）。
- **檔案行為**：
  - 如果檔案**不存在**，JaCoCo 會創建它。
  - 如果檔案**已存在**，JaCoCo 會**附加**新的覆蓋率資料到其中（不會覆蓋或修改現有資料，除非你明確重置或合併檔案）。
  - 原始的 `.exec` 檔案**不會被改動**到破壞或改變其結構的程度——它只會隨著新資料的增加而增長。

---

### `.exec` 檔案會被修改嗎？
- **會，但僅透過附加資料**：每次使用 JaCoCo 代理運行應用程式時，檔案都會更新新的覆蓋率資訊。
- **無結構性變更**：`.exec` 檔案的格式保持不變；它是一個包含覆蓋率資料的二進位檔案。

---

### 最佳實踐
- **合併或重置**：若想重新開始，請在再次運行應用程式前刪除或重新命名 `.exec` 檔案。
- **合併多次運行**：如需合併多個 `.exec` 檔案，可使用 Maven 中的 `jacoco:merge` 目標或 `org.jacoco.agent.rt.RT` 類別。

---

### Liberty 配置範例
在你的 Liberty `server.env` 或 `jvm.options` 中，可能會看到：
```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/path/to/jacoco.exec,append=true
```
- `append=true` 確保新資料會附加到現有檔案中。

---