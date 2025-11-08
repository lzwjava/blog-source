---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 建立 Ubuntu 使用者帳戶
translated: true
type: note
---

### 在 Ubuntu Linux 中建立新使用者

Ubuntu 提供命令列與圖形介面兩種建立使用者的方式。命令列方法簡單直接且適用於所有版本（包括伺服器版），而圖形介面僅在桌面版中提供。

#### 命令列方法（推薦）
1. 開啟終端機（Ctrl+Alt+T）。
2. 執行以下指令，將 `username` 替換為您想要的使用者名稱：
   ```
   sudo adduser username
   ```
   - 系統將提示您為新使用者設定高強度密碼
   - 您還可選擇性填寫全名、房間號碼、工作電話等資料。按 Enter 跳過或根據需要提供資訊
3. （可選）若要授予新使用者管理員（sudo）權限：
   ```
   sudo usermod -aG sudo username
   ```
   - 這會將使用者加入 `sudo` 群組，允許其執行需提升權限的指令

新使用者將擁有位於 `/home/username` 的家目錄，並可立即登入系統。

#### 圖形介面方法（僅限桌面版）
1. 開啟 **設定** 應用程式（可在活動總覽中搜尋）
2. 在側邊欄中前往 **使用者**
3. 點擊右上角的 **解鎖** 並輸入管理員密碼
4. 點擊 **新增使用者**
5. 填寫帳戶類型（標準或管理員）、全名、使用者名稱和密碼
6. 點擊 **新增**

#### 驗證方式
- 使用 `su - username` 切換至新使用者，或登出後重新登入
- 使用 `cat /etc/passwd | grep username` 檢查使用者

此程序適用於 Ubuntu 24.04 LTS 及後續版本。

[使用者管理 - Ubuntu Server 文件](https://documentation.ubuntu.com/server/how-to/security/user-management/)  
[新增使用者帳戶 - Ubuntu 文件](https://help.ubuntu.com/stable/ubuntu-help/user-add.html.en)