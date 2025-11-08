---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 設定 Zed 使用 Emacs 按鍵綁定
translated: true
type: note
---

### 配置 Zed 編輯器使用 Emacs 鍵盤綁定

看來您可能指的是 **Zed**（高效能程式碼編輯器），因為「Zig 編輯器」並非標準工具——Zig 是一種程式語言，沒有內建編輯器。若您指的是其他工具，請隨時說明！假設是 Zed，它內建支援 Emacs 鍵盤綁定（標示為「Emacs (Beta)」）。這預設涵蓋了許多基本操作，例如移動（`Ctrl-b/f/n/p`）和編輯（`Ctrl-d` 刪除字元，`Ctrl-k` 剪切至行尾）。您可以輕鬆啟用，並在需要時進一步自訂。

#### 步驟 1：啟用內建 Emacs 鍵盤映射
Zed 的 Emacs 模式已預先定義，無需手動設定基本綁定。以下是切換方法：

1. 開啟 Zed 設定：
   - macOS：`Cmd-,`
   - Windows/Linux：`Ctrl-,`

2. 在設定介面中，搜尋「base keymap」並設為 **Emacs**。

   *或直接編輯 `settings.json`*（透過 macOS 的 `Cmd-Alt-,` 或 Windows/Linux 的 `Ctrl-Alt-,` 開啟）：
   ```json
   {
     "base_keymap": "Emacs"
   }
   ```

   儲存並重新載入 Zed（`Cmd-R` 或 `Ctrl-R`）。完成——測試版 Emacs 鍵盤映射會立即啟用。

   或者，使用指令面板（`Cmd-Shift-P` 或 `Ctrl-Shift-P`），輸入「toggle base keymap」，然後選擇 Emacs。

這讓您無需額外工作即可使用核心 Emacs 肌肉記憶。內建綁定的完整清單請查閱 Zed 原始碼中的預設鍵盤映射檔案（例如透過 GitHub），但基本操作包括：
- **移動**：`Ctrl-b`（左移字元）、`Ctrl-f`（右移字元）、`Ctrl-p`（上移一行）、`Ctrl-n`（下移一行）、`Alt-b/f`（上一個/下一個單字）。
- **編輯**：`Ctrl-d`（刪除字元）、`Ctrl-k`（剪切至行尾）、`Ctrl-y`（貼上）、`Ctrl-@`（設定標記以選擇區域）、`Ctrl-w`（剪切區域）。
- **其他**：`Ctrl-x Ctrl-s`（儲存）、`Ctrl-g`（取消）、`Ctrl-/`（復原）。

#### 步驟 2：新增或自訂基本綁定（如有需要）
若要調整或實現更接近 Emacs 的行為（例如更好的行首/行尾或段落導航），請編輯 `keymap.json`：
- 透過指令面板開啟：輸入「open keymap file」。
- 路徑：`~/.config/zed/keymap.json`（macOS/Linux）或 `~\AppData\Roaming\Zed\keymap.json`（Windows）。

在如「Editor」的上下文中以 JSON 陣列形式新增綁定。以下是基本移動和編輯的**簡易範例**（貼入陣列；基於社群設定以確保相容性）：

```json
[
  {
    "context": "Editor",
    "bindings": {
      // 基本移動
      "ctrl-a": "editor::MoveToBeginningOfLine",
      "ctrl-e": "editor::MoveToEndOfLine",
      "ctrl-b": "editor::MoveLeft",
      "ctrl-f": "editor::MoveRight",
      "ctrl-p": "editor::MoveLineUp",
      "ctrl-n": "editor::MoveLineDown",
      "alt-b": "editor::MoveToPreviousWordStart",
      "alt-f": "editor::MoveToNextWordEnd",

      // 基本編輯
      "ctrl-d": "editor::DeleteRight",
      "ctrl-k": "editor::CutToEndOfLine",
      "ctrl-y": "editor::Paste",
      "ctrl-w": "editor::Cut",
      "ctrl-@": ["editor::SetSelectionAnchor", { "selection_id": 0 }],  // 設定標記
      "ctrl-x ctrl-x": "editor::FlipSelectionAnchor",  // 交換點與標記

      // 額外導航
      "ctrl-home": "editor::MoveToBeginning",
      "ctrl-end": "editor::MoveToEnd",
      "ctrl-g": "editor::Cancel"
    }
  }
]
```

- 儲存並重新載入 Zed。這些設定會覆蓋或新增至基礎 Emacs 映射。
- 在編輯器緩衝區中測試。若要選擇區域，使用 `Ctrl-Space`（或 `Ctrl-@`）設定標記，然後移動以選擇區域。
- 進階提示：在 settings.json 中結合 `vim_mode: false` 以避免衝突。

#### 提示
- **測試版狀態**：Emacs 模式正在持續改進（追蹤進度[請至此](https://github.com/zed-industries/zed/issues/4856)）。問題請回報至 Zed 的 GitHub。
- **完整自訂設定**：進階需求（例如使用 `Ctrl-x o` 切換窗格），請參閱下方討論區的社群範例。
- 若需同時使用 Vim/Helix 模式，請在設定中設定 `vim_mode: true` 或 `helix_mode: true`——它們會疊加在基礎之上。

這應能滿足 80% 的基本 Emacs 操作感。先從內建模式開始，再逐步調整！

[按鍵綁定文件](https://zed.dev/docs/key-bindings)  
[配置 Zed](https://zed.dev/docs/configuring-zed)  
[Emacs 鍵盤映射討論](https://github.com/zed-industries/zed/discussions/6572)  
[Emacs 相容性問題](https://github.com/zed-industries/zed/issues/4856)