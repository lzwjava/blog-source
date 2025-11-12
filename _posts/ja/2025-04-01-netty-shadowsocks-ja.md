---
audio: false
generated: true
lang: ja
layout: post
title: NettyによるShadowsocksクライアントの構築
translated: true
type: note
---

Nettyを使用してClashやオリジナルのShadowsocksクライアントのようなShadowsocksクライアントを構築するには、Shadowsocksプロトコルを理解し、Nettyの非同期でイベント駆動型のネットワークアプリケーションフレームワークを活用する必要があります。以下に、必要なステップと主要な概念を詳しく説明します：

**1. Shadowsocksプロトコルの理解**

Nettyに取り組む前に、Shadowsocksプロトコルを徹底的に理解する必要があります。大まかには以下のような流れです：

* **接続確立:** クライアントがShadowsocksサーバーへの接続を開始します。
* **認証と方式のネゴシエーション:** クライアントが選択した暗号化方式とパスワードをサーバーに送信して認証を行います。
* **アドレスエンコーディング:** クライアントが実際の宛先サーバーのターゲットアドレス（IPアドレスとポート）を特定のエンコード形式で送信します。
* **データ転送:** 認証とアドレスエンコーディングが成功した後、クライアントとShadowsocksサーバー間で交換されるすべてのデータは、合意された方式を使用して暗号化/復号化されます。

**実装が必要なプロトコルの主要な側面：**

* **方式とパスワードの処理:** 選択した暗号化方式（例：`aes-256-cfb`、`chacha20-ietf-poly1305`）とパスワードの保存と送信。
* **アドレスエンコーディング:** ターゲットアドレスを特定の形式（タイプバイト、アドレス、ポート）にエンコードします。タイプバイトは、アドレスがIPv4アドレス（0x01）、IPv6アドレス（0x04）、またはホスト名（0x03）のいずれであるかを示します。
* **暗号化と復号化:** 選択した暗号化および復号化アルゴリズムの実装。これには、`PyCryptodome`（Python）や`Bouncy Castle`（Java）などのライブラリが役立ちます。
* **TCP転送:** アプリケーションからの接続をリッスンし、トラフィックをShadowsocksトンネルを介して転送するローカルTCPサーバーを確立します。

**2. Nettyプロジェクトのセットアップ**

まず、プロジェクトにNettyの依存関係を含める必要があります（例：JavaプロジェクトでMavenまたはGradleを使用）。

**3. プロキシクライアントのためのコアNettyコンポーネント**

主に以下のNettyコンポーネントを使用します：

* **`Bootstrap`:** クライアント側アプリケーションの設定と起動に使用します。
* **`EventLoopGroup`:** クライアントのI/O操作を処理するイベントループを管理します。通常、非ブロッキングI/Oには`NioEventLoopGroup`を使用します。
* **`Channel`:** ネットワーク接続を表します。
* **`ChannelPipeline`:** インバウンドおよびアウトバウンドのイベントとデータを処理する`ChannelHandler`のチェーンです。
* **`ChannelHandler`:** 特定のイベントとデータ変換を処理するために実装するインターフェースです。Shadowsocksプロトコル用のカスタムハンドラーを作成します。
* **`ByteBuf`:** バイナリデータを扱うためのNettyのバッファーです。

**4. Nettyハンドラーを使用したShadowsocksプロトコルの実装**

Shadowsocksのロジックを実装するために、`ChannelPipeline`内にいくつかのカスタム`ChannelHandler`を作成する必要があります。以下に可能な構造を示します：

* **ローカルプロキシサーバーハンドラー (`ChannelInboundHandlerAdapter`):**
    * このハンドラーは、アプリケーションが接続するローカルサーバーソケット（例：`localhost:1080`）で実行されます。
    * ローカルアプリケーションから新しい接続が入ると、このハンドラーは以下を行います：
        * リモートのShadowsocksサーバーへの接続を確立します。
        * 初期接続リクエスト（ターゲットアドレス）をプロトコルに従ってエンコードした後、Shadowsocksサーバーに転送します。
        * ローカルアプリケーションとShadowsocksサーバー間のデータフローを管理します。

* **Shadowsocksクライアントエンコーダー (`ChannelOutboundHandlerAdapter`):**
    * このハンドラーは、Shadowsocksサーバーに送信されるデータのエンコードを担当します。
    * 以下を行います：
        * Shadowsocksプロトコルに従ってターゲットアドレスをエンコードします（タイプ、アドレス、ポート）。
        * 選択した暗号化方式を使用してデータを暗号化します。

* **Shadowsocksクライアントデコーダー (`ChannelInboundHandlerAdapter`):**
    * このハンドラーは、Shadowsocksサーバーから受信したデータのデコードを担当します。
    * 以下を行います：
        * 受信したデータを復号化します。

* **リモートサーバー転送ハンドラー (`ChannelInboundHandlerAdapter`):**
    * このハンドラーは、リモートのShadowsocksサーバーからデータを受信したときに呼び出されます。
    * 復号化されたデータを元のローカルアプリケーションに転送し戻します。

**5. Nettyパイプラインの構造例**

以下は、Shadowsocksサーバーへの接続に対する`ChannelPipeline`がどのように見えるかの簡略化された例です：

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

        // アウトバウンドハンドラー (Shadowsocksサーバーへ送信されるデータ)
        pipeline.addLast("encoder", new ShadowsocksClientEncoder(method, password));

        // インバウンドハンドラー (Shadowsocksサーバーから受信するデータ)
        pipeline.addLast("decoder", new ShadowsocksClientDecoder(method, password));
        pipeline.addLast("remoteForwarder", new RemoteServerForwardingHandler());
    }
}
```

また、ローカルプロキシサーバーの場合：

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

        // Shadowsocksサーバーへの接続を開始しデータを転送するハンドラー
        pipeline.addLast("localProxyHandler",
                new LocalProxyHandler(shadowsocksServerAddress, shadowsocksServerPort, method, password));
    }
}
```

**6. 主要な実装の詳細**

* **暗号化/復号化の実装:** `ShadowsocksClientEncoder`および`ShadowsocksClientDecoder`内で、選択した暗号化および復号化アルゴリズムを実装する必要があります。これには、外部ライブラリの使用が含まれる可能性があります。選択した方式で必要とされる場合、鍵導出と初期化ベクトルには注意してください。
* **`LocalProxyHandler`でのアドレスエンコーディング:** `LocalProxyHandler`がローカルアプリケーションから初期接続リクエストを受信すると、ターゲットアドレスとポートを抽出し、それらをShadowsocksサーバーに送信する前にShadowsocks形式にエンコードする必要があります。
* **`LocalProxyHandler`でのShadowsocksサーバーへの接続:** `LocalProxyHandler`は、設定されたShadowsocksサーバーへの接続を確立するために、別のNettyの`Bootstrap`を使用します。
* **データ転送:** Shadowsocksサーバーへの接続が確立されると、ハンドラーはローカルアプリケーションの接続とShadowsocksサーバーの接続の間でデータを効率的に転送する必要があります。両方の接続に対する`Channel`オブジェクトを管理する必要があるでしょう。
* **エラーハンドリング:** ネットワーク問題、プロトコルエラー、暗号化/復号化失敗に対する適切なエラーハンドリングを実装します。
* **並行性:** Nettyはそのイベントループモデルで並行性を効率的に処理します。状態を共有する必要がある場合、ハンドラーがスレッドセーフになるように設計されていることを確認してください。

**7. プロキシクライアントの起動**

ローカルプロキシサーバー（ローカル接続をリッスン）を起動し、設定を処理するためのメインクラスを作成する必要があります。

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
        // あなたの設定に置き換えてください
        int localPort = 1080;
        String serverAddress = "your_server_ip";
        int serverPort = 8388;
        String method = "aes-256-cfb";
        String password = "your_password";

        new ShadowsocksClient(localPort, serverAddress, serverPort, method, password).run();
    }
}
```

**8. 高度な考慮事項（Clashのような）**

Clashのようなクライアントを構築するには、より高度な機能を考慮する必要があります：

* **複数のプロキシプロトコル:** Clashは様々なプロキシプロトコル（Shadowsocks、SOCKS5、HTTP）をサポートしています。各プロトコル用のハンドラーを追加する必要があります。
* **ルールベースのルーティング:** Clashでは、ドメイン、IPアドレス、GEOIPなどに基づいてトラフィックをルーティングするルールを定義できます。これには、クライアント内にルールエンジンを実装することが含まれます。
* **設定管理:** ClashはYAML設定ファイルを使用します。このような設定を読み込み、解析する方法を実装する必要があります。
* **DNS処理:** ClashはしばしばDNSリクエストを傍受し、プロキシを介してそれらをルーティングします。DNS傍受と転送を実装する必要があります。
* **UDPサポート:** ShadowsocksはUDP転送もサポートしています。NettyのUDP機能を使用してUDP処理を実装する必要があります。
* **プラグインと拡張機能:** Clashにはプラグインシステムがあります。このようなシステムを実装すると、複雑さが大幅に増加します。

**まとめると、Nettyを使用した基本的なShadowsocksクライアントの構築には以下が含まれます：**

1.  Shadowsocksプロトコルの理解。
2.  Nettyプロジェクトのセットアップ。
3.  データのエンコード、デコード、転送のためのカスタム`ChannelHandler`の作成。
4.  暗号化および復号化ロジックの実装。
5.  アプリケーションからの接続を受け入れるローカルサーバーの起動。
6.  リモートのShadowsocksサーバーへの接続。

Clashのようなより機能豊富なクライアントを構築するには、ネットワーキング、プロキシプロトコル、およびより複雑なソフトウェアアーキテクチャに関するより深い理解が必要です。基本的なShadowsocksの実装から始め、必要に応じて機能を徐々に追加してください。詳細な情報については、公式のShadowsocksドキュメントとNettyの例を参照することを忘れないでください。