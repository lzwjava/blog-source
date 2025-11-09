---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 認識 Ghostty 設定檔
translated: true
type: note
---

### Ghostty 設定檔運作方式

Ghostty 的設定檔採用簡單的文字格式，使用 `key = value` 形式的鍵值對。設計理念是直觀易用，讓您只需覆寫關心的預設值——Ghostty 已為所有設定提供合理的內建預設值，因此即使使用極簡甚至空白的設定檔也能正常運作。

#### 語法快速解析
- **鍵與值**：鍵名始終使用小寫且區分大小寫（例如 `font-family = JetBrains Mono`）。若值包含空格或特殊字元則需使用引號（例如 `font-family = "JetBrains Mono Nerd Font"`）。等號周圍的空格不影響解析。
- **註解**：在行首輸入 `#` 可添加註解（例如 `# 我的自訂主題`）。不支援在值後方添加行內註解，否則會被視為值的一部分。
- **還原預設值**：使用空值如 `key =` 即可將設定恢復為 Ghostty 內建預設值。
- **特殊數值**：部分選項採用特殊格式，例如時間單位（`resize-overlay-duration = 4s 200ms`）——詳情請查閱文件說明。
- **檔案載入**：Ghostty 會在 `~/.config/ghostty/config`（Linux/Windows）或 `~/Library/Application Support/com.mitchellh.ghostty/config`（macOS）路徑尋找設定檔。您可透過 `config-file = path/to/other.conf` 引入其他檔案實現模組化設定。
- **命令列覆寫**：所有設定皆可透過命令列參數設定（例如 `ghostty --font-family="Fira Code"`），此類設定將優先於設定檔。

透過預設快捷鍵（macOS 按 Cmd+Shift+,，Linux/Windows 按 Ctrl+Shift+,）或執行 `ghostty +reload-config`，變更將立即生效。

若要查看所有選項與預設值，請在終端機中執行 `ghostty +show-config --default --docs`。

### 典型設定範例
「典型」設定通常極為精簡——僅調整字型、色彩或邊距等基本項目。Ghostty 的預設值包含 JetBrains Mono 字型系列（內建 Nerd Font 支援）、簡潔的背景/前景配色，且未設置額外邊距。

以下示範一個深色主題的簡易典型設定，採用熱門字型、基礎邊距與快捷鍵配置。請將此內容儲存為您的 `config` 檔案：

```
# 深色主題搭配邊距與自訂字型
background = 1e1e1e
foreground = f8f8f2
font-family = "JetBrains Mono Nerd Font"
font-size = 14

# 在文字周圍保留呼吸空間
window-padding-x = 8
window-padding-y = 8

# 自訂快捷鍵（若需覆寫預設值）
keybind = cmd+t=new_tab
keybind = cmd+w=close_tab
keybind = cmd+d=new_split:right
```

此設定在自訂核心項目的同時保持輕量，您可透過文件擴充更多色彩設定（例如調色盤項目 `color0 = 282a36`）或主題配置。

[Ghostty 設定文件](https://ghostty.org/docs/config)