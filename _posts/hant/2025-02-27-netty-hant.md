---
audio: false
generated: true
lang: hant
layout: post
title: 在 Java 中使用 Netty
translated: true
type: note
---

讓我們深入探討如何使用 Netty——這是一個功能強大的非同步事件驅動網絡框架，專為構建 Java 高性能應用而設計。它廣泛用於建立需要高效處理大量連接的伺服器與客戶端，例如網頁伺服器、代理伺服器或即時通訊系統。我將逐步引導您掌握基礎知識，重點放在簡單的伺服器設定，因為這是最常見的入門點。

---

### 1. **什麼是 Netty？**
- Netty 封裝了 Java NIO（非阻塞 I/O）的複雜性，並提供簡潔的 API 來構建網絡應用。
- 主要功能：非同步 I/O、事件循環、用於處理資料的管道系統，以及高度可擴展性。
- 您可以將其視為高效處理通訊端、協定和資料的工具套件。

---

### 2. **設定專案**
要使用 Netty，請將其加入您的專案。若使用 Maven，請在 `pom.xml` 中加入以下內容：
```xml
<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.108.Final</version> <!-- 截至 2025 年 2 月的最新穩定版本 -->
</dependency>
```
若使用 Gradle：
```gradle
implementation 'io.netty:netty-all:4.1.108.Final'
```

---

### 3. **核心概念**
在編寫程式碼前，先掌握這些基礎知識：
- **EventLoop**：管理 I/O 操作並非同步執行任務。
- **Channel**：代表一個連接（例如通訊端）。
- **ChannelHandler**：處理事件（例如資料接收、連接建立）。
- **ChannelPipeline**：處理內送/外發資料的處理器鏈。
- **Bootstrap**：配置並啟動您的伺服器或客戶端。

---

### 4. **構建簡單的回應伺服器**
讓我們建立一個能將客戶端發送的內容原樣返回的伺服器。這是 Netty 的經典範例。

#### 步驟 1：建立 ChannelInitializer
此步驟為每個新連接設定管道。
```java
import io.netty.channel.ChannelInitializer;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.ChannelPipeline;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;

public class EchoServerInitializer extends ChannelInitializer<SocketChannel> {
    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        ChannelPipeline pipeline = ch.pipeline();
        // 加入處理器以解碼/編碼字串並處理邏輯
        pipeline.addLast(new StringDecoder());  // 將位元組解碼為字串
        pipeline.addLast(new StringEncoder());  // 將字串編碼為位元組
        pipeline.addLast(new EchoServerHandler());  // 自訂邏輯
    }
}
```

#### 步驟 2：建立處理器
此步驟定義資料到達時的處理邏輯。
```java
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;

public class EchoServerHandler extends SimpleChannelInboundHandler<String> {
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        System.out.println("收到: " + msg);
        ctx.writeAndFlush(msg);  // 將訊息回應給客戶端
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        ctx.close();  // 發生錯誤時關閉連接
    }
}
```

#### 步驟 3：設定伺服器
此步驟整合所有元件並啟動伺服器。
```java
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.EventLoopGroup;

public class EchoServer {
    private final int port;

    public EchoServer(int port) {
        this.port = port;
    }

    public void run() throws Exception {
        // 兩個事件循環：一個用於接受連接，一個用於處理連接
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);  // 接受傳入連接
        EventLoopGroup workerGroup = new NioEventLoopGroup(); // 處理流量

        try {
            ServerBootstrap bootstrap = new ServerBootstrap()
                .group(bossGroup, workerGroup)
                .channel(NioServerSocketChannel.class)  // 使用 NIO 傳輸
                .childHandler(new EchoServerInitializer());  // 初始化新連接

            // 綁定端口並啟動伺服器
            bootstrap.bind(port).sync().channel().closeFuture().sync();
        } finally {
            // 優雅關閉
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        int port = 8080;  // 預設端口
        new EchoServer(port).run();
    }
}
```

---

### 5. **測試伺服器**
- 執行 `EchoServer` 類別。
- 使用工具如 `telnet`（`telnet localhost 8080`）或編寫一個簡單的 Netty 客戶端：
```java
import io.netty.bootstrap.Bootstrap;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.channel.EventLoopGroup;

public class EchoClient {
    public static void main(String[] args) throws Exception {
        EventLoopGroup group = new NioEventLoopGroup();
        try {
            Bootstrap bootstrap = new Bootstrap()
                .group(group)
                .channel(NioSocketChannel.class)
                .handler(new EchoServerInitializer());  // 重用相同的初始化器

            bootstrap.connect("localhost", 8080).sync().channel().closeFuture().sync();
        } finally {
            group.shutdownGracefully();
        }
    }
}
```
- 在 `telnet` 中輸入訊息，伺服器會將其回應回來。

---

### 6. **主要自訂選項**
- **編解碼器**：使用 `StringDecoder`/`StringEncoder` 處理字串，或使用 `ByteBuf` 自訂原始位元組或其他協定（例如使用 `HttpServerCodec` 處理 HTTP）。
- **執行緒處理**：調整 `NioEventLoopGroup` 的執行緒數量（例如 `new NioEventLoopGroup(4)` 設定 4 個執行緒）。
- **管道**：加入更多處理器以實現日誌記錄（`LoggingHandler`）、SSL（`SslHandler`）或自訂邏輯。
- **選項**：透過 `bootstrap.option()` 或 `childOption()` 設定 `SO_BACKLOG`、`SO_REUSEADDR` 等。

---

### 7. **最佳實踐**
- **重用 EventLoopGroups**：盡可能跨客戶端/伺服器共享以節省資源。
- **處理異常**：始終在處理器中實作 `exceptionCaught`。
- **優雅關閉**：呼叫 `shutdownGracefully()` 進行清理。
- **緩衝區**：使用 `ByteBuf` 實現高效的記憶體管理（Netty 的緩衝區類別）。

---

### 8. **後續步驟**
- **HTTP 伺服器**：加入 `HttpServerCodec` 並處理 HTTP 請求。
- **WebSocket**：使用 `WebSocketServerProtocolHandler` 構建即時應用。
- **效能優化**：調整 `EventLoopGroup` 大小，並探索 `Epoll`（Linux）或 `KQueue`（macOS）以提升效能。

---

基礎知識就介紹到這裡！您現在已經擁有了一個可運作的回應伺服器。如果您想進行調整——例如加入自訂協定、處理二進位資料或擴展規模——請隨時告訴我，我會進一步指導您！您使用 Netty 的目標是什麼呢？