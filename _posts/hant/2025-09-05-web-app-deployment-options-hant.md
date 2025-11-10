---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 網頁應用程式部署方案詳解
translated: true
type: note
---

明白了 — 讓我為你清楚解釋這些選項。

### 選項 1：快速開發設定（推薦）

這是在開發期間啟動專案最簡單的方式。
如果你的 `pom.xml` 包含 Tomcat 或 Jetty 插件，你可以直接執行：

```bash
mvn tomcat7:run
```

或

```bash
mvn jetty:run
```

這會在內嵌的 Tomcat/Jetty 中啟動網頁應用程式，無需構建 WAR 檔案或手動部署。如果你尚未安裝插件，需要先將其添加到 `pom.xml` 中。

---

### 選項 2：構建並部署 WAR

這是較「傳統」的方法。你將應用程式打包成 WAR 檔案：

```bash
mvn clean package
```

這會生成類似 `target/playground-server-1.0.war` 的檔案。
然後將該 WAR 檔案複製到獨立的 Tomcat/Jetty 伺服器的 `webapps/` 資料夾中，重啟伺服器，並在瀏覽器中訪問已部署的應用程式。

---

### 選項 3：使用內嵌伺服器（手動設定）

目前你的 `Application.main()` 僅啟動 Spring 上下文 — 並未實際啟動網頁伺服器。
如果你希望應用程式本身啟動 Tomcat（無需依賴外部伺服器），則需要修改主類別，以程式方式設定並啟動內嵌的 Tomcat 實例。

這會讓你獲得一個自包含的可執行 JAR，但需要額外的設定程式碼。

---

### 選項 4：Spring Boot 遷移

此專案**已有部分 Spring Boot 測試設定**，但尚未成為真正的 Spring Boot 應用程式。這就是為什麼執行：

```bash
mvn spring-boot:run
```

無法運作的原因。

如果你需要，可以進行遷移：

* 添加適當的 Spring Boot starter 依賴項。
* 將主類別更改為 `@SpringBootApplication`。
* 然後你就可以直接使用 `mvn spring-boot:run` 或甚至 `java -jar target/app.jar` 來執行。

這是最現代化的方法，但需要對你的程式碼和 `pom.xml` 進行一些修改。

---

✅ **簡而言之**：

* 如果你只想快速測試 → 使用**選項 1**。
* 如果你要部署到現有伺服器 → 使用**選項 2**。
* 如果你想要無需外部 Tomcat 的自包含應用程式 → 使用**選項 3**。
* 如果你想要長期現代化和簡化 → 使用**選項 4**。

---

需要我為你展示**確切的 `pom.xml` 程式碼片段**（用於選項 1 的 Tomcat/Jetty 插件）嗎？這樣你就可以立即執行 `mvn tomcat7:run` 了。