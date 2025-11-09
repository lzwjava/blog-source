---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Windows 上的 GPG 主目錄路徑
translated: true
type: note
---

是的，你說得對。在 Windows 的 Git Bash（運行於 MSYS2/Cygwin 類環境）中，於 `gpg` 的 `--homedir` 路徑使用反斜線（`\`）會導致 shell 因轉義和路徑轉換機制而誤解參數。這會使路徑混亂（例如 `C:\Users\me\.gnupg` 可能被解析為無效路徑如 `C:Usersme.gnupg`，或在自動轉換為 Windows 格式時進一步混亂），導致目錄無法解析。因此，GPG 無法找到密鑰文件，從而引發「沒有私鑰」錯誤（或類似錯誤，例如 `pubring.kbx` 的「沒有此文件或目錄」）。

### 快速解決方法
- 使用正斜線（`/`）搭配 MSYS2 風格的驅動器前綴：`gpg --homedir /c/Users/me/.gnupg ...`
- 這樣 MSYS2 會在傳遞給原生 GPG 二進制文件時自動轉換為正確的 Windows 路徑（例如 `C:\Users\me\.gnupg`）。
- 避免使用不帶前導 `/` 的驅動器字母（如 `c:/`）——它們會被視為相對路徑，並在你的當前工作目錄前添加內容，導致同樣的查找失敗問題。

對於環境變數如 `GNUPGHOME`，同樣規則適用：使用 `/` 設置（例如 `export GNUPGHOME=/c/Users/me/.gnupg`）。

[MSYS2 文件系統路徑](https://www.msys2.org/docs/filesystem-paths/)  
[MSYS2 中的 GNUPGHOME 討論](https://lists.gnupg.org/pipermail/gnupg-users/2025-February/067536.html)  
[Windows/MSYS2 上的 GPG --homedir 錯誤](https://www.reddit.com/r/GnuPG/comments/1cl4dw8/bug_windows_homedir_with_drive_letter_treated_as/)