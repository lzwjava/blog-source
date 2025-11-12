---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio CodeでのSpring Bootアプリケーションのデバッグ
translated: true
type: note
---

Visual Studio Code (VSCode) で Maven Spring Boot プロジェクトをデバッグするには、以下の手順に従ってデバッグモードでアプリケーションをセットアップおよび実行できます。このガイドは、`pom.xml` ファイルと `@SpringBootApplication` でアノテーションされたメインクラスを持つ基本的な Maven Spring Boot プロジェクトがあることを前提としています。手順は以下の通りです。

### ステップ 1: 必要な拡張機能のインストール
始める前に、VSCode が Java と Spring Boot 開発に必要な拡張機能を備えていることを確認してください。
- **Java Extension Pack**: これには、デバッグ機能を提供する Red Hat による Language Support for Java など、Java 開発のための必須ツールが含まれています。
- **Spring Boot Extension Pack**: このパックは、Spring Boot Dashboard、Spring Boot Tools などの機能で Spring Boot 開発を強化します。

インストール方法:
1. VSCode を開きます。
2. 拡張機能ビュー (`Ctrl+Shift+X` または macOS では `Cmd+Shift+X`) に移動します。
3. "Java Extension Pack" と "Spring Boot Extension Pack" を検索し、それぞれの **インストール** をクリックします。

### ステップ 2: Maven Spring Boot プロジェクトを開く
- VSCode を起動し、**ファイル > フォルダを開く** を選択して `pom.xml` ファイルを含むディレクトリを選択し、プロジェクトフォルダを開きます。
- VSCode は `pom.xml` を検出し、Java Extension Pack が自動的にプロジェクトのインデックスを作成し、依存関係を解決します。これには少し時間がかかる場合があるため、プロセスが完了するまで待機します（右下のステータスバーに進行状況が表示されます）。

### ステップ 3: `launch.json` ファイルの作成または編集
デバッグを設定するには、VSCode で `launch.json` ファイルをセットアップする必要があります:
1. サイドバーの虫と再生アイコンをクリックするか、`Ctrl+Shift+D` を押して **実行とデバッグ** ビューを開きます。
2. デバッグ構成が存在しない場合は、**"launch.json ファイルを作成"** をクリックします。既に存在する場合は、歯車アイコンをクリックして編集します。
3. プロンプトが表示されたら、環境として **Java** を選択します。VSCode はプロジェクト内の `.vscode` フォルダにデフォルトの `launch.json` ファイルを生成します。
4. Spring Boot アプリケーション用のデバッグ構成を追加または変更します。以下は設定例です:

    ```json
    {
        "type": "java",
        "name": "Debug Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - `"com.example.demo.DemoApplication"` をメインクラスの完全修飾名（例: `com.yourcompany.yourapp.YourApplication`）に置き換えてください。
    - `"demo"` をプロジェクト名（通常は `pom.xml` の `<artifactId>`）に置き換えてください。

5. `launch.json` ファイルを保存します。

#### オプション: 引数の追加
アプリケーションに特定の引数（例: Spring プロファイル）が必要な場合は、それらを含めることができます:
```json
{
    "type": "java",
    "name": "Debug Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### ステップ 4: デバッグの開始
- **実行とデバッグ** ビューで、上部のドロップダウンメニューから **"Debug Spring Boot"** を選択します。
- 緑色の再生ボタンをクリックするか (`F5` を押す)、アプリケーションをデバッグモードで起動します。
- VSCode は Maven を使用してプロジェクトをコンパイルし、Spring Boot アプリケーションを起動し、デバッガを自動的にアタッチします。

### ステップ 5: ブレークポイントの設定とデバッグ
- プロジェクト内の Java ファイル（例: コントローラやサービスクラス）を開きます。
- 行番号の左側の余白をクリックしてブレークポイントを設定します。赤い点が表示されます。
- アプリケーションと対話します（例: ブラウザや API クライアント経由）。実行がブレークポイントに達すると、VSCode は一時停止し、以下を行うことができます:
  - **変数** パネルで変数を検査します。
  - **ステップオーバー** (`F10`)、**ステップイン** (`F11`)、**続行** (`F5`) などのコントロールを使用してコードをステップ実行します。
  - 呼び出しスタックなどをデバッグサイドバーで表示します。

### 代替方法
`launch.json` メソッドは柔軟性が高く推奨されますが、以下を使用してデバッグすることもできます:
- **Maven ビュー**:
  1. サイドバーの Maven ビューを開きます（"M" アイコンを探すか、拡張機能から有効にします）。
  2. プロジェクトを展開し、Plugins の下の `spring-boot` に移動し、`spring-boot:run` を右クリックして **デバッグ** を選択します。
  3. アプリケーションが起動し、デバッガがアタッチされます。
- **Spring Boot Dashboard**:
  1. Spring Boot Dashboard を開きます（通常はエクスプローラビューまたはコマンドパレット: `Spring Boot Dashboard` から）。
  2. アプリケーションを見つけ、右クリックして **デバッグ** を選択します（利用可能な場合）。

### 前提条件と注意点
- システムに **Maven** がインストールされ、コマンドラインからアクセス可能であることを確認するか、VSCode の組み込み Maven（必要に応じて設定で構成）に依存してください。
- デバッグ中のランタイムエラーを避けるため、プロジェクトが正常にビルドされることを確認してください (`mvn clean install`)。
- `pom.xml` で指定された互換性のある Java バージョン（例: `<java.version>` 経由）を使用してください。

これらの手順に従うことで、VSCode で Maven Spring Boot プロジェクトを効果的にデバッグし、その強力なデバッグツールを活用してコード内の問題を特定および解決できます。