---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: ブロブレスGitクローンの利点
translated: true
type: note
---

Gitコマンド:

```bash
git clone --filter=blob:none <リポジトリURL>
```

これは**部分クローン**であり、チェックアウト時に**ほとんどファイルの内容（blob）をダウンロードしません**。以下にその正確な動作と有用性を示します:

### `--filter=blob:none`の意味
- `--filter=blob:none`は、Gitに**blobless cloning**を使用するよう指示します。
- Gitは依然として以下をダウンロードします:
  - すべてのコミット（履歴）
  - すべてのツリーオブジェクト（ディレクトリ構造）
  - すべてのrefs/ブランチ/タグ
- しかし、初期クローン時には**ゼロのファイル内容（blob）**をダウンロードします。
- 後で`git checkout`やブランチの切り替えを行う際に、Gitはその時点で作業ツリーに実際に必要なファイルのblob（ファイル内容）のみをダウンロードします。

### 主な利点
- 非常に高速で小さな初期クローン（Linuxカーネル、Android、Windowsソースなどの巨大なリポジトリでもわずか数MB程度）。
- 最初の段階でネットワーク帯域幅とディスク容量を大幅に節約。
- CI/CD、クイックルックアップ、またはファイルをチェックアウトせずに履歴のみが必要な場合（例: `git log`、blame、コミット間のdiff）に最適。

### サイズ比較の例（実世界）

| リポジトリ       | 通常のクローン | `blob:none`クローン | 速度向上 |
|------------------|--------------|-------------------|------------|
| torvalds/linux   | ~5+ GB       | ~300–400 MB       | 10–20倍高速 |
| microsoft/vscode | ~2–3 GB      | ~200 MB           | 大幅に高速   |

### blob:noneクローン後の一般的なフォローアップコマンド
```bash
# 作業ツリーを初めて必要とする場合:
git checkout <ブランチ>        # 必要なblobのみをダウンロード

# 後ですべてが必要な場合:
git fetch --unshallow        # bloblessでは不要
# 不足しているblobを永続的に補充する場合:
git repack -a -d             # オプション、すべてのblobのダウンロードを強制
```

### 関連するフィルター
- `--filter=blob:none` → 初期段階でblobを一切ダウンロードしない（最も積極的）
- `--filter=tree:0`    → ツリーはダウンロードするがblobはダウンロードしない（同様の効果）
- `--filter=sparse:oid=<oid>` → 部分的なblobを使用したスパースチェックアウト用

### まとめ
```bash
git clone --filter=blob:none https://github.com/example/repo.git
```
= 「完全な履歴と構造を即座に提供し、ファイルの内容は後でオンデマンドでダウンロードする」  
巨大なモノレポや、長時間待たずに履歴を閲覧したい場合に最適。