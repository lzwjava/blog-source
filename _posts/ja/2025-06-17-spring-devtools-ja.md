---
audio: false
generated: true
lang: ja
layout: post
title: Spring Boot DevToolsによる自動再起動
translated: true
type: note
---

`mvn spring-boot:run`を使用してSpring Bootアプリケーションを実行する場合、ファイルウォッチャーや自動再起動、ホットリロード機能はデフォルトでは有効になりません。ただし、`spring-boot-devtools`依存関係をプロジェクトに追加することでこれらを有効にできます。このモジュールは、自動再起動やLiveReloadなどの機能を提供し、開発を高速化します。

### 詳細
1. **DevToolsなしのデフォルト動作**:
   - `spring-boot-devtools`なしで`mvn spring-boot:run`を実行すると、ファイルウォッチャーや自動再起動は含まれません。Javaクラス、静的リソース、またはテンプレートへの変更を適用するには、アプリケーションを手動で停止して再起動する必要があります。
   - 静的リソース（HTML、CSS、JSなど）は、別途設定されていない限り、完全なリビルドまたは再起動が必要になる場合があります。

2. **`spring-boot-devtools`を使用する場合**:
   - **ファイルウォッチャー**: DevToolsは、Javaファイル、プロパティ、および特定のリソース（`/resources`、`/static`、`/templates`など）への変更をクラスパスで監視します。
   - **自動再起動**: クラスパス上のファイル（Javaクラスやプロパティファイルなど）が変更されると、DevToolsはアプリケーションの自動再起動をトリガーします。これは、変更のないサードパーティライブラリ用（ベースクラスローダー）とアプリケーションコード用（再起動クラスローダー）の2つのクラスローダーを使用するため、コールドスタートよりも高速です。[](https://docs.spring.io/spring-boot/reference/using/devtools.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - **LiveReload**: 静的リソース（`/static`、`/public`、`/templates`内のHTML、CSS、JS）またはテンプレート（Thymeleafなど）への変更は、完全な再起動の代わりにブラウザのリフレッシュをトリガーします（LiveReloadブラウザ拡張機能がインストールされている場合）。[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)
   - **除外設定**: デフォルトでは、`/META-INF/maven`、`/META-INF/resources`、`/resources`、`/static`、`/public`、`/templates`内のリソースは再起動をトリガーしませんが、LiveReloadはトリガーします。これは`spring.devtools.restart.exclude`でカスタマイズできます。[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

3. **DevToolsのセットアップ**:
   `pom.xml`に以下の依存関係を追加します:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - `<optional>true</optional>`により、DevToolsが本番ビルドに含まれないようになります。[](https://www.concretepage.com/spring-boot/spring-boot-automatic-restart-using-developer-tools-with-maven)
   - `mvn spring-boot:run`でアプリケーションを実行します。DevToolsは自動的にファイル監視と自動再起動を有効にします。

4. **IDEでの動作**:
   - **Eclipse**: 変更を保存（Ctrl+S）すると自動的にビルドがトリガーされ、DevToolsが検知してアプリケーションを再起動します。[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)
   - **IntelliJ IDEA**: DevToolsが変更を検知するには、手動でビルドをトリガー（Ctrl+F9または「Make Project」）する必要があります。自動ビルドを設定していない場合を除きます。シームレスな再起動のために、IntelliJ設定で「Build project automatically」を有効にすることもできます。[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-restart-and-live-reload-in-intellij-idea)
   - LiveReloadの場合、http://livereload.com/extensions/ からブラウザ拡張機能をインストールして有効にします。[](https://www.codejava.net/frameworks/spring-boot/spring-boot-auto-reload-changes-using-livereload-and-devtools)

5. **代替案: Spring Loaded**:
   - DevToolsの代わりに、Spring Loadedを使用してより高度なホットスワッピング（メソッドシグネチャの変更など）を実現できます。`spring-boot-maven-plugin`に追加します:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - Spring LoadedはDevToolsほど活発にメンテナンスされておらず、すべてのフレームワークをサポートするわけではないため、推奨度は低いです。[](https://docs.spring.io/spring-boot/docs/1.5.7.RELEASE/reference/html/howto-hotswapping.html)[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/howto-hotswapping.html)

6. **静的リソースのホットリロード**:
   - DevToolsなしで静的リソースのホットリロードを有効にするには、`spring-boot-maven-plugin`の`addResources`プロパティを設定します:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - これにより`src/main/resources`がクラスパスに追加され、静的ファイルのその場での編集が可能になりますが、DevToolsほど包括的ではありません。[](https://docs.spring.io/spring-boot/maven-plugin/run.html)

7. **注意点**:
   - DevToolsはマルチモジュールプロジェクトでクラスローディングの問題を引き起こす可能性があります。これが発生した場合は、`spring.devtools.restart.enabled=false`で再起動を無効にするか、高度なリロードにJRebelを使用してみてください。[](https://docs.spring.io/spring-boot/reference/using/devtools.html)
   - クラスパス外のファイルの場合、`spring.devtools.restart.additional-paths`を使用して追加のディレクトリを監視します。[](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-devtools.html)
   - LiveReloadはブラウザ拡張機能を必要とし、すべてのフロントエンド設定（Webpackを使用したReactなど）で動作するとは限りません。[](https://stackoverflow.com/questions/49888724/hot-reload-for-spring-boot-backend-frontend)
   - 再起動が遅い場合は、`spring.devtools.restart.poll-interval`と`spring.devtools.restart.quiet-period`を調整してファイル監視を最適化します。[](https://docs.spring.io/spring-boot/reference/using/devtools.html)

### シンプルなアプリの手順
1. 基本的なSpring Bootアプリを作成します（例: Spring Initializrで`spring-boot-starter-web`を使用）。
2. `spring-boot-devtools`依存関係を`pom.xml`に追加します。
3. `mvn spring-boot:run`を実行します。
4. Javaファイル、プロパティファイル、または静的リソース（`src/main/resources/static`内のHTMLなど）を変更します。
5. 自動再起動（Java/プロパティ用）またはブラウザリフレッシュ（LiveReloadが有効な静的リソース用）を確認します。

### 例
RESTコントローラを持つシンプルなアプリの場合:
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- DevToolsを追加し、`mvn spring-boot:run`を実行して、`hello()`メソッドの戻り値を変更します。アプリは自動的に再起動します。
- `src/main/resources/static`に`index.html`を追加し、LiveReload拡張機能をインストールしてHTMLを変更します。ブラウザは再起動なしでリフレッシュされます。

### 結論
シンプルなSpring Bootアプリの場合、`spring-boot-devtools`を追加することが、ファイルウォッチャー、自動再起動、ホットリロードを有効にする最も簡単な方法です。シームレスな開発体験のために、DevToolsを使用して`mvn spring-boot:run`を実行してください。より高度なホットスワッピングが必要な場合は、Spring LoadedまたはJRebelを検討してくださいが、ほとんどの場合DevToolsで十分です。[](https://www.geeksforgeeks.org/hot-reload-with-spring-boot-devtools/)[](https://docs.spring.io/spring-boot/how-to/hotswapping.html)

---

以下は、`application.yml`ファイルを使用してSpring Bootアプリケーションで`spring-boot-devtools`をファイル監視、自動再起動、ホットリロード用に設定する方法の例です。この設定は、DevToolsがアクティブで`target/classes`を監視していることを示す提供されたログに基づいて、`blog-server`プロジェクト用に調整されています。

### `application.yml`設定
```yaml
spring:
  devtools:
    restart:
      # 自動再起動を有効化 (デフォルト: true)
      enabled: true
      # 再起動をトリガーするために監視する追加ディレクトリ (例: カスタム設定フォルダ)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # 再起動をトリガーしないファイル/ディレクトリ (デフォルトの除外を維持)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # ファイル変更のポーリング間隔 (ミリ秒、デフォルト: 1000)
      poll-interval: 1000
      # ファイル変更後の再起動前のクワイエット期間 (ミリ秒、デフォルト: 400)
      quiet-period: 400
      # オプション: 手動で再起動をトリガーするファイル
      trigger-file: .restart
    livereload:
      # 静的リソース変更時のブラウザリフレッシュ用LiveReloadを有効化 (デフォルト: true)
      enabled: true
```

### 設定の説明
- **`spring.devtools.restart.enabled`**: クラスパスファイルの変更時に自動再起動を有効にします（ログで確認された`target/classes`など）。
- **`spring.devtools.restart.additional-paths`**: 追加のディレクトリ（例: `/home/lzw/Projects/blog-server/config`）を監視して変更時に再起動をトリガーします。
- **`spring.devtools.restart.exclude`**: `static/`、`public/`、`templates/`、`logs/`、`generated/`ディレクトリへの変更による再起動を防ぎ、静的リソース（HTML、CSS、JSなど）用のLiveReloadは許可します。
- **`spring.devtools.restart.poll-interval`**: DevToolsがファイル変更をチェックする頻度を設定します（1000ms = 1秒）。
- **`spring.devtools.restart.quiet-period`**: 変更を検出後、保留中の変更がさらにないことを確認するために400ms待機してから再起動します。
- **`spring.devtools.restart.trigger-file`**: `.restart`を更新することで手動再起動を可能にします（例: `touch /home/lzw/Projects/blog-server/.restart`）。
- **`spring.devtools.livereload.enabled`**: LiveReloadサーバーを有効にし、`static/`や`templates/`内の変更時にブラウザリフレッシュをトリガーします（LiveReloadブラウザ拡張機能が必要）。

### 適用手順
1. 上記の設定で`src/main/resources/application.yml`を作成または更新します。
2. `spring-boot-devtools`が`pom.xml`にあることを確認します:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. `mvn spring-boot:run`を実行します。DevToolsは`target/classes`と`/home/lzw/Projects/blog-server/config`（追加した場合）を監視し、Javaやプロパティファイルの変更時にアプリを再起動し、静的リソースの変更時にブラウザをリフレッシュします。
4. LiveReloadの場合、ブラウザ拡張機能（例: http://livereload.com/extensions/ から）をインストールするか、フロントエンドにLiveReloadクライアントを統合します。

### 注意点
- ログでは高速な起動（0.8秒）が示されているため、デフォルトの`poll-interval`と`quiet-period`で問題ないはずです。大規模なプロジェクトで再起動が遅く感じる場合は調整してください（例: `poll-interval: 500`）。
- LiveReloadが必要ない場合（例: 別のフロントエンド開発サーバーを使用）、`livereload.enabled: false`を設定します。
- 手動再起動の場合、プロジェクトルートに`.restart`を作成し、必要時に更新します。

このYAML設定は、既に確認しているファイル監視と自動再起動機能を強化し、あなたのセットアップとシームレスに連携するはずです。