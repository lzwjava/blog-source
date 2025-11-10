---
audio: false
generated: true
lang: ja
layout: post
title: 事前コミットフックにおけるステージ変更
translated: true
type: note
---

`update_notes_link.py`スクリプトの変更を別のコミットとして作成するのではなく、現在のコミットに統合する（pre-commitフック中に）には、フックを修正して更新されたファイルをステージングする必要があります（別々にコミットせずに）。これにより、Pythonスクリプトからの変更がユーザーのコミットに含まれるようになります。以下に、これを実現する修正済みのpre-commitフックスクリプトを提供します。

### 主な変更点
- **別々のコミットを作成しない**: フック内で`git commit`を実行する代わりに、スクリプトは更新されたファイルをステージングするだけです（`git add`）。これにより、ユーザーのコミットに含まれるようになります。
- **ユーザーのコミットメッセージを保持**: フックは新しいコミットを作成しないため、ユーザーの元のコミットメッセージが使用されます。
- **エラーハンドリング**: Pythonスクリプトが失敗した場合、フックは非ゼロのステータスで終了し、コミットを防ぎます。

### Pre-Commitフックスクリプト

以下は、別々のコミットを作成せずに変更をステージングする更新済みのpre-commitフックスクリプトです：

```x-shellscript
#!/bin/bash

# update_notes_link.pyスクリプトを実行し、その出力をキャプチャする
OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1)
EXIT_CODE=$?

# Pythonスクリプトが正常に実行されたか確認する
if [ $EXIT_CODE -ne 0 ]; then
    echo "エラー: update_notes_link.pyが終了コード$EXIT_CODEで失敗しました"
    echo "$OUTPUT"
    exit 1
fi

# 特定のファイルが更新されたか確認する
if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
    echo "Notesリンクが更新されました。現在のコミットのために変更をステージングしています。"

    # 関連ファイルをステージングする
    git add original/2025-01-11-notes-en.md
    git add _posts/en/*.md

    # ファイルがステージングされたことを確認する
    if ! git diff --cached --quiet; then
        echo "変更は正常にステージングされました。"
    else
        echo "ステージングする変更はありません。"
    fi
else
    echo "original/2025-01-11-notes-en.mdに更新はありません。追加のファイルはステージングされません。"
fi

# コミットを続行できるように成功で終了する
exit 0
```

### スクリプトの説明

- **Shebang (`#!/bin/bash`)**: スクリプトがBashシェルで実行されることを保証します。
- **Pythonスクリプトの実行**: `python scripts/generate/update_notes_link.py`を実行し、その出力と終了コードをキャプチャします。
- **エラーハンドリング**: Pythonスクリプトの終了コード（`$EXIT_CODE`）をチェックします。ゼロ以外の場合、フックは失敗し、エラーを表示してコミットを停止します。
- **出力のチェック**: `grep`を使用して、出力が`original/2025-01-11-notes-en.md`が更新されたことを示しているかチェックします。
- **ファイルのステージング**: 指定されたファイル（`original/2025-01-11-notes-en.md`と`_posts/en/*.md`）に対して`git add`を実行し、ユーザーのコミットに含めます。
- **コミットなし**: `git commit`をスキップし、ユーザーの`git commit`コマンドが元のコミットメッセージでステージングされた変更を含めることを可能にします。
- **フィードバック**: 変更がステージングされたかどうかをユーザーに知らせるメッセージを表示します。
- **終了コード**: Pythonスクリプトが失敗しない限り、コミットを続行できるように`0`で終了します。

### フックの設定

1. **フックの作成**:
   - スクリプトをリポジトリの`.git/hooks/pre-commit`に配置します。

2. **実行可能にする**:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

3. **フックのテスト**:
   - ファイルを変更するか、Pythonスクリプトが`original/2025-01-11-notes-en.md`を更新することを確認します。
   - `git commit -m "あなたのコミットメッセージ"`を実行します。
   - コミット前に`git diff --cached`をチェックするか、コミット後に`git show`をチェックして、更新されたファイルがコミットに含まれていることを確認します。

### `pre-commit`フレームワークの使用（オプション）

`pre-commit`フレームワークを使用する場合は、同じロジックを`.pre-commit-config.yaml`ファイルで定義できます。このアプローチはより移植性が高く、フックをトリガーするファイルを指定できます。

1. **pre-commitのインストール**:
   ```bash
   pip install pre-commit
   ```

2. **`.pre-commit-config.yaml`の作成**:

```yaml
repos:
- repo: local
  hooks:
  - id: update-notes-links
    name: Update Notes Links
    entry: bash -c '
      OUTPUT=$(python scripts/generate/update_notes_link.py 2>&1);
      EXIT_CODE=$?;
      if [ $EXIT_CODE -ne 0 ]; then
        echo "Error: update_notes_link.py failed with exit code $EXIT_CODE";
        echo "$OUTPUT";
        exit 1;
      fi;
      if echo "$OUTPUT" | grep -q "Updated original/2025-01-11-notes-en.md"; then
        echo "Notes links updated, staging changes for the current commit.";
        git add original/2025-01-11-notes-en.md;
        git add _posts/en/*.md;
        if ! git diff --cached --quiet; then
          echo "Changes staged successfully.";
        else
          echo "No changes to stage.";
        fi;
      else
        echo "No updates to original/2025-01-11-notes-en.md, no additional files staged.";
      fi'
    language: script
    files: ^(original/2025-01-11-notes-en\.md|_posts/en/.*\.md)$
    stages: [commit]
```

3. **フックのインストール**:
   ```bash
   pre-commit install
   ```

4. **フックのテスト**:
   - `files`正規表現に一致するファイル（例：`original/2025-01-11-notes-en.md`や`_posts/en/*.md`）への変更をコミットします。
   - フックが実行され、該当する場合は変更がステージングされ、コミットに含まれることを確認します。

### 元のGitHub Actionsとの主な違い

- **別々のコミットを作成しない**: GitHub Actionsワークフローは新しいコミットを作成しましたが、このフックはユーザーの現在のコミットに対して変更をステージングします。
- **プッシュなし**: pre-commitフックはコミットが確定する前にローカルで実行されるため、フックは変更をプッシュしません。ユーザーは手動で`git push`を実行する必要があります。
- **エラーハンドリング**: フックはPythonスクリプトの終了コードをチェックし、サイレントに失敗しないようにします。
- **Gitユーザー設定なし**: スクリプトは`git config user.name`と`user.email`を省略します。コミットにはユーザーのGit設定が使用されます。

### 注意点

- **Pythonスクリプト**: `scripts/generate/update_notes_link.py`が存在し、ローカルで実行可能であることを確認してください。環境変数や依存関係に依存している場合は、それらが利用可能であることを確認してください。
- **ファイルパス**: パス`original/2025-01-11-notes-en.md`と`_posts/en/*.md`がリポジトリ構造と一致することを確認してください。
- **フックの失敗**: Pythonスクリプトが失敗した場合、フックはコミットを防ぎ、部分的な更新がステージングされないようにします。
- **テスト**: `git commit`でテストし、変更がステージングされ、追加のコミットを作成せずにコミットに含まれることを確認してください。`git show`を使用してコミット内容を検査してください。

### 検証

検証するには：
1. ファイルを変更するか、Pythonスクリプトが`original/2025-01-11-notes-en.md`を更新することを確認します。
2. `git commit -m "テストコミット"`を実行します。
3. `git show`をチェックして、更新されたファイルが元のメッセージでコミットに含まれていることを確認します。
4. 追加のコミットが作成されていないことを確認します（例：`chore(notes): Update notes links`コミットがないこと）。

特定のエラーケースの処理やステージングするファイルの追加など、さらに調整が必要な場合はお知らせください！