---
audio: false
generated: true
lang: hant
layout: post
title: 升級Guice以修復不安全警告
translated: true
type: note
---

你看到的警告：

```
WARNING: A terminally deprecated method in sun.misc.Unsafe has been called
WARNING: sun.misc.Unsafe::staticFieldBase has been called by com.google.inject.internal.aop.HiddenClassDefiner (file:/opt/homebrew/Cellar/maven/3.9.10/libexec/lib/guice-5.1.0-classes.jar)
WARNING: Please consider reporting this to the maintainers of class com.google.inject.internal.aop.HiddenClassDefiner
WARNING: sun.misc.Unsafe::staticFieldBase will be removed in a future release
```

這是**來自 Java 虛擬機（JVM）的警告**，並非直接來自你的程式碼。這表示你正在使用的函式庫（此處為 Guice，具體是 `guice-5.1.0-classes.jar`）內部正在呼叫 `sun.misc.Unsafe` 中的一個方法（`staticFieldBase`）。

`sun.misc.Unsafe` 是 Java 中的內部 API，專為 JDK 本身的低階操作而設計。它不屬於標準 Java API，不鼓勵使用，因為它可能導致不穩定或未定義的行為，並且在未來的 Java 版本中可能會變更或移除。JVM 正在提醒你，這個特定方法已被「終極棄用」並將被移除，這意味著如果該函式庫在沒有替代方案的情況下繼續使用它，最終將導致你的應用程式崩潰。

**如何「移除」此警告：**

你無法透過更改程式碼直接「移除」它，因為使用行為發生在第三方函式庫（Guice）內部。以下是你可以採取的措施，按優先順序排列：

1.  **升級 Guice（最推薦）：**
    最好且最可持續的解決方案是升級到不再使用 `sun.misc.Unsafe` 或已遷移到標準 Java API（例如 JDK 9 引入的 `VarHandle` 或 JDK 22 標準化的 Foreign Function & Memory API (JEP 454)）的較新版本 Guice。

    查看版本 `guice-5.1.0-classes.jar`，似乎你正在使用 Guice 5.1.0。請檢查官方 Guice 版本及其文件，尋找專門針對較新 Java 版本中 `sun.misc.Unsafe` 使用問題的更新。通常，函式庫維護者會意識到這些棄用情況並提供更新版本。

      * **行動：** 修改你的 `pom.xml` 以使用較新的 Guice 版本。你需要找到與你的 Java 版本（你的情況是 JDK 21）相容的最新穩定版 Guice。

    ```xml
    <dependency>
        <groupId>com.google.inject</groupId>
        <artifactId>guice</artifactId>
        <version>LATEST_GUICE_VERSION</version> </dependency>
    ```

    如果你的專案使用了 `guice-assistedinject` 或其他 Guice 模組，你可能也需要包含它們。

2.  **抑制警告（臨時解決方案 - 不建議長期使用）：**
    雖然你不應長期依賴此方法，但如果警告純屬表面問題且*目前*不影響應用程式功能，你可以在執行時抑制該警告。這透過 JVM 命令列參數實現。

    對於 JDK 24（你目前的目標是 21，但隨著 Java 發展，了解這一點很好），預設是 `warn`。要抑制它，你可以明確將其設定為 `allow`：

    你可以將此添加到你的 `exec-maven-plugin` 配置中：

    ```xml
    <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.0</version>
        <configuration>
            <executable>bash</executable>
            <arguments>
                <argument>-c</argument>
                <argument>java --add-opens java.base/sun.misc=ALL-UNNAMED --sun-misc-unsafe-memory-access=allow -cp ${project.build.directory}/classes com.lzw.solutions.uva.${problem}.Main &lt; src/main/resources/uva/${problem}/1.in</argument>
            </arguments>
        </configuration>
    </plugin>
    ```

    *自我修正：* 主要警告是關於 `sun.misc.Unsafe::staticFieldBase` 被「終極棄用」，而不是關於非法反射存取。因此，除非你還收到「Illegal reflective access」警告，否則 `--add-opens java.base/sun.misc=ALL-UNNAMED` 在這裡可能不是必需的。對於「終極棄用」警告，更直接的標誌是 `--sun-misc-unsafe-memory-access=allow`。

    **然而，這是一個臨時修復。** 此標誌僅告訴 JVM 允許使用 `sun.misc.Unsafe` 方法而不列印警告。它*並未*解決 `sun.misc.Unsafe` 最終將被移除的根本問題，你的應用程式在未來的 JDK 版本中可能會崩潰。

3.  **向 Guice 維護者報告（警告本身已建議）：**
    警告本身建議「請考慮向 `com.google.inject.internal.aop.HiddenClassDefiner` 類別的維護者報告此問題」。雖然你使用的是特定版本，但如果你能確認此問題在最新的 Guice 版本中仍然存在（按理說不應該，因為它們通常會解決這些問題），向他們報告將對社群有益。

**總之，最佳做法是升級你的 Guice 相依項目。** `sun.misc.Unsafe` API 是一個不斷變化的目標，函式庫需要適應 Java 提供的更新、更安全且官方支援的 API。