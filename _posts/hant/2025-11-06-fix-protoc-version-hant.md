---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修正 Substrait 建構 Protoc 版本錯誤
translated: true
type: note
---

### 理解錯誤原因

這個編譯失敗發生在 `substrait` crate（版本 0.58.0）中，這是 GreptimeDB 用於跨語言查詢計劃的依賴項。錯誤源自 protobuf 編譯器（`protoc`）拒絕接受 `substrait/algebra.proto` 檔案，因為它在 proto3 語法中使用了「optional」欄位——這個功能需要滿足以下任一條件：

- Protoc 版本 ≥3.21（在此版本中支援已穩定，無需特殊標誌），或
- 較舊的 protoc（例如 3.15–3.20）並在編譯時傳遞 `--experimental_allow_proto3_optional` 標誌。

`substrait` 建置腳本中的 `prost-build` 工具沒有傳遞此標誌，因此它假設系統使用的是相容的 protoc 版本。您系統中的 `protobuf-compiler`（可能來自 Ubuntu 22.04 或更早版本的 `apt`，提供約 3.12.4 版本）過於老舊且缺少此標誌，導致了 panic。

GreptimeDB 的文件指定需要 protoc ≥3.15，但對於此依賴項，實際上需要 ≥3.21 版本。

### 快速修復：升級 Protoc 至 ≥3.21

最簡單且無需 root 權限的方法是下載並安裝官方二進位版本（無需編譯）。步驟如下：

1. **下載最新版 Protoc**：
   - 前往 [Protocol Buffers 發布頁面](https://github.com/protocolbuffers/protobuf/releases)。
   - 下載最新的 `protoc-<版本>-linux-x86_64.zip`（例如 `protoc-28.1-linux-x86_64.zip` 或當前最新版本——任何 ≥3.21 的版本均可）。
   - 直接下載連結範例（請調整版本號）：  
     `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2. **安裝**：
   ```
   unzip protoc-*.zip -d protoc-install
   sudo mv protoc-install/bin/protoc /usr/local/bin/
   sudo chmod +x /usr/local/bin/protoc
   rm -rf protoc-install protoc-*.zip  # 清理
   ```

3. **驗證**：
   ```
   protoc --version
   ```
   應輸出 `libprotoc 27.3`（或更高版本）。如果仍顯示舊版本，請檢查您的 PATH（`echo $PATH`）——`/usr/local/bin` 應在 `/usr/bin` 之前。

4. **重新嘗試建置**：
   ```
   make clean  # 清除過時的目標
   make
   ```

這將覆蓋系統的 `protoc`，而不會與 `apt` 套件衝突。如果您使用的是較新的發行版，如 Ubuntu 24.04+，則 `apt install protobuf-compiler` 可能已經提供 ≥3.21 版本——請先雙重檢查您的版本。

### 如果無法升級（罕見情況）
- 如果受困於舊系統，您需要修補 `substrait` 的 `build.rs` 以添加標誌（透過 `Command::new(protoc).arg("--experimental_allow_proto3_optional")`），但這需要 fork 該 crate 並更新 GreptimeDB 的 `Cargo.toml`——過程繁瑣且不建議。
- 或者，某些 crate 提供 `protobuf-src` 功能來捆綁最新的 protoc，但 `substrait` 預設未啟用此功能。

### 其他提示
- 確保滿足其他先決條件：`build-essential`（用於 GCC）、`libc6-dev`（glibc 標頭檔）。
- 如果編譯通過但後續在 C++ 依賴項（例如 Arrow）上失敗，請透過 conda 或 apt 安裝 `libarrow-dev`。
- 對於 CI/CD 或 Docker：將下載步驟添加到您的環境中。

這應該能解決問題——`substrait` 在現代化環境中能乾淨地編譯。如果您遇到其他問題，請分享 `protoc --version` 的輸出和您的發行版資訊。

[GreptimeDB 建置文件](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf 發布頁面](https://github.com/protocolbuffers/protobuf/releases)  
[Proto3 可選欄位說明](https://protobuf.dev/programming-guides/proto3/#optional)