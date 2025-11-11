---
audio: false
generated: true
lang: ja
layout: post
title: TortoiseGitをGitマージツールとして設定する
translated: true
type: note
---

GitでTortoiseGitをマージツールとして設定するには、TortoiseGitに含まれるマージツールであるTortoiseGitMergeをGit設定でセットアップする必要があります。以下にその手順を示します。

### 前提条件
- システムにTortoiseGitがインストールされていることを確認してください。[tortoisegit.org](https://tortoisegit.org)からダウンロードできます。
- TortoiseGitMerge実行ファイルが利用可能であることを確認してください（通常は`C:\Program Files\TortoiseGit\bin\TortoiseGitMerge.exe`にあります）。

### TortoiseGitMergeをGitマージツールとして設定する手順

1. **コマンドプロンプトまたはGit Bashを開く**
   - Windowsコマンドプロンプト、PowerShell、またはGit Bashを使用して必要なGit設定コマンドを実行できます。

2. **TortoiseGitMergeをマージツールとして設定する**
   以下のコマンドを実行して、GitがTortoiseGitMergeを使用するように設定します：

   ```bash
   git config --global merge.tool tortoisegitmerge
   git config --global mergetool.tortoisemerge.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -base:\"$BASE\" -theirs:\"$REMOTE\" -mine:\"$LOCAL\" -merged:\"$MERGED\""
   ```

   **説明**：
   - `merge.tool tortoisegitmerge`：マージツール名を`tortoisegitmerge`に設定します（任意の名前を選択できますが、慣例としてこの名前が使われます）。
   - `mergetool.tortoisemerge.cmd`：TortoiseGitMergeを適切なパラメータで実行するコマンドを指定します：
     - `-base:"$BASE"`：共通の祖先ファイル。
     - `-theirs:"$REMOTE"`：マージされるブランチからのファイル。
     - `-mine:"$LOCAL"`：現在のブランチからのファイル。
     - `-merged:"$MERGED"`：解決されたマージが保存される出力ファイル。
   - パスにはスラッシュ（`/`）を使用し、特にパスにスペースが含まれる場合は引用符をエスケープしてください。

   **注意**：TortoiseGitが異なる場所にインストールされている場合（例：`E:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe`）は、パスを調整してください。

3. **オプション：マージツールのプロンプトを無効にする**
   `git mergetool`を実行するたびにプロンプトが表示されないようにするには、以下の設定を無効にします：

   ```bash
   git config --global mergetool.prompt false
   ```

4. **オプション：TortoiseGitMergeがシステムPATHにあることを確認する**
   GitがTortoiseGitMergeを見つけられない場合は、そのディレクトリがシステムのPATH環境変数に含まれていることを確認してください：
   - 「PC」または「マイコンピュータ」を右クリック → プロパティ → 詳細設定 → 環境変数。
   - 「システム環境変数」で`Path`変数を探し、`C:\Program Files\TortoiseGit\bin`を含むように編集します。
   - または、Git設定で明示的にパスを設定します：

     ```bash
     git config --global mergetool.tortoisemerge.path "C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe"
     ```

5. **設定をテストする**
   - Gitリポジトリでマージコンフリクトを作成します（例：競合する変更を含む2つのブランチをマージする）。
   - 以下のコマンドを実行してマージツールを起動します：

     ```bash
     git mergetool
     ```

   - TortoiseGitMergeが開き、競合ファイルの基本版、他方版、自方版を表示する3ペインビューが表示されます。下部のペインはマージ結果です。

6. **TortoiseGitMergeでコンフリクトを解決する**
   - 3ペインビューでは、TortoiseGitMergeは以下を表示します：
     - **左ペイン**：「他方」バージョン（マージされるブランチからのもの）。
     - **右ペイン**：「自方」バージョン（現在のブランチからのもの）。
     - **中央ペイン**：基本（共通祖先）バージョン。
     - **下部ペイン**：コンフリクトを解決するマージ結果。
   - 競合セクションを右クリックし、「他方のテキストブロックを使用」、「自方のテキストブロックを使用」などのオプションを選択するか、マージファイルを手動で編集します。
   - 解決したら、ファイルを保存し（ファイル → 保存）、TortoiseGitMergeを閉じます。
   - TortoiseGitMergeが正常に終了すると（終了コード0）、Gitはファイルを解決済みとしてマークします。プロンプトが表示された場合は、コンフリクトが解決されたことを確認します。

7. **解決したマージをコミットする**
   コンフリクトを解決した後、変更をコミットします：

   ```bash
   git commit
   ```

   **注意**：リベースやチェリーピック中にコンフリクトが発生した場合は、標準のコミットダイアログではなく、それぞれのTortoiseGitダイアログ（リベースまたはチェリーピック）を使用してプロセスを続行してください。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)

### TortoiseGit GUIを使用してTortoiseGitMergeを利用する
TortoiseGit GUIを使用してコンフリクトを解決する場合：
1. Windowsエクスプローラーで競合ファイルを右クリックします。
2. **TortoiseGit → 競合を編集**を選択します。
3. TortoiseGitMergeが開き、上述のようにコンフリクトを解決できます。
4. 保存後、再度右クリックし、**TortoiseGit → 解決済み**を選択してファイルを解決済みとしてマークします。
5. TortoiseGitのコミットダイアログを使用して変更をコミットします。

### トラブルシューティング
- **エラー：「サポートされていないマージツール 'tortoisemerge'」**
  - `TortoiseGitMerge.exe`へのパスが正しくアクセス可能であることを確認してください。
  - ツール名が`merge.tool`と`mergetool.<tool>.cmd`設定で正確に一致していることを確認してください。
  - TortoiseGitMergeがPATHにあるか、`mergetool.tortoisemerge.path`を使用して明示的に設定されていることを確認してください。[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **ファイルパスにスペースが含まれる場合**
  - ファイルパスにスペースが含まれる場合、上述のエスケープされた引用符を含むコマンド構文で正しく処理されるはずです。[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)
- **Cygwinユーザー**
  - Cygwinを使用する場合は、パスをCygwinのマウントポイントを使用するように調整します。例：

    ```bash
    git config --global mergetool.tortoisemerge.cmd '"/cygdrive/c/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe" -base:"$BASE" -theirs:"$REMOTE" -mine:"$LOCAL" -merged:"$MERGED"'
    ```

    これはCygwinの`/cygdrive/c/`パス構造を考慮します。[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)
- **TortoiseGitMergeが見つからない**
  - 以前にTortoiseSVNのTortoiseMergeを使用していた場合は、TortoiseGitバージョン1.8で実行ファイル名が変更されたため、`TortoiseGitMerge.exe`を指していることを確認してください。[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/15881449/why-doesnt-tortoisemerge-work-as-my-mergetool)

### 追加の注意点
- TortoiseGitMergeはコンフリクト解決のための3ペインビューをサポートしており、マージに理想的です。競合しない変更は自動的にマージされ、競合は手動解決のためにハイライト表示されます。[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://manios.org/2018/05/30/git-merge-conflicts-using-tortoise-git-merge-windows)
- TortoiseGitMergeをdiffツールとしても使用したい場合は、同様に設定します：

  ```bash
  git config --global diff.tool tortoisediff
  git config --global difftool.tortoisediff.cmd "\"C:/Program Files/TortoiseGit/bin/TortoiseGitMerge.exe\" -mine:\"$REMOTE\" -base:\"$LOCAL\""
  ```

  その後、`git difftool`を使用してファイルを比較します。[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)
- 高度な設定では、TortoiseGitにマージツールの終了を待機させ、終了コードに基づいてファイルを自動的に解決済みとしてマークするように設定できます。TortoiseGit設定 → 外部プログラム → マージツールで、「外部マージツールの実行中はTortoiseGitをブロックする」を選択し、「終了コードを信頼する」を有効にします。[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-settings.html)

### ソース
- TortoiseGitドキュメント：[](https://tortoisegit.org/docs/tortoisegitmerge/tmerge-dug.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-merge.html)[](https://tortoisegit.org/docs/tortoisegit/tgit-dug-conflicts.html)
- Stack Overflowおよびその他のWebリソース：[](https://devstuffs.wordpress.com/2013/03/08/setting-tortoisegitmerge-in-msysgit-as-the-git-mergetool/)[](https://stackoverflow.com/questions/5190188/why-cant-i-use-tortoisemerge-as-my-git-merge-tool-on-windows)[](https://stackoverflow.com/questions/16493368/can-tortoisemerge-be-used-as-a-difftool-with-windows-git-bash)

これらの手順に従うことで、コマンドラインまたはTortoiseGit GUIのいずれかから、TortoiseGitMergeをGitマージツールとして効果的に使用できるようになります。