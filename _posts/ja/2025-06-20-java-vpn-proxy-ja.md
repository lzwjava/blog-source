---
audio: false
generated: true
lang: ja
layout: post
title: Nettyを使用したJava VPNプロキシクライアント
translated: true
type: note
---

NettyまたはSpring Bootを使用してJavaでClash VPNプロキシクライアントを構築するには、ネットワーキング、YAML設定パーシング、SOCKS、HTTP、Shadowsocksなどのプロキシプロトコルを扱うための堅牢なフレームワークが必要です。Nettyは高性能なネットワーキングに理想的であり、Spring Bootは設定と依存関係管理を簡素化できます。以下では、低レベルのプロキシ操作により適しているNettyをネットワーキングレイヤーとして焦点を当て、コアロジック、主要ライブラリ、およびサンプル実装を概説します。このクライアントは人気のあるClash YAML設定（プロキシ、ルール、DNSなど）をサポートします。

### メインロジック
1. **設定パーシング**:
   - プロキシサーバー、ルール、DNS設定を含むClash互換のYAML設定ファイル（例: `config.yaml`）をパースします。
   - 一般的なプロキシタイプをサポート: HTTP、SOCKS5、Shadowsocksなど。
   - YAMLフィールドをJavaオブジェクトにマッピングして簡単にアクセスできるようにします。

2. **プロキシサーバーセットアップ**:
   - 受信クライアント接続をリッスンするNettyサーバーを初期化します（例: ローカルポート7890）。
   - クライアントリクエストを受け入れるためにSOCKS5/HTTPプロキシプロトコルを処理します。

3. **ルーティングとルール処理**:
   - YAML設定で定義されたルールベースのルーティング（ドメイン、IP、またはジオベース）を実装します。
   - クライアントリクエストを適切な上流プロキシサーバーまたは直接接続にルーティングします。

4. **接続管理**:
   - Nettyのイベント駆動モデルを使用して、クライアントからプロキシ、プロキシから宛先への接続を管理します。
   - 効率化のために接続プーリングとキープアライブをサポートします。

5. **DNS解決**:
   - 設定で指定されたDNSクエリを処理します（例: 上流DNSまたはローカルリゾルバを使用）。
   - 設定されている場合はDNS over HTTPS (DoH) または他のセキュアなプロトコルをサポートします。

6. **プロトコル処理**:
   - Shadowsocks（例: AEAD暗号化）、SOCKS5、HTTPに対するプロトコル固有のロジックを実装します。
   - 拡張性をサポートするためにプラグ可能なプロトコルハンドラーを使用します。

7. **エラーハンドリングとロギング**:
   - 接続失敗、無効な設定、またはサポートされていないプロトコルを適切に処理します。
   - デバッグのための詳細なログを提供します。

### 主要ライブラリ
- **Netty**: 高性能なネットワーキングとイベント駆動I/Oのため。クライアント接続、プロキシ転送、プロトコルエンコーディング/デコーディングを処理します。
- **SnakeYAML**: Clash互換のYAML設定ファイルをパースするため。
- **Bouncy Castle**: 暗号化操作（例: Shadowsocks AEAD暗号化）のため。
- **SLF4J**: ロギングのため。
- **Apache Commons**: ユーティリティ関数（例: 設定バリデーション）のため。
- **Jackson (オプション)**: YAMLまたは追加の設定フォーマットに対してJSONライクな処理を希望する場合。
- **DNSJava (オプション)**: カスタムDNS解決が必要な場合。

### コア実装
以下は、ClashライクなVPNプロキシクライアントの簡略化されたNettyベースの実装です。焦点は以下にあります:
- Clash YAML設定のパース。
- SOCKS5プロキシサーバーのセットアップ。
- リクエストを上流プロキシまたは宛先に転送。
- 基本的なルールベースのルーティング。

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

    // パースされたYAMLデータを保持する設定クラス
    static class ProxyConfig {
        List<Map<String, String>> proxies;
        List<String> rules;

        public ProxyConfig(Map<String, Object> config) {
            this.proxies = (List<Map<String, String>>) config.get("proxies");
            this.rules = (List<String>) config.get("rules");
        }
    }

    // Clash YAML設定をロード
    public void loadConfig(String configPath) throws Exception {
        Yaml yaml = new Yaml();
        try (FileReader reader = new FileReader(configPath)) {
            config = yaml.load(reader);
            logger.info("設定を {} からロードしました", configPath);
        }
    }

    // プロキシサーバーを起動
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
                            // SOCKS5プロトコルハンドラーを追加
                            pipeline.addLast(new Socks5ServerEncoder());
                            pipeline.addLast(new Socks5InitialRequestDecoder());
                            pipeline.addLast(new Socks5InitialRequestHandler());
                            pipeline.addLast(new Socks5CommandRequestDecoder());
                            pipeline.addLast(new ProxyHandler(new ProxyConfig(config)));
                        }
                    });

            ChannelFuture future = bootstrap.bind(DEFAULT_PORT).sync();
            logger.info("プロキシサーバーをポート {} で起動しました", DEFAULT_PORT);
            future.channel().closeFuture().sync();
        } finally {
            bossGroup.shutdownGracefully();
            workerGroup.shutdownGracefully();
        }
    }

    // SOCKS5コマンドリクエストを処理し、トラフィックをルーティング
    static class ProxyHandler extends SimpleChannelInboundHandler<Socks5CommandRequest> {
        private final ProxyConfig config;

        public ProxyHandler(ProxyConfig config) {
            this.config = config;
        }

        @Override
        protected void channelRead0(ChannelHandlerContext ctx, Socks5CommandRequest request) {
            String destination = request.dstAddr() + ":" + request.dstPort();
            logger.info("{} へのリクエストを処理中", destination);

            // シンプルなルールベースのルーティング（実際のルールパーシングで拡張）
            String selectedProxy = selectProxy(destination);
            if (selectedProxy != null) {
                logger.info("プロキシにルーティング: {}", selectedProxy);
                // プロキシ転送ロジックをここに実装
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.SUCCESS, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            } else {
                logger.warn("{} に一致するプロキシが見つかりません", destination);
                ctx.write(new DefaultSocks5CommandResponse(
                        Socks5CommandStatus.FAILURE, request.dstAddrType(),
                        request.dstAddr(), request.dstPort()));
            }
        }

        private String selectProxy(String destination) {
            // ルールベースのプロキシ選択を実装
            for (String rule : config.rules) {
                // 例: ドメインまたはIPルールに一致
                if (destination.matches(rule)) {
                    return config.proxies.get(0).get("name"); // 簡略化
                }
            }
            return null; // 直接接続またはフォールバック
        }
    }

    // SOCKS5初期リクエストを処理
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

### サンプルYAML設定
上記のコードと互換性のある `config.yaml` の例:

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

### コアロジックの説明
- **YAMLパーシング**: `loadConfig` メソッドはSnakeYAMLを使用してClash設定を `ProxyConfig` オブジェクトにパースします。このオブジェクトはプロキシ定義とルーティングルールを保持します。
- **Nettyサーバー**: `start` メソッドはポート7890でリッスンするNettyサーバーをセットアップし、Nettyの組み込みSOCKS5コーデックを使用してSOCKS5プロトコルリクエストを処理します。
- **リクエスト処理**: `ProxyHandler` はSOCKS5コマンドリクエストを処理し、ルーティングルールを適用し、上流プロキシまたは直接接続を選択します。
- **ルーティング**: `selectProxy` メソッド（簡略化）は宛先アドレスをルールと照合して適切なプロキシを選択します。
- **拡張性**: コードはモジュール式であり、`ProxyHandler` を拡張することで新しいプロトコル（例: Shadowsocks）を簡単に追加できます。

### 次のステップ
1. **プロトコルサポート**: Shadowsocks（暗号化にBouncy Castleを使用）およびHTTPプロキシのハンドラーを追加。
2. **高度なルーティング**: 正規表現またはルールエンジンを使用した完全なClashルールパーシング（例: GEOIP、DOMAIN-SUFFIX）を実装。
3. **DNS処理**: ClashのDNS設定のためにDNSJavaまたはカスタムリゾルバを統合。
4. **接続プーリング**: 効率的な上流接続のためにNettyの `ChannelPool` を使用。
5. **Spring Boot (オプション)**: Spring Bootを設定管理と監視のためのRESTエンドポイントに使用することを希望する場合、コアプロキシロジックにはNettyを維持。

### 依存関係 (Maven)
これらを `pom.xml` に追加:

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

これはClashライクなVPNプロキシクライアントの基盤を提供します。より多くのプロトコルのサポート、高度なルーティング、DNS機能を追加することで拡張できます。特定の部分についてさらに深く掘り下げたい場合はお知らせください！