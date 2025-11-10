---
audio: false
generated: true
lang: hant
layout: post
title: 基於 Netty 的 Java VPN 代理客戶端
translated: true
type: note
---

要使用 Netty 或 Spring Boot 建構一個 Clash VPN 代理客戶端，我們需要一個穩固的框架來處理網路通訊、YAML 配置解析以及代理協定（如 SOCKS、HTTP 和 Shadowsocks）。Netty 非常適合高效能網路通訊，而 Spring Boot 則能簡化配置和依賴管理。以下我將概述核心邏輯、主要函式庫，並提供一個以 Netty 為網路層的範例實作，因為它更適合處理底層代理操作。該客戶端將支援流行的 Clash YAML 配置（例如代理伺服器、規則和 DNS）。

### 主要邏輯
1. **配置解析**：
   - 解析 Clash 相容的 YAML 配置檔案（例如 `config.yaml`），包含代理伺服器、規則和 DNS 設定。
   - 支援常見代理類型：HTTP、SOCKS5、Shadowsocks 等。
   - 將 YAML 欄位映射到 Java 物件以便存取。

2. **代理伺服器設定**：
   - 初始化一個 Netty 伺服器來監聽傳入的客戶端連線（例如在本機埠 7890 上）。
   - 處理 SOCKS5/HTTP 代理協定以接收客戶端請求。

3. **路由與規則處理**：
   - 實作基於規則的路由（例如網域、IP 或地理位置），如 YAML 配置中所定義。
   - 將客戶端請求路由到適當的上游代理伺服器或直接連線。

4. **連線管理**：
   - 使用 Netty 的事件驅動模型來管理客戶端到代理和代理到目的地的連線。
   - 支援連線池和保持連線以提升效率。

5. **DNS 解析**：
   - 根據配置處理 DNS 查詢（例如使用上游 DNS 或本機解析器）。
   - 如果配置了，支援 DNS over HTTPS (DoH) 或其他安全協定。

6. **協定處理**：
   - 為 Shadowsocks（例如 AEAD 加密）、SOCKS5 和 HTTP 實作協定特定邏輯。
   - 使用可插拔的協定處理器來支援擴充性。

7. **錯誤處理與日誌記錄**：
   - 優雅地處理連線失敗、無效配置或不支援的協定。
   - 提供詳細的日誌以供除錯。

### 主要函式庫
- **Netty**：用於高效能網路通訊和事件驅動 I/O。處理客戶端連線、代理轉發和協定編解碼。
- **SnakeYAML**：用於解析 Clash 相容的 YAML 配置檔案。
- **Bouncy Castle**：用於加密操作（例如 Shadowsocks AEAD 加密）。
- **SLF4J**：用於日誌記錄。
- **Apache Commons**：用於工具函數（例如配置驗證）。
- **Jackson（可選）**：如果您偏好以 JSON 方式處理 YAML 或其他配置格式。
- **DNSJava（可選）**：如果需要自訂 DNS 解析。

### 核心實作
以下是一個簡化的基於 Netty 的 Clash 類 VPN 代理客戶端實作。它專注於：
- 解析 Clash YAML 配置。
- 設定一個 SOCKS5 代理伺服器。
- 將請求轉發到上游代理或目的地。
- 基於規則的基本路由。

```x-java-source
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.socksx.v5.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.yaml.snakeyaml.Yaml;

import java.io.FileReader;
import java.util.List;
import java.util.Map;

public class ClashProxyClient {
    private static final Logger logger = LoggerFactory.getLogger(ClashProxyClient.class);
    private static final int DEFAULT_PORT = 7890;
    private Map<String, Object> config;

    // 配置類別，用於保存解析後的 YAML 資料
    static class ProxyConfig {
        List<Map<String, String>> proxies;
        List<String> rules;

        public ProxyConfig(Map<String, Object> config) {
            this.proxies = (List<Map<String, String>>) config.get("proxies");
            this.rules = (List<String>) config.get("rules");
        }
    }

    // 載入 Clash YAML 配置
    public void loadConfig(String configPath) throws Exception {
        Yaml yaml = new Yaml();
        try (FileReader reader = new FileReader(configPath)) {
            config = yaml.load(reader);
            logger.info("已從 {} 載入配置", configPath);
        }
    }

    // 啟動代理伺服器
    public void start() throws Exception {
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            ServerBootstrap bootstrap = new ServerBootstrap();
            bootstrap.group(bossGroup, workerGroup)
                    .channel(NioServerSocketChannel.class)
                    .childHandler(new ChannelInitializer<Channel>() {
                        @Override
                        protected void initChannel(Channel ch) {
                            ChannelPipeline pipeline = ch.pipeline();
                            // 加入 SOCKS5 協定處理器
                            pipeline.addLast(new Socks5ServerEncoder());
                            pipeline.addLast(new Socks5InitialRequestDecoder());
                            pipeline.addLast(new Socks5InitialRequestHandler());
                            pipeline.addLast(new Socks5CommandRequestDecoder());
                            pipeline.addLast(new ProxyHandler(new ProxyConfig(config)));
                        }
                    });

            ChannelFuture future = bootstrap.bind(DEFAULT_PORT).sync();
            logger.info("代理伺服器已啟動在埠號 {}", DEFAULT_PORT);
            future.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    // 處理 SOCKS5 指令請求並路由流量
    static class ProxyHandler extends SimpleChannelInboundHandler<Socks5CommandRequest> {
        private final ProxyConfig config;

        public ProxyHandler(ProxyConfig config) {
            this.config = config;
        }

        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5CommandRequest request) {
            String destination = request.dstAddr() + ":" + request.dstPort();
            logger.info("正在處理對 {} 的請求", destination);

            // 簡單的基於規則的路由（需擴展實際的規則解析）
            String selectedProxy = selectProxy(destination);
            if (selectedProxy != null) {
                logger.info("路由到代理: {}", selectedProxy);
                // 在此實作代理轉發邏輯
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.SUCCESS, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            } else {
                logger.warn("未找到符合 {} 的代理", destination);
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.FAILURE, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            }
        }

        private String selectProxy(String destination) {
            // 實作基於規則的代理選擇
            for (String rule : config.rules) {
                // 範例：匹配網域或 IP 規則
                if (destination.matches(rule)) {
                    return config.proxies.get(0).get("name"); // 簡化處理
                }
            }
            return null; // 直接連線或後備處理
        }
    }

    // 處理 SOCKS5 初始請求
    static class Socks5InitialRequestHandler extends SimpleChannelInboundHandler<Socks5InitialRequest> {
        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5InitialRequest msg) {
            ctx.write(new DefaultSocks5InitialResponse(Socks5AuthMethod.NO_AUTH));
        }
    }

    public static void main(String[] args) throws Exception {
        ClashProxyClient client = new ClashProxyClient();
        client.loadConfig("config.yaml");
        client.start();
    }
}
```

### 範例 YAML 配置
以下是一個與上述程式碼相容的 `config.yaml` 範例：

```yaml
proxies:
  - name: proxy1
    type: socks5
    server: 192.168.1.100
    port: 1080
  - name: proxy2
    type: http
    server: 192.168.1.101
    port: 8080
rules:
  - DOMAIN,example.com,proxy1
  - IP-CIDR,192.168.0.0/16,DIRECT
```

### 核心邏輯說明
- **YAML 解析**：`loadConfig` 方法使用 SnakeYAML 將 Clash 配置解析到 `ProxyConfig` 物件中，該物件保存代理定義和路由規則。
- **Netty 伺服器**：`start` 方法設定一個 Netty 伺服器，監聽埠 7890，使用 Netty 內建的 SOCKS5 編解碼器處理 SOCKS5 協定請求。
- **請求處理**：`ProxyHandler` 處理 SOCKS5 指令請求，應用路由規則，並選擇上游代理或直接連線。
- **路由**：`selectProxy` 方法（簡化版）將目的地位址與規則匹配以選擇適當的代理。
- **擴充性**：程式碼是模組化的，允許透過擴展 `ProxyHandler` 輕鬆加入新協定（例如 Shadowsocks）。

### 後續步驟
1. **協定支援**：為 Shadowsocks（使用 Bouncy Castle 進行加密）和 HTTP 代理加入處理器。
2. **進階路由**：使用正則表達式或規則引擎實作完整的 Clash 規則解析（例如 GEOIP、DOMAIN-SUFFIX）。
3. **DNS 處理**：整合 DNSJava 或自訂解析器以處理 Clash 的 DNS 設定。
4. **連線池**：使用 Netty 的 `ChannelPool` 來實現高效的上游連線。
5. **Spring Boot（可選）**：如果您偏好 Spring Boot，可以使用它來進行配置管理和監控的 REST 端點，但核心代理邏輯仍使用 Netty。

### 依賴項 (Maven)
將以下內容加入您的 `pom.xml`：

```xml
<dependencies>
    <dependency>
        <groupId>io.netty</groupId>
        <artifactId>netty-all</artifactId>
        <version>4.1.111.Final</version>
    </dependency>
    <dependency>
        <groupId>org.yaml</groupId>
        <artifactId>snakeyaml</artifactId>
        <version>2.3</version>
    </dependency>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-api</artifactId>
        <version>2.0.16</version>
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk18on</artifactId>
        <version>1.78.1</version>
    </dependency>
</dependencies>
```

這為 Clash 類 VPN 代理客戶端提供了一個基礎。您可以根據需求擴展它，加入更多協定支援、進階路由和 DNS 功能。如果您想深入了解任何特定部分，請告訴我！