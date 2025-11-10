---
audio: false
generated: true
lang: hant
layout: post
title: 升級 Maven 依賴項與插件
translated: true
type: note
---

以下是您在 `pom.xml` 中可以升級的版本列表，以及截至 2025 年 7 月 5 日的最新可用版本：

**依賴項：**

* `org.junit.jupiter:junit-jupiter-api`
    * 當前版本：`5.9.2`
    * 最新穩定版：`5.13.2`（發佈於 2025 年 6 月 24 日）
    * 最新預覽版：`6.0.0-M1`（發佈於 2025 年 6 月 27 日）- 可考慮是否使用里程碑版本。
* `org.junit.jupiter:junit-jupiter-engine`
    * 當前版本：`5.9.2`
    * 最新穩定版：`5.13.2`（發佈於 2025 年 6 月 24 日）
    * 最新預覽版：`6.0.0-M1`（發佈於 2025 年 6 月 27 日）- 可考慮是否使用里程碑版本。

**插件：**

* `org.apache.maven.plugins:maven-compiler-plugin`
    * 當前版本：`3.13.0`
    * 最新版本：`3.14.0`（發佈於 2025 年 2 月 17 日）
* `org.apache.maven.plugins:maven-jar-plugin`
    * 當前版本：`3.4.2`
    * 最新版本：`3.4.2`（未找到更新的穩定版本。最後發佈於 2024 年 6 月 16 日，但當前時間為 2025 年 7 月 5 日，因此仍是最新版本）。
* `com.diffplug.spotless:spotless-maven-plugin`
    * 當前版本：`2.44.5`
    * 最新版本：`2.44.5`（未找到更新的穩定版本。最後發佈於 2025 年 5 月 28 日，因此仍是最新版本）。
* `org.apache.maven.plugins:maven-checkstyle-plugin`
    * 當前版本：`3.6.0`
    * 最新版本：`3.6.0`（未找到更新的穩定版本。最後發佈於 2024 年 10 月 22 日，因此仍是最新版本）。
    * **注意：** checkstyle 插件配置內的 `checkstyle` 依賴項可以更新：
        * 當前版本：`10.25.0`
        * 最新版本：`10.26.1`（發佈於 2025 年 6 月 29 日）
* `org.apache.maven.plugins:maven-surefire-plugin`
    * 當前版本：`3.0.0-M7`
    * 最新穩定版：`3.5.3`（發佈於 2025 年 3 月 27 日）- 這是從里程碑版本的重大升級。
* `org.codehaus.mojo:exec-maven-plugin`
    * 當前版本：`3.5.1`
    * 最新版本：`3.5.1`（未找到更新的穩定版本。最後發佈於 2025 年 5 月 27 日，因此仍是最新版本）。

**升級摘要：**

* **JUnit Jupiter API：** 5.9.2 -> 5.13.2（或 6.0.0-M1）
* **JUnit Jupiter Engine：** 5.9.2 -> 5.13.2（或 6.0.0-M1）
* **Maven Compiler Plugin：** 3.13.0 -> 3.14.0
* **Checkstyle（插件內的依賴項）：** 10.25.0 -> 10.26.1
* **Maven Surefire Plugin：** 3.0.0-M7 -> 3.5.3

**升級前的重要注意事項：**

* **重大變更：** 請務必檢查每個計劃升級組件的發行說明。主要版本升級（例如從 JUnit 5 到 6，或 Surefire 從 3.0.0-M7 到 3.5.3）可能會引入需要程式碼修改的重大變更。
* **相容性：** 確保新版本與您的 Java 版本（在您的情況中是 JDK 21）及專案中的其他依賴項相容。
* **測試：** 升級後，請徹底測試您的應用程式，以確保所有功能仍按預期運作。