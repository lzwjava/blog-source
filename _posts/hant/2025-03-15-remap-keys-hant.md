---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 24.04 中重新映射按鍵
translated: true
type: note
---

### 重點摘要
- 在 Ubuntu 24.04 中，您似乎可以透過圖形化工具 GNOME Tweaks 或使用命令列的 `gsettings` 來交換左 Ctrl 鍵和 Caps Lock 鍵。
- 研究顯示這兩種方法在多次工作階段中都能保持設定，適合日常穩定使用。
- 現有資料傾向認為 GNOME Tweaks 較為用戶友好，而命令列方法則為進階用戶提供更精細的控制。

#### 使用 GNOME Tweaks
GNOME Tweaks 提供簡易的按鍵交換介面：
- 如需安裝可執行：`sudo apt install gnome-tweak-tool`
- 開啟 Tweaks 後進入「鍵盤與滑鼠」分頁，點擊「額外版面配置選項」，在「Ctrl 鍵位置」下選擇「交換 Ctrl 與 Caps Lock」

#### 使用命令列
技術導向的終端機操作方式：
- 執行 `gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"` 即可永久交換按鍵功能

#### 特別注意
與 Windows PowerToys 可進行細粒度按鍵重映射不同，Ubuntu 的方法主要專注於交換左 Ctrl 鍵與 Caps Lock 鍵，這可能會影響您慣用的鍵盤快捷鍵組合。

---

### 調查報告：Ubuntu 24.04 按鍵交換功能詳析

本節將深入探討在 Ubuntu 24.04 中交換左 Ctrl 鍵與 Caps Lock 鍵的各種方法，類似 Windows 系統中 PowerToys 提供的功能。此分析彙整多方資料來源，同時滿足初學用戶與進階技術使用者的需求。

#### 背景與情境
代號「Noble Numbat」的 Ubuntu 24.04 是長期支援版本，持續採用 GNOME 桌面環境（特別是 46 版）。習慣 Windows 系統的用戶可能會期待類似的自定義選項，例如透過 PowerToys 交換特定按鍵。在 Linux 系統中，鍵盤自定義通常需透過 GNOME Tweaks 或命令列工具實現，其操作邏輯與 Windows 系統有所不同。

交換左 Ctrl 鍵與 Caps Lock 鍵的需求在開發者與進階用戶中相當常見，特別是習慣使用 Emacs 或 Vim 工作流程的用戶。本分析將同時探討圖形介面與命令列操作方法，確保設定能持久生效並與 Ubuntu 24.04 完全相容。

#### 按鍵交換方法

##### 方法一：使用 GNOME Tweaks
GNOME Tweaks 是簡化桌面自定義的圖形化工具，包含鍵盤設定功能。根據現有文件記載，其介面支援按鍵交換功能。操作步驟如下：

1. **安裝步驟：** 若系統未預載，用戶可透過 Ubuntu 軟體中心或執行以下指令安裝：
   ```bash
   sudo apt install gnome-tweak-tool
   ```
   此工具包含在 Ubuntu 24.04 的標準軟體庫中。

2. **存取鍵盤設定：** 從應用程式選單或活動總覽搜尋「Tweaks」開啟程式，在左側選單中進入「鍵盤與滑鼠」區段。

3. **進階版面配置選項：** 點擊「額外版面配置選項」進入進階鍵盤設定，在「Ctrl 鍵位置」區段中應可找到「交換 Ctrl 與 Caps Lock」選項。

4. **設定持久性：** 透過 GNOME Tweaks 進行的修改會儲存於用戶專屬的 `dconf` 資料庫，在每次登入時自動載入，因此能持續生效。

這個方法特別適合不熟悉命令列操作的用户，符合 Windows 用戶對圖形化介面的操作期待。不過需注意此功能選項在 Ubuntu 24.04 的 GNOME Tweaks 中是否可用，主要參考歷史文件如 [Ask Ubuntu: 如何重新映射 Caps Lock 與 Ctrl 鍵？](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys) 與 [Opensource.com: 在 Linux 中交換 Ctrl 與 Caps Lock 鍵](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard) 的記載。

##### 方法二：使用 `gsettings` 命令列
偏好命令列操作或遇到 GNOME Tweaks 問題的用戶，可透過 `gsettings` 指令直接修改鍵盤選項。此方法利用 GNOME 設定系統確保設定持久性。操作流程如下：

1. **開啟終端機：** 透過 Ctrl + Alt + T 快捷鍵或活動總覽啟動終端機。

2. **設定鍵盤選項：** 執行以下指令交換左 Ctrl 鍵與 Caps Lock 鍵：
   ```bash
   gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:swapcaps']"
   ```
   此指令會修改 `org.gnome.desktop.input-sources` 下的 `xkb-options` 鍵值，加入標準 XKB 選項 "ctrl:swapcaps"。

3. **驗證與持久性：** 執行指令後可立即測試按鍵反應，設定會儲存於用戶的 `dconf` 資料庫中，在每次登入時自動應用。

此方法特別適合進階用戶或用於自動化設定腳本，相關技術細節可參考 [EmacsWiki: 移動 Ctrl 鍵](https://www.emacswiki.org/emacs/MovingTheCtrlKey) 等資料來源。

#### 方法比較
為協助用戶選擇合適方法，以下表格從易用性、技術需求與持久性等面向比較兩種方法：

| **比較維度**          | **GNOME Tweaks**                     | **gsettings 命令列**           |
|-----------------------|--------------------------------------|--------------------------------------|
| **操作簡易度**        | 高（圖形化介面）                     | 中（需終端機操作知識）               |
| **技術需求**          | 低（適合初學者）                     | 中（適合進階用戶）                   |
| **設定持久性**        | 自動（儲存於 dconf）                 | 自動（儲存於 dconf）                 |
| **需額外安裝**        | 可能需要安裝                         | 無需額外安裝                         |
| **設定彈性**          | 受限於圖形介面選項                   | 高（可組合多種選項）                 |

此表格顯示 GNOME Tweaks 適合追求操作簡便的用戶，而 `gsettings` 則為熟悉命令列操作的用戶提供更高彈性。

#### 注意事項與限制
- **左 Ctrl 鍵專屬性：** 兩種方法預設皆交換左 Ctrl 鍵與 Caps Lock 鍵，因為 "ctrl:swapcaps" 在標準 XKB 配置中通常僅影響左 Ctrl 鍵。但實際效果可能因鍵盤佈局而異，建議用戶實際驗證。
- **快捷鍵影響：** 交換按鍵可能影響既有快捷鍵組合（如 Ctrl+C 複製、Ctrl+V 貼上），建議在設定後測試常用快捷鍵，特別是在終端機或整合開發環境中的操作。
- **潛在問題：** 目前未發現 Ubuntu 24.04 中「交換 Ctrl 與 Caps Lock」功能失效的具體報告，但用戶應注意可能的鍵盤相關錯誤，如 [Ubuntu 24.04 鍵盤問題：登入後 Caps Lock 功能反轉](https://ubuntuforums.org/showthread.php?t=2497465)。若遇問題可改用命令列方法作為備案。

#### 特別發現：與 Windows PowerToys 的差異
與 Windows PowerToys 可精確重映射特定按鍵的功能不同，Ubuntu 的方法較為標準化。GNOME Tweaks 中的「交換 Ctrl 與 Caps Lock」選項或 `gsettings` 的 "ctrl:swapcaps" 主要專注於交換左 Ctrl 鍵與 Caps Lock 鍵，這可能連帶影響其他鍵盤行為。此差異可能讓期待完全相同功能的用戶感到意外，建議在設定後進行全面測試。

#### 結論
在 Ubuntu 24.04 中，GNOME Tweaks 與 `gsettings` 均能有效實現左 Ctrl 鍵與 Caps Lock 鍵的交換功能，且設定能持久保存。GNOME Tweaks 提供圖形化的簡易操作，`gsettings` 則滿足進階用戶的精細控制需求。建議用戶在設定後驗證按鍵行為，並注意可能對既有快捷鍵造成的影響，特別是與 Windows PowerToys 的功能差異。

### 主要參考資料
- [如何重新映射 Caps Lock 與 Ctrl 鍵 Ask Ubuntu](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys)
- [在 Linux 中交換 Ctrl 與 Caps Lock 鍵 Opensource.com](https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard)
- [移動 Ctrl 鍵 EmacsWiki](https://www.emacswiki.org/emacs/MovingTheCtrlKey)
- [Ubuntu 24.04 鍵盤問題：登入後 Caps Lock 功能反轉 Ubuntu Forums](https://ubuntuforums.org/showthread.php?t=2497465)