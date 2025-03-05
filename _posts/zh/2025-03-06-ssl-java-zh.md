---
audio: false
generated: true
lang: zh
layout: post
title: Java 中的安全连接
translated: true
---

要在 Java 中使用 `javax.net.ssl` 包，你需要利用其类来通过 SSL（安全套接字层）或 TLS（传输层安全）协议建立网络上的安全通信。这个包对于创建安全连接（如 HTTPS 通信）是必不可少的。下面，我将解释如何在客户端和服务器端应用程序中使用它，包括基本示例和关键考虑事项。

---

### **`javax.net.ssl` 概述**
`javax.net.ssl` 包提供了安全套接字通信的工具。它包括：
- **`SSLSocket`**：用于安全通信的客户端套接字。
- **`SSLServerSocket`**：用于接受安全连接的服务器端套接字。
- **`SSLSocketFactory`**：用于创建 `SSLSocket` 实例的工厂。
- **`SSLServerSocketFactory`**：用于创建 `SSLServerSocket` 实例的工厂。
- **`SSLContext`**：用于配置 SSL/TLS 协议的类，允许自定义安全设置。
- **`KeyManager` 和 `TrustManager`**：用于管理证书和信任决策的类。

这些组件使得数据加密交换成为可能，确保客户端和服务器之间的机密性和完整性。

---

### **作为客户端使用 `javax.net.ssl`**
对于连接到安全服务器（例如 HTTPS 服务器）的客户端应用程序，通常使用 `SSLSocketFactory` 创建一个 `SSLSocket`。以下是如何操作的：

#### **步骤**
1. **获取一个 `SSLSocketFactory`**：
   使用 Java 提供的默认工厂，它依赖系统的默认 SSL/TLS 设置和信任库（受信任证书的存储库）。

   ```java
   import javax.net.ssl.SSLSocketFactory;
   SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
   ```

2. **创建一个 `SSLSocket`**：
   使用工厂连接到服务器，指定主机名和端口（例如 443 端口用于 HTTPS）。

   ```java
   import javax.net.ssl.SSLSocket;
   SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);
   ```

3. **通过套接字通信**：
   使用套接字的输入和输出流发送和接收数据。SSL/TLS 握手（建立安全连接）在你第一次从套接字读取或写入时自动发生。

#### **示例：发送 HTTP GET 请求**
以下是一个完整的示例，连接到服务器并检索网页：

```java
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;
import java.io.*;

public class SSLClientExample {
    public static void main(String[] args) {
        try {
            // 获取默认的 SSLSocketFactory
            SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
            // 创建一个到 example.com 443 端口的 SSLSocket
            SSLSocket socket = (SSLSocket) factory.createSocket("example.com", 443);

            // 获取输入和输出流
            OutputStream out = socket.getOutputStream();
            InputStream in = socket.getInputStream();

            // 发送一个简单的 HTTP GET 请求
            String request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n";
            out.write(request.getBytes());
            out.flush();

            // 读取并打印响应
            BufferedReader reader = new BufferedReader(new InputStreamReader(in));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // 关闭套接字
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### **关键说明**
- **握手**：使用套接字时，SSL/TLS 握手会自动处理。
- **信任**：默认情况下，Java 信任由知名证书颁发机构（CA）签名的证书，这些证书存储在其信任库中。如果服务器的证书不受信任，你需要配置一个自定义信任库（稍后会详细介绍）。
- **主机名验证**：`SSLSocket` 默认不执行主机名验证（与 `HttpsURLConnection` 不同）。要启用它，使用 `SSLParameters`：

   ```java
   import javax.net.ssl.SSLParameters;
   SSLParameters params = new SSLParameters();
   params.setEndpointIdentificationAlgorithm("HTTPS");
   socket.setSSLParameters(params);
   ```

   这确保服务器的证书与主机名匹配，防止中间人攻击。

---

### **作为服务器使用 `javax.net.ssl`**
对于接受安全连接的服务器，使用 `SSLServerSocketFactory` 创建一个 `SSLServerSocket`。服务器必须提供一个证书，通常存储在密钥库中。

#### **步骤**
1. **设置密钥库**：
   创建一个包含服务器私钥和证书的密钥库（例如，使用 Java 的 `keytool` 生成一个 `.jks` 文件）。

2. **初始化一个 `SSLContext`**：
   使用密钥库配置一个 `SSLContext`，其中包含一个 `KeyManager`。

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

3. **创建一个 `SSLServerSocket`**：
   使用 `SSLContext` 中的 `SSLServerSocketFactory` 创建一个服务器套接字。

   ```java
   SSLServerSocketFactory factory = context.getServerSocketFactory();
   SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);
   ```

4. **接受连接**：
   接受客户端连接并通过结果的 `SSLSocket` 通信。

#### **示例：简单的 SSL 服务器**
```java
import javax.net.ssl.*;
import java.io.*;
import java.security.KeyStore;

public class SSLServerExample {
    public static void main(String[] args) {
        try {
            // 加载密钥库
            KeyStore ks = KeyStore.getInstance("JKS");
            ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());

            // 初始化 KeyManagerFactory
            KeyManagerFactory kmf = KeyManagerFactory.getInstance("SunX509");
            kmf.init(ks, "password".toCharArray());

            // 初始化 SSLContext
            SSLContext context = SSLContext.getInstance("TLS");
            context.init(kmf.getKeyManagers(), null, null);

            // 创建 SSLServerSocket
            SSLServerSocketFactory factory = context.getServerSocketFactory();
            SSLServerSocket serverSocket = (SSLServerSocket) factory.createServerSocket(8443);

            System.out.println("服务器在 8443 端口启动...");
            while (true) {
                SSLSocket socket = (SSLSocket) serverSocket.accept();
                System.out.println("客户端连接。");

                // 处理客户端通信
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("来自安全服务器的问候！");
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

#### **关键说明**
- **密钥库**：服务器需要一个证书，通常是一个 `.jks` 文件，你必须生成并配置它。
- **客户端认证**：如果服务器要求客户端提供证书，初始化 `SSLContext` 并使用 `TrustManager`，然后调用 `serverSocket.setNeedClientAuth(true)`。

---

### **高级配置**
为了对 SSL/TLS 行为有更多控制，可以自定义以下内容：

#### **1. 自定义信任库**
如果服务器的证书没有由受信任的 CA 签名，加载一个自定义信任库：

```java
KeyStore trustStore = KeyStore.getInstance("JKS");
trustStore.load(new FileInputStream("truststore.jks"), "password".toCharArray());

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(trustStore);

SSLContext context = SSLContext.getInstance("TLS");
context.init(null, tmf.getTrustManagers(), null);

SSLSocketFactory factory = context.getSocketFactory();
```

#### **2. 协议版本**
指定安全协议（例如 TLS 1.2 或 1.3），以避免过时的不安全版本：

```java
socket.setEnabledProtocols(new String[] {"TLSv1.2", "TLSv1.3"});
```

#### **3. 密码套件**
限制用于加密的密码套件：

```java
socket.setEnabledCipherSuites(new String[] {"TLS_AES_128_GCM_SHA256"});
```

---

### **总结**
要使用 `javax.net.ssl`：
- **客户端**：使用 `SSLSocketFactory` 创建一个 `SSLSocket`，连接到服务器，并可选地使用 `SSLParameters` 配置主机名验证。
- **服务器**：配置一个包含密钥库和 `KeyManager` 的 `SSLContext`，然后使用 `SSLServerSocketFactory` 创建一个 `SSLServerSocket`。
- **自定义**：使用 `SSLContext`、`KeyManager` 和 `TrustManager` 进行高级证书处理，并根据需要设置协议或密码套件。

这个包为 Java 提供了安全通信的基础，适用于简单和复杂的应用程序。对于 HTTPS，考虑使用更高级别的 API 如 `HttpsURLConnection`，但 `javax.net.ssl` 在需要时提供了对 SSL/TLS 套接字的直接控制。