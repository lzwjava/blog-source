---
audio: false
generated: true
lang: ja
layout: post
title: 高度なGit：リベース、マージ、競合解決、スカッシュ
translated: true
type: note
---

このガイドでは、`git rebase`と`git merge`の高度な使用方法、コンフリクトの解決、`ours`と`theirs`戦略の使用、コミットのsquashについて説明します。各トピックについて簡潔な説明と実践的な例を提供し、基本的なGitコマンドに慣れていることを前提とした高度なワークフローに焦点を当てます。

## 1. Git Merge: 高度な使用方法
`git merge`は複数の開発シーケンスを単一の統一された履歴に結合します。高度な使用法には、複雑なマージの処理、マージ戦略の使用、マージコミットの管理が含まれます。

### 主要なマージ戦略
- **Recursive (デフォルト)**: 複数の共通祖先を処理し、ほとんどのマージに適しています。
  - 例: `git merge --strategy=recursive branch-name`
- **Ours**: 現在のブランチの変更を保持し、マージされるブランチの変更を破棄します。
  - 例: `git merge --strategy=ours feature-branch`
- **Theirs**: 真の戦略ではありませんが、エミュレート可能です（コンフリクト解決については以下を参照）。
- **Octopus**: 複数のブランチを一度にマージします（2つ以上のブランチに使用）。
  - 例: `git merge branch1 branch2 branch3`

### 高度なマージオプション
- `--no-ff`: ファストフォワードが可能な場合でもマージコミットを強制し、ブランチの履歴を保存します。
  - 例: `git merge --no-ff feature-branch`
- `--squash`: マージされるブランチからのすべてのコミットを、現在のブランチ上の単一のコミットに結合します。
  - 例: `git merge --squash feature-branch && git commit`
- `--allow-unrelated-histories`: 共通の履歴を持たないブランチをマージします。
  - 例: `git merge --allow-unrelated-histories external-repo-branch`

### 例: ファストフォワードなしでのマージ
```bash
git checkout main
git merge --no-ff feature-branch
# マージコミットを作成し、feature-branchの履歴を保存
```

## 2. Git Rebase: 高度な使用方法
`git rebase`は、コミットを移動または修正して履歴を書き換え、線形の履歴を作成します。ブランチのクリーンアップに強力ですが、履歴を変更するため、共有ブランチでは注意して使用してください。

### リベースの種類
- **標準リベース**: 現在のブランチからのコミットをベースブランチに再生します。
  - 例: `git rebase main` (`feature-branch`にいる場合)
- **インタラクティブリベース**: コミットの編集、squash、または並べ替えを可能にします。
  - 例: `git rebase -i main`

### インタラクティブリベースのコマンド
`git rebase -i <base>`を実行します（例: 最後の3コミットには`git rebase -i HEAD~3`）。これにより、以下のようなコマンドを含むエディタが開きます:
- `pick`: コミットをそのまま保持します。
- `reword`: コミットメッセージを編集します。
- `edit`: コミットを修正するためにリベースを一時停止します。
- `squash`: 前のコミットと結合します。
- `fixup`: squashと同様ですが、コミットメッセージを破棄します。
- `drop`: コミットを削除します。

### 例: インタラクティブリベース
最後の3つのコミットをsquashするには:
```bash
git rebase -i HEAD~3
# エディタで、結合するコミットの"pick"を"squash"または"fixup"に変更
# 保存して終了して完了
```

### 異なるベースへのリベース
ブランチを新しいベースに移動するには（例: `feature-branch`を`old-base`から`main`に移動）:
```bash
git rebase --onto main old-base feature-branch
```

### マージコミットを含むリベース
デフォルトでは、リベースはマージコミットを平坦化します。これらを保存するには:
```bash
git rebase -i --preserve-merges main
```

### リベースの中止
問題が発生した場合:
```bash
git rebase --abort
```

## 3. マージ/リベースのコンフリクト解決
Gitが変更を自動的に調整できない場合にコンフリクトが発生します。`merge`と`rebase`の両方でコンフリクトが発生する可能性があり、同様に解決されます。

### コンフリクト解決の手順
1. **コンフリクトの識別**: Gitは一時停止し、コンフリクトしたファイルをリストします。
   - マージの場合: `git status`がコンフリクトのあるファイルを表示します。
   - リベースの場合: コンフリクトは`git rebase -i`中にコミットごとに解決されます。
2. **コンフリクトファイルの編集**: ファイルを開き、コンフリクトマーカーを探します:
   ```text
   <<<<<<< HEAD
   あなたの変更
   =======
   マージされる変更
   >>>>>>> branch-name
   ```
   希望の変更を保持するように手動で編集し、マーカーを削除します。
3. **解決済みとしてマーク**:
   - マージの場合: `git add <file>`
   - リベースの場合: `git add <file>`、その後`git rebase --continue`
4. **プロセスの完了**:
   - マージ: `git commit` (Gitは自動的にコミットメッセージを生成する場合があります)。
   - リベース: すべてのコミットが適用されるまで`git rebase --continue`。

### 例: マージコンフリクトの解決
```bash
git checkout main
git merge feature-branch
# コンフリクト発生
git status  # コンフリクトしたファイルをリスト
# ファイルを編集してコンフリクトを解決
git add resolved-file.txt
git commit  # マージを確定
```

### 例: リベースコンフリクトの解決
```bash
git checkout feature-branch
git rebase main
# コンフリクト発生
# コンフリクトしたファイルを編集
git add resolved-file.txt
git rebase --continue
# リベースが完了するまで繰り返し
```

## 4. コンフリクト解決でのOursとTheirsの使用
コンフリクト中に、一方の変更（`ours`または`theirs`）を優先させたい場合があります。`ours`と`theirs`の意味は操作によって異なります。

### マージ: Ours vs. Theirs
- `ours`: 現在のブランチからの変更（例: `main`）。
- `theirs`: マージされるブランチからの変更（例: `feature-branch`）。
- `--strategy-option` (`-X`) フラグを使用:
  - `ours`を保持: `git merge -X ours feature-branch`
  - `theirs`を保持: `git merge -X theirs feature-branch`

### リベース: Ours vs. Theirs
- `ours`: ベースブランチからの変更（例: `main`）。
- `theirs`: リベースされるブランチからの変更（例: `feature-branch`）。
- リベースコンフリクト解決中に使用:
  ```bash
  git checkout --ours file.txt  # ベースブランチのバージョンを保持
  git checkout --theirs file.txt  # リベースされるブランチのバージョンを保持
  git add file.txt
  git rebase --continue
  ```

### 例: Theirsを使用したマージ
`feature-branch`を`main`にマージし、`feature-branch`の変更を優先するには:
```bash
git checkout main
git merge -X theirs feature-branch
```

### 例: Oursを使用したリベース
`feature-branch`を`main`にリベース中に、`main`のバージョンを保持してコンフリクトを解決するには:
```bash
git checkout feature-branch
git rebase main
# コンフリクト発生
git checkout --ours file.txt
git add file.txt
git rebase --continue
```

## 5. コミットのSquash
Squashは複数のコミットを1つに結合し、よりクリーンな履歴を作成します。これは通常、インタラクティブリベースで行われます。

### コミットをSquashする手順
1. 対象のコミットに対してインタラクティブリベースを開始:
   ```bash
   git rebase -i HEAD~n  # n = squashするコミット数
   ```
2. エディタで、前のコミットに結合するコミットの`pick`を`squash`（または`fixup`）に変更します。
3. 保存して終了。Gitは結合されたコミットのコミットメッセージを編集するよう促す場合があります。
4. 更新された履歴をプッシュ（既に共有されている場合はforce push）:
   ```bash
   git push --force-with-lease
   ```

### 例: 3つのコミットをSquash
```bash
git rebase -i HEAD~3
# エディタに表示:
# pick abc123 Commit 1
# pick def456 Commit 2
# pick ghi789 Commit 3
# 以下に変更:
# pick abc123 Commit 1
# squash def456 Commit 2
# squash ghi789 Commit 3
# 保存して終了
# プロンプトが表示されたら結合されたコミットメッセージを編集
git push --force-with-lease
```

### マージ中のSquash
ブランチからのすべてのコミットをマージ中にsquashするには:
```bash
git checkout main
git merge --squash feature-branch
git commit  # 単一のコミットを作成
```

## ベストプラクティスとヒント
- **リベース前のバックアップ**: リベースは履歴を書き換えます。バックアップブランチを作成:
  ```bash
  git branch backup-branch
  ```
- **共有ブランチのリベースを避ける**: 公開ブランチでの履歴の書き換えは、共同作業者に問題を引き起こす可能性があります。代わりに`merge`を使用してください。
- **安全性のために`--force-with-lease`を使用**: 書き換えられた履歴をプッシュする場合、他の人の変更を上書きするのを防ぎます。
- **コンフリクト解決後のテスト**: コンフリクト解決後、プロジェクトがビルドされテストが合格することを確認してください。
- **コンフリクト解決にツールを使用**: VS Code、SourceTree、`git mergetool`などのGUIツールはコンフリクト解決を簡素化できます。
- **チームとのコミュニケーション**: チームで作業する場合、コンフリクトを避けるためにリベースを調整してください。

## 一般的な落とし穴
- **リベースでの作業の喪失**: 常にバックアップするか、`git reflog`を使用して失われたコミットを回復してください。
- **Ours/Theirsの誤用**: マージとリベースのコンテキストで、どのブランチが`ours` vs `theirs`であるかを再確認してください。
- **調整なしのForce Push**: 共有ブランチへのforce pushはチームメートの作業を混乱させる可能性があります。`--force-with-lease`を使用し、コミュニケーションを取ってください。

## ミスからの回復
- **履歴の表示**: `git reflog`を使用して以前の状態を表示し、失われたコミットを回復:
  ```bash
  git reflog
  git checkout <commit-hash>
  ```
- **マージ前の状態へのリセット**:
  ```bash
  git reset --hard HEAD^  # 最後のマージコミットを元に戻す
  ```
- **マージの中止**: マージがうまくいかない場合:
  ```bash
  git merge --abort
  ```

このガイドは、高度なGitワークフローのための強固な基盤を提供します。特定のシナリオやエラーについては、お知らせいただければ、さらに深く掘り下げたり、リアルタイムのソリューションを検索したりできます！