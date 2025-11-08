---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復遺漏的 Protobuf 包含檔案
translated: true
type: note
---

### 理解錯誤原因

`greptime-proto`（鎖定在 GreptimeTeam 倉庫的 `14b9dc40` 提交）的編譯失敗發生在 protobuf 編譯階段。具體來說，`protoc` 無法找到 Google 的標準 well-known 類型 `google/protobuf/duration.proto`（可能還包括其他如 `timestamp.proto`）。這導致 GreptimeDB 自身的 proto 文件出現導入錯誤（例如 `ddl.proto` 導入 Duration 類型，從而在 `database.proto` 中產生未定義類型錯誤）。

根本原因：您安裝的 `protoc`（透過手動升級）僅包含二進制文件（`/usr/local/bin/protoc`），但缺少包含 Google 核心 proto 文件的 include 文件。crate 的 `build.rs` 中的 `prost-build` 在執行 `protoc` 時，沒有明確設定 `--proto_path` 指向 Google 的 include 目錄，因此無法解析像 `"google/protobuf/duration.proto"` 這樣的相對導入。

這是僅安裝二進制版本 protobuf 時的常見問題；完整 SDK 會提供 `/usr/include/google/protobuf/`（或等效路徑）。

### 快速修復：安裝 Protobuf Include 文件

既然您已經有較新版本的 `protoc` 二進制文件，只需添加缺失的 include 文件而無需降級：

1. **下載完整 Protobuf 發行版**（需與您的 protoc 版本匹配，例如 27.3 或最新版）：
   ```
   wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
   unzip protoc-27.3-linux-x86_64.zip -d protoc-full
   ```

2. **安裝 Include 文件**：
   ```
   sudo mkdir -p /usr/local/include/google/protobuf
   sudo cp -r protoc-full/include/google /usr/local/include/
   sudo chmod -R a+r /usr/local/include/google/protobuf  # 確保可讀權限
   rm -rf protoc-full protoc-*.zip  # 清理
   ```

3. **驗證**：
   - 檢查 protoc：`protoc --version`（應為 ≥3.21）。
   - 測試 include 文件：`ls /usr/local/include/google/protobuf/duration.proto`（應存在）。
   - 快速冒煙測試：`protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null`（在項目目錄下執行；忽略輸出，只需確認沒有 "File not found" 錯誤）。

4. **重新嘗試構建**：
   ```
   make clean  # 清除部分構建文件
   make
   ```

如果您使用的是帶有 `apt` 的發行版（例如 Ubuntu），替代方案是 `sudo apt install libprotobuf-dev`——但這可能會安裝舊版本（例如 3.12），與您手動安裝的 protoc 衝突。如果出現這種情況，請堅持使用手動複製 include 文件的方法，並明確設定 `PROTOC=/usr/local/bin/protoc`。

### 補充提示
- 如果錯誤持續（例如缺少其他 proto 文件如 `wrappers.proto`），完整的 `include/google/` 複製應能涵蓋它們。
- 對於容器化構建（Docker），請將這些步驟添加到您的 Dockerfile 中。
- 構建完成後，使用 `cargo run --bin greptime -- standalone start` 進行測試，以確保 proto 文件正確整合。
- 此版本的 greptime-proto 較新（約 2024 年 10 月）；如果問題仍然存在，請檢查上游倉庫是否有修復。

[GreptimeDB 構建文檔](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf Well-Known 類型](https://protobuf.dev/reference/protobuf/google.protobuf/)