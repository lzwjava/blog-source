---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: Ghosttyシェル設定ガイド
translated: true
type: note
---

### UbuntuにおけるGhosttyと.bashrc

Ghosttyは、`.bashrc`の読み込みに関して、Ubuntu（および他のLinuxディストリビューション）のデフォルトのGNOMEターミナルと同様に動作します。デフォルトでは、Ghosttyはbashに対して**非ログイン対話シェル**を起動するため、GNOMEターミナルと同様に`~/.bashrc`を直接読み込みます。これは、ほとんどのLinuxターミナルにおける標準的な動作であり、`.bashrc`は対話シェルの設定（例: エイリアス、プロンプト、非ログインセッション用の環境変数）を扱います。

#### .bashrcの読み込み方法
- 新しいGhosttyウィンドウまたはタブを開くと、非ログインシェルとして`bash`（またはデフォルトシェル）を実行します。
- Bashは、シェルが対話的である場合（デフォルトでは対話的）、`~/.bashrc`をチェックして読み込みます。
- `~/.bash_profile`（通常はログインシェル用）がある場合、Ghosttyを明示的にログインシェルとして起動するように設定しない限り（例: `~/.config/ghostty/config`に`initial-command = bash --login`を追加）、読み込まれません。
- 潜在的な問題: 一部のユーザーは、新規ユーザーの初回起動時や特定の設定（例: UbuntuでのリモートSSHセッション）で`.bashrc`が読み込まれないと報告しています。これは、競合する`~/.bash_profile`が存在しないことを確認するか、設定で手動で読み込むことで修正できることが多いです。`.bashrc`に`[[ $- != *i* ]] && return`のようなガードを追加すると、非対話的なコンテキストでの問題を防ぐことができます。

要するに、GhosttyはUbuntuで`.bashrc`を使用する点においてデフォルトのターミナルと同じであり、同じ非ログインのデフォルト設定を持っています。

### macOSにおけるGhostty: .zprofile または .bash_profile？

macOSでは、Ghosttyはプラットフォームの伝統（Terminal.appなど）に従い、シェルに関係なくデフォルトで**ログインシェル**を起動します。これは、どのプロファイルが読み込まれるかに影響します:

- **zshを使用する場合（Catalina以降のmacOSデフォルト）**: 新しいターミナルを開くたびに、`~/.zprofile`（ログイン設定用）*と*`~/.zshrc`（対話設定用）の両方を読み込みます。
- **bashを使用する場合**: `~/.bash_profile`（ログインシェル）を読み込みます。Bashはここでは`~/.bashrc`を直接読み込みません—`~/.bashrc`は非ログイン対話シェル専用です。`.bashrc`の内容を含めるには、`~/.bash_profile`に以下を追加します:
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

したがって、デフォルトのzsh設定では`~/.zprofile`を、bashを使用している場合は`~/.bash_profile`を読み込みます。必要に応じて、シェルを切り替えるか、Ghosttyの設定を調整できます。

[シェル統合 - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOSログインシェル - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[潜在的なバグ、起動時に.bashrcが読み込まれない - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash起動ファイル - GNUマニュアル](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)