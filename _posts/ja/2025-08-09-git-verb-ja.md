---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 詳細な Git ログ
translated: true
type: note
---

Gitで詳細なログ出力を有効にするには、コマンドや必要な詳細レベルに応じて特定のフラグや環境変数を使用できます。主な方法は以下の通りです：

1. **`--verbose` または `-v` フラグを使用**:
   多くのGitコマンドは、より詳細な出力を提供するために `--verbose`（または `-v`）フラグをサポートしています。例：
   ```bash
   git commit --verbose
   ```
   これにより、通常の出力に加えてコミットされる変更の差分が表示されます。

2. **特定のコマンドで詳細モードを有効化**:
   - `git push` の場合：
     ```bash
     git push --verbose
     ```
     これにより、プッシュされる参照やサーバー通信を含むプッシュプロセスの詳細が提供されます。
   - `git fetch` の場合：
     ```bash
     git fetch --verbose
     ```
     これにより、フェッチされる内容の詳細情報が表示されます。
   - `git clone` の場合：
     ```bash
     git clone --verbose <repository>
     ```
     これにより、クローン中の進捗状況と追加の詳細が表示されます。

3. **`GIT_TRACE` 環境変数を設定**:
   より深いデバッグのために、Gitのトレース出力を有効にしてGitの操作に関する低レベルな詳細を確認できます：
   ```bash
   GIT_TRACE=1 git <command>
   ```
   これにより、コマンド実行やシステムコールなどのGitの内部プロセスに関する詳細なログが出力されます。

4. **特定のトレースレベルを有効化**:
   Gitの特定の側面に対してより細かい環境変数を使用できます：
   - `GIT_TRACE_CURL`: HTTP操作の詳細ログを有効化（リモート操作に有用）：
     ```bash
     GIT_TRACE_CURL=1 git <command>
     ```
   - `GIT_TRACE_PACKET`: Gitプロトコルのパケットレベルの詳細を表示：
     ```bash
     GIT_TRACE_PACKET=1 git <command>
     ```
   - `GIT_TRACE_PERFORMANCE`: パフォーマンスデータを記録：
     ```bash
     GIT_TRACE_PERFORMANCE=1 git <command>
     ```

5. **diff関連コマンドの詳細度を上げる**:
   `git diff` や `git log` などのコマンドでは、詳細を取得するためのオプションを使用できます：
   - `git diff --stat` は変更の概要を表示します。
   - `git log --verbose` または `git log -p` は各コミットの完全な差分を含みます。

6. **詳細出力のグローバル設定**:
   エイリアスの設定や設定オプションを使用して、特定のコマンドで常に詳細表示されるようにGitを設定できます。例：
   ```bash
   git config --global alias.logv "log --verbose"
   ```
   その後、`git logv` を実行すると常に詳細出力が含まれます。

**例**:
プッシュ操作の詳細な出力を完全なトレースで確認するには：
```bash
GIT_TRACE=1 git push --verbose
```

**注意点**:
- 詳細出力は、特に `GIT_TRACE` を使用する場合、情報量が多すぎることがあるため、特定の問題をデバッグする際に使用してください。
- 特定のコマンドが `--verbose` や他のデバッグフラグをサポートしているか確認するには、マニュアルページ（例：`man git-push`）を参照してください。
- Windowsでは、コマンドプロンプト（`set GIT_TRACE=1`）またはPowerShell（`$env:GIT_TRACE=1`）で同じ環境変数構文を使用してください。

特定のGitコマンドやシナリオに対する詳細なログ出力が必要な場合は、お知らせいただければ、具体的な例を提供できます！