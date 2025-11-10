---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Python APIテストのためのJaCoCoガイド
translated: true
type: note
---

良い質問です — これは **Javaコードカバレッジツール**（JaCoCo）と**非Javaテストハーネス**（Pythonの`unittest`がRESTエンドポイントを呼び出す場合など）の間の典型的な統合問題です。

---

### JaCoCoがJUnitでは動作するが、Pythonテストでは直接動作しない理由

* JaCoCoは、**Javaエージェント**（`-javaagent:jacocoagent.jar`）をJVMにアタッチすることで動作します。
* テストが**同じJVM内で実行される**場合（JUnit、TestNGなど）、JaCoCoはどのクラスやメソッドが読み込まれ/実行されたかを確認し、詳細なカバレッジレポートを生成できます。
* Pythonの`unittest` + `requests`を使用してAPIエンドポイントを呼び出す場合、**JVMの外部から実行中のサーバー**を操作していることになります。
  これは、サーバープロセス自体にエージェントがアタッチされていない限り、JaCoCoが自動的にカバレッジを認識できないことを意味します。

---

### JaCoCoとPythonテストで正確なカバレッジを取得する方法

JUnitに切り替える必要はありません。JaCoCoを引き続き使用できますが、エージェントをテストランナーではなく、**大きなJavaプロジェクト（サーバー）が実行されているJVMにアタッチする**必要があります。

1. **JaCoCoエージェントを付けてJavaアプリケーションを実行する**
   サーバーの起動時にエージェントを追加します：

   ```bash
   java -javaagent:/path/to/jacocoagent.jar=destfile=jacoco-it.exec,output=file,append=false \
        -jar myserver.jar
   ```

   これにより、Pythonテストがエンドポイントを呼び出している間の実行データ（`jacoco-it.exec`）が収集されます。

2. **通常通りPythonテストを実行する**

   ```bash
   python -m unittest discover tests/
   ```

   サーバーがすでにエージェント付きで実行されているため、HTTPリクエストによって呼び出されたすべてのクラスとメソッドが記録されます。

3. **サーバーをシャットダウンする**
   `.exec`ファイルがフラッシュされます。

4. **カバレッジレポートを生成する**
   MavenプラグインまたはCLIを使用して、`.exec`ファイルをHTML/XMLレポートに変換します：

   ```bash
   mvn jacoco:report -Djacoco.dataFile=jacoco-it.exec
   ```

   またはCLIで：

   ```bash
   java -jar jacococli.jar report jacoco-it.exec \
        --classfiles target/classes \
        --sourcefiles src/main/java \
        --html report
   ```

---

### JaCoCoを使用した2つのテストモード

* **ユニットテスト（JVM内でのJUnit）：** Mavenプラグイン（`prepare-agent` + `report`）でそのまま動作します。
* **統合テスト（Pythonのような外部クライアント）：** エージェントを付けてJVMを起動し、その後`.exec`データをレポートにマージする必要があります。

---

### log4jのアイデアについて

ファイルごとのログステートメントをカウントする方法は非常に大雑把です：

* すべてのメソッドがログを出力するわけではありません。
* ログは条件分岐やブランチをカバーしません。
* カバレッジは信頼性がありません。

対照的に、JaCoCoは**クラス、メソッド、行、ブランチカバレッジ**を測定します — はるかに細かい粒度です。

---

✅ **回答：** テストがPythonで書かれていても、JaCoCoのアプローチを**絶対に使用できます**。コツは、JaCoCoをテストランナーではなく、**テスト対象のJavaプロセス（サーバー）にアタッチすること**です。その後、レポートを生成します。この方法により、JUnitを使用した場合と同じメソッドレベルおよびブランチレベルのカバレッジが得られます。

---

JaCoCoを使用してサーバーを起動し、Pythonテストで呼び出し、1つのコマンドでカバレッジを生成する「統合テスト」用の特別な**Maven設定例**を作成しましょうか？