---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 詳細記錄 Git
translated: true
type: note
---

要在 Git 中啟用詳細記錄功能，您可以根據指令和所需細節程度使用特定標誌或環境變數。以下是主要方法：

1. **使用 `--verbose` 或 `-v` 標誌**：
   許多 Git 指令支援 `--verbose`（或 `-v`）標誌以提供更詳細的輸出。例如：
   ```bash
   git commit --verbose
   ```
   這會顯示即將提交的變更差異以及常規輸出。

2. **為特定指令啟用詳細模式**：
   - 針對 `git push`：
     ```bash
     git push --verbose
     ```
     這會提供推送過程的詳細資訊，包括正在推送的引用和伺服器通訊。
   - 針對 `git fetch`：
     ```bash
     git fetch --verbose
     ```
     這會顯示正在獲取內容的詳細資訊。
   - 針對 `git clone`：
     ```bash
     git clone --verbose <repository>
     ```
     這會在克隆過程中顯示進度和額外細節。

3. **設定 `GIT_TRACE` 環境變數**：
   若要進行深度除錯，您可以啟用 Git 的追蹤輸出以查看 Git 操作的底層細節：
   ```bash
   GIT_TRACE=1 git <command>
   ```
   這會輸出有關 Git 內部流程的詳細記錄，例如指令執行和系統呼叫。

4. **啟用特定追蹤層級**：
   您可以使用更細緻的環境變數來針對 Git 的特定方面：
   - `GIT_TRACE_CURL`：啟用 HTTP 操作的詳細記錄（適用於遠端互動）：
     ```bash
     GIT_TRACE_CURL=1 git <command>
     ```
   - `GIT_TRACE_PACKET`：顯示 Git 通訊協定的封包層級細節：
     ```bash
     GIT_TRACE_PACKET=1 git <command>
     ```
   - `GIT_TRACE_PERFORMANCE`：記錄效能資料：
     ```bash
     GIT_TRACE_PERFORMANCE=1 git <command>
     ```

5. **增加差異相關指令的詳細程度**：
   對於像 `git diff` 或 `git log` 這樣的指令，您可以使用選項來獲取更多細節：
   - `git diff --stat` 顯示變更摘要。
   - `git log --verbose` 或 `git log -p` 包含每個提交的完整差異。

6. **全域設定詳細輸出**：
   您可以透過設定別名或使用設定選項，來配置 Git 始終以詳細模式執行特定指令。例如：
   ```bash
   git config --global alias.logv "log --verbose"
   ```
   之後，執行 `git logv` 將始終包含詳細輸出。

**範例**：
若要查看推送操作的詳細輸出並啟用完整追蹤：
```bash
GIT_TRACE=1 git push --verbose
```

**注意事項**：
- 詳細輸出可能會令人難以消化，特別是使用 `GIT_TRACE` 時，因此請在除錯特定問題時使用。
- 請查閱特定指令的手冊頁（例如 `man git-push`）以確認是否支援 `--verbose` 或其他除錯標誌。
- 在 Windows 上，請於命令提示字元中使用相同的環境變數語法（`set GIT_TRACE=1`）或 PowerShell（`$env:GIT_TRACE=1`）。

如果您需要針對特定 Git 指令或情境的詳細記錄，請告訴我，我可以提供量身訂製的範例！