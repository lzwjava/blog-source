---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 啟用 Java SSL TLS 除錯
translated: true
type: note
---

### 在 Java 中啟用 SSL/TLS 除錯功能

要啟用 Java 中 SSL/TLS 相關活動（例如握手、憑證驗證、金鑰交換）的詳細記錄功能，您需要使用 JVM 系統屬性 `-Djavax.net.debug`。這會在 Java 應用程式運行時將除錯資訊輸出到控制台（stdout/stderr）。

#### 逐步操作說明

1. **選擇除錯層級**：
   - 使用 `ssl` 取得基本 SSL/TLS 握手細節。
   - 使用 `ssl:handshake` 取得詳細的握手訊息（包括加密套件和憑證）。
   - 使用 `all` 取得全面除錯資訊（包含 SSL 及其他網路協定——請謹慎使用，因為輸出非常冗長）。
   - 常見建議：從 `ssl:handshake:verbose,keymanager:trustmanager` 開始，以獲得針對性的 SSL 資訊。

2. **運行 Java 應用程式時設定屬性**：
   - **命令列執行**（例如透過 `java` 指令）：
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar
     ```
     請將 `your-app.jar` 替換為您的實際應用程式或類別（例如 `com.example.Main`）。

   - **在 IDE 中（例如 IntelliJ IDEA、Eclipse）**：
     - 前往 Run/Debug Configurations。
     - 在 **VM options** 欄位中加入 `-Djavax.net.debug=ssl:handshake`。
     - 運行或除錯該配置。

   - **在建置工具中（例如 Maven 或 Gradle）**：
     - **Maven**（在 `pom.xml` 中的 `<build><plugins><plugin>` 下針對 surefire 設定）：
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle**（在 `build.gradle` 中）：
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **擷取記錄**：
   - 輸出會顯示在您的控制台/終端機中。
   - 可重新導向至檔案以便檢視：
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar > ssl-debug.log 2>&1
     ```
   - 尋找以 `***` 開頭的行（例如 `*** ClientHello` 表示握手開始）或 `javax.net.ssl` 前綴。

4. **停用功能**：
   - 完成後只需移除 `-D` 標記——預設未啟用以避免效能負擔。

#### 輸出片段範例
啟用後，您會看到類似以下內容：
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### 實用提示
- 此功能適用於 Java 8+（包括 11、17、21 版）。在新版本中，您還可啟用 `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` 來取得協定特定記錄。
- 高冗長度可能會拖慢應用程式並淹沒記錄——請在開發環境中測試。
- 若使用 Spring Boot 等框架，可將其加入 `application.properties`：`debug=true`（用於一般除錯）或透過命令列參數設定。

更多詳細資訊，請參閱官方 Oracle 文件：[Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names)。