---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Netty 於 Java
translated: true
---

讓我們深入了解 Netty，一個強大的非同步、事件驅動的網絡框架，用於在 Java 中構建高性能應用程序。它廣泛用於創建需要高效處理多個連接的伺服器和客戶端，如網頁伺服器、代理或即時消息系統。我將逐步引導你，重點放在簡單的伺服器設置上，因為這是一個常見的起點。

---

### 1. **什麼是 Netty？**
- Netty 抽象了 Java NIO（非阻塞 I/O）的複雜性，並提供了一個乾淨的 API 來構建網絡應用程序。
- 主要特點：非同步 I/O、事件循環、數據處理管道和可擴展性。
- 可以將其視為一個處理套接字、協議和數據的工具包。

---

### 2. **設置你的項目**
要使用 Netty，將其添加到你的項目中。如果你使用 Maven，在你的 `pom.xml` 中包含以下內容：
```xml
<dependency>
    <groupId>io.netty</groupId>
    <artifactId>netty-all</artifactId>
    <version>4.1.108.Final</version> <!-- 截至 2025 年 2 月的最新穩定版本 -->
</dependency>
```
對於 Gradle：
```gradle
implementation 'io.netty:netty-all:4.1.108.Final'
```

---

### 3. **核心概念**
在編碼之前，掌握這些基本概念：
- **EventLoop**：管理 I/O 操作並非同步執行任務。
- **Channel**：表示一個連接（如套接字）。
- **ChannelHandler**：處理事件（例如，接收數據、連接建立）。
- **ChannelPipeline**：處理入站/出站數據的處理器鏈。
- **Bootstrap**：配置和啟動你的伺服器或客戶端。

---

### 4. **構建簡單的回聲伺服器**
讓我們創建一個伺服器，它會回顯客戶端發送的任何內容。這是一個經典的 Netty 示例。

#### 步驟 1：創建一個 ChannelInitializer
這將為每個新連接設置管道。
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
        // 添加處理器來解碼/編碼字符串並處理邏輯
        pipeline.addLast(new StringDecoder());  // 將字節解碼為字符串
        pipeline.addLast(new StringEncoder());  // 將字符串編碼為字節
        pipeline.addLast(new EchoServerHandler());  // 自定義邏輯
    }
}
```

#### 步驟 2：創建一個處理器
這定義了數據到達時會發生什麼。
```java
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;

public class EchoServerHandler extends SimpleChannelInboundHandler<String> {
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        System.out.println("接收到: " + msg);
        ctx.writeAndFlush(msg);  // 將消息回顯給客戶端
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        cause.printStackTrace();
        ctx.close();  // 發生錯誤時關閉連接
    }
}
```

#### 步驟 3：設置伺服器
這將所有內容綁定在一起並啟動伺服器。
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
        // 兩個事件循環：一個用於接受連接，一個用於處理它們
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);  // 接受傳入連接
        EventLoopGroup workerGroup = new NioEventLoopGroup(); // 處理流量

        try {
            ServerBootstrap bootstrap = new ServerBootstrap()
                .group(bossGroup, workerGroup)
                .channel(NioServerSocketChannel.class)  // 使用 NIO 運輸
                .childHandler(new EchoServerInitializer());  // 初始化新連接

            // 綁定到端口並啟動伺服器
            bootstrap.bind(port).sync().channel().closeFuture().sync();
        } finally {
            // 优雅地關閉
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    public static void main(String[] args) throws Exception {
        int port = 8080;  // 默認端口
        new EchoServer(port).run();
    }
}
```

---

### 5. **測試伺服器**
- 運行 `EchoServer` 類。
- 使用 `telnet` 工具（`telnet localhost 8080`）或編寫簡單的 Netty 客戶端：
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
- 在 `telnet` 中輸入消息，伺服器將回顯它。

---

### 6. **關鍵自定義選項**
- **編碼器/解碼器**：對於字符串使用 `StringDecoder`/`StringEncoder`，或者對於原始字節或其他協議（例如，使用 `HttpServerCodec` 的 HTTP）進行自定義。
- **線程**：調整 `NioEventLoopGroup` 線程計數（例如，`new NioEventLoopGroup(4)` 為 4 個線程）。
- **管道**：添加更多處理器進行日誌記錄（`LoggingHandler`）、SSL（`SslHandler`）或自定義邏輯。
- **選項**：通過 `bootstrap.option()` 或 `childOption()` 設置 `SO_BACKLOG`、`SO_REUSEADDR` 等。

---

### 7. **最佳實踐**
- **重用 EventLoopGroups**：如果可能，在客戶端/伺服器之間共享它們以節省資源。
- **處理異常**：在處理器中始終實現 `exceptionCaught`。
- **優雅關閉**：調用 `shutdownGracefully()` 進行清理。
- **緩衝區**：使用 `ByteBuf` 進行高效的內存管理（Netty 的緩衝區類）。

---

### 8. **下一步**
- **HTTP 伺服器**：添加 `HttpServerCodec` 並處理 HTTP 請求。
- **WebSocket**：使用 `WebSocketServerProtocolHandler` 進行即時應用。
- **性能**：調整 `EventLoopGroup` 大小並探索 `Epoll`（Linux）或 `KQueue`（macOS）以獲得更好的性能。

---

這就是基礎！你現在有一個運行中的回聲伺服器。如果你想進行調整——例如，添加自定義協議、處理二進制數據或擴展它——請告訴我，我將進一步指導你！你對 Netty 的目標是什麼？