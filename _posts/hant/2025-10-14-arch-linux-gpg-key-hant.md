---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Arch Linux ISO 驗證 GPG 密鑰
translated: true
type: note
---

您的金鑰環中存有這把 GPG 金鑰（指紋為 `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C`，屬於 Pierre Schmitz），因為這是 Arch Linux 開發者用來為 ISO 映像進行加密簽署的官方簽署金鑰。此機制能確保下載檔案的完整性與真實性，避免遭到篡改。

當您在 macOS 系統上準備 Arch Linux 可啟動 USB 安裝碟時（很可能參照了 Arch 官方維基指南），標準驗證流程包含兩個步驟：
1. 下載 ISO 檔案及其對應的 `.sig` 簽章檔
2. 匯入相關開發者的 GPG 金鑰（本案中為 Pierre Schmitz 的金鑰，因他是近期 ISO 的主要簽署者之一），並透過 `gpg --verify archlinux-YYYY.MM.DD-x86_64.iso.sig` 這類指令驗證簽章

您可能曾執行過類似 `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` 的指令來取得並匯入金鑰，這會將其永久儲存於本機 GPG 金鑰環中，因此能在 `gpg --list-keys` 的清單中看見。

請放心 — GPG 金鑰僅是用于驗證的公開資料，多數 Arch 使用者在驗證 ISO 後都會保留數把這類金鑰。若您不再需要該金鑰，可執行下列指令移除：
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
（系統將要求您確認；此操作僅刪除公開金鑰，不影響已完成的簽章驗證）

[Arch Linux ISO 下載頁面](https://archlinux.org/download/)  
[Arch 維基：在 Mac 上安裝 Arch Linux](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[Pierre Schmitz 的 GPG 金鑰](https://pierre-schmitz.com/gpg-keys/)