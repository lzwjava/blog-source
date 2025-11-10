---
audio: false
generated: true
lang: ja
layout: post
title: Git pre-add フックの代替手段の作成
translated: true
type: note
---

Gitには組み込みの`pre-add`フックはありませんが、同様の機能を実現する方法がいくつかあります。以下にいくつかのアプローチを示します：

### 1. **Gitエイリアス（推奨アプローチ）**
`git add`を呼び出す前にチェックを実行するGitエイリアスを作成できます：

```bash
git config --global alias.safe-add '!your-pre-add-script.sh && git add'
```

その後、`git add`の代わりに`git safe-add`を使用します。

### 2. **ラッパースクリプト**
PATH内に`git-pre-add`というスクリプトを作成し、以下のように動作させます：
1. pre-addチェックを実行
2. チェックが成功した場合に`git add`を呼び出す

```bash
#!/bin/bash
# pre-add検証ロジックをここに記述
if [ some_condition ]; then
  git add "$@"
else
  echo "Pre-add checks failed"
  exit 1
fi
```

### 3. **既存のフックの活用**
既存のフックを創造的に活用する方法：
- **pre-commit**: addの後、commitの前に実行されますが、ここでステージングされたファイルをチェックできます
- **prepare-commit-msg**: pre-commitと同様ですが、プロセスのより早い段階で実行されます

### 4. **ファイルシステム監視**
より高度なニーズには以下を使用できます：
- **inotifywait** (Linux) - ワーキングディレクトリを監視
- **fswatch** (Mac) - 同様の機能

### 例：Pre-Addチェックスクリプト
末尾の空白を含むファイルの追加を防止する簡単な例：

```bash
#!/bin/bash
# .git/hooks/pre-commit（ただしステージングされたファイルで動作）

# 空白エラーのチェック
if git diff --cached --check; then
  exit 0
else
  echo "ステージングされたファイルに空白エラーが見つかりました"
  exit 1
fi
```

フックスクリプトは実行可能にすることを忘れないでください（`chmod +x script.sh`）。

特定のアプローチについて、あなたのユースケースに合わせて詳しく説明しましょうか？