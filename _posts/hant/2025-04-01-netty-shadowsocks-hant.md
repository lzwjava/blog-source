---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Netty 構建 Shadowsocks 客戶端
translated: true
type: note
---

使用 Netty 建構類似 Clash 或原始 Shadowsocks 客戶端的 Shadowsocks 客戶端，需要理解 Shadowsocks 協議並善用 Netty 的異步事件驅動網絡應用框架。以下是涉及的步驟與關鍵概念解析：

**1. 理解 Shadowsocks 協議**

在深入 Netty 之前，您需要徹底理解 Shadowsocks 協議。高層次來看，它包含：

* **連線建立：** 客戶端向 Shadowsocks 伺服器發起連線。
* **認證與方法協商：** 客戶端發送選擇的加密方法與密碼至伺服器進行認證。
* **地址編碼：** 客戶端以特定編碼格式發送目標伺服器的實際地址（IP 地址與端口）。
* **資料轉發：** 成功認證與地址編碼後，客戶端與 Shadowsocks 伺服器之間交換的所有後續資料皆使用約定的方法進行加密/解密。

**您需要實作的協議關鍵面向：**

* **方法與密碼處理：** 儲存並發送選擇的加密方法（例如 `aes-256-cfb`、`chacha20-ietf-poly1305`）與密碼。
* **地址編碼：** 將目標地址編碼為特定格式（類型位元組、地址、端口）。類型位元組指示地址是 IPv4 地址 (0x01)、IPv6 地址 (0x04) 還是主機名稱 (0x03)。
* **加密與解密：** 實作選擇的加密與解密演算法。像 `PyCryptodome` (Python) 或 `Bouncy Castle` (Java) 這類函式庫對此有幫助。
* **TCP 轉發：** 建立一個本地 TCP 伺服器，監聽應用程式的連線，並透過 Shadowsocks 通道轉發流量。

**2. 設定 Netty 專案**

首先，您需要在專案中包含 Netty 相依性（例如，在 Java 專案中使用 Maven 或 Gradle）。

**3. 代理客戶端的核心 Netty 元件**

您將主要使用以下 Netty 元件：

* **`Bootstrap`：** 用於配置與啟動客戶端應用程式。
* **`EventLoopGroup`：** 管理處理客戶端 I/O 操作的事件循環。通常使用 `NioEventLoopGroup` 進行非阻塞 I/O。
* **`Channel`：** 代表一個網絡連線。
* **`ChannelPipeline`：** 一串 `ChannelHandler`，用於處理入站與出站事件及資料。
* **`ChannelHandler`：** 您實作以處理特定事件與資料轉換的介面。您將為 Shadowsocks 協議建立自訂的處理器。
* **`ByteBuf`：** Netty 用於處理二進位資料的緩衝區。

**4. 使用 Netty 處理器實作 Shadowsocks 協議**

您需要在 `ChannelPipeline` 內建立數個自訂的 `ChannelHandler` 來實作 Shadowsocks 邏輯。以下是一個可能的結構：

* **本地代理伺服器處理器 (`ChannelInboundHandlerAdapter`):**
    * 此處理器將運行於本地伺服器通訊端上，您的應用程式將連線至此（例如 `localhost:1080`）。
    * 當有來自本地應用程式的新連線時，此處理器將：
        * 建立與遠端 Shadowsocks 伺服器的連線。
        * 根據協議編碼後，將初始連線請求（目標地址）轉發給 Shadowsocks 伺服器。
        * 管理本地應用程式與 Shadowsocks 伺服器之間的資料流。

* **Shadowsocks 客戶端編碼器 (`ChannelOutboundHandlerAdapter`):**
    * 此處理器負責編碼發送至 Shadowsocks 伺服器的資料。
    * 它將：
        * 根據 Shadowsocks 協議編碼目標地址（類型、地址、端口）。
        * 使用選擇的加密方法加密資料。

* **Shadowsocks 客戶端解碼器 (`ChannelInboundHandlerAdapter`):**
    * 此處理器負責解碼從 Shadowsocks 伺服器接收的資料。
    * 它將：
        * 解密接收到的資料。

* **遠端伺服器轉發處理器 (`ChannelInboundHandlerAdapter`):**
    * 當從遠端 Shadowsocks 伺服器接收到資料時，將呼叫此處理器。
    * 它將轉發解密後的資料回原始的本地應用程式。

**5. Netty Pipeline 的範例結構**

以下是連線至 Shadowsocks 伺服器時，您的 `ChannelPipeline` 可能看起來的簡化範例：

```java
public class ShadowsocksClientInitializer extends ChannelInitializer<SocketChannel> {

    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClientInitializer(String serverAddress, int serverPort, String method, String password) {
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // 出站處理器 (發送至 Shadowsocks 伺服器的資料)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // 入站處理器 (從 Shadowsocks 伺服器接收的資料)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

而對於本地代理伺服器：

```java
public class LocalProxyInitializer extends ChannelInitializer<SocketChannel> {

    private final String shadowsocksServerAddress;
    private final int shadowsocksServerPort;
    private final String method;
    private final String password;

    public LocalProxyInitializer(String shadowsocksServerAddress, int shadowsocksServerPort, String method, String password) {
        this.shadowsocksServerAddress = shadowsocksServerAddress;
        this.shadowsocksServerPort = shadowsocksServerPort;
        this.method = method;
        this.password = password;
    }

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();

        // 處理器用於初始化連線至 Shadowsocks 伺服器並轉發資料
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. 關鍵實作細節**

* **加密/解密實作：** 您需要在 `ShadowsocksClientEncoder` 和 `ShadowsocksClientDecoder` 中實作選擇的加密與解密演算法。這很可能涉及使用外部函式庫。如果選擇的方法需要，請小心處理金鑰推導與初始化向量。
* **`LocalProxyHandler` 中的地址編碼：** 當 `LocalProxyHandler` 從本地應用程式接收到初始連線請求時，它需要提取目標地址與端口，並在發送給 Shadowsocks 伺服器之前，將它們編碼成 Shadowsocks 格式。
* **在 `LocalProxyHandler` 中連線至 Shadowsocks 伺服器：** `LocalProxyHandler` 將使用獨立的 Netty `Bootstrap` 來建立與配置的 Shadowsocks 伺服器的連線。
* **資料轉發：** 一旦與 Shadowsocks 伺服器的連線建立，處理器需要有效地在本地應用程式的連線與 Shadowsocks 伺服器的連線之間轉發資料。您很可能需要管理兩個連線的 `Channel` 物件。
* **錯誤處理：** 為網絡問題、協議錯誤以及加密/解密失敗實作適當的錯誤處理。
* **並行處理：** Netty 透過其事件循環模型高效處理並行。如果您需要共享狀態，請確保您的處理器設計為執行緒安全。

**7. 啟動代理客戶端**

您需要建立一個主類別來啟動本地代理伺服器（監聽本地連線）並可能處理配置。

```java
public class ShadowsocksClient {

    private final int localPort;
    private final String serverAddress;
    private final int serverPort;
    private final String method;
    private final String password;

    public ShadowsocksClient(int localPort, String serverAddress, int serverPort, String method, String password) {
        this.localPort = localPort;
        this.serverAddress = serverAddress;
        this.serverPort = serverPort;
        this.method = method;
        this.password = password;
    }

    public void run() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();

        try {
            ServerBootstrap b = new ServerBootstrap();
            b.group(bossGroup, workerGroup)
             .channel(NioServerSocketChannel.class)
             .childHandler(new LocalProxyInitializer(serverAddress, serverPort, method, password))
             .option(ChannelOption.SO_BACKLOG, 128)
             .childOption(ChannelOption.SO_KEEPALIVE, true);

            ChannelFuture f = b.bind(localPort).sync();
            System.out.println("Shadowsocks client started on port: " + localPort);
            f.channel().closeFuture().sync();
        } finally {
            workerGroup.shutdownGracefully();
            bossGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        // 替換為您的配置
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. 進階考量（如 Clash）**

要建構像 Clash 這樣的客戶端，您需要考量更多進階功能：

* **多種代理協議：** Clash 支援多種代理協議（Shadowsocks、SOCKS5、HTTP）。您需要為每種協議添加處理器。
* **基於規則的路由：** Clash 允許您定義規則，根據網域、IP 地址、GEOIP 等來路由流量。這將涉及在您的客戶端內實作規則引擎。
* **配置管理：** Clash 使用 YAML 配置檔案。您需要實作加載與解析此類配置的方法。
* **DNS 處理：** Clash 通常會攔截 DNS 請求並透過代理路由它們。您需要實作 DNS 攔截與轉發。
* **UDP 支援：** Shadowsocks 也支援 UDP 轉發。您需要使用 Netty 的 UDP 功能來實作 UDP 處理。
* **外掛與擴充：** Clash 有一個外掛系統。實作這樣的系統將增加顯著的複雜度。

**總結來說，使用 Netty 建構基礎的 Shadowsocks 客戶端涉及：**

1.  理解 Shadowsocks 協議。
2.  設定 Netty 專案。
3.  為編碼、解碼與轉發資料建立自訂的 `ChannelHandler`。
4.  實作加密與解密邏輯。
5.  啟動本地伺服器以接受應用程式的連線。
6.  連線至遠端 Shadowsocks 伺服器。

建構像 Clash 這樣功能豐富的客戶端，需要對網絡、代理協議以及更複雜的軟體架構有更深的理解。從基礎的 Shadowsocks 實作開始，並根據需要逐步添加功能。請記得查閱官方的 Shadowsocks 文件與 Netty 範例以獲取更詳細的資訊。