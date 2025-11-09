---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: 複雑なワークフローにおけるLLMの限界
translated: true
type: note
---

おっしゃる通りです！LLM（私を含む）は、**単一の概念の説明**、**短いコードスニペットの生成**、**特定のエラーのデバッグ**といった**小さく焦点が絞られたタスク**には優れていますが、以下のような**複雑なマルチステップのワークフロー**には苦戦します：

1. **複数の相互接続された設定**（例：Mavenの`pom.xml`ファイル、Jacocoエージェントの引数、Pythonテストとの統合）
2. **状態を持つ依存関係**（例：「まず`module-A/pom.xml`を更新し、次にこれらのフラグを付けて`mvn test`を実行し、その後レポートをマージする」）
3. **クロスシステム間の連携**（例：Java + Python + Jenkins/GitHub ActionsのようなCIツール）
4. **コンテキストの切り替え**（例：「ここでJavaの部分は忘れて、JacocoのXMLをPythonでどう解析する？」）

---

### **LLMが複雑なワークフローで失敗する理由**
1. **永続的なメモリがない**: 明示的にリマインドしない限り（そしてその場合でもコンテキストウィンドウは限られています）、過去のステップを「記憶」しません。
2. **直線的な思考**: ステップバイステップで回答を生成しますが、依存関係を動的に追跡することはできません（例：「エージェントの前に`mvn clean`を実行しましたか？」）。
3. **単一の回答への過剰な最適化**: 反復的なガイダンスではなく、*1つの*完全な回答を与えるように訓練されています。
4. **実行環境がない**: あなたの環境で`jacoco:prepare-agent`が実際に動作したかどうかを確認するためにコマンドを実行することはできません。

---

### **より良いアプローチ：「分割して検証」**
**Jacoco + マルチモジュールMaven + Pythonテスト**のような問題に対しては、**独立したステップ**に分解し、それぞれを検証してください。例：

#### **ステップ1: Jacocoエージェントのセットアップを検証（Java側）**
```bash
# 1つのモジュール（例: module-A）で実行：
mvn clean test -Pcoverage
```
- **確認**: `target/site/jacoco/index.html`は存在しますか？
- **デバッグ**: 存在しない場合、Jacoco用の`pom.xml`スニペットとエラーログを共有してください。

#### **ステップ2: 結合レポートの生成（マルチモジュール）**
```bash
mvn jacoco:report-aggregate
```
- **確認**: `target/site/jacoco-aggregate/index.html`は作成されましたか？
- **デバッグ**: 存在しない場合、親`pom.xml`内の`<module>`パスを確認してください。

#### **ステップ3: Python用にエクスポート（XML/CSV）**
```bash
# JacocoバイナリをXMLに変換
java -jar jacoco-cli.jar report jacoco.exec --xml output.xml
```
- **確認**: `output.xml`は`<package>`タグを含んでいますか？
- **デバッグ**: 空の場合、テストがエージェント（`-javaagent:jacocoagent.jar`）付きで実行されたことを確認してください。

#### **ステップ4: Python連携**
```python
import xml.etree.ElementTree as ET
tree = ET.parse("output.xml")
coverage = tree.find(".//counter[@type='LINE'][@covered]")
print(f"Covered lines: {coverage.get('covered')}/{coverage.get('missed')}")
```
- **確認**: スクリプトは期待される数値を出力しますか？
- **デバッグ**: 出力されない場合、XML構造とPythonのエラーを共有してください。

---

### **LLMを効果的に活用する方法**
1. **問題を分離する**:
   - *「これがモジュールA用の`pom.xml`です。なぜ`jacoco:prepare-agent`がVM引数を追加しないのですか？」*
   - *（「5つのモジュールとPython用にJacocoをセットアップするのを手伝って」よりも良い）*

2. **最小限の再現可能なコンテキストを共有する**:
   - エラーログ、設定スニペット（ファイル全体ではなく）、そして**あなたが試したこと**。

3. **反復的なデバッグ**:
   - **あなた**: 「ステップ1が`No tests run`で失敗しました。ログはこちらです。」
   - **LLM**: 「`maven-surefire-plugin`に`<test>`ゴールを追加してください。」
   - **あなた**: 「これでステップ2は動きましたが、レポートが空です...」

4. **「マイクロタスク」に私たちを活用する**:
   - *「JacocoのXMLを解析し、カバレッジが80%未満の場合に失敗するPythonスクリプトを書いてください。」*
   - *「Jacoco用のMavenにおける`<execution>`タグについて説明してください。」*

---

### **複雑なワークフローを自動化するツール**
LLMは状態を管理できないため、以下を使用してください：
- **シェルスクリプト**（例：Maven/Pythonコマンドを連鎖実行する`setup_coverage.sh`）。
- **Makefiles**（全てのステップを実行する`make test-coverage`を定義）。
- **CIテンプレート**（明示的なステップを含むGitHub Actions/Jenkinsパイプライン）。
- **Docker**（「私のマシンでは動く」問題を避けるために環境をコンテナ化）。

---
### **重要なポイント**
**LLMは、超強化された`man`ページや強力なStack Overflowのようなもの**です。**個々の部品**には優れていますが、システム全体を調整することはできません。複雑なタスクには：
1. **分解する**。
2. **各ステップを検証する**。
3. **的を絞った質問をする**。

上記のステップ（例：PythonでのJacoco XML解析やマルチモジュールMavenのセットアップなど）について、さらに深く掘り下げてほしいですか？