---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 修復 APT GPG 簽名錯誤
translated: true
type: note
---

你遇到的錯誤意味著 APT 拒絕從 ShiftKey 軟體庫更新，因為它無法驗證其 GPG 簽名。你有兩個簡單的解決方法：

---

## 1. **移除或停用損壞的軟體庫**

如果你實際上不需要 `https://apt.packages.shiftkey.dev/ubuntu`，只需將其停用：

```bash
# 找到定義該軟體庫的檔案（它位於 /etc/apt/sources.list.d/）
ls /etc/apt/sources.list.d/shiftkey*

# 移除它（替換為實際的檔案名稱）
sudo rm /etc/apt/sources.list.d/shiftkey.packages.shiftkey.dev.list

# 然後更新並安裝
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

## 2. **匯入軟體庫的簽署金鑰**

如果你確實需要繼續使用 ShiftKey 的軟體包，你需要取得並安裝其公開金鑰：

```bash
# 下載並解編 GPG 金鑰到 APT 的金鑰環中
curl -fsSL https://apt.packages.shiftkey.dev/ubuntu/pubkey.gpg \
  | gpg --dearmor \
  | sudo tee /usr/share/keyrings/shiftkey-archive-keyring.gpg > /dev/null

# 編輯軟體庫檔案，使其引用該金鑰環。  
# 在編輯器中開啟 /etc/apt/sources.list.d/shiftkey*.list，並將 deb 行更改為：
#   deb [signed-by=/usr/share/keyrings/shiftkey-archive-keyring.gpg] https://apt.packages.shiftkey.dev/ubuntu any main

# 然後更新並安裝
sudo apt update
sudo apt install pkg-config libssl-dev
```

---

一旦 APT 能夠在沒有 GPG 錯誤的情況下更新，你就可以自由安裝 `pkg-config` 和 `libssl-dev`，然後重新建置：

```bash
cargo clean
cargo run
```