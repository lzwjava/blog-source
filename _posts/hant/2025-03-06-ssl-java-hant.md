---
audio: true
generated: true
lang: hant
layout: post
title: Java 之安全連接
translated: true
---

要在 Java 中使用 `javax.net.ssl` 包，您需要利用其類別來建立使用 SSL（安全套接字層）或 TLS（傳輸層安全）協議的安全網絡通信。這個包對於創建安全連接（例如用於 HTTPS 通信的連接）至關重要。以下，我將解釋如何在客戶端和伺服器端應用程序中使用它，包括基本示例和關鍵考量。

---

### **`javax.net.ssl` 總覽**
`javax.net.ssl` 包提供了安全套接字通信的工具。它包括：
- **`SSLSocket`**：用於安全通信的客戶端套接字。
- **`SSLServerSocket`**：用於接受安全連接的伺服器端套接字。
- **`SSLSocketFactory`**：用於創建 `SSLSocket` 實例的工廠。
- **`SSLServerSocketFactory`**：用於創建 `SSLServerSocket` 實例的工廠。
- **`SSLContext`**：用於配置 SSL/TLS 協議的類別，允許自定義安全設置。
- **`KeyManager` 和 `TrustManager`**：用於管理證書和信任決策的類別。

這些組件使得數據加密交換成為可能，確保客戶端和伺服器之間的機密性和完整性。

---

### **作為客戶端使用 `javax.net.ssl`**
對於連接到安全伺服器（例如 HTTPS 伺服器）的客戶端應用程序，通常使用 `SSLSocketFactory` 來創建一個 `SSLSocket`。以下是如何進行的：

#### **步驟**
1. **獲取一個 `SSLSocketFactory`**：
   使用 Java 提供的默認工廠，它依賴於系統的默認 SSL/TLS 設置和信任存儲（受信任證書的存儲庫）。

   ```java
   import javax.net.ssl.SSLSocketFactory;
   SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
   ```

2. **創建一個 `SSLSocket`**：
   使用工廠連接到伺服器，指定主機名和端口（例如 443 端口用於 HTTPS）。

   ```java
   import javax.net.ssl.SSLSocket;
   SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
   ```

3. **通過套接字通信**：
   使用套接字的輸入和輸出流發送和接收數據。SSL/TLS 握手（建立安全連接）在您第一次從套接字讀取或寫入時自動發生。

#### **示例：發送 HTTP GET 請求**
以下是一個完整的示例，它連接到伺服器並檢索網頁：

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // 獲取默認的 SSLSocketFactory
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // 創建一個連接到 example.com 的 SSLSocket，端口 443
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // 获取輸入和輸出流
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // 發送簡單的 HTTP GET 請求
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // 讀取並打印響應
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // 關閉套接字
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **關鍵注意事項**
- **握手**：當您使用套接字時，SSL/TLS 握手會自動處理。
- **信任**：默認情況下，Java 信任由知名證書授權機構（CA）簽署的證書，這些證書存儲在其信任存儲中。如果伺服器的證書不受信任，您需要配置自定義信任存儲（稍後會有更多內容）。
- **主機名驗證**：`SSLSocket` 默認不執行主機名驗證（與 `HttpsURLConnection` 不同）。要啟用它，請使用 `SSLParameters`：

   ```java
   import javax.net.ssl.SSLParameters;
   SSLParameters params = new SSLParameters();
   params.setEndpointIdentificationAlgorithm("HTTPS");
   socket.setSSLParameters(params);
   ```

   這樣可以確保伺服器的證書與主機名匹配，從而防止中間人攻擊。

---

### **作為伺服器使用 `javax.net.ssl`**
對於接受安全連接的伺服器，使用 `SSLServerSocketFactory` 來創建一個 `SSLServerSocket`。伺服器必須提供一個證書，通常存儲在密鑰存儲中。

#### **步驟**
1. **設置密鑰存儲**：
   創建一個包含伺服器私鑰和證書的密鑰存儲（例如使用 Java 的 `keytool` 生成一個 `.jks` 文件）。

2. **初始化一個 `SSLContext`**：
   使用密鑰存儲配置一個 `SSLContext`，並使用 `KeyManager`。

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

3. **創建一個 `SSLServerSocket`**：
   使用 `SSLContext` 中的 `SSLServerSocketFactory` 創建一個伺服器套接字。

   ```java
   SSLServerSocketFactory factory = context.getServerSocketFactory();
   SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
   ```

4. **接受連接**：
   接受客戶端連接並通過結果的 `SSLSocket` 通信。

#### **示例：簡單的 SSL 伺服器**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // 加載密鑰存儲
            KeyStore ks = KeyStore.getInstance("JKS");
            ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

            // 初始化 KeyManagerFactory
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            kmf.init(ks, "password".toCharArray());

            // 初始化 SSLContext
            SSLContext context = SSLContext.getInstance("TLS");
            context.init(kmf.getKeyManagers(), null, null);

            // 創建 SSLServerSocket
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);

            System.out.println("伺服器在 8443 端口啟動...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("客戶端已連接。");

                // 處理客戶端通信
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
- **密鑰存儲**：伺服器需要一個證書，通常在一個 `.jks` 文件中，您必須生成並配置它。
- **客戶端驗證**：如果伺服器要求客戶端提供證書，請初始化 `SSLContext` 並使用 `TrustManager`，然後調用 `serverSocket.setNeedClientAuth(true)`。

---

### **高級配置**
為了更好地控制 SSL/TLS 行為，您可以自定義以下內容：

#### **1. 自定義信任存儲**
如果伺服器的證書未由受信任的 CA 簽署，請加載自定義信任存儲：

```java
KeyStore trustStore = KeyStore.getInstance("JKS");
trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

SSLContext context = SSLContext.getInstance("TLS");
context.init(null, tmf.getTrustManagers(), null);

SSLSocketFactory factory = context.getSocketFactory();
```

#### **2. 協議版本**
指定安全協議（例如 TLS 1.2 或 1.3）以避免過時的不安全版本：

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
- **對於客戶端**：使用 `SSLSocketFactory` 創建一個 `SSLSocket`，連接到伺服器，並可選地使用 `SSLParameters` 配置主機名驗證。
- **對於伺服器**：配置一個帶有密鑰存儲和 `KeyManager` 的 `SSLContext`，然後使用 `SSLServerSocketFactory` 創建一個 `SSLServerSocket`。
- **自定義**：使用 `SSLContext`、`KeyManager` 和 `TrustManager` 進行高級證書處理，並根據需要設置協議或加密套件。

這個包為 Java 提供了安全通信的基礎，適用於簡單和複雜的應用程序。對於 HTTPS 具體來說，考慮使用更高級別的 API 如 `HttpsURLConnection`，但 `javax.net.ssl` 在需要時提供了對 SSL/TLS 套接字的直接控制。