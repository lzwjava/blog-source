---
audio: false
generated: true
lang: hant
layout: post
title: 縮排偵測於檢查樣式
translated: true
type: note
---

我明白你在疑惑為什麼 Checkstyle 沒有偵測到你 `logAfter` 方法中 `System.out.println` 語句前缺少的縮排。讓我們一步步分析問題並解決它。

### 為什麼 Checkstyle 沒有偵測到縮排問題？
Checkstyle 使用特定模組來強制執行編碼標準，對於縮排，它依賴 `Indentation` 模組。如果這個模組沒有在你的 Checkstyle 設定中正確配置或包含，它就不會偵測到你程式碼中的縮排錯誤。

這是你目前的程式碼：

```java
package org.lzwjava;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.springframework.stereotype.Component;

@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
    System.out.println("Method executed: " + joinPoint.getSignature());  // 沒有縮排
    }
}
```

在標準的 Java 慣例中，方法內的語句（如 `System.out.println`）應該相對於方法宣告進行縮排。在你的程式碼中，`System.out.println` 這行沒有縮排，如果配置正確，Checkstyle 應該將其標記為錯誤。以下是它未被偵測到的最可能原因：

1. **`Indentation` 模組未包含**在你的 Checkstyle 設定檔中（例如 `checks.xml`）。
2. **模組已包含但配置錯誤**，因此它沒有強制執行預期的縮排規則。
3. **你的設定排除了某些檔案或套件**，導致檢查無法在此程式碼上執行。
4. **執行 Checkstyle 的方式有問題**（例如透過 Maven 或 IDE），覆蓋了預期的行為。

讓我們處理這些可能性並使其正常運作。

---

### 步驟 1：驗證你的設定中的 `Indentation` 模組
首先，檢查你的 Checkstyle 設定檔（可能是 `checks.xml`），看看是否包含了 `Indentation` 模組。方法如下：

1. **找到你的 `checks.xml` 檔案**。它通常在你的專案目錄中（例如，如果你使用類似設定，可能在 `/home/lzw/Projects/blog-server/checks.xml`）。
2. **在 `TreeWalker` 區段中尋找 `Indentation` 模組**。它應該看起來像這樣：

   ```xml
   <module name="TreeWalker">
       <!-- 其他檢查 -->
       <module name="Indentation">
           <property name="basicOffset" value="4"/>  <!-- 每個縮排層級 4 個空格 -->
           <property name="lineWrappingIndentation" value="4"/>  <!-- 可選：用於換行的行 -->
       </module>
       <!-- 其他檢查 -->
   </module>
   ```

   - **如果你沒有看到這個模組**，那就是問題所在——Checkstyle 根本沒有檢查縮排。
   - **如果它存在**，請檢查 `basicOffset` 是否設定為合理的值（例如 4 個空格，這是 Java 的標準）。

---

### 步驟 2：新增或修正 `Indentation` 模組
如果模組缺失或設定不正確，以下是修正方法：

#### 如果缺失：新增 `Indentation` 模組
在你的 `checks.xml` 的 `TreeWalker` 區段內新增以下內容：

```xml
<module name="Indentation">
    <property name="basicOffset" value="4"/>  <!-- 4 個空格是典型的 -->
    <property name="lineWrappingIndentation" value="4"/>
</module>
```

#### 如果存在：驗證設定
確保：
- `basicOffset` 設定為你期望的縮排空格數（例如 4）。
- 沒有屬性以某種方式停用或覆蓋檢查，從而跳過你的程式碼。

進行更改後儲存檔案。

---

### 步驟 3：檢查排除項目
有時，Checkstyle 設定會排除某些檔案或套件。在你的 `checks.xml` 中，尋找：
- 可能跳過 `org.lzwjava` 套件或此特定檔案的 `SuppressionFilter` 或 `SuppressionCommentFilter`。
- 任何排除 `.java` 檔案或特定目錄的模式。

如果你找到影響你程式碼的此類排除項目，請移除或調整它，以便檢查 `DebugAspect.java`。

---

### 步驟 4：測試修正
更新你的設定後，再次執行 Checkstyle。例如，如果你使用 Maven：

```bash
mvn clean checkstyle:check
```

檢查輸出。你應該會看到類似這樣的錯誤：

```
[ERROR] DebugAspect.java:13: 'System.out.println' 應相對於其封閉區塊縮排 +4 個空格。
```

這表示 Checkstyle 現在偵測到了缺少的縮排。作為參考，以下是你的程式碼*應該*具有正確縮排的樣子：

```java
@Aspect
@Component
public class DebugAspect {
    @After("execution(* org.lzwjava..*(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());  // 4 個空格縮排
    }
}
```

---

### 步驟 5：如果仍然無效，進行疑難排解
如果 Checkstyle 仍然沒有標記出問題：
- **使用除錯輸出執行**：使用詳細指令來查看 Checkstyle 正在做什麼：
  ```bash
  mvn -X checkstyle:check
  ```
  尋找關於 `Indentation` 模組或跳過檔案的訊息。
- **使用最小設定測試**：建立一個臨時的 `checks.xml`，僅包含 `Indentation` 檢查：
  ```xml
  <?xml version="1.0"?>
  <!DOCTYPE module PUBLIC
      "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
      "https://checkstyle.org/dtds/configuration_1_3.dtd">
  <module name="Checker">
      <module name="TreeWalker">
          <module name="Indentation">
              <property name="basicOffset" value="4"/>
          </module>
      </module>
  </module>
  ```
  將 Checkstyle 指向此檔案並再次測試以隔離問題。
- **檢查你的設定**：如果你透過 IDE（如 IntelliJ 或 Eclipse）執行 Checkstyle，請確保 IDE 使用的是更新後的 `checks.xml`，而不是舊的或單獨的配置。

---

### 結論
Checkstyle 沒有偵測到缺少的縮排，可能是因為 `Indentation` 模組在你的 `checks.xml` 中缺失或配置錯誤。透過新增或修正此模組並確保沒有適用的排除項目，Checkstyle 應該會標記出 `System.out.println` 前缺少的縮排。按照所示更新你的配置，重新執行 Checkstyle，你應該會看到預期的錯誤報告。如果你需要後續步驟的幫助，請告訴我！