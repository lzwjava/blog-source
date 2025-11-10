---
audio: false
generated: true
lang: hant
layout: post
title: 人工智能編程助手指南
translated: true
type: note
---

Claude Code 是由 Anthropic 開發的人工智慧編程助手，旨在無縫整合到您的終端機中，並透過自然語言指令增強軟件開發工作流程。以下是一份有效使用 Claude Code 的完整指南，涵蓋設定、主要功能、最佳實踐、限制及實際範例。本指南適合所有層級的開發者，從初學者到經驗豐富的工程師，並匯集了來自各方的見解，以提供清晰且可操作的概述。

---

## 什麼是 Claude Code？

Claude Code 是一個基於終端機的工具，利用 Anthropic 的先進 AI 模型（例如 Claude 3.5 Sonnet 和 Opus 4）來協助編程任務。與傳統的編程助手不同，它直接在您的開發環境中運作，理解您的程式碼庫、執行指令，並自動化除錯、重構和 Git 操作等任務。它基於 Anthropic 的「Constitutional AI」框架構建，優先考慮安全性、清晰度和道德使用。[](https://docs.anthropic.com/en/docs/claude-code/overview)

主要功能包括：
- **程式碼庫理解**：分析整個程式碼庫，包括專案結構和依賴項。
- **程式碼編輯與重構**：修改檔案、優化程式碼並提升可讀性。
- **除錯**：識別並修復錯誤，包括類型錯誤和效能問題。
- **測試與 Linting**：生成並執行測試，修復失敗的測試，並強制執行編碼標準。
- **Git 整合**：管理 Git 工作流程，例如提交、拉取請求和合併衝突解決。
- **自然語言互動**：允許您以純英語發出指令，使其對非編程人員也易於使用。[](https://docs.anthropic.com/en/docs/claude-code/overview)[](https://www.datacamp.com/tutorial/claude-code)

---

## 設定 Claude Code

### 先決條件
- **Anthropic 帳戶**：您需要一個有效的 Anthropic 帳戶並設定帳單。Claude Code 作為 Pro 或 Max 計劃的一部分提供，或作為某些用戶的有限研究預覽。[](https://x.com/AnthropicAI/status/1930307943502590255)[](https://www.anthropic.com/claude-code)
- **終端機存取**：Claude Code 在您的終端機中運行，因此請確保您有相容的環境（例如 Bash、Zsh）。
- **專案目錄**：準備好一個供 Claude Code 分析的程式碼庫。

### 安裝步驟
1. **註冊或登入**：訪問 [claude.ai](https://claude.ai) 或 [anthropic.com](https://www.anthropic.com) 創建帳戶或登入。對於電子郵件登入，請輸入發送到您收件箱的驗證碼。對於 Google 登入，請透過您的 Google 帳戶進行驗證。[](https://dorik.com/blog/how-to-use-claude-ai)
2. **安裝 Claude Code**：
   - 驗證後，Anthropic 提供一個連結來安裝 Claude Code。在您的終端機中運行提供的指令以下載並設定它。例如：
     ```bash
     npm install -g claude-code
     ```
     此指令全域安裝 Claude Code。[](https://www.datacamp.com/tutorial/claude-code)
3. **導航到您的專案**：在終端機中切換到您的專案目錄：
     ```bash
     cd /path/to/your/project
     ```
4. **啟動 Claude Code**：通過運行以下指令啟動 Claude Code：
     ```bash
     claude-code
     ```
     這將啟動一個互動式 REPL（讀取-求值-輸出循環）會話，您可以在其中發出自然語言指令。[](https://docs.anthropic.com/en/docs/claude-code/overview)

### 配置
- **環境整合**：Claude Code 繼承您的 Bash 環境，使其能夠存取 `git`、`npm` 或 `python` 等工具。請確保您的自訂工具已記錄或在提示中指定，因為 Claude 可能無法自動識別它們。[](https://www.anthropic.com/engineering/claude-code-best-practices)[](https://harper.blog/2025/05/08/basic-claude-code/)
- **Model Context Protocol (MCP)**：要與外部工具（例如 GitHub、Slack）整合，請在您的專案目錄中的 `.mcp.json` 檔案中配置 MCP 設定。對於除錯 MCP 問題，請使用 `--mcp-debug` 標誌。[](https://www.anthropic.com/engineering/claude-code-best-practices)[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
- **權限**：Claude Code 會提示允許執行指令。僅對唯讀指令（例如 `git status`、`ls`）授予「自動執行」權限，以避免意外更改。拒絕對 `git commit` 或 `rm` 等指令的自動執行。[](https://waleedk.medium.com/claude-code-top-tips-lessons-from-the-first-20-hours-246032b943b4)

---

## 主要功能與使用案例

### 1. 程式碼生成
Claude Code 可以根據自然語言提示生成程式碼片段。它支援多種編程語言，包括 Python、JavaScript、C 等。[](https://www.tutorialspoint.com/claude_ai/claude_ai_code_generation.htm)

**範例**：
提示：「編寫一個 Python 函數來排序數字列表，處理正數和負數。」
```python
def sort_numbers(numbers):
    """
    以升序排序數字列表（正數和負數）。
    
    Args:
        numbers (list): 整數或浮點數的列表。
    
    Returns:
        list: 排序後的數字列表。
    """
    return sorted(numbers)

# 使用範例
numbers = [5, -2, 10, -8, 3]
sorted_list = sort_numbers(numbers)
print(sorted_list)  # 輸出：[-8, -2, 3, 5, 10]
```
Claude 生成程式碼，解釋其功能，並確保符合您的要求。請始終審查和測試輸出。[](https://www.tutorialspoint.com/claude_ai/claude_ai_code_generation.htm)

### 2. 程式碼重構
Claude Code 擅長提升程式碼的可讀性、可維護性和效能。它可以重構整個檔案或特定函數。

**範例**：
提示：「重構我 Supabase 專案中的 `client.py` 檔案以提升可讀性並添加文件字串。」
- Claude 分析 `client.py`，建議更改（例如重構函數、添加類型提示），並等待確認。批准後，它會用更整潔的程式碼更新檔案，添加文件字串，並在終端機中總結更改。[](https://www.datacamp.com/tutorial/claude-code)

### 3. 除錯
Claude 識別並修復錯誤，包括類型錯誤、缺少依賴項和效能瓶頸。

**範例**：
提示：「除錯這個拋出 TypeError 的 Python 函數。」
```python
def add_numbers(a, b):
    return a + b
# 呼叫方式：add_numbers("1", 2)
```
Claude 可能回應：「TypeError 是因為 `a` 是字串而 `b` 是整數。這是修復後的版本：」
```python
def add_numbers(a, b):
    """
    將兩個數字相加，必要時將字串轉換為數字。
    
    Args:
        a: 第一個數字（int、float 或 string）。
        b: 第二個數字（int、float 或 string）。
    
    Returns:
        float 或 int: 兩個數字的總和。
    """
    a = float(a) if isinstance(a, str) else a
    b = float(b) if isinstance(b, str) else b
    return a + b
```
運行更新後的程式碼以驗證修復。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)

### 4. 測試與 Linting
Claude 可以生成單元測試、運行它們，並修復失敗的測試或 linting 問題。

**範例**：
提示：「為 `sort_numbers` 函數編寫單元測試並運行它們。」
Claude 生成：
```python
import unittest

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([5, -2, 10, -8, 3]), [-8, -2, 3, 5, 10])
        self.assertEqual(sort_numbers([1.5, -1.5, 0]), [-1.5, 0, 1.5])
        self.assertEqual(sort_numbers([]), [])

if __name__ == '__main__':
    unittest.main()
```
然後它運行測試並報告結果。[](https://www.anthropic.com/engineering/claude-code-best-practices)

### 5. Git 整合
Claude 自動化 Git 任務，例如提交更改、解決合併衝突和創建拉取請求。

**範例**：
提示：「提交我的更改並創建一個帶有描述的拉取請求。」
Claude 執行：
```bash
git add .
git commit -m "Refactored client.py for better readability and added docstrings"
git push origin feature-branch
gh pr create --title "Refactor client.py" --body "Improved readability and added documentation."
```
審查提交和 PR 以確保準確性。[](https://docs.anthropic.com/en/docs/claude-code/overview)

### 6. 程式碼庫分析
Claude 可以解釋程式碼架構、邏輯或依賴項。

**範例**：
提示：「解釋我 Supabase 專案中 `client.py` 檔案的工作原理。」
Claude 提供檔案結構、關鍵函數及其用途的詳細分解，通常突出顯示依賴項或潛在改進。[](https://www.datacamp.com/tutorial/claude-code)

---

## 使用 Claude Code 的最佳實踐

1. **提示要具體**：
   - 使用清晰、詳細的提示以避免模糊的結果。例如，與其說「讓這個更好」，不如說「重構這個函數以降低時間複雜度並添加註釋。」[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
2. **分解複雜任務**：
   - 將大型任務分解為較小的步驟（例如一次重構一個模組）以提高準確性和速度。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
3. **先要求計劃**：
   - 在編碼前要求 Claude 概述計劃。例如：「制定重構此檔案的計劃，然後等待我的批准。」這確保與您的目標一致。[](https://www.anthropic.com/engineering/claude-code-best-practices)
4. **審查和測試輸出**：
   - 始終驗證 Claude 的建議，特別是對於關鍵專案，因為它可能忽略邊緣情況或專案特定邏輯。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
5. **作為配對編程夥伴使用**：
   - 將 Claude 視為協作夥伴。要求它解釋更改、建議替代方案或互動式除錯。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
6. **利用 Tab 鍵自動完成**：
   - 使用 tab 鍵自動完成快速參考檔案或資料夾，幫助 Claude 準確定位資源。[](https://www.anthropic.com/engineering/claude-code-best-practices)
7. **謹慎管理權限**：
   - 僅對安全指令允許自動執行，以防止意外更改（例如意外的 `git add .` 包含敏感檔案）。[](https://waleedk.medium.com/claude-code-top-tips-lessons-from-the-first-20-hours-246032b943b4)
8. **儲存提示模板**：
   - 將可重複使用的提示儲存在 `.claude/commands` 中作為 Markdown 檔案，用於重複性任務（例如除錯、日誌分析）。[](https://www.anthropic.com/engineering/claude-code-best-practices)
9. **測試驅動開發 (TDD)**：
   - 要求 Claude 在實現代碼前編寫測試以確保穩健的解決方案。明確指定 TDD 以避免模擬實作。[](https://www.anthropic.com/engineering/claude-code-best-practices)
10. **與工具結合使用**：
    - 將 Claude 與 ClickUp Docs 等工具整合以進行集中文件管理，或與 Apidog 整合以進行 API 測試，從而增強工作流程。[](https://clickup.com/blog/how-to-use-claude-ai-for-coding/)[](https://apidog.com/blog/claude-code/)

---

## 實際範例：重構 Supabase Python 客戶端

讓我們通過一個使用 Supabase Python 庫 (`supabase-py`) 的實際範例進行操作。

1. **設定**：
   - 導航到 `supabase-py` 目錄：
     ```bash
     cd /path/to/supabase-py
     claude-code
     ```
2. **重構**：
   - 提示：「重構 `client.py` 以提升可讀性、添加文件字串並優化效能。」
   - Claude 分析檔案，建議更改（例如重構函數、添加類型提示），並等待批准。
3. **添加文件**：
   - 提示：「添加內聯註釋和文件字串以澄清 `client.py` 中每個函數的用途。」
   - Claude 用清晰的文件更新檔案。
4. **測試**：
   - 提示：「為 `client.py` 編寫單元測試並運行它們。」
   - Claude 生成並執行測試，修復任何失敗。
5. **提交更改**：
   - 提示：「提交重構後的 `client.py` 並帶有描述性訊息，並創建一個拉取請求。」
   - Claude 自動化 Git 工作流程並提供 PR 連結。

**結果**：`client.py` 檔案現在更具可讀性、文件齊全、經過測試並已提交，節省了數小時的手動工作。[](https://www.datacamp.com/tutorial/claude-code)

---

## Claude Code 的限制

1. **跨檔案上下文**：
   - Claude 在大型專案中可能難以處理跨檔案依賴項，除非明確引導。在提示中提供相關檔案路徑或上下文。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
2. **領域特定知識**：
   - 它缺乏對專案特定業務邏輯的深入理解。您必須為小眾需求提供詳細的上下文。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
3. **過度自信**：
   - Claude 可能對邊緣情況提出合理但不正確的程式碼。請始終徹底測試。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)
4. **工具識別**：
   - 如果沒有明確指示，Claude 可能無法識別自訂工具（例如 `uv` 而不是 `pip`）。[](https://harper.blog/2025/05/08/basic-claude-code/)
5. **速率限制**：
   - 使用量有限（例如 Pro 計劃每 5 小時 45 條訊息）。重度用戶可能需要管理配額或升級到 Max 計劃。[](https://zapier.com/blog/claude-vs-chatgpt/)
6. **預覽狀態**：
   - 截至 2025 年 6 月，Claude Code 處於有限研究預覽階段，因此存取可能受限。如果不可用，請加入等候名單。[](https://www.datacamp.com/tutorial/claude-code)

---

## 最大化生產力的技巧

- **使用 Artifacts**：Claude 的 Artifacts 功能創建持久、可編輯的內容（例如程式碼片段、文件），您可以重新訪問和改進。[](https://zapier.com/blog/claude-ai/)
- **與 IDE 結合使用**：將 Claude Code 與 VS Code 或 Cursor 等 IDE 配對以進行實時預覽（例如使用 Tailwind CSS 的 React 應用程式）。[](https://www.descope.com/blog/post/claude-vs-chatgpt)
- **Vibe Coding**：對於非編程人員，將 Claude 視為通用代理。描述您的目標（例如「建立一個待辦事項應用程式」），它將逐步指導您。[](https://natesnewsletter.substack.com/p/the-claude-code-complete-guide-learn)
- **從反饋中學習**：與 Anthropic 分享反饋以改進 Claude Code。反饋會儲存 30 天，不用於模型訓練。[](https://github.com/anthropics/claude-code)
- **嘗試提示**：使用結構化提示，例如：
  ```
  <behavior_rules>
  完全按照要求執行。生成實現以下內容的程式碼：[描述任務]。無附加功能。遵循 [語言/框架] 標準。
  </behavior_rules>
  ```
  這確保了精確的輸出。

---

## 定價與存取

- **免費存取**：有限使用權包含在 Claude 的 Pro 計劃中，該計劃每月 20 美元（或每年 200 美元並享有折扣）。[](https://www.anthropic.com/claude-code)
- **Max 計劃**：提供更高的配額並同時存取 Claude Sonnet 4 和 Opus 4，適用於較大的程式碼庫。[](https://www.anthropic.com/claude-code)
- **API 存取**：對於自訂整合，請使用 Anthropic 的 API。詳細資訊請參閱 [x.ai/api](https://x.ai/api)。[](https://www.anthropic.com/claude-code)
- **等候名單**：如果 Claude Code 處於預覽階段，請在 [anthropic.com](https://www.anthropic.com) 加入等候名單。[](https://www.datacamp.com/tutorial/claude-code)

---

## 為什麼選擇 Claude Code？

Claude Code 因其深入的程式碼庫感知、無縫的終端機整合以及處理複雜多步驟任務的能力而脫穎而出。它在以下方面特別有效：
- **開發者**：加速編程、除錯和測試，每週節省數小時。[](https://medium.com/dare-to-be-better/claude-code-the-ai-developers-secret-weapon-0faac1248080)
- **非編程人員**：實現「vibe coding」，任何人都可以通過用純英語描述想法來建立應用程式。[](https://natesnewsletter.substack.com/p/the-claude-code-complete-guide-learn)
- **團隊**：透過標準化文件和自動化 Git 工作流程來增強協作。[](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)

與 ChatGPT 或 GitHub Copilot 等替代方案相比，Claude Code 提供了卓越的上下文理解和安全導向設計，儘管它可能缺乏實時網絡存取或圖像生成功能。[](https://www.descope.com/blog/post/claude-vs-chatgpt)[](https://zapier.com/blog/claude-vs-chatgpt/)

---

## 結論

Claude Code 是一個變革性的工具，透過將 AI 推理與基於終端機的工作流程相結合，簡化了軟件開發。通過遵循最佳實踐——清晰的提示、逐步任務和徹底審查——您可以利用其功能來高效地編寫、重構、除錯和記錄程式碼。儘管它有局限性，例如在大型專案中的上下文空白，但其理解程式碼庫和自動化任務的能力使其成為開發者和非編程人員的強大盟友。

要開始使用，請在 [anthropic.com](https://www.anthropic.com) 註冊，安裝 Claude Code，並在您的程式碼庫中嘗試小型任務。與 Anthropic 分享反饋以幫助塑造其未來，並探索與 ClickUp 或 Apidog 等工具的整合以最大化其潛力。[](https://www.datacamp.com/tutorial/claude-code)[](https://apidog.com/blog/claude-code/)[](https://clickup.com/blog/how-to-use-claude-ai-for-coding/)

有關更多詳細資訊，請訪問：
- [Anthropic 的 Claude Code 概述](https://docs.anthropic.com)[](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 最佳實踐](https://www.anthropic.com)[](https://www.anthropic.com/engineering/claude-code-best-practices)

祝您使用 Claude Code 編程愉快！