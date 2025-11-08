---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復翻譯 API 認證錯誤
translated: true
type: note
---

### 工作流程與錯誤原因分析

你的「翻譯近期筆記」GitHub Actions 工作流程整體結構良好——它會檢出儲存庫、設定 Python 環境、安裝依賴套件、對最近 N 篇貼文執行翻譯腳本，並將變更提交至 `_notes/` 目錄。然而，根據你稍早分享的日誌（其中顯示翻譯成 ar、de、fr 等語言時出現 401 錯誤），問題在於 `scripts/translation/update_lang_notes.py` 內部呼叫翻譯 API 時的身份驗證環節。

#### 根本原因
- 錯誤 `"No cookie auth credentials found"` (HTTP 401) 是 **OpenRouter API**（或是與其互動的 Python 客戶端/函式庫，例如 LiteLLM 或非官方 SDK）特有的錯誤。這通常發生在 API 請求缺少正確的身份驗證標頭時。
- OpenRouter 預期在請求中包含 `Authorization: Bearer <your_openrouter_api_key>` 標頭。如果 API 金鑰未正確傳遞，某些客戶端會回退到（或誤解為需要）基於 cookie 的會話驗證，從而觸發此特定錯誤。
- 在你的工作流程中：
  - 你設定了 `OPENROUTER_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}`，這會將秘密值傳遞給腳本的環境變數。
  - 但腳本可能未能正確讀取/使用此環境變數。常見的不匹配情況包括：
    - 腳本預期使用 `OPENAI_API_KEY`（適用於像 OpenRouter 這類與 OpenAI 相容的端點）。
    - 或者它使用的函式庫（例如 `openai` Python SDK）未將基礎 URL 設定為 `https://openrouter.ai/api/v1`。
    - 秘密值 `DEEPSEEK_API_KEY` 可能實際儲存的是你的 **OpenRouter API 金鑰**（用於路由至 DeepSeek/Grok 模型），但如果它是直接的 DeepSeek 金鑰，則無法用於 OpenRouter。
- 從日誌來看，腳本正在使用模型 `'x-ai/grok-4-fast'`（透過 OpenRouter 的 Grok 4），並且它能成功處理 front matter/標題，但在按語言翻譯內容時失敗。
- 這並非 GitHub Actions 的問題——問題在於 Python 腳本的 API 客戶端設定。工作流程會繼續執行至提交步驟（因此你會看到 `git config user.name "github-actions[bot]"` 的日誌記錄），但由於沒有翻譯內容，只有英文檔案被新增。

#### 建議的修復方法
1. **更新工作流程中的環境變數**：
   - 調整為符合常見的 OpenRouter 設定（與 OpenAI 相容）。將「Translate posts」步驟中的 `env` 區塊更改為：
     ```
     env:
       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
       OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}  # 將變數名稱改為腳本預期的名稱
       OPENAI_BASE_URL: https://openrouter.ai/api/v1   # 路由至 OpenRouter 所需
     ```
   - 如果 `DEEPSEEK_API_KEY` 是你的 OpenRouter 金鑰，那沒問題。如果它是直接的 DeepSeek 金鑰，請在儲存庫設定中建立一個新的秘密值 `OPENROUTER_API_KEY`，並填入你實際的 OpenRouter 金鑰（可在 [openrouter.ai/keys](https://openrouter.ai/keys) 取得）。
   - 測試：在執行步驟中加入 `echo $OPENAI_API_KEY`（敏感資訊會以星號遮罩）以便在日誌中進行除錯。

2. **修正 Python 腳本 (`update_lang_notes.py`)**：
   - 確保它像這樣初始化 OpenAI 客戶端（假設使用 `openai` 函式庫）：
     ```python
     import os
     from openai import OpenAI

     client = OpenAI(
         api_key=os.getenv("OPENAI_API_KEY"),
         base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")  # 若未設定，預設為 OpenAI
     )

     # 然後使用 client.chat.completions.create(..., model="x-ai/grok-4-fast")
     ```
   - 如果使用 LiteLLM（常用於多供應商情境）：如果 `requirements.txt` 中未包含，請安裝它，並呼叫 `completion(model="openrouter/x-ai/grok-4-fast", api_key=os.getenv("OPENAI_API_KEY"), api_base="https://openrouter.ai/api/v1", ...)`。
   - 對於翻譯迴圈：為每個語言加入錯誤處理（例如，在 API 呼叫周圍使用 `try/except`，記錄失敗情況，若遇到 401 錯誤則跳過）。
   - 需要明確處理 cookies 嗎？很可能不需要——堅持使用 API 金鑰即可。如果腳本包含瀏覽器/Selenium 程式碼，請將其移除以確保 CI 的可靠性。

3. **工作流程改進**：
   - **輸入驗證**：加入對 N=0 或無效 `--n` 的檢查，以避免處理空內容。
   - **條件式提交**：你目前的 `git diff --cached --quiet || git commit` 寫法很好，但請更新提交訊息以反映所有語言：`-m "Add translated posts (ar, de, es, fr, hi, ja, zh, hant)"`。
   - **快取**：加入 `actions/cache` 用於 `pip` 以加速安裝過程。
   - **除錯模式**：加入可選的輸入參數 `debug: true` 和腳本的 `--debug` 旗標，以啟用詳細日誌記錄。
   - **權限**：確保 `github-pages` 環境具有所需的讀取/寫入權限。
   - 完整的「Translate posts」步驟更新後的 YAML 程式碼片段：
     ```
     - name: Translate posts
       run: |
         python scripts/translation/update_lang_notes.py --n ${{ inputs.n }}
       env:
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         OPENAI_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
         OPENAI_BASE_URL: https://openrouter.ai/api/v1
     ```

4. **測試步驟**：
   - **本地測試**：在本地匯出環境變數（例如 `export OPENAI_API_KEY=your_key`）後，執行 `python scripts/translation/update_lang_notes.py --n 1`。
   - **工作流程測試**：使用 `workflow_dispatch` 觸發並設定 N=1，檢查日誌中的 API 呼叫情況。
   - **驗證秘密值**：在儲存庫設定 > Secrets 中，確認 `DEEPSEEK_API_KEY` 包含有效的 OpenRouter 金鑰（以 `sk-or-...` 開頭）。
   - 如果仍然失敗，請在腳本中加入 `--verbose` 參數，並檢查請求標頭（例如透過 `print(client.api_key)`）。

這些調整應能解決 401 錯誤並讓翻譯流程正常運作。如果你能分享 `update_lang_notes.py` 的程式碼片段（例如 API 客戶端初始化的部分），我可以更精確地指出問題所在。

#### 參考資料
- [OpenRouter 快速入門 (API 驗證設定)](https://openrouter.ai/docs/quickstart)
- [LiteLLM OpenRouter 整合](https://docs.litellm.ai/docs/providers/openrouter)（如果使用）
- [關於類似 OpenRouter 驗證錯誤的 GitHub Issue](https://github.com/mendableai/firecrawl/issues/1352)
- [關於 OpenRouter 401 錯誤的 Reddit 討論串](https://www.reddit.com/r/openrouter/comments/1oqiaol/error_401_no_cookie_auth_credentials_found/)