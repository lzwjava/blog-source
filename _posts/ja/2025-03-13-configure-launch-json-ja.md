---
audio: false
generated: true
lang: ja
layout: post
title: VSCodeでのSpring Boot用launch.jsonの設定
translated: true
type: note
---

Visual Studio Code (VSCode) で Maven Spring Boot プロジェクトの `launch.json` ファイルを設定するには、VSCode が Java 拡張機能を使用してアプリケーションを実行およびデバッグできるように起動設定を構成する必要があります。以下に、これを実現するためのステップバイステップガイドを示します。

### 前提条件
進める前に以下を確認してください：
- VSCode に **Java Extension Pack** がインストールされていること。このパックには、Spring Boot プロジェクトを含む Java アプリケーションの実行とデバッグをサポートする、Red Hat による「Debugger for Java」や「Language Support for Java」などの必須拡張機能が含まれています。
- あなたの Spring Boot プロジェクトが有効な `pom.xml` ファイルを持つ Maven プロジェクトであること。
- プロジェクトに、アプリケーションを起動するための `main` メソッドを含む `@SpringBootApplication` アノテーションが付けられたメインクラスがあること。

### `launch.json` の設定手順
1. **メインクラスの特定**
   - 典型的な Spring Boot プロジェクトでは、メインクラスは `src/main/java` ディレクトリにあり、`@SpringBootApplication` アノテーションが付けられています。例えば、`com.example.demo.DemoApplication` という名前かもしれません。
   - VSCode でプロジェクトを開き、このクラスの完全修飾名 (例: `com.example.demo.DemoApplication`) を特定してください。

2. **プロジェクト名の決定**
   - Maven プロジェクトにおけるプロジェクト名は、`pom.xml` ファイルで定義された `artifactId` に対応します。
   - `pom.xml` ファイルを開き、`<artifactId>` タグを探してください。例：
     ```xml
     <artifactId>demo</artifactId>
     ```
     ここでは、プロジェクト名は `demo` となります。

3. **デバッグビューの表示**
   - VSCode で、左サイドバーの **デバッグ** アイコンをクリックするか (Mac では `Ctrl+Shift+D` / `Cmd+Shift+D` を押します)、
   - 「実行とデバッグ」ドロップダウンの横にある歯車アイコン ⚙️ をクリックして起動設定を構成します。`launch.json` が存在しない場合、VSCode は作成するよう促します。

4. **`launch.json` の作成または編集**
   - 環境の選択を促された場合は、**Java** を選択してください。これにより、プロジェクトの `.vscode` フォルダに基本的な `launch.json` ファイルが生成されます。
   - `launch.json` ファイルを開きます。既に存在する場合は、直接編集できます。

5. **起動設定の追加**
   - `launch.json` 内の `"configurations"` 配列内に以下の設定を追加します。プレースホルダーをあなたのプロジェクトの詳細に置き換えてください：
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **フィールドの説明:**
       - `"type": "java"`: これが Java の起動設定であることを指定します。
       - `"name": "Launch Spring Boot App"`: デバッグドロップダウンに表示される、この設定の説明的な名前。
       - `"request": "launch"`: VSCode がアプリケーションを起動するべきであることを示します (既存のプロセスへのアタッチとは対照的)。
       - `"mainClass"`: Spring Boot メインクラスの完全修飾名 (例: `com.example.demo.DemoApplication`)。
       - `"projectName"`: あなたの `pom.xml` からの `artifactId` (例: `demo`)。これは、マルチモジュール設定で VSCode がプロジェクトを見つけるのに役立ちます。

   - この設定を含む完全な `launch.json` ファイルの例を以下に示します：
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **オプション: VM 引数またはプログラム引数の追加**
   - アプリケーションに追加の設定 (例: Spring プロファイルの有効化) が必要な場合は、`"vmArgs"` または `"args"` を使用して追加できます：
     - Spring プロファイルを使用した例：
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       これは `spring.profiles.active` プロパティを `dev` に設定します。
     - プログラム引数の例：
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **保存と実行**
   - `launch.json` ファイルを保存します。
   - デバッグビューに戻り、ドロップダウンから **"Launch Spring Boot App"** を選択し、緑色の再生ボタンをクリックするか (`F5` を押します)。
   - VSCode は Maven と Java 拡張機能を使用してあなたの Spring Boot アプリケーションをビルドし実行します。デバッグコンソールに Spring Boot の起動ログが表示されるはずです。

### 設定の確認
- あなたの Spring Boot アプリケーションが Web アプリケーションの場合、ブラウザを開いて `http://localhost:8080` (または `application.properties` または `application.yml` ファイルで指定されたポート) に移動し、実行されていることを確認してください。
- コードにブレークポイントを設定し、デバッグコントロール (一時停止、ステップオーバーなど) を使用してアプリケーションをデバッグすることもできます。

### 注意点
- VSCode の Java 拡張機能は、`pom.xml` に基づいてクラスパスとビルドプロセスを自動的に処理するため、通常、事前に `mvn clean install` を手動で実行する必要はありません。
- プロジェクトがマルチモジュール Maven 設定の一部である場合、`projectName` が正しいモジュールの `artifactId` と一致していることを確認してください。
- 高度な設定 (例: カスタム作業ディレクトリや起動前タスク) については、[VSCode Java デバッグドキュメント](https://code.visualstudio.com/docs/java/java-debugging)を参照してください。

このセットアップにより、VSCode で Maven Spring Boot プロジェクトを実行およびデバッグするための `launch.json` が正しく設定されるはずです！