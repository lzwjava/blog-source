---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Azure DevOps ブランチトリガーの構成
translated: true
type: note
---

Azure DevOps Pipelinesでは、どのブランチがビルドとデプロイをトリガーするかを設定できます。これは主に**CIトリガー**（コードプッシュ時のビルド用）と**PRトリガー**（プルリクエスト用）を通じて行われます。設定方法はYAMLパイプライン（バージョン管理に推奨）とクラシックパイプラインで若干異なります。以下では、現代的なアプローチであるYAMLを最初に焦点を当て、その後クラシックについて簡単に説明します。すべての例はGitリポジトリを想定しています。

## YAMLパイプライン：ブランチトリガーの設定

YAMLパイプラインは、`azure-pipelines.yml`ファイルでトリガーを直接定義します。デフォルトでは、パイプラインは**すべてのブランチ**へのプッシュでトリガーされます（`trigger: branches: include: - '*'`と同等）。より細かい制御のためにこれをカスタマイズできます。

### ステップ1：基本設定
1. Azure DevOpsプロジェクトで、**パイプライン > ビルド**（またはCDの場合は**リリース**）に移動します。
2. パイプラインを作成または編集し、テンプレートとして**YAML**を選択します。
3. YAMLエディターで、トップレベルに`trigger`セクションを追加します。

### ステップ2：シンプルなブランチのインクルード
特定のブランチやパターンでトリガーするにはシンプルなリストを使用します：
```yaml
trigger:
- main          # 'main'へのプッシュでトリガー
- develop       # 'develop'も同様
- releases/*    # 'releases/'で始まる任意のブランチ（例：releases/v1.0）
```
- YAMLファイルを保存してリポジトリにコミットします。パイプラインはこれらのブランチでのみ実行されるようになります。
- `*`（0文字以上）や`?`（1文字）などのワイルドカードがサポートされています。`*`で始まるパターンは引用符で囲みます（例：`*-hotfix`）。

### ステップ3：高度なインクルード/エクスクルード
除外やより精密な制御には：
```yaml
trigger:
  branches:
    include:
    - main
    - releases/*
    - feature/*
    exclude:
    - releases/old-*     # 'releases/old-v1'などを除外
    - feature/*-draft    # ドラフト機能を除外
```
- **Include**: トリガー可能なブランチ（省略時はすべてのブランチから開始）。
- **Exclude**: インクルードリストからフィルターで除外（インクルード後に適用）。
- 何らかの`branches`句を指定すると、デフォルト（すべてのブランチ）が上書きされ、明示的にインクルードされたもののみがトリガーします。
- タグの場合：インクルードで`refs/tags/v1.*`を使用します。

### ステップ4：パスフィルター（オプション）
ファイルパスと組み合わせて細かい制御を実現：
```yaml
trigger:
  branches:
    include:
    - main
  paths:
    include:
    - src/*.cs          # 'src'フォルダーの変更時のみ
    exclude:
    - docs/*.md         # ドキュメントの変更は無視
```
- パスはリポジトリルートからの相対パスで、大文字小文字を区別します。

### ステップ5：バッチ処理とオプトアウト
- **バッチ実行**: 複数のプッシュを1つのビルドにキューイング（ノイズ低減）：
  ```yaml
  trigger:
    batch: true
    branches:
      include:
      - main
  ```
- **トリガー無効化**: CIを無効にするには`trigger: none`を設定。
- **コミットごとのスキップ**: コミットメッセージに`[skip ci]`または`***NO_CI***`を追加。

### PRトリガー
プルリクエストには`pr`セクションを追加：
```yaml
pr:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - src/*
```
- これにより、これらのブランチをターゲットとするPRが検証されます。

### テスト
- 一致するブランチにプッシュ：パイプラインが自動的に実行されます。
- **パイプライン > 実行**で実行を表示し、トリガーの詳細を確認します。

## クラシックパイプライン：ブランチトリガーの設定
レガシー/クラシックパイプライン（UIベース）の場合：
1. **パイプライン > ビルド**でパイプラインを編集します。
2. **トリガー > 継続的インテグレーション**に移動します。
3. **継続的インテグレーションを有効にする**をチェックします。
4. **ブランチフィルター**で、インクルード（例：`main`）またはエクスクルード（例：`develop`）を追加します。
5. パスの場合：同じタブの**パスフィルター**を使用します。
6. PRの場合：**トリガー > プルリクエストの検証**に移動し、ブランチフィルターを設定します。

保守性を高めるためにYAMLに切り替えてください。

## ベストプラクティス
- シンプルに開始：`main`と`develop`のみでトリガー。
- `*-hotfix`のようなノイズの多いブランチにはエクスクルードを使用。
- 必須レビュアーのためのブランチポリシー（リポジトリ > ブランチ > ポリシー）で保護。
- 監視：トリガー頻度にパイプライン分析を使用。

最新の詳細については、公式ドキュメントを参照してください。

[Build Azure Repos Git repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml)  
[Triggers in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops&tabs=yaml)