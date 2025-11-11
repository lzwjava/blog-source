---
audio: false
generated: true
lang: hant
layout: post
title: WebSphere Liberty 中缺失的 JAR 檔案
translated: true
type: note
---

在 WebSphere Liberty 中，您可能會在 `console.log` 檔案中看到類似這樣的警告訊息：*"the manifest class path: grpc-protobuf.jar cannot be found in jar file ..ear/war or its parent"*。這些警告表示伺服器無法找到 `grpc-protobuf.jar` 檔案，該檔案在您應用程式的 EAR 或 WAR 檔案的 manifest class path 中被引用。以下將解答您的疑問：這些警告是否重要、是否會影響應用程式的運行，以及如何消除它們。

---

### 這些警告是否重要？

視情況而定，取決於遺失的 JAR 檔案是否為應用程式所必需：

- **若 JAR 檔案是必需的：**  
  如果 `grpc-protobuf.jar` 包含您的應用程式在運行時所需的類別或資源，那麼這個警告就非常重要。沒有這個 JAR 檔案，您的應用程式可能會遇到運行時錯誤，例如 `ClassNotFoundException`，這可能導致部分功能失效或行為異常。

- **若 JAR 檔案並非必需：**  
  如果該 JAR 檔案實際上並不需要——可能是舊配置遺留的引用，或是可選的依賴項——那麼這個警告是無害的，不會影響應用程式的功能。但它仍會使日誌檔案變得雜亂。

總之，如果遺失的 JAR 檔案對您的應用程式至關重要，這些警告就值得關注。您需要進一步調查以確定其重要性。

---

### 是否會影響應用程式的運行？

對應用程式運行時的影響取決於遺失 JAR 檔案的作用：

- **會影響，若 JAR 檔案是必需的：**  
  如果您的應用程式嘗試使用 `grpc-protobuf.jar` 中的類別或資源，而該檔案遺失，您很可能會看到運行時錯誤。這可能導致應用程式無法正常運作或完全失敗。

- **不會影響，若 JAR 檔案非必需：**  
  如果該 JAR 檔案不需要，您的應用程式將正常運行，儘管有警告訊息。該訊息僅會作為干擾留在日誌中。

為確認情況，請檢查應用程式的行為和日誌，尋找除了該警告之外的錯誤。如果一切運作正常，該 JAR 檔案可能並非必需。

---

### 如何消除警告？

要消除警告，您需要確保 JAR 檔案正確包含在應用程式中，或移除不必要的引用。以下是逐步方法：

1. **確認 JAR 檔案是否必需：**  
   - 檢查應用程式的文件、原始碼或依賴項列表（例如，若使用 Maven 則檢查 `pom.xml`），以確定 `grpc-protobuf.jar` 是否為必需。  
   - 如果不需要，請繼續步驟 3 以移除引用。如果需要，請繼續步驟 2。

2. **修正打包配置（若 JAR 檔案是必需的）：**  
   - 確保 `grpc-protobuf.jar` 包含在應用程式套件中的正確位置：  
     - **對於 WAR 檔案：** 將其置於 `WEB-INF/lib` 目錄中。  
     - **對於 EAR 檔案：** 將其置於 EAR 的根目錄或指定的函式庫目錄（例如 `lib/`）。  
   - 重新建置並重新部署應用程式，以確認 WebSphere Liberty 現在可以找到該 JAR 檔案。  
   - 檢查 `console.log` 以確認警告是否消失。

3. **更新 Manifest（若 JAR 檔案非必需）：**  
   - 開啟您的 EAR 或 WAR 中的 `MANIFEST.MF` 檔案，該檔案位於 `META-INF/` 目錄中。  
   - 尋找 `Class-Path` 屬性，其內容可能類似：  
     ```
     Class-Path: grpc-protobuf.jar some-other-lib.jar
     ```  
   - 移除對 `grpc-protobuf.jar` 的引用，使其不再出現在列表中。  
   - 儲存檔案，重新建置應用程式並重新部署。警告應不再出現。

4. **檢查 Classpath 配置：**  
   - 如果您的應用程式在 WebSphere Liberty 中使用共享函式庫或自訂類別載入器，請確認伺服器的配置（例如 `server.xml`）包含必要的 JAR 檔案，或沒有錯誤地引用 `grpc-protobuf.jar`。  
   - 如有需要，調整配置並重新啟動伺服器。

---

### 一般建議

- **調查警告：** 即使應用程式似乎運行正常，了解警告的原因以避免日後出現意外情況是良好的做法。  
- **變更後測試：** 在添加 JAR 檔案或更新 manifest 後，徹底測試您的應用程式以確保其行為符合預期。  
- **保持日誌整潔：** 解決不必要的警告可以使日誌保持清晰，便於未來發現真正的問題。

透過遵循這些步驟，您可以確定 `grpc-protobuf.jar` 警告是否關鍵，解決任何潛在的運行時影響，並從 WebSphere Liberty 的 `console.log` 中移除該警告。

---

當您執行 `mvn package` 來建置 EAR 檔案並遇到有關 manifest class path 中遺失 JAR 檔案（如 `grpc-protobuf.jar`）的警告時，問題不太可能來自遺失的命令列參數。`mvn package` 命令本身足以觸發 Maven 建置生命週期直至 `package` 階段，該階段包括編譯、測試和打包您的 EAR。然而，該警告表明您的 Maven 專案存在配置問題，而非命令或其參數的問題。讓我們逐步探討這個問題。

---

### 警告的含義是什麼？

該警告表示您的 EAR 中的 `MANIFEST.MF` 檔案在其 `Class-Path` 屬性中引用了 `grpc-protobuf.jar`，但該 JAR 檔案在 EAR 內的預期位置（例如 `lib/` 目錄）中找不到。`Class-Path` 屬性列出了您的應用程式在運行時所需的 JAR 檔案，遺失 JAR 檔案可能導致運行時錯誤，例如 `ClassNotFoundException`。

---

### 是否與遺失參數有關？

不，您不需要為 `mvn package` 添加額外參數來解決此問題。Maven 依賴您的專案的 `pom.xml` 檔案和外掛配置（例如 `maven-ear-plugin`）來確定 EAR 中包含的內容以及如何產生 manifest。添加參數如 `-DskipTests` 或 `-U` 可能會調整建置過程，但它們不會直接解決此警告。根本原因在於您的專案設置，而非命令本身。

---

### 警告的常見原因

以下是導致警告的可能原因：

1. **遺失依賴項宣告**  
   如果 `grpc-protobuf.jar` 是您的應用程式所必需的，它可能未在您的 EAR 模組的 `pom.xml` 或其子模組（例如 WAR 或 JAR 模組）中宣告為依賴項。

2. **錯誤的依賴項範圍**  
   如果 `grpc-protobuf.jar` 以 `provided` 等範圍宣告，Maven 會假設它由運行時環境（例如 WebSphere Liberty）提供，因此不會將其打包到 EAR 中。

3. **不必要的 Manifest 條目**  
   `maven-ear-plugin` 可能被配置為將 `grpc-protobuf.jar` 添加到 manifest 的 `Class-Path` 中，即使它未包含在 EAR 中。

4. **傳遞依賴項問題**  
   該 JAR 檔案可能是一個傳遞依賴項（另一個依賴項的依賴項），該依賴項要么被排除，要么未正確包含在 EAR 中。

---

### 如何調查

要找出問題，請嘗試以下步驟：

1. **檢查 Manifest 檔案**  
   執行 `mvn package` 後，解壓縮產生的 EAR 並查看 `META-INF/MANIFEST.MF`。檢查 `grpc-protobuf.jar` 是否列在 `Class-Path` 中。這可以確認警告是否與 manifest 的內容相符。

2. **檢視 EAR 的 `pom.xml`**  
   查看 `maven-ear-plugin` 配置。例如：
   ```xml
   <plugin>
       <groupId>org.apache.maven.plugins</groupId>
       <artifactId>maven-ear-plugin</artifactId>
       <version>3.2.0</version>
       <configuration>
           <version>7</version> <!-- 符合您的 Java EE 版本 -->
           <defaultLibBundleDir>lib</defaultLibBundleDir>
       </configuration>
   </plugin>
   ```
   確保其設置為將依賴項包含在 `lib/` 目錄（或您的 JAR 檔案應放置的位置）中。

3. **檢查依賴項**  
   在您的 EAR 模組上執行 `mvn dependency:tree`，查看 `grpc-protobuf.jar` 是否出現。如果它遺失了，表示它在您的依賴項樹中的任何地方都未宣告。

4. **查看子模組**  
   如果您的 EAR 包含 WAR 或 JAR，請檢查它們的 `pom.xml` 檔案是否對 `grpc-protobuf.jar` 有依賴項。

---

### 如何修復

根據您的發現，應用以下解決方案之一：

1. **若 JAR 檔案是必需的**  
   在您的 EAR 的 `pom.xml` 中添加 `grpc-protobuf.jar` 作為依賴項：
   ```xml
   <dependency>
       <groupId>io.grpc</groupId>
       <artifactId>grpc-protobuf</artifactId>
       <version>1.39.0</version> <!-- 使用正確版本 -->
   </dependency>
   ```
   確保 `maven-ear-plugin` 將其包含在 EAR 中（例如在 `lib/` 目錄中）。

2. **若範圍錯誤**  
   如果它被宣告為 `<scope>provided</scope>` 但需要被打包，請將其更改為 `<scope>compile</scope>`（預設範圍）。

3. **若 JAR 檔案非必需**  
   如果 `grpc-protobuf.jar` 不應在 manifest 中，請檢查 `maven-ear-plugin` 中的自訂 manifest 配置：
   ```xml
   <configuration>
       <manifestFile>META-INF/MANIFEST.MF</manifestFile>
   </configuration>
   ```
   移除任何對 `grpc-protobuf.jar` 的手動條目，或讓 Maven 自動產生 manifest。

4. **處理傳遞依賴項**  
   如果它是您不需要的傳遞依賴項，請排除它：
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

5. **重新建置並驗證**  
   執行 `mvn clean package` 以重新建置 EAR，然後檢查輸出的 EAR 檔案以確保警告消失且結構正確。

---

### 結論

`mvn package` 命令本身不需要額外參數來修復此警告。相反，問題很可能是由於您的 `pom.xml` 或 `maven-ear-plugin` 的配置錯誤所致。通過確保 `grpc-protobuf.jar` 要么被正確包含（如果需要），要么從 manifest 中移除（如果不需要），您可以消除警告。首先檢查您的 manifest 和依賴項，然後相應地調整配置。這應該可以解決問題，而無需更改您的建置命令。