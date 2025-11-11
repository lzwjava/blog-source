---
audio: false
generated: true
lang: ja
layout: post
title: Visual Studio CodeにおけるJavaランタイム
translated: true
type: note
---

Visual Studio Code (VS Code) の設定で `java.configuration.runtimes` を使用するには、`settings.json` ファイルで設定を行う必要があります。この設定により、VS Code が Java プロジェクトで使用できる複数の Java Development Kit (JDK) バージョンを指定できます。特に、異なる Java バージョンを必要とする様々なプロジェクトで作業する際に便利です。設定方法をステップバイステップで説明します：

### `java.configuration.runtimes` の設定手順

1.  **VS Code 設定を開く**:
    - Windows/Linux: `ファイル > 基本設定 > 設定` に移動するか、`Ctrl + ,` を押します。
    - macOS: `Code > 基本設定 > 設定` に移動するか、`Cmd + ,` を押します。

2.  **JSON 設定ファイルにアクセスする**:
    - 設定 UI で `java.configuration.runtimes` を検索します。
    - 「Java: 構成: ランタイム」のようなオプションが表示されます。設定説明の下にある「settings.json で編集」 (通常はリンク) をクリックして `settings.json` ファイルを開きます。

3.  **`settings.json` を編集する**:
    - `settings.json` ファイルで、`java.configuration.runtimes` 配列を追加または変更します。この配列には、VS Code に認識させたい JDK バージョンをそれぞれ表すオブジェクトが含まれます。
    - 各オブジェクトには通常、以下が含まれます：
        - `name`: Java バージョン識別子 (例: `JavaSE-1.8`, `JavaSE-11`, `JavaSE-17`)。
        - `path`: システム上の JDK インストールディレクトリへの絶対パス。
        - `default` (オプション): アンマネージドフォルダ (Maven や Gradle などのビルドツールがないプロジェクト) のデフォルト JDK とする場合は `true` に設定します。

    設定例：

    ```json
    {
        "java.configuration.runtimes": [
            {
                "name": "JavaSE-1.8",
                "path": "C:/Program Files/Java/jdk1.8.0_351",
                "default": true
            },
            {
                "name": "JavaSE-11",
                "path": "C:/Program Files/Java/jdk-11.0.15"
            },
            {
                "name": "JavaSE-17",
                "path": "C:/Program Files/Java/jdk-17.0.6"
            }
        ]
    }
    ```

4.  **JDK パスを確認する**:
    - `path` が JDK インストールのルートディレクトリ (`java.exe` または `java` を含む `bin` フォルダがある場所) を指していることを確認してください。
    - Windows では、パス内でスラッシュ (`/`) を使用するか、バックスラッシュをエスケープします (`\\`)。
    - macOS/Linux では、適切なファイルシステムパスを使用します (例: `/usr/lib/jvm/java-17-openjdk`)。

5.  **保存して再読み込みする**:
    - `settings.json` ファイルを保存します。
    - VS Code を再起動するか、ウィンドウを再読み込みします (`Ctrl + R` または `Cmd + R`)。

6.  **構成を確認する**:
    - コマンドパレット (`Ctrl + Shift + P` または `Cmd + Shift + P`) を開き、`Java: Configure Java Runtime` コマンドを実行します。
    - これにより、プロジェクトで利用可能な JDK が表示されるビューが開きます。「Project JDKs」タブの下に設定したランタイムが表示されていることを確認します。

### 動作の仕組み
- **アンマネージドフォルダ**: ビルドツールがないプロジェクト (例: プレーンな Java ファイル) の場合、VS Code は `java.configuration.runtimes` で指定された `default` JDK を使用します。
- **マネージドプロジェクト (Maven/Gradle)**: ビルドツールを使用するプロジェクトの場合、JDK バージョンはビルド構成 (例: `pom.xml` または `build.gradle`) によって決定されますが、互換性のためにここにリストされたランタイムを VS Code は認識します。
- **Language Server**: Java Language Server (Java 拡張機能の一部) は実行に JDK 17+ を必要とします。必要に応じて、`java.jdt.ls.java.home` で個別に指定できます (例: `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`)。

### 複数 JDK の使用例
Mac で Homebrew 経由で JDK 8 と 17 をインストールしている場合、構成は以下のようになります：

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### ヒント
- 正しい `name` フォーマット (`JavaSE-<バージョン>`) を使用してください。Java バージョンと一致させること (例: Java 11 の場合は `JavaSE-11`)。
- JDK が 1 つしかない場合でも、VS Code が明示的にそれを使用するようにするためにリストに含めることができます。
- JDK パスを見つけるには、ターミナルで `java -version` を実行し、インストールディレクトリを確認してください (例: Windows では `where java`、Unix 系システムでは `which java` を実行し、JDK ルートまで遡ります)。

この設定により、VS Code で複数の Java バージョンをシームレスに操作する柔軟性が得られます！ JDK パスの検索やトラブルシューティングでヘルプが必要な場合はお知らせください。