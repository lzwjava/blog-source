---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Ghostty 安裝與啟動問題
translated: true
type: note
---

### 問題診斷

根據您分享的日誌，透過 `.deb` 套件安裝 Ghostty 1.1.3 已成功，但啟動失敗主要有兩個原因：

1. **CLI 參數錯誤**：指令 `ghostty .` 將 `.` 視為無效的配置欄位（可能意圖是指定目錄，但 Ghostty 不支援該語法）。這導致立即退出並顯示「無效欄位」。

2. **OpenGL/GTK 相容性問題**：當不帶參數執行 `ghostty` 時，它會初始化但隨即崩潰，原因是「OpenGL 版本過舊。Ghostty 需要 OpenGL 3.3」（您的系統向 Ghostty 報告的版本是 3.2）。這是在 Ubuntu 22.04 上已知的問題，特別是在使用 NVIDIA 驅動程式並運行於 X11 環境下。儘管 `glxinfo` 通常顯示 OpenGL 4.6+，但 Ghostty 的 GTK 4.6 運行時無法在 NVIDIA GL 環境下正確存取更高版本。「GDK_DEBUG=vulkan-disable」警告是嘗試的解決方法，但未能解決核心問題。最終的 Gtk-CRITICAL 錯誤是表面實現失敗的症狀。

這影響了許多 Ubuntu 22.04（及其衍生版本如 Pop!_OS）的使用者，原因是 GTK 版本較舊（4.6 對比需要完全相容 NVIDIA 的較新版本 4.12+）。

### 快速檢查
- 驗證您實際的 OpenGL 支援（如有需要，請安裝 `mesa-utils`：`sudo apt install mesa-utils`）：
  ```
  glxinfo | grep "OpenGL version"
  ```
  如果報告為 3.3+，則問題確實是 GTK/NVIDIA 特有的。
- 檢查您的會話類型：`echo $XDG_SESSION_TYPE`。如果是 `x11`，這可能是導致問題的原因之一。

### 解決方案
以下是逐步修復方法，從最簡單的開始：

1. **切換到 Wayland（如果您使用混合顯示卡，例如 Intel + NVIDIA）**：
   - 登出並在登入時選擇 Wayland 會話（或在 `/etc/gdm3/custom.conf` 中加入 `WaylandEnable=true` 並重新啟動 GDM）。
   - 使用整合顯示卡執行 Ghostty：`prime-run --gpu intel ghostty`（如有需要，請安裝 `nvidia-prime`）。
   - 這可以為某些使用者繞過 NVIDIA X11 的問題。

2. **透過 Snap 安裝（更簡單的替代套件）**：
   - 您使用的非官方 `.deb` 套件可能會繼承系統的特定問題。請嘗試官方的 Snap，它捆綁了依賴項：
     ```
     sudo snap install ghostty --classic
     ```
   - 使用 `snap run ghostty` 啟動。如果 OpenGL 仍然失敗，請繼續進行升級。

3. **升級至 Ubuntu 24.04（推薦的長期修復方案）**：
   - Ubuntu 24.04 包含 GTK 4.14+，解決了 NVIDIA 相容性問題。
   - 遵循官方升級指南：`sudo do-release-upgrade`。
   - 升級後，透過相同的 `.deb` 或 Snap 重新安裝 Ghostty。使用者報告升級後可完美運行。

4. **從原始碼建構並使用 GLFW 後端（臨時解決方法）**：
   - 這使用非 GTK 運行時來繞過 OpenGL 問題（注意：不支援分頁，僅供測試）。
     ```
     sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
     git clone https://github.com/ghostty-org/ghostty.git
     cd ghostty
     zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
     sudo cp zig-out/bin/ghostty /usr/local/bin/
     ```
   - 執行 `ghostty`。如需完整功能，請在升級後切換回 GTK。

### 額外提示
- 更新您的 NVIDIA 驅動程式：`sudo ubuntu-drivers autoinstall`（或手動使用 550+ 系列）。
- 如果您僅使用 AMD/Intel，請確保 Mesa 已更新：`sudo apt update && sudo apt upgrade mesa-vulkan-drivers`。
- 對於範本檔案（`~/.config/ghostty/config`）中的配置警告，請編輯它以移除任何無效的行（例如，多餘的 `.`）。

如果這些方法都無效，請分享您的 `glxinfo` 輸出或 GPU 詳細資訊（`lspci | grep VGA`）以獲得更有針對性的建議。

[OpenGL 版本過舊討論](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Ghostty Ubuntu 建置版本](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty Snap](https://snapcraft.io/ghostty)