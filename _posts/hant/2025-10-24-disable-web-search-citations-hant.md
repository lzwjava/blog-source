---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 停用 LibreChat 網絡搜尋引用
translated: true
type: note
---

## 在 LibreChat 網頁搜尋模式中停用引用標註

LibreChat 的網頁搜尋功能（由 Serper.dev 或 SearxNG 等供應商提供，並結合 Firecrawl 等爬蟲工具）會自動在回覆中包含引用標註，以註明來源並提高透明度。根據官方文件和社群討論，目前並未內建專為個別使用者關閉網頁搜尋引用標註的切換開關。然而，您可以透過修改設定來達成或近似此效果，這主要適用於管理員或自行託管的使用者。方法如下：

### 1. **管理員層級設定（建議方法）**
   如果您正在運行自己的 LibreChat 實例（自行託管），可以修改設定檔來限制或移除引用標註的呈現。引用標註是透過介面和搜尋元件處理的。

   - **編輯 `librechat.yaml` 以設定介面**：
     LibreChat 使用 YAML 檔案進行全域設定。尋找控制引用標註可見度的 `interface` 區段（靈感來自檔案搜尋的引用控制，這可能延伸影響到網頁搜尋的 UI 呈現）。
     - 將 `fileCitations` 設為 `false` 以全域停用引用標註權限。雖然這明確是針對檔案搜尋，但在某些設定中可能會影響網頁搜尋的 UI 呈現。
       ```yaml
       interface:
         fileCitations: false  # 停用所有搜尋的引用標註顯示
       ```
     - 針對網頁搜尋，您可以在 `webSearch` 區段下停用或自訂供應商，以避免詳細的來源連結：
       ```yaml
       webSearch:
         enabled: true  # 保持啟用，但調整供應商
         serper:  # 或您的供應商
           enabled: true
           # 沒有直接的 'citations' 旗標，但省略像 Firecrawl 這類爬蟲工具的 API 金鑰可以減少詳細提取內容/引用
         firecrawl:
           enabled: false  # 停用內容爬取，這通常會產生引用標註
       ```
     - 變更後請重啟您的 LibreChat 實例。介面設定來源：[LibreChat Interface Object Structure](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface)[1]。

   - **環境變數 (.env 檔案)**：
     在您的 `.env` 檔案中，停用可能強制加入引用標註的偵錯或記錄模式，或將網頁搜尋設定為最精簡的供應商。
     - 範例：
       ```
       DEBUG_PLUGINS=false  # 減少冗長輸出，包括引用標註
       SERPER_API_KEY=your_key  # 使用不帶爬取功能的基礎搜尋供應商以減少引用
       FIRECRAWL_API_KEY=  # 留空以停用爬蟲（無頁面提取內容/引用標註）
       ```
     - 這會將回覆轉變為僅有摘要的搜尋結果，而不包含內嵌引用標註。完整設定：[LibreChat .env Configuration](https://www.librechat.ai/docs/configuration/dotenv)[2]。

   - **網頁搜尋供應商自訂**：
     切換到像 SearxNG 這樣的供應商，它可以在伺服器端進行設定以省略來源連結。
     - 在 `.env` 中設定 `SEARXNG_INSTANCE_URL=your_minimal_searxng_url`。
     - 在您的 SearxNG 實例中，編輯其設定以抑制結果元數據（例如，透過 SearxNG 的 `settings.yml`：停用 `reveal_version: false` 並自訂模板以移除連結）。
     - 文件：[Web Search Configuration](https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search)[3]。

### 2. **使用者層級的解決方法（無管理員權限）**
   如果您使用的是託管版 LibreChat（例如公開實例），選項將非常有限，因為引用標註通常為了確保準確性而強制加入：
   - **提示詞工程**：在您的訊息中明確指示 AI，例如：「搜尋網路，但在回覆中不要包含引用標註或來源。」此方法效果不穩定，因為搜尋工具可能仍會附加它們，但許多模型會部分遵從。
   - **完全停用網頁搜尋**：如果引用標註是主要問題，可以針對每個對話關閉網頁搜尋：
     - 在聊天介面中，避免點擊「Web Search」按鈕。
     - 對於代理：在建立/編輯代理時，透過代理設定 UI 移除代理設定中的 `web_search` 功能。來源：[Agents Documentation](https://www.librechat.ai/docs/features/agents)[4]。
     - 請求管理員加入切換開關；社群討論已將此列為功能請求（例如，[GitHub Discussion on Web Search Toggle](https://github.com/danny-avila/LibreChat/discussions/7738)[5]）。

### 3. **限制與注意事項**
   - 引用標註是網頁搜尋的核心部分，旨在確保合乎道德的 AI 使用和可追溯性，因此完全停用它們可能需要自訂程式碼修改（例如，編輯 GitHub 儲存庫中的前端元件如 `WebSearchResults.jsx` 來隱藏引用元素）。
   - 目前版本（截至 2025 年 10 月）不存在直接的「關閉引用標註」旗標。請查閱 [Web Search Feature Docs](https://www.librechat.ai/docs/features/web_search)[6] 以獲取更新，因為功能會不斷演進。
   - 如果自行託管，請在開發環境中測試變更——停用爬蟲可能會降低回覆品質。
   - 社群回饋（例如 Reddit）指出搜尋功能偶有錯誤，但沒有特別針對引用標註：[Reddit Thread on LibreChat Issues](https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/)[7]。

如需官方支援，請加入 LibreChat Discord 或開啟 GitHub issue 並提供您的設定詳情。如果這未能解決問題，請提供更多關於您的 LibreChat 版本或託管方式的背景資訊！

引用來源：
[1] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/interface
[2] https://www.librechat.ai/docs/configuration/dotenv
[3] https://www.librechat.ai/docs/configuration/librechat_yaml/object_structure/web_search
[4] https://www.librechat.ai/docs/features/agents
[5] https://github.com/danny-avila/LibreChat/discussions/7738
[6] https://www.librechat.ai/docs/features/web_search
[7] https://www.reddit.com/r/LocalLLaMA/comments/1k2hraj/is_it_just_me_or_is_librechat_a_complete_buggy/