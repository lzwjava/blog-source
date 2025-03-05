---
audio: false
generated: true
lang: hant
layout: post
title: 缺失的 JAR 文件在 WebSphere Liberty
translated: true
---

在 WebSphere Liberty 中，你可能會在 `console.log` 文件中看到類似以下的警告：*"the manifest class path: grpc-protobuf.jar cannot be found in jar file ..ear/war or its parent"*。這些警告表示伺服器無法找到 `grpc-protobuf.jar` 文件，該文件在應用程序的 EAR 或 WAR 文件的清單類路徑中被引用。以下，我將回答你的問題：這些警告是否重要，是否會影響應用程序的運行，以及如何移除它們。

---

### 這些警告重要嗎？

是和否——這取決於缺失的 JAR 是否被你的應用程序所需：

- **如果 JAR 是必要的：**
  如果 `grpc-protobuf.jar` 包含應用程序在運行時需要的類或資源，這個警告是重要的。沒有這個 JAR，你的應用程序可能會遇到運行時錯誤，如 `ClassNotFoundException`，這可能會導致部分應用程序失敗或行為不正常。

- **如果 JAR 不需要：**
  如果 JAR 實際上不需要——可能是舊配置的遺留引用或可選依賴——這個警告是無害的，不會影響應用程序的功能。然而，它仍然會使你的日誌變得混亂。

總之，這些警告在缺失的 JAR 對應用程序至關重要時才重要。你需要調查以確定其重要性。

---

### 這會影響應用程序的運行嗎？

應用程序運行時的影響取決於缺失的 JAR 的角色：

- **是的，如果 JAR 是必要的：**
  如果你的應用程序嘗試使用 `grpc-protobuf.jar` 中的類或資源，並且它缺失，你可能會看到運行時錯誤。這可能會阻止應用程序正常工作或導致它完全失敗。

- **否，如果 JAR 是不必要的：**
  如果 JAR 不需要，你的應用程序會在警告之外正常運行。消息將僅在日誌中作為一個煩惱。

要確認，檢查應用程序的行為和日誌，查找超出警告本身的錯誤。如果一切都按預期運行，JAR 可能不重要。

---

### 如何移除警告？

要消除警告，你需要確保 JAR 正確包含在應用程序中，或者移除對它的不必要引用。以下是逐步方法：

1. **驗證 JAR 是否需要：**
   - 審查應用程序的文檔、源代碼或依賴列表（例如，如果使用 Maven，則為 `pom.xml`），以確定 `grpc-protobuf.jar` 是否需要。
   - 如果它不需要，繼續到步驟 3 移除引用。如果需要，繼續到步驟 2。

2. **更正打包（如果 JAR 是需要的）：**
   - 確保 `grpc-protobuf.jar` 包含在應用程序包的正確位置：
     - **對於 WAR 文件：** 將其放在 `WEB-INF/lib` 目錄中。
     - **對於 EAR 文件：** 將其放在 EAR 的根目錄或指定的庫目錄（例如，`lib/`）。
   - 重新構建並重新部署應用程序，以確認 WebSphere Liberty 現在找到 JAR。
   - 檢查 `console.log` 以查看警告是否消失。

3. **更新清單（如果 JAR 不需要）：**
   - 打開 EAR 或 WAR 中的 `MANIFEST.MF` 文件，位於 `META-INF/` 目錄中。
   - 查找 `Class-Path` 屬性，可能看起來像這樣：
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```
   - 移除對 `grpc-protobuf.jar` 的引用，使其不再出現在列表中。
   - 保存文件，重新構建應用程序並重新部署它。警告不應再出現。

4. **檢查類路徑配置：**
   - 如果你的應用程序使用 WebSphere Liberty 中的共享庫或自定義類加載器，請驗證伺服器的配置（例如，`server.xml`）是否包含必要的 JAR 或不正確地引用 `grpc-protobuf.jar`。
   - 根據需要調整配置並重新啟動伺服器。

---

### 一般建議

- **調查警告：** 即使應用程序似乎運行正常，了解警告的原因也是一個好習慣，以避免未來的驚訝。
- **更改後測試：** 在添加 JAR 或更新清單後，彻底測試應用程序，以確保其行為如預期。
- **保持日誌清晰：** 解決不必要的警告可以保持日誌清晰，使未來更容易發現真正的問題。

通過這些步驟，你可以確定 `grpc-protobuf.jar` 警告是否重要，解決任何潛在的運行時影響，並從 WebSphere Liberty 的 `console.log` 中移除警告。

---

當你運行 `mvn package` 來構建 EAR 文件並遇到有關缺失 JAR（如 `grpc-protobuf.jar`）的警告時，清單類路徑，這不太可能是由於缺少命令行參數。`mvn package` 命令本身足以觸發 Maven 构建生命周期，直到 `package` 階段，這包括編譯、測試和打包你的 EAR。然而，警告表明你的 Maven 專案中存在配置問題，而不是命令或其參數的問題。讓我們逐步探討這一點。

---

### 警告的意思是什麼？

警告表示你的 EAR 中的 `MANIFEST.MF` 文件在其 `Class-Path` 屬性中引用了 `grpc-protobuf.jar`，但這個 JAR 沒有在 EAR 中的預期位置（例如，`lib/` 目錄）。`Class-Path` 屬性列出了應用程序在運行時需要的 JAR，缺失的 JAR 可能會導致運行時錯誤，如 `ClassNotFoundException`。

---

### 是否與缺少參數有關？

否，你不需要在 `mvn package` 中添加額外的參數來解決這個問題。Maven 依賴於你的專案的 `pom.xml` 文件和插件配置（例如，`maven-ear-plugin`）來確定什麼將包含在 EAR 中以及如何生成清單。添加像 `-DskipTests` 或 `-U` 這樣的參數可能會改變構建過程，但它們不會直接解決這個警告。根本原因在於你的專案設置，而不是命令本身。

---

### 警告的常見原因

以下是警告的可能原因：

1. **缺少依賴聲明**
   如果 `grpc-protobuf.jar` 由你的應用程序所需，它可能沒有在 EAR 模塊的 `pom.xml` 或其子模塊（例如，WAR 或 JAR 模塊）中聲明為依賴。

2. **不正確的依賴範圍**
   如果 `grpc-protobuf.jar` 以 `provided` 範圍聲明，Maven 假設它由運行時環境（例如，WebSphere Liberty）提供，並不會將其打包到 EAR 中。

3. **不需要的清單條目**
   `maven-ear-plugin` 可能配置為將 `grpc-protobuf.jar` 添加到清單的 `Class-Path` 中，即使它沒有包含在 EAR 中。

4. **傳遞依賴問題**
   JAR 可能是傳遞依賴（另一個依賴的依賴），它可能被排除或沒有正確包含在 EAR 中。

---

### 如何調查

要確定問題，請嘗試以下步驟：

1. **檢查清單文件**
   運行 `mvn package` 後，解壓縮生成的 EAR 並查看 `META-INF/MANIFEST.MF`。檢查 `grpc-protobuf.jar` 是否列在 `Class-Path` 中。這確認了警告是否與清單的內容匹配。

2. **檢查 EAR 的 `pom.xml`**
   查看 `maven-ear-plugin` 的配置。例如：
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-ear-plugin</artifactId>
       <version>3.2.0</version>
       <configuration>
           <version>7</version> <!-- 與你的 Java EE 版本匹配 -->
           <defaultLibBundleDir>lib</defaultLibBundleDir>
       </configuration>
   </plugin>
   ```
   確保它設置為在 `lib/` 目錄（或你的 JAR 應該去的地方）中包含依賴。

3. **檢查依賴**
   在 EAR 模塊上運行 `mvn dependency:tree`，查看 `grpc-protobuf.jar` 是否出現。如果它缺失，它在依賴樹中沒有任何地方聲明。

4. **檢查子模塊**
   如果你的 EAR 包含 WAR 或 JAR，檢查它們的 `pom.xml` 文件，查找對 `grpc-protobuf.jar` 的依賴。

---

### 如何修復它

根據你找到的內容，應用以下解決方案之一：

1. **如果 JAR 是需要的**
   在 EAR 的 `pom.xml` 中添加 `grpc-protobuf.jar` 作為依賴：
   ```xml
   <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-protobuf</artifactId>
       <version>1.39.0</version> <!-- 使用正確的版本 -->
   </dependency>
   ```
   確保 `maven-ear-plugin` 將其包含在 EAR 中（例如，在 `lib/` 目錄中）。

2. **如果範圍是錯誤的**
   如果它以 `<scope>provided</scope>` 聲明但需要打包，將其更改為 `<scope>compile</scope>`（默認範圍）。

3. **如果 JAR 不需要**
   如果 `grpc-protobuf.jar` 不應在清單中，檢查 `maven-ear-plugin` 中的自定義清單配置：
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   移除對 `grpc-protobuf.jar` 的任何手動條目，或者讓 Maven 自動生成清單。

4. **處理傳遞依賴**
   如果它是你不需要的傳遞依賴，排除它：
   ```xml
   <dependency>
       <groupId>some.group</groupId>
       <artifactId>some-artifact</artifactId>
       <exclusions>
           <exclusion>
               <groupId>io.grpc</groupId>
               <artifactId>grpc-protobuf</artifactId>
           </exclusion>
       </exclusions>
   </dependency>
   ```

5. **重新構建並驗證**
   運行 `mvn clean package` 重新構建 EAR，然後檢查輸出 EAR 文件，以確保警告消失並結構正確。

---

### 結論

`mvn package` 命令本身不需要額外的參數來修復這個警告。相反，問題可能是由於 `pom.xml` 或 `maven-ear-plugin` 中的配置錯誤。通過確保 `grpc-protobuf.jar` 要麼正確包含（如果需要），要麼從清單中移除（如果不需要），你可以消除警告。從檢查你的清單和依賴開始，然後根據需要調整你的配置。這應該解決問題，而不需要更改你的構建命令。