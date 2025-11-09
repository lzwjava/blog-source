---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Claude Code 多目錄支援
translated: true
type: note
---

Claude Code 是 Anthropic 推出的 AI 編碼助手，主要在其初始化的作業目錄中運行以確保安全性與專注度，但透過近期更新（例如 1.0.18 及後續版本）推出的多目錄功能，現已全面支援跨專案操作。這項突破讓單一會話能存取並處理原始目錄外多個無關聯專案或目錄的檔案，實現諸如參照共享配置、整合前後端程式碼，或處理 monorepo 設定等任務，而無需切換操作環境。[1][2][3]

### 跨專案功能運作原理
- **核心機制**：Claude Code 啟動時會以根目錄（您的「主要」專案）為基礎，但可透過 `--add-dir` 參數或會話中的互動指令 `/add-dir` 擴展讀取、編輯與執行指令的權限至其他目錄。新增的目錄將被視為工作空間的延伸，實現無縫檔案操作（例如在編輯專案 B 時同步對專案 A 的檔案進行檢測）。[3][4]
- **會話範圍**：除非透過設定檔保存，否則新增的專案均屬臨時性。透過 Git worktrees 可在專案局部開啟同步會話以實現深度協作。[5][6]
- **限制說明**：Claude Code 僅限存取已新增的目錄，不會自動探索無關聯路徑。若需建立持久性多專案環境（如 monorepo），請從包含子資料夾的父層目錄啟動。[3][7]
- **應用場景**：
  - **Monorepo 架構**：為前後端分離專案新增子目錄。[3][5][7][8]
  - **共享資源**：參照獨立專案中的設定檔或函式庫。[3][6]
  - **跨專案協作**：整合不同程式庫或工具倉庫的程式碼。[1][3]

### 指示 Claude Code 引入其他專案的方法
若要新增當前目錄外的專案（例如 `${another_project_path}`）：

1. **啟動 Claude Code**：於主要專案目錄執行（例如 `cd /path/to/primary/project && claude`）。
2. **互動式新增目錄**：
   - 在會話中輸入 `/add-dir /完整路徑/至/其他專案` 或相對路徑（例如 `../another-project`）。
   - Claude Code 將確認存取權限——若出現提示請回覆「yes」。[2][3][4]
3. **透過 CLI 參數啟動**（適用即時多目錄設定）：
   - 執行：`claude --add-dir /path/to/another/project`（可重複參數新增多個目錄）。[4][5][7]
4. **指示 Claude 機器人/代理**：新增完成後，可直接使用自然語言指令，例如「請參照新增目錄 `/path/to/another/project` 中的 API 檔案」或「整合專案 B 的共享設定檔」。Claude 的代理設計能在擴展情境中理解這些需求。[3][5][6]

### 最佳實踐與技巧
- **路徑指定**：為確保跨環境清晰度，建議使用絕對路徑。避免新增過多目錄以防效能下降。[3][7]
- **工作空間設定**：團隊作業可考慮使用設定檔建立可重複使用的環境。搭配 Apidog 等工具實現跨目錄 API 測試。[3][8]
- **疑難排解**：若路徑解析失敗，請確認寫入權限。重大變更後建議重啟會話。若問題持續，請檢查日誌或改由更高層級目錄啟動。[3][7]
- **團隊工作流**：此功能適用於微服務或共享函式庫開發，並可透過 Git 進行版本同步。[5][6][8]

這項功能徹底改變了複雜專案架構的工作流程，相較於在各目錄開啟獨立會話，大幅降低了操作摩擦。[3][6] 若您遇到特定工具的問題或需要範例，歡迎提供更多細節！

參考文獻：
[1] https://www.reddit.com/r/ClaudeAI/comments/1l896ek/claude_code_v1018_we_can_now_specify_additional/
[2] https://www.threads.com/@boris_cherny/post/DMtFLWOzKAS/video-claude-code-can-now-work-across-multiple-directories-in-a-single-sessiontype-add?hl=en
[3] https://apidog.com/blog/claude-code-multi-directory-support/
[4] https://claudelog.com/faqs/--add-dir/
[5] https://www.anthropic.com/engineering/claude-code-best-practices
[6] https://www.linkedin.com/posts/valokafor_how-to-set-up-claude-code-the-right-way-for-activity-7353146981034201089-dhdX
[7] https://stackoverflow.com/questions/79763754/best-practices-for-multi-project-workspaces-in-claude-code
[8] https://www.siddharthbharath.com/claude-code-the-complete-guide/