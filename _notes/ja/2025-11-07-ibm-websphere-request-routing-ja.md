---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-4.5-sonnet
title: IBM WebSphere リクエストルーティングの解説
translated: true
---

IBM WebSphere Application Server (WAS) が受信リクエストとルーティングをどのように処理するか説明します：

## IBM WAS におけるリクエストフロー

IBM WAS にリクエストが届くと、典型的なフローは以下の通りです：

**1. Web サーバーレイヤー（オプション）**
- リクエストは最初に IBM HTTP Server (IHS) または別の Web サーバーに到達します
- Web サーバープラグインが適切な WAS インスタンスにルーティングします

**2. Web コンテナーのエントリーポイント**
リクエストは **Web コンテナー** を通じて WAS に入ります。これはメインのサーブレットエンジンの一部です。主要なパッケージ構造は以下の通りです：

```
com.ibm.ws.webcontainer.*
```

**3. リクエスト処理チェーン**

ルーティングはいくつかのコンポーネントを通じて行われます：

**トランスポートチャネルフレームワーク**
- `com.ibm.ws.channel.*` - ネットワーク通信を処理します
- HTTP トランスポートチャネルがリクエストを受信します

**Web コンテナー処理**
```
com.ibm.ws.webcontainer.servlet.ServletWrapper
com.ibm.ws.webcontainer.filter.WebAppFilterManager
```

**4. フィルターチェーンの実行**

フィルターは標準の Java Servlet フィルターとまったく同じように動作しますが、WAS によって管理されます：

- **アプリケーションの web.xml で定義** されます
- フィルターは指定された順序でチェーンされます
- 各フィルターはリクエストとレスポンスを検査/変更できます
- 標準の `javax.servlet.Filter` インターフェースを使用します

```xml
<filter>
    <filter-name>MyFilter</filter-name>
    <filter-class>com.example.MyFilter</filter-class>
</filter>

<filter-mapping>
    <filter-name>MyFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

**フィルター実行順序：**
1. WAS はアプリケーション起動時にフィルター設定をロードします
2. WebAppFilterManager がフィルターチェーンを作成します
3. 各リクエストで：リクエスト → フィルター1 → フィルター2 → ... → サーブレット

## IBM WAS の主要パッケージ

**コアパッケージ：**
- `com.ibm.ws.webcontainer.*` - Web コンテナー実装
- `com.ibm.ws.runtime.*` - ランタイムサービス
- `com.ibm.websphere.servlet.*` - WAS 固有のサーブレット拡張
- `com.ibm.ws.channel.*` - トランスポート層
- `com.ibm.ejs.*` - EJB コンテナーサービス
- `com.ibm.ws.naming.*` - JNDI 実装

## ルーティングメカニズム

**バーチャルホストルーティング：**
- WAS 管理コンソールで設定されます
- `ホスト名:ポート` の組み合わせをアプリケーションにマッピングします
- 設定：`バーチャルホスト → ホストエイリアス → アプリケーション`

**コンテキストルートルーティング：**
- 各アプリケーションはコンテキストルートを持ちます（例：`/myapp`）
- WAS はデプロイされたアプリケーションのレジストリを維持します
- URI マッピング：`http://server:port/contextRoot/servletPath`

**サーブレットマッピング：**
- web.xml またはアノテーションで定義されます
- パターンマッチング（完全一致、パス、拡張子、デフォルト）

## アプリケーション起動シーケンス

アプリケーション起動時：
1. **クラスローダーの初期化** - アプリケーション独自のクラスローダーを取得します
2. **web.xml のパース** - フィルター、サーブレット、リスナーがロードされます
3. **ServletContextListener の発火** - `contextInitialized()`
4. **フィルターのインスタンス化** - `init()` メソッドが呼び出されます
5. **load-on-startup サーブレット** - 早期初期化サーブレットを初期化します
6. **アプリケーションが STARTED とマーク** - リクエストを受け入れる準備が整います

ルーティングレジストリが更新され、アプリケーションはコンテキストルートで利用可能になります。

これで WAS がリクエストルーティングとフィルタリングをどのように処理するか明確になりましたか？