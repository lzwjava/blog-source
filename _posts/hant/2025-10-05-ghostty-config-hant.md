---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ghostty 終端機配置指南
translated: true
type: note
---

### Ghostty 與 Ubuntu 上的 .bashrc

在載入 `.bashrc` 方面，Ghostty 的行為與 Ubuntu（及其他 Linux 發行版）上的預設 GNOME 終端機相似。預設情況下，Ghostty 為 bash 啟動**非登入互動式 shell**，這意味著它會直接載入 `~/.bashrc`——就像 GNOME 終端機一樣。這是大多數 Linux 終端機的標準行為，其中 `.bashrc` 負責處理互動式 shell 的設定（例如別名、提示符、非登入階段的環境變數）。

#### 它如何載入 .bashrc
- 當您開啟新的 Ghostty 視窗或分頁時，它會以非登入 shell 的形式執行 `bash`（或您的預設 shell）。
- 如果 shell 是互動式的（預設情況下是），Bash 會檢查並載入 `~/.bashrc`。
- 如果您有 `~/.bash_profile`（通常用於登入 shell），除非您明確配置 Ghostty 啟動登入 shell（例如，在 `~/.config/ghostty/config` 中加入 `initial-command = bash --login`），否則它不會被載入。
- 潛在問題：部分使用者回報，在新使用者首次啟動或特定設定（例如 Ubuntu 上的遠端 SSH 連線）中，`.bashrc` 未載入。這通常可以透過確保沒有衝突的 `~/.bash_profile` 存在，或在設定中手動載入它來解決。在 `.bashrc` 中加入如 `[[ $- != *i* ]] && return` 的防護措施，可以避免在非互動式情境中出現問題。

總之，是的——在 Ubuntu 上使用 `.bashrc` 方面，Ghostty 與預設終端機相同，都具有相同的非登入預設行為。

### macOS 上的 Ghostty：.zprofile 還是 .bash_profile？

在 macOS 上，Ghostty 遵循平台的傳統（如 Terminal.app），預設啟動**登入 shell**，無論使用何種 shell。這會影響哪些設定檔被載入：

- **如果使用 zsh（自 Catalina 起為 macOS 預設）**：每次開啟新終端時，它會載入 `~/.zprofile`（用於登入設定）*和* `~/.zshrc`（用於互動式設定）。
- **如果使用 bash**：它會載入 `~/.bash_profile`（登入 shell）。Bash 在這裡不會直接載入 `~/.bashrc`——`~/.bashrc` 僅用於非登入互動式 shell。要包含 `.bashrc` 的內容，請在您的 `~/.bash_profile` 中加入：
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

因此，對於預設的 zsh 設定，它會載入 `~/.zprofile`；如果您使用 bash，則會載入 `~/.bash_profile`。您可以根據需要切換 shell 或透過 Ghostty 的設定進行調整。

[Shell Integration - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[macOS Login Shells - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Potential bug, .bashrc not read on startup - GitHub Discussion](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Bash Startup Files - GNU Manual](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)