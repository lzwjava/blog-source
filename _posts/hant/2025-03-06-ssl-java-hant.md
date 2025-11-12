---
audio: false
generated: true
lang: hant
layout: post
title: Java 安全連接
translated: true
type: note
---

要在 Java 中使用 `javax.net.ssl` 套件，您需要利用其類別來透過 SSL（安全通訊層）或 TLS（傳輸層安全）協定建立安全的網路通訊。此套件對於建立安全連線（例如 HTTPS 通訊中使用的連線）至關重要。以下我將說明如何在客戶端和伺服器端應用程式中使用它，包括基本範例和關鍵注意事項。

---

### **`javax.net.ssl` 概述**
`javax.net.ssl` 套件提供了安全通訊端通訊的工具。它包括：
- **`SSLSocket`**：用於安全通訊的客戶端通訊端。
- **`SSLServerSocket`**：用於接受安全連線的伺服器端通訊端。
- **`SSLSocketFactory`**：用於建立 `SSLSocket` 實例的工廠。
- **`SSLServerSocketFactory`**：用於建立 `SSLServerSocket` 實例的工廠。
- **`SSLContext`**：用於配置 SSL/TLS 協定的類別，允許自訂安全設定。
- **`KeyManager` 和 `TrustManager`**：用於管理憑證和信任決策的類別。

這些元件實現了客戶端與伺服器之間的加密資料交換，確保了機密性和完整性。

---

### **作為客戶端使用 `javax.net.ssl`**
對於連接到安全伺服器（例如 HTTPS 伺服器）的客戶端應用程式，您通常使用 `SSLSocketFactory` 來建立 `SSLSocket`。方法如下：

#### **步驟**
1. **取得 `SSLSocketFactory`**：
   使用 Java 提供的預設工廠，它依賴系統的預設 SSL/TLS 設定和信任庫（受信任憑證的儲存庫）。

   ```java
   import javax.net.ssl.SSLSocketFactory;
   SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
   ```

2. **建立 `SSLSocket`**：
   使用工廠透過指定主機名稱和連接埠（例如 HTTPS 的 443）連接到伺服器。

   ```java
   import javax.net.ssl.SSLSocket;
   SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
   ```

3. **透過通訊端進行通訊**：
   使用通訊端的輸入和輸出串流來傳送和接收資料。當您首次從通訊端讀取或寫入時，SSL/TLS 握手（建立安全連線的過程）會自動進行。

#### **範例：傳送 HTTP GET 請求**
以下是一個連接到伺服器並擷取網頁的完整範例：

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // 取得預設的 SSLSocketFactory
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // 建立連接到 example.com 連接埠 443 的 SSLSocket
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // 取得輸入和輸出串流
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // 傳送簡單的 HTTP GET 請求
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // 讀取並列印回應
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // 關閉通訊端
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **關鍵注意事項**
- **握手**：當您使用通訊端時，SSL/TLS 握手會自動處理。
- **信任**：預設情況下，Java 信任儲存在其信任庫中由知名憑證授權機構（CA）簽署的憑證。如果伺服器的憑證不受信任，您需要配置自訂信任庫（稍後詳述）。
- **主機名稱驗證**：`SSLSocket` 預設不執行主機名稱驗證（與 `HttpsURLConnection` 不同）。要啟用它，請使用 `SSLParameters`：

   ```java
   import javax.net.ssl.SSLParameters;
   SSLParameters params = new SSLParameters();
   params.setEndpointIdentificationAlgorithm("HTTPS");
   socket.setSSLParameters(params);
   ```

   這確保伺服器的憑證與主機名稱相符，防止中間人攻擊。

---

### **作為伺服器使用 `javax.net.ssl`**
對於接受安全連線的伺服器，您使用 `SSLServerSocketFactory` 來建立 `SSLServerSocket`。伺服器必須提供憑證，通常儲存在金鑰庫中。

#### **步驟**
1. **設定金鑰庫**：
   建立一個包含伺服器私密金鑰和憑證的金鑰庫（例如使用 Java 的 `keytool` 產生 `.jks` 檔案）。

2. **初始化 `SSLContext`**：
   使用金鑰庫配置帶有 `KeyManager` 的 `SSLContext`。

   ```java
   import javax.net.ssl.*;
   import java.io.FileInputStream;
   import java.security.KeyStore;

   KeyStore ks = KeyStore.getInstance("JKS");
   ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

   KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
   kmf.init(ks, "password".toCharArray());

   SSLContext context = SSLContext.getInstance("TLS");
   context.init(kmf.getKeyManagers(), null, null);
   ```

3. **建立 `SSLServerSocket`**：
   使用來自 `SSLContext` 的 `SSLServerSocketFactory` 來建立伺服器通訊端。

   ```java
   SSLServerSocketFactory factory = context.getServerSocketFactory();
   SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
   ```

4. **接受連線**：
   接受客戶端連線，並透過產生的 `SSLSocket` 進行通訊。

#### **範例：簡單的 SSL 伺服器**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // 載入金鑰庫
            KeyStore ks = KeyStore.getInstance("JKS");
            ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

            // 初始化 KeyManagerFactory
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            kmf.init(ks, "password".toCharArray());

            // 初始化 SSLContext
            SSLContext context = SSLContext.getInstance("TLS");
            context.init(kmf.getKeyManagers(), null, null);

            // 建立 SSLServerSocket
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);

            System.out.println("伺服器已在連接埠 8443 啟動...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("客戶端已連線。");

                // 處理客戶端通訊
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("來自安全伺服器的問候！");
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **關鍵注意事項**
- **金鑰庫**：伺服器需要憑證，通常位於 `.jks` 檔案中，您必須產生並配置它。
- **客戶端驗證**：如果伺服器要求客戶端提供憑證，請使用 `TrustManager` 初始化 `SSLContext` 並呼叫 `serverSocket.setNeedClientAuth(true)`。

---

### **進階配置**
為了更精確地控制 SSL/TLS 行為，您可以自訂以下項目：

#### **1. 自訂信任庫**
如果伺服器的憑證不是由受信任的 CA 簽署，請載入自訂信任庫：

```java
KeyStore trustStore = KeyStore.getInstance("JKS");
trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

SSLContext context = SSLContext.getInstance("TLS");
context.init(null, tmf.getTrustManagers(), null);

SSLSocketFactory factory = context.getSocketFactory();
```

#### **2. 協定版本**
指定安全協定（例如 TLS 1.2 或 1.3）以避免使用過時、不安全的版本：

```java
socket.setEnabledProtocols(new String[] {"TLSv1.2", "TLSv1.3"});
```

#### **3. 加密套件**
限制用於加密的加密套件：

```java
socket.setEnabledCipherSuites(new String[] {"TLS_AES_128_GCM_SHA256"});
```

---

### **總結**
要使用 `javax.net.ssl`：
- **對於客戶端**：使用 `SSLSocketFactory` 建立 `SSLSocket`，連接到伺服器，並可選擇使用 `SSLParameters` 配置主機名稱驗證。
- **對於伺服器**：使用金鑰庫和 `KeyManager` 配置 `SSLContext`，然後使用 `SSLServerSocketFactory` 建立 `SSLServerSocket`。
- **自訂**：使用 `SSLContext`、`KeyManager` 和 `TrustManager` 進行進階憑證處理，並根據需要設定協定或加密套件。

此套件為 Java 中的安全通訊提供了基礎，適用於簡單和複雜的應用程式。對於 HTTPS，可以考慮使用更高階的 API 如 `HttpsURLConnection`，但當需要直接控制 SSL/TLS 通訊端時，`javax.net.ssl` 提供了這種能力。